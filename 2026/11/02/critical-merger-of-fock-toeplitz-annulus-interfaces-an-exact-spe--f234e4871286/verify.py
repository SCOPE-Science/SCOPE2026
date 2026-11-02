#!/usr/bin/env python3
"""Finite reproducibility checks for a Gaussian Fock annulus spectral theorem.

This script tests numerical identities and convergence only; it does not
replace the analytic proof of infinite-dimensional asymptotics.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import erf, erfc, gammainc, ndtr


def profile(x, c):
    return ndtr(x + c) - ndtr(x - c)


def eigenvalues(N, c):
    n = np.arange(3 * N + 200, dtype=int)
    a, b = N - c * math.sqrt(N), N + c * math.sqrt(N)
    lam = np.maximum(0.0, gammainc(n + 1, b) - gammainc(n + 1, a))
    return np.minimum(lam, 1.0)


def trace_defect_limit(c):
    return 2 * c * erfc(c) + 2 / math.sqrt(math.pi) * (-math.expm1(-c * c))


def gaussian_trace_defect(c, p):
    f = lambda x: (profile(x, c) * (1 - profile(x, c))) ** p
    return quad(f, -30.0, 30.0, epsabs=2e-11, limit=200)[0]


def check():
    checks = 0
    for c in (0.4, 0.6, 1.0, 2.0):
        assert abs(gaussian_trace_defect(c, 1) - trace_defect_limit(c)) < 2e-10
        checks += 1
        h = 1e-5
        d = (trace_defect_limit(c+h)-trace_defect_limit(c-h))/(2*h)
        assert abs(d - 2 * erfc(c)) < 1e-8
        checks += 1
        for N in (400, 1600):
            lam = eigenvalues(N, c)
            assert np.all((lam >= 0) & (lam <= 1))
            checks += 1
            exact = 2 * c * math.sqrt(N)
            assert abs(lam.sum() - exact) < 1e-8
            checks += 1
            for p in (0.5, 1.0, 2.0):
                val = np.sum((lam * (1-lam))**p)/math.sqrt(N)
                target = gaussian_trace_defect(c,p)
                assert abs(val - target) < 0.016, (c,N,p,val,target)
                checks += 1
            max_target = 2 * ndtr(c)-1
            assert abs(np.max(lam) - max_target) < 0.014
            checks += 1
    for c in (0.1, 0.3, 0.8, 1.5, 3.0, 5.0):
        assert 0 < trace_defect_limit(c) < 2/math.sqrt(math.pi)
        checks += 1
    for c in (0.2, 0.8, 1.7):
        x = np.linspace(0, 6, 100)
        l = profile(x, c)
        assert np.all(np.diff(l) < 0)
        checks += 1
    print(f"PASS: {checks} supplementary finite numerical checks")


if __name__ == '__main__':
    check()
