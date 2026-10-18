#!/usr/bin/env python3
"""Exhaustive cross-checks for induced-three-vertex-path convex-set polynomials.

Run: python verify.py
Standard library only. Edge masks enumerate each labelled simple graph exactly once.
"""
from itertools import combinations
from math import comb


def graph(n, edge_mask):
    adj = [0] * n
    for k, (u, v) in enumerate(combinations(range(n), 2)):
        if (edge_mask >> k) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return tuple(adj)


def direct(adj):
    n = len(adj)
    f, k = [0] * (n + 1), [0] * (n + 1)
    for s in range(1 << n):
        size = s.bit_count()
        clique = all(not (s >> u & 1) or ((s & ~(1 << u)) & ~adj[u]) == 0
                     for u in range(n))
        if clique:
            k[size] += 1
            f[size] += 1
            continue
        ok = True
        for v in range(n):
            if (s >> v) & 1:
                continue
            neighbors = [u for u in range(n) if (s >> u) & 1 and (adj[v] >> u) & 1]
            if any(not ((adj[u] >> w) & 1) for u, w in combinations(neighbors, 2)):
                ok = False
                break
        if ok:
            f[size] += 1
    return f, k


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def sub(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] -= x
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def complete(adj, vertices):
    return all((adj[u] >> v) & 1 for u, v in combinations(vertices, 2))


def components(adj, vertices, complement=False):
    verts = set(vertices)
    ans = []
    while verts:
        start = min(verts)
        found, stack = {start}, [start]
        verts.remove(start)
        while stack:
            u = stack.pop()
            for v in sorted(verts):
                if bool((adj[u] >> v) & 1) != complement:
                    verts.remove(v)
                    found.add(v)
                    stack.append(v)
        ans.append(tuple(sorted(found)))
    return ans


def cotree(adj, vertices):
    n = len(vertices)
    if n == 0:
        return [1], [1]
    if n == 1:
        return [1, 1], [1, 1]
    co = components(adj, vertices)
    if len(co) > 1:
        left = co[0]
        right = tuple(sorted(set(vertices) - set(left)))
        fa, ka = cotree(adj, left)
        fb, kb = cotree(adj, right)
        return mul(fa, fb), (sub(add(ka, kb), [1]) + [0] * (n + 1 - len(sub(add(ka, kb), [1]))))
    co = components(adj, vertices, True)
    if len(co) <= 1:
        raise ValueError("not a cograph")
    left = co[0]
    right = tuple(sorted(set(vertices) - set(left)))
    fa, ka = cotree(adj, left)
    fb, kb = cotree(adj, right)
    base = mul(ka, kb)
    a_complete, b_complete = complete(adj, left), complete(adj, right)
    if a_complete:
        base = add(base, [0] * len(left) + sub(fb, kb))
    if b_complete:
        base = add(base, [0] * len(right) + sub(fa, ka))
    if not (a_complete or b_complete):
        base = add(base, [0] * n + [1])
    assert len(base) == n + 1
    return base, mul(ka, kb)


def has_induced(adj, chosen, pattern):
    edges = sum((adj[u] >> v) & 1 for u, v in combinations(chosen, 2))
    degrees = sorted(sum((adj[u] >> v) & 1 for v in chosen if v != u) for u in chosen)
    if pattern == "P4":
        return edges == 3 and degrees == [1, 1, 2, 2]
    if pattern == "C4":
        return edges == 4 and degrees == [2, 2, 2, 2]
    raise ValueError(pattern)


def unimodal(a):
    p = a.index(max(a))
    return all(a[i] <= a[i + 1] for i in range(p)) and \
           all(a[i] >= a[i + 1] for i in range(p, len(a) - 1))


def star(n, adj):
    return any(sum((adj[v] >> w) & 1 for w in range(n) if v != w) == n - 1 and
               all((adj[u] >> w) & 1 == 0 for u, w in combinations([x for x in range(n) if x != v], 2))
               for v in range(n))


def main():
    checked = 0
    n_by_size = {}
    convex_small = 0
    nonunimodal_five = []
    for n in range(1, 7):
        count = 0
        for mask in range(1 << comb(n, 2)):
            adj = graph(n, mask)
            p4 = any(has_induced(adj, q, "P4") for q in combinations(range(n), 4))
            if p4:
                continue
            count += 1
            f, k = cotree(adj, tuple(range(n)))
            f0, k0 = direct(adj)
            assert (f, k) == (f0, k0), (n, mask, f, f0, k, k0)
            checked += 1
            if n <= 5:
                c4 = any(has_induced(adj, q, "C4") for q in combinations(range(n), 4))
                if not c4:
                    convex_small += 1
                    if not unimodal(f):
                        assert n == 5 and star(n, adj) and f == [1, 5, 4, 6, 4, 1]
                        nonunimodal_five.append(mask)
        n_by_size[n] = count
    assert len(nonunimodal_five) == 5, nonunimodal_five
    for d in range(1, 12):
        f = [1, d + 1] + [comb(d, i - 1) for i in range(2, d + 2)]
        assert (not unimodal(f)) == (d >= 4)
        logconcave = all(f[j] * f[j] >= f[j-1] * f[j+1]
                         for j in range(1, len(f)-1))
        assert logconcave == (d <= 2)
    print("VERIFY_OK cographs=" + str(checked) + " by_size=" + str(n_by_size)
          + " trivially_perfect_checked_through5=" + str(convex_small)
          + " nonunimodal_five_labelled=" + str(len(nonunimodal_five))
          + " all_unique_star=" + str(len(nonunimodal_five) == 5))


if __name__ == "__main__":
    main()
