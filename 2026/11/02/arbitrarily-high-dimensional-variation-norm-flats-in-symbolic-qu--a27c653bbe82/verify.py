#!/usr/bin/env python3
"""Exact illustrative finite checks of periodic ratios for a locally constant three-cell partition."""
from fractions import Fraction
from itertools import product

def cell(p, j):
    n = len(p)
    a = tuple(p[(j + i) % n] for i in range(3))
    if a == (1, 1, 1):
        return 1
    if a in ((0, 1, 0), (1, 0, 1)):
        return 2
    return 0

def ratio(word, numerator, denominator):
    c = [0, 0, 0]
    for i in range(len(word)):
        c[cell(word, i)] += 1
    return Fraction(sum(c[i] * numerator[i] for i in range(3)),
                    sum(c[i] * denominator[i] for i in range(3)))

witnesses = ((0,), (1,), (0, 1))
tested = 0
for numerator, denominator in [((2, 3, 5), (7, 11, 13)),
                               ((12, 1, 9), (2, 8, 6))]:
    coordinates = [Fraction(a, b) for a, b in zip(numerator, denominator)]
    low, high = min(coordinates), max(coordinates)
    assert set(ratio(w, numerator, denominator) for w in witnesses) == set(coordinates)
    for n in range(1, 13):
        for word in product((0, 1), repeat=n):
            q = ratio(word, numerator, denominator)
            assert low <= q <= high, (word, q, low, high)
            tested += 1
    print(f"EXACT_PERIODIC_RATIO_BOUNDS_PASS low={low} high={high}")
print(f"TOTAL_FINITE_WORDS_CHECKED {tested}")
print("FINITE_CHECKS_NOT_AN_INFINITE_PROOF")
