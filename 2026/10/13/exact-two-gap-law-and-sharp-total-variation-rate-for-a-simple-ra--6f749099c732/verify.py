#!/usr/bin/env python3
"""Exact checks for the two-gap law of a symmetric nearest-neighbor walk.

Finite enumeration supports the accompanying analytic proof; it is not an
infinite-horizon proof or an independent mathematical audit.
"""
from fractions import Fraction
from itertools import product
from math import comb

STATES = ((0, 0), (0, 1), (1, 1), (1, 2))
LIMIT = {(0, 0): Fraction(1, 4), (0, 1): Fraction(1, 4),
         (1, 1): Fraction(1, 2), (1, 2): Fraction(0)}


def central(k):
    return Fraction(comb(2*k, k), 4**k)


def cvalue(n):
    assert n >= 2
    return Fraction(comb(n - 2, (n - 2)//2), 2**(n - 1))


def predicted(n):
    u, c = central(n//2), cvalue(n)
    return {(0, 0): Fraction(1, 4) - u / 2,
            (0, 1): Fraction(1, 4),
            (1, 1): Fraction(1, 2) + u / 2 - c,
            (1, 2): c}


def enumerate_walks(n):
    counts = {pair: 0 for pair in STATES}
    for increments in product((-1, 1), repeat=n):
        heights = [0]
        for step in increments:
            heights.append(heights[-1] + step)
        ordered = sorted(heights)
        pair = (ordered[1] - ordered[0], ordered[2] - ordered[0])
        assert pair in counts, (n, pair)
        counts[pair] += 1
    return {pair: Fraction(count, 2**n) for pair, count in counts.items()}


def run():
    paths = 0
    for n in range(2, 15):
        observed, formula = enumerate_walks(n), predicted(n)
        assert observed == formula, (n, observed, formula)
        assert sum(formula.values()) == 1 and all(x >= 0 for x in formula.values())
        tv = sum(abs(observed[state] - LIMIT[state]) for state in STATES)/2
        assert tv == cvalue(n), (n, tv)
        paths += 2**n
    for k in range(1, 31):
        assert cvalue(2*k) == central(k - 1)/2
        assert cvalue(2*k + 1) == central(k)/2
        assert central(k - 1) > central(k)
    print(f'VERIFY_OK horizons=13 paths={paths} parity_cases=30 exact_rational=True')


if __name__ == '__main__':
    run()
