#!/usr/bin/env python3
"""Numerical and finite-identity checks for KL calibration of exponential maxima.

Run with Python 3 and only its standard library. These tests do not replace
analytic existence, uniqueness, or asymptotic arguments.
"""
import math


def harmonic(n):
    return sum(1.0 / j for j in range(1, n + 1))


def derivative(n, t):
    return harmonic(n) - 1.0 / t - sum(1.0 / (t + j) for j in range(1, n + 1))


def second_derivative(n, t):
    return 1.0 / (t * t) + sum(1.0 / (t + j)**2 for j in range(1, n + 1))


def log_laplace(n, t):
    return ((t + 1.0) * math.log(n) + math.lgamma(t + 1.0)
            + math.lgamma(n) - math.lgamma(n + t + 1.0))


def optimal_parameters(n):
    low, high = 1.0, 2.0
    assert derivative(n, low) < 0 < derivative(n, high)
    for _ in range(70):
        mid = (low + high) / 2.0
        if derivative(n, mid) < 0:
            low = mid
        else:
            high = mid
    t = (low + high) / 2.0
    mu = -log_laplace(n, t) / t
    return t, mu


def objective(n, t):
    m = harmonic(n) - math.log(n)
    return 1.0 / n + (t - 1.0) * m - math.log(t) + log_laplace(n, t)


def direct_divergence_quadrature(n, t, mu, subdivisions=120000):
    # Integrate directly over the maximum s on [0,50]. The omitted
    # exponential tail is negligible at the stated numerical tolerance.
    def fn(s):
        if s == 0.0 and n > 1:
            return 0.0
        z = s - math.log(n)
        q = -math.expm1(-s)
        density = n * math.exp(-s) * (q ** (n - 1))
        log_f_z = math.log(n) - s + ((n - 1) * math.log(q) if n > 1 else 0.0)
        log_g_z = math.log(t) - t * (z - mu) - math.exp(-t * (z - mu))
        return density * (log_f_z - log_g_z)
    upper = 50.0
    h = upper / subdivisions
    s = fn(0.0) + fn(upper)
    for j in range(1, subdivisions):
        s += (4 if j % 2 else 2) * fn(j * h)
    return s * h / 3


def verify():
    phi = (1 + math.sqrt(5)) / 2
    limit_constant = 0.5 - 3.0 / (math.pi**2)
    previous_t = 1.7
    for n in range(1, 101):
        t, mu = optimal_parameters(n)
        assert 1.0 < t < previous_t
        previous_t = t
        assert abs(derivative(n, t)) < 2e-13
        assert second_derivative(n, t) > 0
        assert objective(n, t) > 0
        assert objective(n, t) < objective(n, 1.0)
        assert abs(objective(n, 1) - (1 / n - math.log1p(1 / n))) < 2e-11
        if n == 1:
            assert abs(t - phi) < 1e-14
        if n in (1, 2, 3, 5):
            quadrature = direct_divergence_quadrature(n, t, mu)
            assert abs(quadrature - objective(n, t)) < 4e-7, (n, quadrature, objective(n, t))
    # Independent checks of exact integer-moment identities of W = n min(U_i).
    for n in range(1, 501):
        A1 = math.exp(log_laplace(n, 1.0))
        A2 = math.exp(log_laplace(n, 2.0))
        assert abs(A1 - n / (n + 1)) < 2e-10
        assert abs(A2 - 2 * n*n / ((n + 1)*(n + 2))) < 2e-10
    for n in (100, 1000, 3000):
        t, _ = optimal_parameters(n)
        d = objective(n, t)
        assert abs(n*(t - 1) - 6/(math.pi**2)) < 0.02
        assert abs(n*n*d - limit_constant) < 0.001
    print('VERIFY_OK roots=100 moment_pairs=500 quadratures=4 asymptotic_points=3')
    print('n=1 scale inverse=', optimal_parameters(1)[0])
    print('n=1000 n^2 optimum KL=', 1000000*objective(1000, optimal_parameters(1000)[0]))


if __name__ == '__main__':
    verify()
