#!/usr/bin/env python3
"""Exact finite tests of the fixed-input-norm sign-class formula.

The theorem for arbitrary dimensions is proved mathematically in RESULT.md.
This program checks small combinatorial instances only.
"""
from fractions import Fraction
from itertools import combinations, product


def check(n, m, weights):
    signs = [(1,) + s for s in product((-1, 1), repeat=n - 1)]
    k = len(signs)
    smallest = min(weights)
    total = sum(weights)
    asserted = Fraction(m * total**2 + (k - m) * (total - 2 * smallest)**2, k)
    maximum = None
    for selected in combinations(range(k), m):
        value = Fraction(sum(
            max(sum(weights[j] * signs[u][j] * signs[v][j] for j in range(n))**2
                for u in selected)
            for v in range(k)), k)
        if maximum is None or value > maximum:
            maximum = value
    assert maximum == asserted, (n, m, weights, maximum, asserted)


def main():
    count = 0
    for n in range(2, 5):
        k = 2**(n - 1)
        for m in range(k // 2, k + 1):
            profiles = [
                (Fraction(1),) * n,
                (Fraction(1),) * (n - 1) + (Fraction(1, 2),),
                (Fraction(2),) + (Fraction(1),) * (n - 1),
            ]
            for profile in profiles:
                check(n, m, profile)
                count += 1
    assert count == 30
    print('PASS', count, 'exact-rational combinatorial checks')


if __name__ == '__main__':
    main()
