#!/usr/bin/env python3
"""Exact finite checks for random-cut increasing affine contractions.
Finite checks do not replace the all-size proof.
"""
from fractions import Fraction
from math import factorial


def compositions(total, parts, positive=False):
    low = 1 if positive else 0
    if parts == 1:
        if total >= low:
            yield (total,)
        return
    for first in range(low, total - low * (parts - 1) + 1):
        for rest in compositions(total - first, parts - 1, positive):
            yield (first,) + rest


def product(values):
    answer = Fraction(1)
    for v in values:
        answer *= v
    return answer


def exact_factorial_moment(n, r):
    N = n + 1
    total = sum((product(Fraction(a ** a, factorial(a)) for a in gaps)
                 for gaps in compositions(N, r + 1, positive=True)), Fraction(0))
    return Fraction(factorial(r) * factorial(N-2), N ** (N-2)) * total


def check(n):
    N = n + 1
    denominator = N ** (n - 1)
    histogram = [0] * (n + 1)
    for bins in compositions(n - 1, N):
        configurations = factorial(n - 1)
        for count in bins:
            configurations = Fraction(configurations, factorial(count))
        assert configurations.denominator == 1
        count_orbits = 0
        prefix = 0
        for i in range(1, n + 1):
            prefix += bins[i - 1]
            count_orbits += int(prefix == i - 1)
        assert 1 <= count_orbits <= n
        histogram[count_orbits] += configurations.numerator
    assert sum(histogram) == denominator
    for r in range(1, n + 1):
        direct = sum((Fraction(histogram[k] * factorial(k),
                               denominator * factorial(k-r))
                      for k in range(r, n + 1)), Fraction(0))
        assert direct == exact_factorial_moment(n, r), (n, r)
    assert histogram[n] == factorial(n - 1)


if __name__ == '__main__':
    for n in range(2, 9):
        check(n)
    print('VERIFY_OK: exact all-path occupancy and factorial moments for n=2..8')
