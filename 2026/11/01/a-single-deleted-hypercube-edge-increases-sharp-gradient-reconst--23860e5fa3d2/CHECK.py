#!/usr/bin/env python3
"""Exact standalone checks for one-edge-outage Hodge stability on Boolean cubes.

Requires Python 3 and only the standard library. No external files.
"""
from fractions import Fraction as F
from collections import Counter
from math import comb


def edges(d):
    return [(axis, base) for axis in range(d)
            for base in range(1 << d) if not base & (1 << axis)]


def inverse(A):
    """Fractional Gauss-Jordan inverse; raises on singularity."""
    n = len(A)
    aug = [[F(v) for v in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(A)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        factor = aug[k][k]
        aug[k] = [v / factor for v in aug[k]]
        for i in range(n):
            if i == k:
                continue
            factor = aug[i][k]
            if factor:
                aug[i] = [x - factor * y for x, y in zip(aug[i], aug[k])]
    return [row[n:] for row in aug]


def direct_projector(d, E):
    """Grounded vertex-Laplacian inversion, independent of Walsh formula."""
    n = 1 << d
    D = []
    for axis, base in E:
        row = [F(0) for _ in range(n - 1)]
        for v, sign in [(base, 1), (base ^ (1 << axis), -1)]:
            if v:  # pin potential at vertex zero
                row[v - 1] += sign
        D.append(row)
    L = [[sum(row[i] * row[j] for row in D) for j in range(n - 1)]
         for i in range(n - 1)]
    W = inverse(L)
    X = [[sum(W[i][j] * row[j] for j in range(n - 1))
          for i in range(n - 1)] for row in D]
    return [[sum(X[e][i] * D[f][i] for i in range(n - 1))
             for f in range(len(E))] for e in range(len(E))]


def walsh_projector(d, E):
    n = 1 << d
    M = []
    for i, x in E:
        row = []
        for j, y in E:
            total = F(0)
            for S in range(1, n):
                if S & (1 << i) and S & (1 << j):
                    term = F(2, n * S.bit_count())
                    total += -term if ((S & (x ^ y)).bit_count() % 2) else term
            row.append(total)
        M.append(row)
    return M


def exact_prediction(d):
    alpha = F((1 << d) - d - 1,
              (d - 1) * ((d - 2) * (1 << (d - 1)) + 1))
    return F(d + 1, 2) + F(d - 3, 2) * alpha


def check(d):
    E = edges(d)
    assert E[0] == (0, 0)
    full = direct_projector(d, E)
    independent = walsh_projector(d, E)
    assert full == independent
    assert max(sum(map(abs, row)) for row in full) == F(d + 1, 2)
    reduced = direct_projector(d, E[1:])
    q = full[0][0]
    assert q == F((1 << d) - 1, d * (1 << (d - 1)))
    a = full[0][E.index((0, 2))]
    assert a == F((1 << d) - d - 1, d * (d - 1) * (1 << (d - 1)))
    alpha = a / (1 - q)
    assert 0 < alpha <= 1
    for r in range(len(reduced)):
        for c in range(len(reduced)):
            assert reduced[r][c] == (full[r + 1][c + 1] +
                                   full[r + 1][0] * full[0][c + 1] / (1 - q))
    sums = [sum(map(abs, row)) for row in reduced]
    neighbor = E.index((0, 2)) - 1
    assert sums[neighbor] == exact_prediction(d)
    witness = [F(1) if entry >= 0 else F(-1) for entry in reduced[neighbor]]
    assert sum(entry * s for entry, s in zip(reduced[neighbor], witness)) == sums[neighbor]
    if d == 2:
        assert all(v == 1 for v in sums)
    if d == 3:
        assert Counter(sums) == Counter({F(2): 2, F(9, 5): 1,
                                         F(15, 8): 4, F(39, 20): 4})
    if d == 4:
        assert Counter(sums) == Counter({F(133, 51): 3, F(125, 51): 3,
                                         F(41, 17): 1, F(22, 9): 6,
                                         F(42, 17): 12, F(127, 51): 6})
        assert [E[k + 1] for k, v in enumerate(sums) if v == max(sums)] == [
            (0, 2), (0, 4), (0, 8)]
    print(f'd={d}, full_norm={(d + 1)/2}, deleted_norm={max(sums)}, '
          f'adjacent_parallel_row={sums[neighbor]}, edges={len(E)-1}')


if __name__ == '__main__':
    for dim in (2, 3, 4):
        check(dim)
    print('PASS: all claimed finite-dimensional exact certificates')
