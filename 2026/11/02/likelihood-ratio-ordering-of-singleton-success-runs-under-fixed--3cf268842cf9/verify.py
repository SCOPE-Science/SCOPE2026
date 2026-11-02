#!/usr/bin/env python3
"""Exact finite checks for singleton one-run likelihood-ratio ordering.

All integer arithmetic uses Python's standard library. Run: python3 verify.py
These finite checks supplement rather than replace the proof in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def composition_count(a, r, s):
    if not (a >= 1 and 1 <= r <= a and 0 <= s <= a):
        return 0
    if a == r:
        return int(s == a)
    if s >= r:
        return 0
    return choose(r, s) * choose(a - r - 1, r - s - 1)


def run_statistics(word):
    runs = []
    length = 0
    for bit in word + (0,):
        if bit:
            length += 1
        elif length:
            runs.append(length)
            length = 0
    return len(runs), sum(k == 1 for k in runs)


def exhaustive_counts(a, b):
    n = a + b
    table = Counter()
    for locations in combinations(range(n), a):
        word = [0] * n
        for i in locations:
            word[i] = 1
        table[run_statistics(tuple(word))] += 1
    return table


def prove_finite_check():
    assertions = 0
    for n in range(3, 14):
        for a in range(2, n):
            b = n - a
            observed = exhaustive_counts(a, b)
            assert sum(observed.values()) == choose(n, a)
            assertions += 1
            R = Fraction(0)
            S = Fraction(0)
            RS = Fraction(0)
            for r in range(1, min(a, b + 1) + 1):
                for s in range(a + 1):
                    expected = choose(b + 1, r) * composition_count(a, r, s)
                    assert observed[(r, s)] == expected, (a, b, r, s)
                    assertions += 1
                    p = Fraction(expected, choose(n, a))
                    R += r * p
                    S += s * p
                    RS += r * s * p
                assert sum(composition_count(a, r, s) for s in range(a + 1)) == choose(a - 1, r - 1)
                assertions += 1
            expected_cov = Fraction(2 * a * b * b * (a - 1) * (b + 1), n * n * (n - 1) * (n - 2))
            assert RS - R*S == expected_cov, (a, b, RS - R*S, expected_cov)
            assertions += 1

    for a in range(2, 65):
        rows = [[composition_count(a, r, s) for s in range(a + 1)] for r in range(1, a + 1)]
        for r in range(a - 1):
            left, right = rows[r], rows[r + 1]
            for lo in range(a + 1):
                for hi in range(lo + 1, a + 1):
                    assert left[lo] * right[hi] >= left[hi] * right[lo], (a, r, lo, hi)
                    assertions += 1
        if a <= 19:
            for i in range(a):
                for j in range(i + 1, a):
                    left, right = rows[i], rows[j]
                    for lo in range(a + 1):
                        for hi in range(lo + 1, a + 1):
                            assert left[lo] * right[hi] >= left[hi] * right[lo], (a, i, j, lo, hi)
                            assertions += 1
    print(f"PASS: {assertions:,} exact assertions; all claims tested in stated finite regimes.")


if __name__ == '__main__':
    prove_finite_check()
