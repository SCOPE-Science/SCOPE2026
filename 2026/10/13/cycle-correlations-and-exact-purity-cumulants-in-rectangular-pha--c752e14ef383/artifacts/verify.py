#!/usr/bin/env python3
"""Exact Laurent-coefficient checks for random-phase reduced purity."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations


def nonconstant_purity(d, m):
    # Q = (dm)^2(P - E[P]); every nonconstant oriented rectangle term
    # appears with coefficient 2 after merging the ordered row pairs.
    poly = Counter()
    for a, b in combinations(range(d), 2):
        for j, k in combinations(range(m), 2):
            exponent = [0] * (d * m)
            exponent[a * m + j] += 1
            exponent[a * m + k] -= 1
            exponent[b * m + j] -= 1
            exponent[b * m + k] += 1
            e = tuple(exponent)
            poly[e] += 2
            poly[tuple(-x for x in e)] += 2
    return poly


def phase_cumulants(d, m):
    poly = nonconstant_purity(d, m)
    second = sum(c * poly.get(tuple(-x for x in e), 0)
                 for e, c in poly.items())
    third = sum(c * f * poly.get(tuple(-x - y for x, y in zip(e, g)), 0)
                for e, c in poly.items() for g, f in poly.items())
    return (Fraction(second, (d * m) ** 4),
            Fraction(third, (d * m) ** 6))


def cycle_centered_product(vertex_count, m, cyclic_edges):
    zero = (0,) * (vertex_count * m)
    poly = {zero: 1}
    for a, b in cyclic_edges:
        successor = defaultdict(int)
        for j in range(m):
            for k in range(m):
                if j == k:
                    continue
                term = [0] * (vertex_count * m)
                term[a * m + j] += 1
                term[a * m + k] -= 1
                term[b * m + j] -= 1
                term[b * m + k] += 1
                for exponent, coefficient in poly.items():
                    successor[tuple(x + y for x, y in zip(exponent, term))] += coefficient
        poly = successor
    return poly.get(zero, 0)


def main():
    cases = [(2, 2), (2, 3), (3, 2), (3, 3), (3, 4), (4, 3)]
    for d, m in cases:
        variance, third = phase_cumulants(d, m)
        required_variance = Fraction(2 * (d - 1) * (m - 1), d**3 * m**3)
        required_third = Fraction(8 * (d - 1) * (m - 1) * (d + m - 4),
                                  d**5 * m**5)
        assert variance == required_variance, (d, m, variance, required_variance)
        assert third == required_third, (d, m, third, required_third)
    for vertex_count in (3, 4):
        cyclic_edges = [(a, (a + 1) % vertex_count)
                        for a in range(vertex_count)]
        for m in (2, 3):
            got = cycle_centered_product(vertex_count, m, cyclic_edges)
            assert got == m * (m - 1), (vertex_count, m, got)
    print('VERIFY_OK dimensions=6 cycle_sizes=3,4 column_counts=2,3 exact_rationals=passed')


if __name__ == '__main__':
    main()
