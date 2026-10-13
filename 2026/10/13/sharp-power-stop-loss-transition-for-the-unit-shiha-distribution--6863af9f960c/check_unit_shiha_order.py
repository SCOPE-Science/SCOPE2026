#!/usr/bin/env python3
"""Exact-fraction and numerical-quadrature checks for the unit Shiha ordering theorem.

Run: python3 check_unit_shiha_order.py
The theoretical classification is proved analytically; finite tests are diagnostics only.
"""
from fractions import Fraction as Q
import math


def mellin(z, q):
    return (Q(1) / (1 + z) + q * (Q(2) / (2 + z) + Q(8) / (2 + z) ** 2)) / (1 + 3 * q)


def gap_formula(z, q1, q2):
    return (q2 - q1) * z * (2 - z) / ((1 + 3 * q1) * (1 + 3 * q2) * (1 + z) * (2 + z) ** 2)


def phi(u):
    return u * (3.0 - 4.0 * math.log(u)) - 3.0


def cdf_U(u, q):
    if u <= 0.0:
        return 0.0
    return (u + q * u * u * (3.0 - 4.0 * math.log(u))) / (1.0 + 3.0 * q)


def cdf_power(v, omega, power, q):
    if v <= 0.0:
        return 0.0
    if v >= 1.0:
        return 1.0
    return cdf_U(v ** (omega / power), q)


def integral_cdf_gap(t, a):
    """Integral from t to 1 of u^(2a)(3-4a log u)-3u^a du."""
    if t == 1.0:
        return 0.0
    top = 2.0 * a + 1.0
    bottom = a + 1.0
    term = (3.0 / top + 4.0 * a / top**2) * (1.0 - t**top)
    term -= 3.0 / bottom * (1.0 - t**bottom)
    if t > 0.0:
        term += 4.0 * a / top * t**top * math.log(t)
    return term


def simpson(func, left, right, intervals=6000):
    h = (right - left) / intervals
    acc = func(left) + func(right)
    for j in range(1, intervals):
        acc += (4 if j % 2 else 2) * func(left + j * h)
    return acc * h / 3.0


def bisect(f, left, right):
    fl = f(left)
    fr = f(right)
    assert fl * fr < 0
    for _ in range(95):
        center = (left + right) / 2.0
        fc = f(center)
        if fl * fc > 0:
            left, fl = center, fc
        else:
            right, fr = center, fc
    return (left + right) / 2.0


checks = 0
for q1, q2 in [(Q(1, 10), Q(1, 2)), (Q(1, 3), Q(3, 1)), (Q(0), Q(7, 4))]:
    for z in [Q(1, 10), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(3), Q(4), Q(10)]:
        assert mellin(z, q2) - mellin(z, q1) == gap_formula(z, q1, q2)
        sign = 1 if z < 2 else (-1 if z > 2 else 0)
        gap = gap_formula(z, q1, q2)
        assert (gap > 0) - (gap < 0) == sign
        checks += 2

u_star = bisect(phi, 0.5, 0.75)
assert abs(u_star - 0.5768340041423087) < 5e-15
checks += 1
for q in [0.0, 0.1, 0.35, 1.0, 15.0]:
    assert abs(cdf_U(u_star, q) - u_star) < 2e-15
    for u in [0.01, 0.1, 0.5]:
        assert cdf_U(u, q) >= 0
    checks += 4

for omega in [0.25, 0.5, 1.0, 2.0, 4.0]:
    for factor in [0.25, 1.0, 1.5, 2.0, 2.5, 3.0]:
        power = factor * omega
        a = omega / power
        pivot = u_star ** (power / omega)
        q1, q2 = 0.2, 1.5
        k = (q2 - q1) / ((1.0 + 3.0 * q1) * (1.0 + 3.0 * q2))
        for t in [0.0, 0.05, 0.25, 0.5, 0.7, 0.9]:
            # A separate numerical quadrature checks the closed-form primitive.
            f = lambda v: cdf_power(v, omega, power, q2) - cdf_power(v, omega, power, q1)
            direct = -simpson(lambda z: f(t + (1.0-t) * z**6) * (1.0-t) * 6.0 * z**5, 0.0, 1.0, 3000)
            formula = -k * integral_cdf_gap(t, a)
            assert abs(direct - formula) < 3e-8, (omega, power, t, direct, formula)
            checks += 1
        assert abs(cdf_power(pivot, omega, power, q2) - u_star) < 2e-14
        assert abs(cdf_power(pivot, omega, power, q1) - u_star) < 2e-14
        checks += 2
        if power < 2.0 * omega:
            assert -k * integral_cdf_gap(0.0, a) > 1e-8
            assert -k * integral_cdf_gap(pivot, a) < -1e-8
            crossing = bisect(lambda t: integral_cdf_gap(t, a), 0.0, pivot)
            assert crossing < pivot
            checks += 3
        else:
            assert -k * integral_cdf_gap(pivot, a) < -1e-8
            for j in range(1, 100):
                assert -k * integral_cdf_gap(j / 100.0, a) < 0
                checks += 1

for q in [Q(0), Q(1, 5), Q(1), Q(4), Q(100)]:
    mean = mellin(Q(2), q)
    variance = mellin(Q(4), q) - mean * mean
    assert mean == Q(1, 3)
    assert variance == (4 + 10 * q) / (45 * (1 + 3 * q))
    checks += 2
assert Q(2, 27) / Q(4, 45) == Q(5, 6)
checks += 1
print(f'PASS: {checks} checks')
print(f'Universal quantile pivot: {u_star:.15f}')
print(f'Stop-loss crossover at omega=power=1: {bisect(lambda t: integral_cdf_gap(t, 1), 0.0, u_star):.15f}')
print('All integral tests are finite diagnostics, not the proof.')
