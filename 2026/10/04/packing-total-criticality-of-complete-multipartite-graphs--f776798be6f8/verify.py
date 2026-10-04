#!/usr/bin/env python3
from functools import lru_cache
from collections import deque


def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest


def complete_multipartite(parts):
    part = []
    for i, s in enumerate(parts):
        part += [i] * s
    n = len(part)
    edges = [(u, v) for u in range(n) for v in range(u+1, n) if part[u] != part[v]]
    return n, edges


def components(n, edges):
    a = [[] for _ in range(n)]
    for u, v in edges:
        a[u].append(v); a[v].append(u)
    seen = [False] * n
    out = []
    for s in range(n):
        if seen[s]:
            continue
        seen[s] = True
        q = [s]
        c = []
        while q:
            u = q.pop(); c.append(u)
            for v in a[u]:
                if not seen[v]:
                    seen[v] = True; q.append(v)
        out.append(c)
    return out


def total_graph(vertices, edges):
    V = set(vertices)
    es = [tuple(sorted(e)) for e in edges if e[0] in V and e[1] in V]
    eset = set(es)
    el = [('v', v) for v in vertices] + [('e', e) for e in es]
    q = len(el)
    a = [set() for _ in range(q)]
    for i in range(q):
        x = el[i]
        for j in range(i+1, q):
            y = el[j]
            if x[0] == y[0] == 'v':
                ok = tuple(sorted((x[1], y[1]))) in eset
            elif x[0] == y[0] == 'e':
                ok = bool(set(x[1]) & set(y[1]))
            else:
                v = x[1] if x[0] == 'v' else y[1]
                e = y[1] if x[0] == 'v' else x[1]
                ok = v in e
            if ok:
                a[i].add(j); a[j].add(i)
    return a


def distances(a):
    n = len(a); INF = 10**6
    d = [[INF] * n for _ in range(n)]
    for s in range(n):
        d[s][s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in a[u]:
                if d[s][v] == INF:
                    d[s][v] = d[s][u] + 1; q.append(v)
    return d


def alpha(a, allowed=None):
    n = len(a)
    if allowed is None:
        allowed = (1 << n) - 1
    nbr = [sum(1 << v for v in a[u]) for u in range(n)]
    @lru_cache(None)
    def f(mask):
        if not mask:
            return 0
        mm = mask; best = -1; bd = -1
        while mm:
            bit = mm & -mm; u = bit.bit_length() - 1; mm -= bit
            deg = (nbr[u] & mask).bit_count()
            if deg > bd:
                best, bd = u, deg
        return max(f(mask & ~(1 << best)),
                   1 + f(mask & ~(1 << best) & ~nbr[best]))
    return f(allowed)


def packing_chi_component(a):
    q = len(a)
    if q == 1:
        return 1
    d = distances(a)
    diam = max(max(row) for row in d)
    if diam <= 2:
        return q - alpha(a) + 1
    if diam > 3:
        raise AssertionError('unexpected total-graph diameter > 3')
    # With diameter 3, colors >=3 occur at most once.  Enumerate every
    # possible color-2 packing, and choose a maximum independent color-1 set
    # in the remaining vertices.
    compat = [set(v for v in range(q) if v != u and d[u][v] >= 3) for u in range(q)]
    best = 0
    full = (1 << q) - 1
    def rec(chosen, candidates):
        nonlocal best
        if chosen:
            mask = full
            for v in chosen:
                mask &= ~(1 << v)
            best = max(best, len(chosen) + alpha(a, mask))
        candidates = list(candidates)
        while candidates:
            v = candidates.pop()
            rec(chosen + [v], [w for w in candidates if w in compat[v]])
    rec([], range(q))
    return q + 2 - best


def packing_total_chi(n, edges):
    vals = []
    for c in components(n, edges):
        vals.append(packing_chi_component(total_graph(c, edges)))
    return max(vals)


def singleton_edge(parts, edge):
    if len(parts) != 3 or parts[1:] != (1, 1) or parts[0] < 2:
        return False
    return set(edge) == {parts[0], parts[0] + 1}


types = 0
edge_deletions = 0
exceptional_equalities = 0
for order in range(2, 9):
    for parts in partitions(order):
        if len(parts) < 2:
            continue
        n, edges = complete_multipartite(parts)
        value = packing_total_chi(n, edges)
        m = len(edges)
        n1, n2 = parts[0], parts[1]
        S = n - n1
        formula = m + 1 + max(n2, (S + 1) // 2)
        assert value == formula, (parts, value, formula)
        types += 1
        for e in edges:
            reduced = [f for f in edges if f != e]
            value2 = packing_total_chi(n, reduced)
            equal = value2 == value
            expected_equal = singleton_edge(parts, e)
            assert equal == expected_equal, (parts, e, value, value2, expected_equal)
            edge_deletions += 1
            exceptional_equalities += int(equal)

print('ALL CHECKS PASSED; multipartite_types=%d; edge_deletions=%d; max_order=8; exceptional_equalities=%d' %
      (types, edge_deletions, exceptional_equalities))
