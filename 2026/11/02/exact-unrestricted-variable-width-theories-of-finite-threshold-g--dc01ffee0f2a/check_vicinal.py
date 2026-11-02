#!/usr/bin/env python3
"""Reproducible finite structural checks for threshold graphs.

Run: python3 check_vicinal.py
Python 3 standard library only.
"""
from itertools import product


def adjacency(bits):
    # First vertex is unmarked; each later 0 is isolated, 1 universal.
    n = len(bits) + 1
    a = [[False] * n for _ in range(n)]
    for i, flag in enumerate(bits, start=1):
        if flag:
            for j in range(i):
                a[i][j] = a[j][i] = True
    return a


def quotient(a):
    n = len(a)
    dominates = [[all(not a[x][z] or a[y][z]
                      for z in range(n) if z != x and z != y)
                  for y in range(n)] for x in range(n)]
    assert all(dominates[x][y] or dominates[y][x]
               for x in range(n) for y in range(n)), 'non-total order'
    assert all(not (dominates[x][y] and dominates[y][z]) or dominates[x][z]
               for x in range(n) for y in range(n) for z in range(n)), 'not transitive'
    classes = []
    for x in range(n):
        if not any(x in c for c in classes):
            classes.append([y for y in range(n) if dominates[x][y] and dominates[y][x]])
    classes.sort(key=lambda c: sum(dominates[x][c[0]] and
                                   not dominates[c[0]][x]
                                   for x in range(n)))
    # The sort key above is the number of strictly lower vertices.
    assert all(dominates[classes[i][0]][classes[j][0]] and
               not dominates[classes[j][0]][classes[i][0]]
               for i in range(len(classes)) for j in range(i + 1, len(classes)))
    edge_pattern = tuple(tuple(int(a[c[0]][d[0]]) for d in classes[i + 1:])
                         for i, c in enumerate(classes))
    internals = []
    for c in classes:
        edges = {a[x][y] for x in c for y in c if x != y}
        assert len(edges) <= 1
        internals.append(None if len(c) == 1 else int(next(iter(edges))))
    return classes, tuple(internals), edge_pattern


def signature(a, k):
    classes, internals, cross = quotient(a)
    return tuple(min(len(c), k) for c in classes), internals, cross


def induced(a, chosen):
    return [[a[i][j] for j in chosen] for i in chosen]


def main():
    graphs = 0
    max_classes = 0
    counts = {3: {}, 4: {}}
    for n in range(1, 10):
        for bits in product((0, 1), repeat=n - 1):
            a = adjacency(bits)
            classes, internals, cross = quotient(a)
            graphs += 1
            max_classes = max(max_classes, len(classes))
            for k in (3, 4):
                keep = [v for c in classes for v in c[:k]]
                b = induced(a, keep)
                expected = signature(a, k)
                got = signature(b, k)
                assert expected == got, ('compression mismatch', n, bits, k, expected, got)
                counts[k][(n, bits)] = expected
    assert graphs == 511
    # Explicit sharp hierarchy: different star leaf multiplicities.
    for k in (3, 4, 5, 6):
        star_k = adjacency((0,) * (k - 1) + (1,))
        star_next = adjacency((0,) * k + (1,))
        assert signature(star_k, k) == signature(star_next, k)
        assert signature(star_k, k + 1) != signature(star_next, k + 1)
    print('structural instances:', graphs)
    print('maximum twin classes:', max_classes)
    print('compression invariants at widths 3 and 4: PASS')
    print('sharp star boundaries for widths 3,4,5,6: PASS')


if __name__ == '__main__':
    main()
