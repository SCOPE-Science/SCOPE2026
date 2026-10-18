#!/usr/bin/env python3
"""Exact small bipartite site-deletion connectivity certificate.

Python 3.9+ standard library. Run: python3 check_robustness.py
Each row is a nonzero bit mask of its adjacent pollinators.
"""
from collections import defaultdict
from itertools import combinations_with_replacement
from math import comb


def degrees(rows, b):
    return (tuple(sorted(x.bit_count() for x in rows)),
            tuple(sorted(sum((r >> j) & 1 for r in rows) for j in range(b))))


def largest_dsu(rows, b, alive):
    a = len(rows)
    parent = list(range(a + b))
    sizes = [1] * (a + b)

    def root(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = root(x), root(y)
        if x == y:
            return
        if sizes[x] < sizes[y]:
            x, y = y, x
        parent[y] = x
        sizes[x] += sizes[y]

    for i, r in enumerate(rows):
        mask = r & alive
        while mask:
            low = mask & -mask
            mask ^= low
            union(i, a + low.bit_length() - 1)
    return max(sizes[root(i)] for i in range(a))


def largest_flood(rows, b, alive):
    a = len(rows)
    adj = [set() for _ in range(a + b)]
    active = set(range(a))
    for j in range(b):
        if alive & (1 << j):
            active.add(a + j)
            for i, r in enumerate(rows):
                if r & (1 << j):
                    adj[i].add(a + j)
                    adj[a + j].add(i)
    unused = active.copy()
    largest = 0
    while unused:
        root = unused.pop()
        component = {root}
        frontier = [root]
        while frontier:
            v = frontier.pop()
            for w in adj[v]:
                if w not in component:
                    component.add(w)
                    frontier.append(w)
                    unused.remove(w)
        largest = max(largest, len(component))
    return largest


def coefficients(rows, b):
    out = [0] * (b + 1)
    for alive in range(1 << b):
        n = largest_dsu(rows, b, alive)
        assert n == largest_flood(rows, b, alive)
        out[alive.bit_count()] += n
    return tuple(out)


def max_matching(rows, b, alive):
    reachable = {0}
    for r in rows:
        new_reachable = set(reachable)
        for used in reachable:
            eligible = r & alive & ~used
            while eligible:
                low = eligible & -eligible
                eligible ^= low
                new_reachable.add(used | low)
        reachable = new_reachable
    return max(used.bit_count() for used in reachable)


def small_census():
    totals = {}
    for n in range(2, 9):
        connected = 0
        signatures = 0
        vector_count = 0
        pair_count = 0
        for b in range(1, n):
            a = n - b
            catalog = defaultdict(set)
            for rows in combinations_with_replacement(range(1, 1 << b), a):
                if largest_dsu(rows, b, (1 << b) - 1) != n:
                    continue
                connected += 1
                catalog[degrees(rows, b)].add(coefficients(rows, b))
            signatures += len(catalog)
            for vecs in catalog.values():
                vecs = sorted(vecs)
                vector_count += len(vecs)
                for j, x in enumerate(vecs):
                    for y in vecs[:j]:
                        differences = [u - v for u, v in zip(x, y)]
                        assert min(differences) >= 0 or max(differences) <= 0, (
                            'incomparable', n, a, b, x, y)
                        pair_count += 1
        totals[n] = (connected, signatures, vector_count, pair_count)
    # These totals independently guard enumeration cardinalities in the small census.
    assert [totals[n][:3] for n in range(2, 9)] == [
        (1, 1, 1), (2, 2, 2), (5, 4, 4), (18, 10, 10),
        (89, 27, 27), (590, 80, 85), (5160, 241, 285)]
    return totals


def witness_check():
    G, H = (3, 5, 10, 28), (3, 5, 14, 24)
    b = 5
    assert degrees(G, b) == degrees(H, b) == (
        (2, 2, 2, 3), (1, 2, 2, 2, 2))
    assert largest_flood(G, b, 31) == largest_flood(H, b, 31) == 9
    cg, ch = coefficients(G, b), coefficients(H, b)
    assert cg == (1, 14, 40, 59, 40, 9)
    assert ch == (1, 14, 41, 58, 38, 9)
    assert tuple(x - y for x, y in zip(cg, ch)) == (0, 0, -1, 1, 2, 0)
    # Expand the polynomial in q with exact integer binomial coefficients.
    diff = [x - y for x, y in zip(cg, ch)]
    qcoeff = [0] * (b + 1)
    for k, val in enumerate(diff):
        # val*(1-q)^k*q^(b-k)
        for j in range(k + 1):
            qcoeff[b-k+j] += val * (-1)**j * comb(k, j)
    assert qcoeff == [0, 2, -7, 8, -3, 0]  # q(1-q)^2(2-3q)
    # Both networks give exactly the same maximum number of
    # simultaneous plant-pollinator assignments after EACH failure set.
    assert all(max_matching(G, b, t) == max_matching(H, b, t)
               for t in range(1 << b))
    match_coeffs = [sum(max_matching(G, b, t) for t in range(1 << b)
                        if t.bit_count() == k) for k in range(b + 1)]
    assert match_coeffs == [0, 5, 20, 30, 20, 4]
    # For survival u the exact expected-size difference is
    # -u^2(1-u)^3 + u^3(1-u)^2 + 2u^4(1-u)
    # = u^2(1-u)(3u-1); for failure q=1-u this is
    # q(1-q)^2(2-3q), with unique interior zero q=2/3.
    print('witness coefficient vectors:', cg, ch)
    print('matching coefficients:', match_coeffs)
    print('expected difference: q*(1-q)^2*(2-3*q)')


if __name__ == '__main__':
    for n, info in small_census().items():
        print('total vertices', n, 'connected profiles, degree classes, '
              'different coefficient vectors, compared pairs:', *info)
    witness_check()
    print('ALL EXACT CHECKS PASSED')
