#!/usr/bin/env python3
"""Reproducible finite-grid checks for an SSH Lindblad rapidity-gap law.

Python standard library only. These samples do not certify the all-size theorem.
"""
import cmath
import math


def gap_direct(n, a, b, g):
    values = []
    for j in range(n):
        q = 2.0 * math.pi * j / n
        d = a * a + b * b - g * g + 2.0 * a * b * math.cos(q)
        d += 2j * b * g * math.sin(q)
        y = abs(cmath.sqrt(d).imag)
        values.append(2.0 * (g - y))
    return min(values)


def leading(n, a, b, g):
    theta = math.acos(-a / b) / (2.0 * math.pi)
    dist = abs(n * theta - round(n * theta))
    kappa = g * (b * b - a * a) / (b * b - a * a + g * g)
    return 4.0 * math.pi * math.pi * kappa * dist ** 2 / n ** 2


def run():
    a, b, g = 0.5, 1.0, 1.5  # theta = 1/3
    for n in (15, 30, 60):
        gap = gap_direct(n, a, b, g)
        assert abs(gap) < 1.e-11, (n, gap)
        print('rational exact zero', n, format(gap, '.9g'))
    for n in (31, 61, 101, 301):
        observed = gap_direct(n, a, b, g)
        predicted = leading(n, a, b, g)
        ratio = observed / predicted
        print('rational positive', n, format(observed, '.9g'),
              'leading', format(predicted, '.9g'), 'ratio', format(ratio, '.9g'))
        assert abs(ratio - 1.0) < 1.0 / (n ** 0.3)
    theta = math.sqrt(2.0) / 5.0  # irrational, in (1/4, 1/2)
    a, b, g = -math.cos(2.0 * math.pi * theta), 1.0, 1.2
    for n in (11, 43, 46, 53, 99):
        observed = gap_direct(n, a, b, g)
        predicted = leading(n, a, b, g)
        ratio = observed / predicted
        print('irrational', n, format(observed, '.9g'),
              'leading', format(predicted, '.9g'), 'ratio', format(ratio, '.9g'))
        assert observed > 0.0
        assert abs(ratio - 1.0) < 0.05
    print('Sample checks passed (not an infinite-dimensional certificate).')


if __name__ == '__main__':
    run()
