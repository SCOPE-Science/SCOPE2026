#!/usr/bin/env python3
"""Exact finite-grid and branching-tree checks for sup-product four-point constants.

These exhaustive finite tests complement, and do not replace, the general proof.
"""
from itertools import combinations, product
from fractions import Fraction


def fourth_constant(distances, size):
    maximum = Fraction(0)
    quartets = 0
    for a, b, c, d in combinations(range(size), 4):
        ab = distances[a][b]
        ac = distances[a][c]
        ad = distances[a][d]
        bc = distances[b][c]
        bd = distances[b][d]
        cd = distances[c][d]
        first, second, third = sorted((ab + cd, ac + bd, ad + bc), reverse=True)
        if second < third or first < second:
            raise AssertionError("invalid ordering")
        value = Fraction(first - second, 2)
        maximum = max(maximum, value)
        quartets += 1
    return maximum, quartets


def interval_grid(tick_lengths):
    # One tick represents a geodesic step of length 1/2.
    points = list(product(*(range(length + 1) for length in tick_lengths)))
    dm = [[max(abs(p[i] - q[i]) for i in range(len(tick_lengths))) for q in points] for p in points]
    delta_in_ticks, quartets = fourth_constant(dm, len(points))
    observed = delta_in_ticks / 2
    expected = Fraction(sorted(tick_lengths, reverse=True)[1], 4)
    assert observed == expected, (tick_lengths, observed, expected)
    return len(points), quartets, observed


def star_product(factors):
    # Each star has one center (0) and n labeled leaves at distance 1.
    # Distinct leaves have distance 2. Branching differs between factors.
    points = list(product(*(range(n + 1) for n in factors)))
    def distance(x, y):
        if x == y:
            return 0
        if x == 0 or y == 0:
            return 1
        return 2
    dm = [[max(distance(p[i], q[i]) for i in range(len(factors))) for q in points] for p in points]
    observed, quartets = fourth_constant(dm, len(points))
    expected = Fraction(1) if min(factors) > 0 else Fraction(0)
    assert observed == expected, (factors, observed, expected)
    return len(points), quartets, observed


if __name__ == '__main__':
    total = 0
    for lengths in ((2, 2), (4, 4), (6, 4), (4, 2, 2), (4, 2, 2, 2), (4, 4, 2)):
        n, quartets, observed = interval_grid(lengths)
        total += quartets
        print(f"interval ticks={lengths}: {n} points, {quartets} exact quartets, delta={observed}")
    for arms in ((2, 2), (3, 2), (2, 2, 2)):
        n, quartets, observed = star_product(arms)
        total += quartets
        print(f"star arms={arms}: {n} points, {quartets} exact quartets, delta={observed}")
    print(f"PASS: {total} exact four-point checks across 9 finite spaces")
