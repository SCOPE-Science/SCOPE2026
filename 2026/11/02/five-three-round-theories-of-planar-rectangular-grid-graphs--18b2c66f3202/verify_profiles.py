#!/usr/bin/env python3
"""Exact three-round pointed extension profiles for Cartesian path grids.
Only Python standard library is used. Run: python verify_profiles.py
"""
from collections import Counter


def neighbors(m, n):
    graph = []
    for i in range(m):
        for j in range(n):
            u = set()
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n:
                    u.add(x*n+y)
            graph.append(u)
    return graph


def pair_type(G, u, v):
    if u == v:
        assert any(w != u and w in G[u] for w in range(len(G)))
        assert any(w != u and w not in G[u] for w in range(len(G)))
        return 'D'
    counts = Counter((w in G[u], w in G[v]) for w in range(len(G))
                     if w != u and w != v)
    p11 = counts[True, True] > 0
    p10 = counts[True, False] > 0
    p01 = counts[False, True] > 0
    p00 = counts[False, False] > 0
    if v in G[u]:
        assert not p11 and p10 and p01
        return 'E1' if p00 else 'E0'
    if p11:
        if p10 and p01:
            return 'F'
        if not p10 and p01:
            return 'G'
        if p10 and not p01:
            return 'H'
        assert not p10 and not p01 and not p00
        return 'K'
    assert p10 and p01
    return 'I1' if p00 else 'I0'


def type_of_grid(m, n):
    G = neighbors(m, n)
    return frozenset(frozenset(pair_type(G, u, v) for v in range(len(G)))
                     for u in range(len(G)))


D = 'D'
A = frozenset({'D', 'E1', 'F', 'G', 'I1'})
B = frozenset({'D', 'E1', 'F', 'H', 'I1'})
C = frozenset({'D', 'E1', 'F', 'I1'})
EXCEPTIONS = {
    (2, 2): frozenset([frozenset({'D','E0','K'})]),
    (2, 3): frozenset([frozenset({'D','E1','F','G','I0'}),
                       frozenset({'D','E0','E1','H'})]),
    (2, 4): frozenset([A, B]),
    (3, 3): frozenset([A, C, frozenset({'D', 'E1', 'H'})]),
}
TAIL = frozenset([A, B, C])


def expected(m, n):
    return EXCEPTIONS.get((m, n), TAIL)


def main():
    total = 0
    for m in range(2, 13):
        for n in range(m, 13):
            actual = type_of_grid(m, n)
            want = expected(m, n)
            assert actual == want, (m, n, actual, want)
            total += 1
    print('PROFILE_CHECK_PASS')
    print('rectangles_checked=', total)
    print('parameter_range=2<=m<=n<=12')
    print('pair_pointed_type_classes=', len(set(expected(m,n)
        for m in range(2,13) for n in range(m,13))))
    for m,n in ((2,2),(2,3),(2,4),(3,3),(2,5),(3,4)):
        print('grid=',m,n,'vertices=',m*n,'singleton_profiles=',
              sorted([','.join(sorted(x)) for x in type_of_grid(m,n)]))


if __name__ == '__main__':
    main()
