#!/usr/bin/env python3
"""Exact polynomial and analytic-phase tests for ferromagnetic Ising stars.

Usage: python3 verify_lee_yang_star.py
All finite tests supplement (rather than replace) the published analytic argument.
"""
from fractions import Fraction as F
from math import atan2, cos, pi, sin


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def star_polynomial(qs):
    a, b = [F(1)], [F(1)]
    for q in qs:
        a = mul(a, [F(1), q])
        b = mul(b, [q, F(1)])
    return [
        (a[i] if i < len(a) else F(0)) +
        (b[i - 1] if 0 <= i - 1 < len(b) else F(0))
        for i in range(len(qs) + 2)
    ]


def root_power_sums(coefficients, max_k):
    n = len(coefficients) - 1
    assert coefficients[-1] == 1
    out = []
    for k in range(1, max_k + 1):
        assert k <= n
        term = k * coefficients[n - k]
        for j in range(1, k):
            term += coefficients[n - j] * out[k - j - 1]
        out.append(-term)
    return out


def phase(qs, angle):
    half = angle / 2.0
    return angle + sum(2 * atan2((1 - float(q)) * sin(half),
                                      (1 + float(q)) * cos(half)) for q in qs)


def root_angles(qs):
    m = len(qs)
    out = []
    for j in range(m + 1):
        target = (2*j + 1) * pi
        left, right = 0.0, 2*pi
        for _ in range(54):
            mid = (left + right) / 2
            if phase(qs, mid) < target:
                left = mid
            else:
                right = mid
        out.append((left + right) / 2)
    return out


def check():
    exact_cases = 0
    total_moment_cases = 0
    seed = [F(1, 5), F(1, 2), F(3, 5), F(2, 7)]
    for m in [1, 2, 3, 4, 5, 8, 12, 25, 50, 90]:
        qs = [seed[(j*j + 3*j + m) % len(seed)] for j in range(m)]
        c = star_polynomial(qs)
        assert len(c) == m+2
        assert c == c[::-1] and c[0] == c[-1] == 1
        assert all(x > 0 for x in c)
        tau = (max(qs) + F(1, 2)) / (1 + max(qs)/2)
        for k, actual in enumerate(root_power_sums(c, min(m+1, 7)), 1):
            predicted = (-1)**k * sum((q**k for q in qs), F(0))
            assert abs(actual - predicted) <= k*(2**k)*tau**m, (m, k, actual, predicted)
            total_moment_cases += 1
        exact_cases += 1

    numeric_cases = 0
    for m in (3, 7, 20, 80, 160):
        qs = [F(1, 5) if j%2 else F(3, 5) for j in range(m)]
        angles = root_angles(qs)
        assert len(angles) == m+1
        assert all(0 < angles[j] < angles[j+1] for j in range(m))
        assert max(abs(phase(qs, th)-(2*j+1)*pi) for j,th in enumerate(angles)) < 3e-11
        # Exact Lee-Yang quantization is compared against the Fourier moments.
        for k in (1, 2, 3):
            observed = sum(complex(cos(k*th), sin(k*th)) for th in angles) / (m+1)
            predicted = (-1)**k * sum(float(q)**k for q in qs) / m
            assert abs(observed - predicted) < 4/(m+1), (m,k,observed,predicted)
            numeric_cases += 1
        if m >= 80:
            slope = 1+sum((1-float(q))/(1+float(q)) for q in qs)
            first = angles[0]
            assert abs(first - pi/slope) < 120/(m**3), (m, first, slope)
    print('VERIFY_OK rational_polynomials=%d exact_power_sum_bounds=%d numeric_fourier_cases=%d phase_roots=%d' %
          (exact_cases, total_moment_cases, numeric_cases, 3+7+20+80+160+5))


if __name__ == '__main__':
    check()
