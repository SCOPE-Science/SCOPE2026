#!/usr/bin/env python3
"""Exact-rational finite checks for the vertex covariance of simplex-sum stellohedra.

Requires only Python's standard library. This is a finite independent check,
not a substitute for the all-dimensional argument in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial


def analytic(m):
    z = sum((Q(1, factorial(j)) for j in range(m + 1)), Q(0))
    v = sum((Q(2**j, factorial(j)) for j in range(m + 1)), Q(0)) / z
    w = sum((Q(4**j, factorial(j)) for j in range(m + 1)), Q(0)) / z
    a = Q(m + 1, m) * (w - v * v)
    c = (Q(4**m) - w) / (3 * (m - 1)) - (
        Q(4**m) - 2**(m + 1) * v + w
    ) / (m * (m - 1))
    return a, c, v


def vertex_from_order(order, m):
    # Index 0 is the hub; indices 1,...,m are leaves.
    tubes = [(0,)] + [(j,) for j in range(1, m + 1)]
    tubes += [(0,) + tuple(j + 1 for j in range(m) if mask & (1 << j))
              for mask in range(1, 1 << m)]
    priority = {label: idx for idx, label in enumerate(order)}
    coords = [0] * (m + 1)
    for tube in tubes:
        coords[min(tube, key=priority.__getitem__)] += 1
    return tuple(coords)


def exact_bruteforce(m):
    verts = {vertex_from_order(perm, m) for perm in permutations(range(m + 1))}
    n = len(verts)
    expected = factorial(m) * sum(Q(1, factorial(j)) for j in range(m+1))
    assert n == expected, (m, n, expected)
    p = [sum(Q(v[i], n) for v in verts) for i in range(m + 1)]
    cov = [[sum(Q((v[i]-p[i]) * (v[j]-p[j]), n) for v in verts)
            for j in range(m + 1)] for i in range(m + 1)]
    a = Q(m + 1, m) * cov[0][0]
    c = cov[1][1] - cov[1][2]
    target_a, target_c, target_h = analytic(m)
    assert (a, c, p[0]) == (target_a, target_c, target_h), (m, a, c)
    assert sum(p) == m + 2**m
    assert all(sum(cov[i]) == 0 for i in range(m + 1))
    assert all(cov[i][j] == cov[1][2]
               for i in range(1, m + 1) for j in range(1, m + 1) if i != j)
    assert all(cov[i][i] == cov[1][1] for i in range(1, m + 1))
    return n


def main():
    total = sum(exact_bruteforce(m) for m in range(2, 7))
    for m in range(2, 65):
        a, c, _ = analytic(m)
        assert (a > c) == (m <= 3)
    print('STELLOHEDRON_VERTEX_COVARIANCE_CHECKS_PASSED',
          'dimensions=5', 'vertices=', total, 'spectral_tests=63')


if __name__ == '__main__':
    main()
