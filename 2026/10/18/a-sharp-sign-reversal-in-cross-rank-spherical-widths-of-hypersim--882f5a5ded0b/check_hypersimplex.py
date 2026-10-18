"""Standalone numerical checks for the angular-width covariance theorem.

Run with Python 3 and NumPy/SciPy installed:
    python check_hypersimplex.py
Finite checks corroborate only the stated finite identities and asymptotic
predictions; they do not constitute a proof of limiting convergence.
"""
from itertools import combinations
from math import erfc, exp, gamma, pi, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtri

C = 1 / sqrt(2 * pi)


def t_alpha(alpha):
    assert 0 < alpha <= .5
    return float(-ndtri(alpha))


def phi(t):
    return C * exp(-t * t / 2)


def tail(t):
    return erfc(t / sqrt(2)) / 2


def x_mean(alpha):
    t = t_alpha(alpha)
    return 2 * (phi(t) - t * alpha)


def gaussian_integrated_cov(alpha, beta):
    a, b = sorted((alpha, beta))
    ta, tb = t_alpha(a), t_alpha(b)
    cross = 2 * ((1 + ta * tb) * a - tb * phi(ta))
    return cross - x_mean(a) * x_mean(b)


def angular_cov(alpha, beta):
    return gaussian_integrated_cov(alpha, beta) - 2 * phi(t_alpha(alpha)) * phi(t_alpha(beta))


def half_cov_t(t):
    a = tail(t)
    return 2 * a + 4 * C * t * a - 6 * C * phi(t)


def check_exact_support():
    rng = np.random.default_rng(71629)
    checks = 0
    for n in range(4, 9):
        for k in range(1, n):
            corners = np.asarray([np.eye(n, dtype=int)[list(B)].sum(axis=0)
                                  for B in combinations(range(n), k)], dtype=float)
            for _ in range(10):
                z = rng.normal(size=n)
                z -= z.mean()
                u = z / np.linalg.norm(z)
                direct = float(np.max(corners @ u) - np.min(corners @ u))
                zz = np.sort(z)
                fast = float((sum(zz[-k:]) - sum(zz[:k])) / np.linalg.norm(z))
                assert abs(direct - fast) < 2e-13, (n, k, direct, fast)
                checks += 1
    return checks


def check_integrals():
    tests = 0
    for a, b in [(0.03, .5), (.1, .25), (.18, .49), (.25, .25), (.4, .5), (.5, .5)]:
        ta, tb = t_alpha(a), t_alpha(b)
        lo = max(ta, tb)
        integrand = lambda z: 2 * (z - ta) * (z - tb) * phi(z)
        mixed = quad(integrand, lo, np.inf, epsabs=2e-13, epsrel=2e-13)[0]
        a0, b0 = sorted((a, b))
        exact = 2 * ((1 + t_alpha(a0) * t_alpha(b0)) * a0
                     - t_alpha(b0) * phi(t_alpha(a0)))
        assert abs(mixed - exact) < 2e-11, (a, b, mixed, exact)
        tests += 1
    return tests


def check_threshold():
    root = brentq(half_cov_t, .5, 1.5, xtol=1e-14)
    critical = tail(root)
    assert .81338 < root < .81340
    assert .20799 < critical < .20801
    assert half_cov_t(0) > 0
    assert half_cov_t(2) < 0
    assert angular_cov(.05, .5) < -.015
    assert angular_cov(.3, .5) > .018
    assert abs(half_cov_t(root)) < 1e-15
    return root, critical


def check_samples():
    rng = np.random.default_rng(72013)
    n = 768
    n_trials = 20000
    ranks = [round(.05 * n), round(.3 * n), n // 2]
    widths = np.empty((n_trials, len(ranks)), dtype=float)
    batch = 1000
    for a in range(0, n_trials, batch):
        z = rng.normal(size=(batch, n))
        z -= z.mean(axis=1, keepdims=True)
        radius = np.linalg.norm(z, axis=1)
        z.sort(axis=1)
        prefix = np.cumsum(z, axis=1)
        total = prefix[:, -1]
        for j, k in enumerate(ranks):
            upper = total - prefix[:, n - k - 1]
            lower = prefix[:, k - 1]
            widths[a:a+batch, j] = (upper - lower) / radius
    emp = np.cov(widths, rowvar=False, ddof=1)
    k05 = angular_cov(.05, .5)
    k30 = angular_cov(.3, .5)
    assert emp[0, 2] < -.007, ('small-rank sign', emp[0, 2])
    assert emp[1, 2] > .010, ('large-rank sign', emp[1, 2])
    assert abs(emp[0, 2] - k05) < .009, (emp[0, 2], k05)
    assert abs(emp[1, 2] - k30) < .009, (emp[1, 2], k30)
    return {'n': n, 'trials': n_trials,
            'low_empirical': float(emp[0, 2]), 'low_theoretical': float(k05),
            'high_empirical': float(emp[1, 2]), 'high_theoretical': float(k30)}


def main():
    n = check_exact_support()
    i = check_integrals()
    root, critical = check_threshold()
    sims = check_samples()
    print('PASS', n, 'exact support-function comparisons;', i, 'Gaussian integrations')
    print(f'PASS critical root t={root:.12f}, rank fraction={critical:.12f}')
    print('PASS fixed-seed spherical-width covariance sign comparisons', sims)


if __name__ == '__main__':
    main()
