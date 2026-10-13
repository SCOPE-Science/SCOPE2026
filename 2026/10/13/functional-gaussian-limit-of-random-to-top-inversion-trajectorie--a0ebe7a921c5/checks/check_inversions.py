#!/usr/bin/env python3
"""Exact small-deck cross-checks for the random-to-top inversion trajectory."""
from itertools import permutations
from collections import defaultdict
from fractions import Fraction


def inversions(p):
    return sum(v > w for j, v in enumerate(p) for w in p[j + 1:])


def falling(n, k):
    z = 1
    for j in range(k):
        z *= n - j
    return z if k <= n else 0


def formula_variance(n, r):
    a = Fraction(n - 2, n) ** r
    b = Fraction(n - 3, n) ** r
    c = Fraction(n - 4, n) ** r
    return (Fraction(n * (n - 1) * (2 * n + 5), 72)
            + Fraction(2 * falling(n, 3), 9) * b
            + Fraction(falling(n, 4), 16) * c
            - Fraction(falling(n, 2) ** 2, 16) * a * a)


def move_to_front(p, j):
    return (p[j],) + p[:j] + p[j + 1:]


regressions = 0
for n in range(2, 8):
    for p in permutations(range(n)):
        v = inversions(p)
        mean_step = Fraction(sum(inversions(move_to_front(p, j)) for j in range(n)), n)
        assert mean_step == Fraction(n - 1, 2) + Fraction(n - 2, n) * v
        regressions += 1

moments = 0
for n in range(2, 7):
    counts = {tuple(range(n)): 1}
    for k in range(8):
        denominator = sum(counts.values())
        mean = Fraction(sum(cnt * inversions(p) for p, cnt in counts.items()), denominator)
        second = Fraction(sum(cnt * inversions(p) ** 2 for p, cnt in counts.items()), denominator)
        assert second - mean * mean == formula_variance(n, k), (n, k)
        assert mean == Fraction(n * (n - 1), 4) * (1 - Fraction(n - 2, n) ** k)
        moments += 1
        if k < 7:
            nxt = defaultdict(int)
            for p, cnt in counts.items():
                for j in range(n):
                    nxt[move_to_front(p, j)] += cnt
            counts = nxt

print(f"PASS: {regressions} exact conditional regressions; {moments} exact finite-time moment pairs")
