#!/usr/bin/env python3
"""Exact-rational small-colonization checks for finite habitat graphs.

Run: python3 CHECK.py
Uses only the Python standard library. All numerical graph tests are finite
checks; the all-size statements follow from the written combinatorial proof.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import random


def harmonic(k):
    return sum((Q(1, i) for i in range(1, k + 1)), Q())


def fall(x, t):
    out = 1
    for j in range(t):
        out *= x - j
    return out


def p(n, k, r, s):
    return Q(fall(k, r) * fall(n - k, s), fall(n, r + s))


def uv(k):
    u = Q(2, k * (k - 1)) * ((k + 1) * harmonic(k) - 2 * k) if k > 1 else Q()
    v = (harmonic(k + 1) - 1) / k
    return u, v


def graph_formula(n, m, wedge):
    disjoint_pairs = comb(m, 2) - wedge
    total = Q()
    for k in range(1, n):
        u, v = uv(k)
        up, vp = uv(k + 1)
        edge_cut = 2 * m * p(n, k, 1, 1)
        internal_cut = 2 * wedge * p(n, k, 2, 1) + 4 * disjoint_pairs * p(n, k, 3, 1)
        cut_square = edge_cut + 2 * wedge * p(n, k, 1, 1) + 8 * disjoint_pairs * p(n, k, 2, 2)
        colon_square = edge_cut + 2 * wedge * p(n, k, 2, 1)
        colon_degree = 2 * (m + wedge) * p(n, k, 1, 1)
        total += ((up - u) * internal_cut + (vp - v) * cut_square +
                  (up - 2 * vp) * colon_square + vp * colon_degree) / k
    return total


def subset_series(n, edges, degree=2):
    """Solve the absorbing backward equations coefficient by coefficient."""
    neighbor = [0] * n
    for a, b in edges:
        neighbor[a] |= 1 << b
        neighbor[b] |= 1 << a
    size = 1 << n
    result = [[Q()] * size for _ in range(degree + 1)]
    masks_by_size = [[] for _ in range(n + 1)]
    for mask in range(1, size):
        masks_by_size[mask.bit_count()].append(mask)
    for k in range(1, n + 1):
        for mask in masks_by_size[k]:
            result[0][mask] = (1 + sum((result[0][mask & ~(1 << j)] for j in range(n)
                                        if mask & (1 << j)), Q())) / k
    for order in range(1, degree + 1):
        for k in range(1, n + 1):
            for mask in masks_by_size[k]:
                losses = sum((result[order][mask & ~(1 << j)] for j in range(n)
                              if mask & (1 << j)), Q())
                gains = sum((Q((neighbor[j] & mask).bit_count()) *
                             (result[order - 1][mask | (1 << j)] - result[order - 1][mask])
                             for j in range(n) if not mask & (1 << j)), Q())
                result[order][mask] = (losses + gains) / k
    return tuple(level[size - 1] for level in result)


def degree_invariants(n, edges):
    d = [0] * n
    for x, y in edges:
        d[x] += 1
        d[y] += 1
    return len(edges), sum(comb(t, 2) for t in d)


def first_coefficient(n, edges):
    m = len(edges)
    return m * Q(2, n * (n - 1)) * ((n + 1) * harmonic(n) - 2 * n)


def wedge_coefficient(n):
    return graph_formula(n, 2, 1) - graph_formula(n, 2, 0)


def assert_graph(n, edges):
    m, w = degree_invariants(n, edges)
    actual = subset_series(n, edges)
    assert actual[0] == harmonic(n)
    assert actual[1] == first_coefficient(n, edges)
    assert actual[2] == graph_formula(n, m, w)
    return 1


def positivity_certificate(t, r):
    """Expanded all-positive polynomial in t=k-3, r=n-k-1."""
    return (r*r*(6*t**4+82*t**3+395*t*t+797*t+586)
            +r*(6*t**5+110*t**4+730*t**3+2117*t*t+2585*t+1202)
            +10*t**5+143*t**4+726*t**3+1507*t*t+1034*t+120)


def main():
    count = 0
    for n in (4, 5):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [e for j, e in enumerate(possible) if mask & (1 << j)]
            count += assert_graph(n, edges)
    rng = random.Random(1729)
    for n, samples in ((6, 150), (7, 60), (8, 20)):
        possible = list(combinations(range(n), 2))
        for _ in range(samples):
            edges = [e for e in possible if rng.randrange(2)]
            count += assert_graph(n, edges)
    star = [(0, i) for i in (1, 2, 3)]
    path = [(0, 1), (1, 2), (2, 3)]
    assert subset_series(4, star)[:3] == (Q(25, 12), Q(29, 24), Q(11, 16))
    assert subset_series(4, path)[:3] == (Q(25, 12), Q(29, 24), Q(61, 144))
    assert wedge_coefficient(4) == Q(19, 72)
    for n in range(4, 55):
        assert wedge_coefficient(n) > 0
        for k in range(3, n):
            t, r = k-3, n-k-1
            assert positivity_certificate(t, r) > 0
            harmonic_bound = harmonic(k) >= Q(3) - Q(11, 3*k)
            assert harmonic_bound
    print(f'PASS: {count} independent exact-rational graph comparisons, '
          'two four-vertex coefficients, and 51 universal-positivity spot checks.')
    print('Infinite-graph-size theorem relies on the algebraic positivity certificate in RESULT.md.')


if __name__ == '__main__':
    main()
