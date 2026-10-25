#!/usr/bin/env python3
"""Independent quadrature and Fourier checks of a sharp harmonic coefficient envelope.

Requires Python 3, scipy and numpy. These finite checks supplement the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def angular_integral(lambda_):
    return 2 / math.pi * quad(lambda t: math.hypot(lambda_, 2 * math.cos(t)),
                              0, math.pi / 2, epsabs=5e-13)[0]


def angular_derivative(lambda_):
    return 2 / math.pi * quad(lambda t: lambda_ / math.hypot(lambda_, 2 * math.cos(t)),
                              0, math.pi / 2, epsabs=5e-13)[0]


def solve_lambda(c):
    hi = 1.0
    while angular_derivative(hi) < c:
        hi *= 2
    return brentq(lambda v: angular_derivative(v) - c, 0.0, hi,
                  xtol=2e-14)


def run():
    assert abs(angular_integral(0) - 4 / math.pi) < 1e-12
    configurations = 0
    for c in (0.03, 0.2, 0.5, 0.9, 0.99):
        lam = solve_lambda(c)
        C = angular_integral(lam) - lam * c
        assert abs(angular_derivative(lam) - c) < 1e-12
        N = 32768
        theta = 2 * math.pi * np.arange(N) / N
        for n in (1, 3, 7):
            x = np.cos(n * theta)
            F = (lam - 2j * x) / np.sqrt(lam ** 2 + 4 * x ** 2)
            assert abs(F.mean() - c) < 1e-11
            assert abs(np.abs(F).max() - 1) < 1e-12
            cp = np.mean(F * np.exp(-1j * n * theta))
            cm = np.mean(F * np.exp(1j * n * theta))
            assert abs(abs(cp) + abs(cm) - C) < 1e-11
            configurations += 1
        # Strictly lower than the unconstrained sharp constant.
        assert 0 < C < 4 / math.pi
    # Independent asymptotic sanity checks at the endpoints.
    c = 1 - 1e-5
    lam = solve_lambda(c)
    C = angular_integral(lam) - lam * c
    assert abs(C / (2 * math.sqrt(1 - c)) - 1) < 1e-4
    print(f"VERIFY_OK extremal_Fourier_profiles={configurations} "
          "stationarity_cases=5 endpoint_checks=2")


if __name__ == '__main__':
    run()
