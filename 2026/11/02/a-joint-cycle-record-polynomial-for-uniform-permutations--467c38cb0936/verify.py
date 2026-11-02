#!/usr/bin/env python3
"""Exact finite checks for joint cycle/upper-record polynomials.

Usage: python3 verify.py
Only Python's standard library is required.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def poly_product(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for j, av in enumerate(a):
        for k, bv in enumerate(b):
            out[j + k] += av * bv
    return out


def rising_poly(shift, order):
    p = [1]
    for t in range(order):
        p = poly_product(p, [shift + t, 1])
    return p


def cycle_count(perm):
    seen = set()
    count = 0
    for i in range(len(perm)):
        if i not in seen:
            count += 1
            v = i
            while v not in seen:
                seen.add(v)
                v = perm[v]
    return count


def predicted_counts(n, i):
    a = rising_poly(0, n)
    b = poly_product(rising_poly(0, n - i), rising_poly(-1, i))
    return [Fraction(a[j] + (i - 1) * b[j], i) for j in range(n + 1)]


def run():
    objects = 0
    coefficient_checks = 0
    moment_checks = 0
    ewens_checks = 0
    for n in range(2, 9):
        by_pos = {i: Counter() for i in range(2, n + 1)}
        for perm in permutations(range(n)):
            objects += 1
            count = cycle_count(perm)
            maximum = -1
            for i, x in enumerate(perm, start=1):
                if x > maximum:
                    maximum = x
                    if i >= 2:
                        by_pos[i][count] += 1
        for i in range(2, n + 1):
            theory = predicted_counts(n, i)
            for c in range(n + 1):
                assert by_pos[i][c] == theory[c], (n, i, c)
                coefficient_checks += 1
            mean_record_cycle = sum(Fraction(c * by_pos[i][c], factorial(n)) for c in by_pos[i])
            harmonic = sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))
            covariance = mean_record_cycle - harmonic / i
            target = Fraction(i - 1, i * i * comb(n, i))
            assert covariance == target, (n, i, covariance, target)
            moment_checks += 1
            for theta in (Fraction(1, 2), Fraction(1, 1), Fraction(3, 2), Fraction(3, 1)):
                numer = sum(theta ** c * multiplicity for c, multiplicity in by_pos[i].items())
                denom = 1
                for j in range(n):
                    denom *= theta + j
                actual = numer / denom
                rise = lambda a, q: __import__('math').prod(a+j for j in range(q))
                pred = Fraction(1, i) * (1 + (i - 1) * rise(theta - 1, i) / rise(theta + n - i, i))
                assert actual == pred, (n, i, theta, actual, pred)
                ewens_checks += 1
    print('VERIFY_OK')
    print('permutations_enumerated', objects)
    print('exact_coefficient_comparisons', coefficient_checks)
    print('exact_covariance_checks', moment_checks)
    print('exact_ewens_probability_checks', ewens_checks)


if __name__ == '__main__':
    run()
