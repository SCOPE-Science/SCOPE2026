#!/usr/bin/env python3
"""Independent finite checks for an exact conditional triangle variance identity.

Standard library only. This is a finite corroboration, not the all-n proof.
Run with: python3 verify.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if n >= k >= 0 else 0


def prediction(n, h, inside, p):
    """Formula in the accompanying theorem; input graph has h labeled vertices."""
    N = n - h
    inside = {tuple(sorted(edge)) for edge in inside}
    degree = [0] * h
    for u, v in inside:
        degree[u] += 1
        degree[v] += 1
    e = len(inside)
    w = sum(choose(d, 2) for d in degree)
    tri = sum(
        all(edge in inside for edge in combinations(vertices, 2))
        for vertices in combinations(range(h), 3)
    )
    mu = tri + e * N * p ** 2 + (choose(N, 3) + h * choose(N, 2)) * p ** 3
    var = (choose(N, 3) + h * choose(N, 2)) * (p ** 3 - p ** 6)
    var += e * N * (p ** 2 - p ** 4)
    var += 2 * choose(N, 2) * (
        choose(N - 2, 2) + 2 * h * (N - 2) + choose(h, 2)
    ) * p ** 5 * (1 - p)
    var += 4 * e * N * (N - 1) * p ** 4 * (1 - p)
    var += 2 * N * w * p ** 3 * (1 - p)
    return mu, var, e, w


def exact_enumeration(n, h, inside, p):
    """Enumerate all independent cross/outside edge outcomes and exact weights."""
    free_edges = [(u, v) for u in range(n) for v in range(u + 1, n) if v >= h]
    triangles = [tuple(combinations(t, 2)) for t in combinations(range(n), 3)]
    inside = {tuple(sorted(edge)) for edge in inside}
    a, b = p.numerator, p.denominator - p.numerator
    m = len(free_edges)
    moment0 = moment1 = moment2 = 0
    for mask in range(1 << m):
        k = mask.bit_count()
        weight = a ** k * b ** (m - k)
        present = inside | {free_edges[j] for j in range(m) if (mask >> j) & 1}
        t = sum(all(edge in present for edge in tri) for tri in triangles)
        moment0 += weight
        moment1 += weight * t
        moment2 += weight * t * t
    mu = Fraction(moment1, moment0)
    return mu, Fraction(moment2, moment0) - mu ** 2


def main():
    tests = 0
    for h, N in [(2, 0), (2, 1), (2, 2), (3, 1), (3, 2),
                 (4, 0), (4, 1), (4, 2), (5, 1)]:
        n = h + N
        inside_universe = list(combinations(range(h), 2))
        masks = range(1 << len(inside_universe)) if h <= 4 else (
            0, 1, 3, 7, 31, 63, 127, 511, 1023
        )
        for mask in masks:
            inside = {edge for j, edge in enumerate(inside_universe) if (mask >> j) & 1}
            for p in (Fraction(1, 3), Fraction(2, 5)):
                predicted = prediction(n, h, inside, p)
                enumerated = exact_enumeration(n, h, inside, p)
                assert predicted[:2] == enumerated, (n, h, inside, p, predicted, enumerated)
                tests += 1
    # The path and claw have h=4 and e=3, but w=2 and 3 respectively.
    path = {(0, 1), (1, 2), (2, 3)}
    claw = {(0, 1), (0, 2), (0, 3)}
    for n in range(4, 50):
        for p in (Fraction(1, 3), Fraction(2, 5), Fraction(5, 7)):
            m1, v1, e1, w1 = prediction(n, 4, path, p)
            m2, v2, e2, w2 = prediction(n, 4, claw, p)
            assert e1 == e2 == 3 and (w1, w2) == (2, 3)
            assert m1 == m2 and v2 - v1 == 2 * (n - 4) * p ** 3 * (1 - p)
            tests += 1
    # Two nonisomorphic 3-regular graphs on six vertices, with different triangle counts.
    k33 = {(u, v) for u in range(3) for v in range(3, 6)}
    prism = {(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5),
             (0, 3), (1, 4), (2, 5)}
    for n in range(6, 20):
        for p in (Fraction(1, 3), Fraction(2, 5)):
            m1, v1, e1, w1 = prediction(n, 6, k33, p)
            m2, v2, e2, w2 = prediction(n, 6, prism, p)
            assert e1 == e2 == 9 and w1 == w2 == 18 and v1 == v2
            assert m2 - m1 == 2
            tests += 1
    print('PASS: ' + str(tests) + ' exact independent checks; no external files or packages required.')


if __name__ == '__main__':
    main()
