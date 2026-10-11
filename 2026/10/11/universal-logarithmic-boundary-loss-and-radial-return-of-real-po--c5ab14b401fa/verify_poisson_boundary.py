#!/usr/bin/env python3
"""Independent finite consistency checks for real Poisson norms.

Reproducibility: Python 3 standard library only. The analytic proof,
not the finite checks here, establishes the asymptotic for all real p >= 1.
"""
import math


def moment(p, r, panels=32768):
    assert p >= 1 and 0 < r < 1 and panels % 2 == 0
    a = (1 - r*r)/(2*r)
    step = (math.pi/2)/panels
    total = 0.0
    for k in range(panels + 1):
        angle = k * step
        x = math.cos(angle)
        value = (2/math.pi * math.atan(x/a)) ** p
        weight = (1 if k in (0, panels) else 4 if k % 2 else 2)
        total += weight * value
    return (2/math.pi) * (step/3) * total


def fourier_second_moment(r):
    total = 0.0
    k = 0
    while True:
        term = r ** (4*k + 2) / (2*k + 1)**2
        total += term
        if term < 1e-18 or k > 100000:
            break
        k += 1
    assert k < 100000
    return 8/math.pi**2 * total


def normalized_norm(p, r):
    return moment(p, r) ** (1/p) / r


if __name__ == '__main__':
    checks = 0
    for r in (0.2, 0.6, 0.95, 0.99):
        a = moment(2, r)
        b = fourier_second_moment(r)
        assert abs(a-b) < 5e-10, (r, a, b)
        checks += 1
    # The supercritical real exponent first fails the global bound at small
    # radii, but the bound returns for radii near 1.
    assert normalized_norm(5, 0.10) > 1
    assert normalized_norm(5, 0.90) < 1
    assert normalized_norm(8, 0.10) > 1
    assert normalized_norm(8, 0.99) < 1
    checks += 4
    # For the angular deficit, test that multiplying by 1/[a log(1/a)]
    # gives the predicted p-linear leading coefficient to finite tolerance.
    # The O_p(a) term explains the slow 1/log convergence.
    for p in (1, 2, 4, 5):
        a = 1e-4
        r = math.sqrt(1 + a*a) - a
        deficit = 1 - moment(p, r, panels=131072)
        quotient = deficit / (a * math.log(1/a))
        expected = 4*p/math.pi**2
        assert abs(quotient - expected) < 0.14, (p, quotient, expected)
        checks += 1
    print(f'OK: {checks} finite consistency checks; proof needed for all-r/all-p theorem')
