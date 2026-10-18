#!/usr/bin/env python3
"""Reproducible independent checks for the stated skew-OU entropy edge law.

Dependencies: Python >=3.10, numpy, scipy; no network access required.
The analytic proof is in RESULT.md; numeric checks are finite corroboration.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp

GAMMA = 0.577215664901532860606512090082402431


def skew_chain(n, coupling):
    m = np.zeros((n, n), dtype=float)
    for i in range(n - 1):
        m[i, i + 1] = coupling
        m[i + 1, i] = -coupling
    return m


def mode_frequencies(n, coupling):
    return 2 * coupling * np.cos(np.pi * np.arange(1, n // 2 + 1) / (n + 1))


def edge_tilt(kappa, coupling):
    return (math.sqrt(1 + (kappa / (2 * coupling)) ** 2) - 1) / 2


def scgf(n, kappa, coupling, tilt):
    w = mode_frequencies(n, coupling)
    return float(np.sum(kappa - np.sqrt(kappa ** 2 - 4 * w ** 2 * tilt * (1 + tilt))))


def slope(n, kappa, coupling, tilt):
    w = mode_frequencies(n, coupling)
    return float(np.sum(2 * w ** 2 * (1 + 2 * tilt) / np.sqrt(kappa ** 2 - 4 * w ** 2 * tilt * (1 + tilt))))


def finite_t_log_mgf_pair(T, kappa, omega, tilt):
    """Independent time-domain Feynman--Kac Riccati IVP for a planar OU mode."""
    c = omega ** 2 * tilt * (1 + tilt)
    def rhs(t, y):
        a, logm = y
        return [2 * (a * a - kappa * a + c), 2 * a]
    solution = solve_ivp(rhs, (0, T), [0., 0.], rtol=1e-11, atol=1e-12, method='DOP853')
    assert solution.success
    a, logm = solution.y[:, -1]
    assert a < kappa
    return logm - math.log1p(-a / kappa)


def main():
    tests = 0
    for kappa, coupling in [(1.2, .8), (.7, 1.6), (3., .33)]:
        lam = edge_tilt(kappa, coupling)
        for n in range(1, 29):
            m = skew_chain(n, coupling)
            eig = np.linalg.eigvalsh(1j * m)
            positive = np.sort(eig[eig > 1e-10])
            target = np.sort(mode_frequencies(n, coupling))
            assert len(positive) == len(target)
            assert np.allclose(positive, target, atol=2e-13, rtol=2e-13)
            exact_edge = kappa / 2 * (n - 1 / math.tan(math.pi / (2 * (n + 1))))
            assert abs(scgf(n, kappa, coupling, lam) - exact_edge) < 2e-12 * n
            assert abs(scgf(n, kappa, coupling, lam) - scgf(n, kappa, coupling, -1 - lam)) < 2e-12 * n
            assert abs(slope(n, kappa, coupling, 0.) - 2 * coupling ** 2 * (n - 1) / kappa) < 2e-12 * n
            tests += 4
        for n in [50, 200, 1000, 4000]:
            lam = edge_tilt(kappa, coupling)
            fac = 8 * coupling ** 2 * (1 + 2 * lam) / (kappa * math.pi)
            predicted = fac * (n + 1) * (math.log(n + 1) + GAMMA + math.log(2 / math.pi) - 1)
            discrepancy = slope(n, kappa, coupling, lam) - predicted
            assert abs(discrepancy) < max(2e-5 * n, 1)
            print(f'kappa={kappa} J={coupling} N={n}: exact_slope={slope(n,kappa,coupling,lam):.9f}  asym_slope={predicted:.9f}  error={discrepancy:.5g}')
            tests += 1
        n = 4
        for theta in [lam / 4, -0.3, lam / 2]:
            target = scgf(n, kappa, coupling, theta)
            for T in [30., 60.]:
                result = sum(finite_t_log_mgf_pair(T, kappa, w, theta) for w in mode_frequencies(n, coupling)) / T
                assert abs(result - target) < .15 / T + .02
                tests += 1
    print('All checks passed:', tests)


if __name__ == '__main__':
    main()
