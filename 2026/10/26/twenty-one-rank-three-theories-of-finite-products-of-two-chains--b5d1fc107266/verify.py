#!/usr/bin/env python3
"""Exact first-order rank-three census for products of two finite chains.

Use: python3 verify.py
The only dependencies are Python's standard library.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations_with_replacement


def make_grid(a, b):
    assert a > 0 and b > 0
    points = [(i, j) for i in range(a) for j in range(b)]
    le = tuple(tuple(int(i <= k and j <= ell) for k, ell in points)
               for i, j in points)
    return le


def relation(le, x, y):
    if x == y:
        return 1
    if le[x][y]:
        return 2
    if le[y][x]:
        return 3
    return 0


def canonical_type(le):
    """The full finite-rank Hintikka type in the one-binary-relation language.

    Rank 0 with three free variables is the full atomic diagram of a
    triple.  Rank 1 of a pair is the set of all extension diagrams;
    rank 2 of one element is the set of rank-1 pair types; rank 3 of
    the structure is the set of rank-2 element types. The dual
    universal conditions are implicit because the complete set of
    extension types is recorded, not only some existential witnesses.
    """
    n = len(le)
    atom = tuple(tuple(relation(le, x, y) for y in range(n))
                 for x in range(n))
    rank1 = tuple(tuple(frozenset((atom[x][y], atom[x][z], atom[y][z])
                                   for z in range(n)) for y in range(n))
                  for x in range(n))
    rank2 = tuple(frozenset(rank1[x][y] for y in range(n))
                  for x in range(n))
    return frozenset(rank2)


def independent_type(le):
    """Independent full atomic-diagram representation of the recursion."""
    n = len(le)
    triples = tuple(tuple(tuple(tuple(le[u][v] for u in (x, y, z)
                                     for v in (x, y, z))
                               for z in range(n)) for y in range(n))
                     for x in range(n))
    first = tuple(tuple(frozenset(triples[x][y]) for y in range(n))
                  for x in range(n))
    second = tuple(frozenset(first[x]) for x in range(n))
    return frozenset(second)


def direct_game(le1, le2, q):
    """Independent finite EF game recursion for tiny verification pairs."""
    n1, n2 = len(le1), len(le2)

    @lru_cache(maxsize=None)
    def can_survive(p, h, k):
        assert len(p) == len(h)
        for i in range(len(p)):
            for j in range(len(p)):
                if (p[i] == p[j]) != (h[i] == h[j]):
                    return False
                if le1[p[i]][p[j]] != le2[h[i]][h[j]]:
                    return False
        if k == 0:
            return True
        for x in range(n1):
            if not any(can_survive(p+(x,), h+(y,), k-1)
                       for y in range(n2)):
                return False
        for y in range(n2):
            if not any(can_survive(p+(x,), h+(y,), k-1)
                       for x in range(n1)):
                return False
        return True

    return can_survive((), (), q)


def main():
    types = {}
    for a in range(1, 8):
        for b in range(a, 8):
            le = make_grid(a, b)
            t = canonical_type(le)
            # The second implementation uses different literal encodings;
            # compare the equality partitions, not the raw encodings.
            types[(a, b)] = t
    alt = {ab: independent_type(make_grid(*ab)) for ab in types}
    assert all((types[u] == types[v]) == (alt[u] == alt[v])
               for u in types for v in types)
    groups = defaultdict(list)
    for ab, t in types.items():
        groups[t].append(ab)
    groups = sorted(groups.values(), key=lambda g: (min(a*b for a,b in g),g[0]))
    assert len(groups) == 21
    labels = {ab: i+1 for i, g in enumerate(groups) for ab in g}
    assert len(labels) == 28
    assert labels[(5, 6)] == labels[(6, 6)] == labels[(7, 7)] == 21
    assert labels[(5, 5)] != labels[(5, 6)]
    assert labels[(2, 6)] == labels[(2, 7)]
    assert labels[(3, 6)] == labels[(3, 7)]
    assert labels[(4, 6)] == labels[(4, 7)]
    assert labels[(1, 6)] != labels[(1, 7)]
    sizes = [min(a*b for a,b in g) for g in groups]
    assert max(sizes) == 30
    assert sorted(sizes)[-2] == 25
    for a in range(1, 8):
        print('RANK_THREE_MATRIX',a,
              ' '.join('%d:%d' % (b,labels[a,b]) for b in range(a,8)))
    print('EXACT_CANONICAL_OK', 'models=28', 'classes=21', 'type_algorithms=2')
    print('CLASS_REPRESENTATIVES', ' '.join('%d=%sx%s' %
          (i+1,*min(g,key=lambda t:t[0]*t[1])) for i,g in enumerate(groups)))
    # Supplemental instances outside the seven-element coordinate cutoff.
    for a,b in ((1,8),(2,8),(3,9),(4,10),(5,8),(6,9),(7,9),(8,8),(8,10),(11,12)):
        assert canonical_type(make_grid(a,b)) == types[tuple(sorted((min(a,7), min(b,7))))]
    print('SUPPLEMENTAL_CUTOFF_OK', 'instances=10', 'maximal_coordinates=11x12')
    small = [(a,b) for a in range(1,7) for b in range(a,7) if a*b <=6]
    for u in small:
        for v in small:
            actual = direct_game(make_grid(*u), make_grid(*v), 3)
            expect = (types[u] == types[v])
            assert actual == expect, (u,v, actual, expect)
    print('DIRECT_GAME_OK', 'models=%d' % len(small),
          'ordered_comparisons=%d' %(len(small)**2))
    print('SHARP_BOUND_OK', 'minimum_maximum_representative=30',
          'uniquely_represented_by=5x6')
    print('VERIFY_OK')

if __name__ == '__main__':main()
