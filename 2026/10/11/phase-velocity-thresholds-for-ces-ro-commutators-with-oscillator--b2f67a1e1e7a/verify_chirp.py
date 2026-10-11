#!/usr/bin/env python3
"""Finite quadrature checks of an analytic exponential-kernel asymptotic.

No finite computation is used to justify operator-ideal membership.
"""
import math


def integrate_simpson(func, upper=35.0, n=14000):
    assert n % 2 == 0
    h = upper / n
    total = func(0.0) + func(upper)
    for k in range(1, n):
        total += (4 if k % 2 else 2) * func(k * h)
    return total * h / 3.0


def phase_delta(theta, s, t):
    return (1 + s) ** theta * math.expm1(theta * math.log1p(t / (1 + s)))


def j_value(theta, s):
    return integrate_simpson(lambda t: math.exp(-t) * 4 * math.sin(phase_delta(theta, s, t) / 2) ** 2)


if __name__ == '__main__':
    s = 10000.0
    for theta in (0.25, 0.5, 0.75):
        speed = theta * (1 + s) ** (theta - 1)
        ratio = j_value(theta, s) / (2 * speed * speed)
        print('theta', theta, 'density_ratio', round(ratio, 7))
        assert abs(ratio - 1.0) < 0.02, (theta, ratio)
    j_one = j_value(1.0, s)
    print('theta', 1, 'density', round(j_one, 7))
    assert abs(j_one - 1.0) < 0.001, j_one
    print('CHIRP_FINITE_DIAGNOSTIC_OK')
