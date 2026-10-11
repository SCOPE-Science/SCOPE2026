"""Exact finite-branch checks for a Bernoulli circle-lift graph construction.

These tests confirm algebraic identities and finite jump accounting.
The almost-sure ergodic assertion is proved mathematically, not by finite tests.
"""
from fractions import Fraction
from itertools import product


def fibre_lift(sign, x):
    if sign == '+':
        return 3*x if x < Fraction(2, 3) else 4-3*x
    return -3*x if x < Fraction(1, 3) else 3*x-2


def value(digits):
    return sum((Fraction(d, 3**(k+1)) for k, d in enumerate(digits)), Fraction(0))


def check():
    total = 0
    for n in range(1, 7):
        for choices in product(range(4), repeat=n):
            signs = ['+' if a < 2 else '-' for a in choices]
            marks = [a % 2 for a in choices]
            digits = [mark + (sign == '-') for sign, mark in zip(signs, marks)]
            for k in range(n):
                x = value(digits[k:])
                tail = value(digits[k+1:])
                assert fibre_lift(signs[k], x) == tail + marks[k] - (signs[k] == '-')
                total += 1
    # Finite staircase with distinct atom locations: ordered jumps sum exactly to 1/2 up to tail.
    for n in range(1, 15):
        weights = [Fraction(1, 3**(k+1)) for k in range(n)]
        threshold = [Fraction((5*k) % (n+1)+1, n+2) for k in range(n)]
        assert sum(weights) == (Fraction(1, 2)-Fraction(1, 2*3**n))
        grid = sorted(set([Fraction(0), Fraction(1)] + threshold))
        vals = [sum((w for t, w in zip(threshold, weights) if t <= l), Fraction(0)) for l in grid]
        assert all(x <= y for x, y in zip(vals, vals[1:]))
    print('FINITE_IDENTITIES_OK', total)


if __name__ == '__main__':
    check()
