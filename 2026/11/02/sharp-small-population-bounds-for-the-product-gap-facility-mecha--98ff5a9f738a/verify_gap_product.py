#!/usr/bin/env python3
"""Exact rational finite checks of the product-gap omission theorem.

The infinite statements are proved in RESULT.md, not by enumeration.
"""
from fractions import Fraction
from itertools import combinations, product


def direct_expected(gaps):
    """Enumerate all subsets of k reports among k+1 distinct reports."""
    k = len(gaps)
    x = (0,)
    for gap in gaps:
        x += (x[-1] + gap,)
    num = den = 0
    for indices in combinations(range(k + 1), k):
        selected = [x[j] for j in indices]
        omitted = next(j for j in range(k + 1) if j not in indices)
        weight = 1
        for a, b in zip(selected, selected[1:]):
            weight *= b - a
        cost = min(abs(x[omitted] - z) for z in selected)
        num += weight * cost
        den += weight
    assert den > 0
    return Fraction(num, den)


def closed_expected(gaps):
    k = len(gaps)
    harmonic = sum((Fraction(1, v) for v in gaps), Fraction(0))
    local = sum((Fraction(min(u, v), max(u, v))
                 for u, v in zip(gaps, gaps[1:])), Fraction(0))
    return (k + 1 + local) / (2 * harmonic)


def check():
    cases = 0
    for k in range(2, 9):
        for gaps in product(range(1, 5), repeat=k):
            cost = direct_expected(gaps)
            assert cost == closed_expected(gaps), (k, gaps, cost)
            optimum = min(gaps)
            assert cost / optimum <= Fraction(2 * k - 1, 2)
            if k >= 3 and any(gaps[i] == optimum for i in range(1, k - 1)):
                assert cost / optimum <= k - 1
            cases += 1
        for L in (2, 10, 100, 1000):
            endpoint = (1,) + (L,) * (k - 1)
            assert closed_expected(endpoint) / min(endpoint) == Fraction((2*k-1)*L+1, 2*(L+k-1))
            if k >= 3:
                interior = (L, 1) + (L,) * (k - 2)
                assert closed_expected(interior) / min(interior) < k - 1
    print(f"VERIFY_OK exact_profiles={cases} k=2..8 integer_gaps=1..4 endpoint_and_interior_asymptotic_families=checked")


if __name__ == "__main__":
    check()
