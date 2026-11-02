#!/usr/bin/env python3
"""Exact small-instance checks for the bipartite best-shot dynamics theorem.

Only standard-library arithmetic is used. This finite verifier corroborates, but
cannot replace, the all-size argument in RESULT.md.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb


def h(n):
    assert n >= 0
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def joint_a(i, j, k):
    assert i > 0 and j > 0 and 1 <= k <= i
    return Fraction(comb(i + j - k - 1, j - 1), comb(i + j, j))


def joint_b(i, j, ell):
    assert i > 0 and j > 0 and 1 <= ell <= j
    return Fraction(comb(i + j - ell - 1, i - 1), comb(i + j, i))


def predicted_prob(a, b, i, j):
    if i + j == 0:
        return Fraction(a, a + b)
    if j == 0:
        return Fraction(1)
    if i == 0:
        return Fraction(0)
    return Fraction(i, i + j)


def predicted_steps(a, b, i, j):
    n = a + b
    if not (i or j):
        return 1 + a * h(a - 1) + b * h(b - 1)
    if j == 0:
        return n * h(a - i)
    if i == 0:
        return n * h(b - j)
    expected_t = h(i) + h(j) - h(i + j)
    expected_t += sum((joint_a(i, j, k) * h(a - k)
                       for k in range(1, i + 1)), Fraction(0))
    expected_t += sum((joint_b(i, j, ell) * h(b - ell)
                       for ell in range(1, j + 1)), Fraction(0))
    return n * expected_t


def independent_dp(a, b):
    n = a + b

    @lru_cache(None)
    def probability(i, j):
        if i + j == 0:
            return Fraction(a, n)
        if j == 0:
            return Fraction(1)
        if i == 0:
            return Fraction(0)
        return (i * probability(i - 1, j) + j * probability(i, j - 1)) / (i + j)

    @lru_cache(None)
    def steps(i, j):
        if i + j == 0:
            return 1 + Fraction(a, n) * steps(1, 0) + Fraction(b, n) * steps(0, 1)
        if j == 0:
            return n * h(a - i)
        if i == 0:
            return n * h(b - j)
        return (n + i * steps(i - 1, j) + j * steps(i, j - 1)) / (i + j)

    return probability, steps


count = 0
for a in range(1, 9):
    for b in range(1, 9):
        probability, steps = independent_dp(a, b)
        for i in range(a + 1):
            for j in range(b + 1):
                assert predicted_prob(a, b, i, j) == probability(i, j), (a, b, i, j)
                assert predicted_steps(a, b, i, j) == steps(i, j), (a, b, i, j)
                if i and j:
                    assert sum((joint_a(i, j, k) for k in range(1, i + 1)), Fraction(0)) == Fraction(i, i + j)
                    assert sum((joint_b(i, j, ell) for ell in range(1, j + 1)), Fraction(0)) == Fraction(j, i + j)
                count += 1
print(f"PASS: {count} exact rational states, two independent recurrences; suffix mass checked")
