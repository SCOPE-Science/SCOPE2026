#!/usr/bin/env python3
"""Exact small-instance and numerical checks for a record-count asymptotic."""
from fractions import Fraction
from itertools import product
from math import log, pi, sqrt
EULER_GAMMA = 0.577215664901532860606512090082402431


def exact_expectation(n):
    """Independent-summand form of the exact expected record count."""
    p = Fraction(1)
    total = Fraction(0)
    for k in range(1, n + 1):
        p *= Fraction(n + 1 - k, n + 1)
        total += p * (1 + Fraction(1, k))
    return total


def alternate_expectation(n):
    """Original finite formula before the summation-by-parts reduction."""
    p = Fraction(1)
    total = Fraction(n)
    for k in range(1, n + 1):
        p *= Fraction(n + 1 - k, n + 1)
        total -= Fraction(n - k, k * (k + 1)) * p
    return total


def direct_enumeration(n):
    successful, record_total = 0, 0
    for preferences in product(range(1, n + 1), repeat=n):
        places = [0] * n
        for label, start in enumerate(preferences, 1):
            idx = start - 1
            while idx < n and places[idx]:
                idx += 1
            if idx == n:
                break
            places[idx] = label
        else:
            successful += 1
            high = records = 0
            for label in places:
                if label > high:
                    high = label
                    records += 1
            record_total += records
    return successful, Fraction(record_total, successful)


def numeric_expectation(n):
    p, total, a, b = 1.0, 0.0, 0.0, 0.0
    for k in range(1, n + 1):
        p *= (n + 1 - k) / (n + 1)
        a += p
        b += p / k
        total += p * (1 + 1 / k)
    return total, a, b


def main():
    checks = 0
    for n in range(1, 7):
        count, found = direct_enumeration(n)
        assert count == (n + 1) ** (n - 1)
        assert found == exact_expectation(n)
        assert found == alternate_expectation(n)
        print(f"n={n}: {count} successful preference vectors; exact mean {found}")
        checks += 3
    c = (EULER_GAMMA + log(2)) / 2 - Fraction(4, 3)
    print(f"Additive constant: {c:.12f}")
    tolerance = {1000: 0.005, 10000: 0.002, 100000: 0.0006, 1000000: 0.0002}
    for n, threshold in tolerance.items():
        mean, gauss_sum, harmonic_sum = numeric_expectation(n)
        predicted = sqrt(pi * n / 2) + log(n) / 2 + c
        residual = mean - predicted
        assert abs(residual) < threshold
        assert abs(mean - (gauss_sum + harmonic_sum)) < 1e-8
        print(f"n={n}: exact-sum={mean:.9f}, three-term={predicted:.9f}, residual={residual:+.8f}")
        checks += 2
    print(f"PASSED: {checks} checks (exact enumeration, exact identities, numerical asymptotics)")


if __name__ == '__main__':
    main()
