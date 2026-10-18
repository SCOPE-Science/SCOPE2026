#!/usr/bin/env python3
"""Check clique and facet enumeration for rank-one Boolean idempotents."""
from collections import Counter, deque
from itertools import combinations
from math import comb, factorial


def choose_clique(n, k, maximal=False):
    if k == 0:
        return 1 if not maximal else 0
    base = (1 << (k + 1)) + k - (2 if maximal else 1)
    numerator = sum((-1) ** j * comb(k, j) * (base - j) ** n
                    for j in range(k + 1))
    assert numerator % factorial(k) == 0
    return numerator // factorial(k)


def pairs(n):
    return [(u, v) for u in range(1, 1 << n)
            for v in range(1, 1 << n) if u & v]


def matrix(n, u, v):
    return tuple(v if (u & (1 << i)) else 0 for i in range(n))


def product(n, x, y):
    out = []
    for row in x:
        r, bits = 0, row
        while bits:
            lsb = bits & -bits
            r |= y[lsb.bit_length() - 1]
            bits -= lsb
        out.append(r)
    return tuple(out)


def neighbors(n, use_literal):
    vertex = pairs(n)
    N = len(vertex)
    adj = [0] * N
    mats = [matrix(n, *v) for v in vertex]
    for a in range(N):
        u, v = vertex[a]
        for b in range(a + 1, N):
            w, z = vertex[b]
            if use_literal:
                commute = product(n, mats[a], mats[b]) == product(n, mats[b], mats[a])
                assert commute == (not (v & w or z & u))
            else:
                commute = not (v & w or z & u)
            if commute:
                adj[a] |= 1 << b
                adj[b] |= 1 << a
    return vertex, adj


def degree_distribution_formula(n):
    return Counter({}) + sum((Counter({(1 << u) * (4 ** s - 3 ** s):
                 comb(n, s) * comb(n-s, u) * (1 << u)})
                 for s in range(n) for u in range(n - s)), Counter())


def clique_census(adj):
    # DFS visits every unordered clique exactly once, in ascending vertex order.
    counts, maximal = Counter(), Counter()
    N = len(adj)
    allv = (1 << N) - 1
    def walk(depth, possible, common):
        while possible:
            bit = possible & -possible
            possible ^= bit
            idx = bit.bit_length() - 1
            newcommon = common & adj[idx]
            counts[depth + 1] += 1
            if newcommon == 0:
                maximal[depth + 1] += 1
            walk(depth + 1, possible & adj[idx], newcommon)
    walk(0, allv, allv)
    return counts, maximal


def graph_diameter_nonisolated(adj):
    live = [i for i, m in enumerate(adj) if m]
    if not live:
        return 0
    assert len(live) + sum(not m for m in adj) == len(adj)
    overall = 0
    for src in live:
        dist = {src: 0}
        queue = deque([src])
        while queue:
            x = queue.popleft()
            bits = adj[x]
            while bits:
                bit = bits & -bits
                bits -= bit
                y = bit.bit_length() - 1
                if y not in dist:
                    dist[y] = dist[x] + 1
                    queue.append(y)
        assert len(dist) == len(live)
        overall = max(overall, max(dist.values()))
    return overall


def main():
    for n in range(2, 6):
        verts, adj = neighbors(n, use_literal=(n <= 4))
        assert len(verts) == 4 ** n - 3 ** n
        count, maximal = clique_census(adj)
        for k in range(1, n + 1):
            assert count[k] == choose_clique(n, k), (n, k, count[k])
            assert maximal[k] == choose_clique(n, k, True), (n, k, maximal[k])
        assert not any(count[k] for k in range(n + 1, n + 5))
        assert count[n] == maximal[n] == 1
        assert max(adj[i].bit_count() for i in range(len(adj))) == 4 ** (n - 1) - 3 ** (n - 1)
        degrees = Counter(a.bit_count() for a in adj)
        expected = degree_distribution_formula(n)
        assert degrees == expected, (n, degrees, expected)
        assert degrees[0] == 3 ** n - 2 ** n
        assert count[2] == (9 ** n - 2 * 8 ** n + 7 ** n) // 2
        diameter = graph_diameter_nonisolated(adj)
        assert diameter == (1 if n == 2 else 3)
        print('n=', n, 'vertices=', len(verts), 'cliques=', [count[k] for k in range(1,n+1)],
              'facets=', [maximal[k] for k in range(1,n+1)], 'diameter=',diameter)
    # Algebraic boundary and integer checks beyond the brute-force graph range.
    for n in range(6, 14):
        assert choose_clique(n, n) == choose_clique(n, n, True) == 1
        for k in range(1, n + 1):
            assert 0 < choose_clique(n, k, True) <= choose_clique(n, k)
        assert choose_clique(n, 1, True) == 3 ** n - 2 ** n
    print('VERIFY_OK_BOOLEAN_RANK_ONE_IDEMPOTENT_CLIQUES')

if __name__ == '__main__':
    main()
