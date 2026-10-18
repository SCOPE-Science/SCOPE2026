#!/usr/bin/env python3
"""Independent finite checks of the isocanted-cube width formulas.
Requires Python 3.10+, NumPy, SciPy. Finite checks do not prove asymptotic claims.
"""
from itertools import product
from math import asin, exp, pi, sqrt

import numpy as np
from scipy.optimize import linprog
from scipy.special import gammaln
from scipy.stats import kstest, skewnorm


def sphere_abs_mean(d):
    return exp(gammaln(d / 2) - gammaln((d + 1) / 2) - .5 * np.log(pi))


def g(r):
    return 2 / pi * (sqrt(1 - r * r) + r * asin(r))


def width_mean_var(d, ell, a):
    p = ell - a
    c = sphere_abs_mean(d)
    mean = (d * p + sqrt(d) * a) * c
    variance = (
        p * p * (1 + 2 * (d - 1) / pi - d * d * c * c)
        + a * a * (1 - d * c * c)
        + 2 * p * a * sqrt(d) * (g(1 / sqrt(d)) - d * c * c)
    )
    return mean, variance


def lp_description(d, ell, a):
    A, bounds = [], []
    for i in range(d):
        v = np.eye(d)[i]
        A.extend((v, -v))
        bounds.extend((ell / 2, ell / 2))
    for i in range(d):
        for j in range(i):
            v = np.eye(d)[i] - np.eye(d)[j]
            A.extend((v, -v))
            bounds.extend((ell - a, ell - a))
    return np.array(A), np.array(bounds)


def main():
    rng = np.random.default_rng(20261017)
    ell, a = 1.7, .6
    # Direct linear-program tests against the original facet inequalities.
    num_lp = 0
    for d in range(2, 7):
        A, b = lp_description(d, ell, a)
        for _ in range(60):
            u = rng.standard_normal(d)
            u /= np.linalg.norm(u)
            res = linprog(-u, A_ub=A, b_ub=b, bounds=[(None, None)] * d, method="highs")
            assert res.success, res.message
            expected_support = .5 * ((ell - a) * np.abs(u).sum() + a * abs(u.sum()))
            assert abs(-res.fun - expected_support) < 1e-9
            num_lp += 1
    print("facet-support LP comparisons:", num_lp)

    # Independent uniform-spherical simulations check all finite moment terms.
    for d in (3, 16, 128, 512):
        G = rng.standard_normal((18000, d))
        U = G / np.linalg.norm(G, axis=1)[:, None]
        w = (ell - a) * np.abs(U).sum(axis=1) + a * np.abs(U.sum(axis=1))
        theo_mean, theo_var = width_mean_var(d, ell, a)
        print("d=%d predicted_mean=%.8f empirical_mean=%.8f predicted_var=%.8f empirical_var=%.8f"
              % (d, theo_mean, w.mean(), theo_var, w.var()))
        assert abs(w.mean() - theo_mean) < .05
        assert abs(w.var() - theo_var) < .03
        assert theo_var >= 0

    # The limiting law is the centered skew-normal convolution.
    d = 800
    G = rng.standard_normal((20000, d))
    U = G / np.linalg.norm(G, axis=1)[:, None]
    centered = ((ell - a) * np.abs(U).sum(axis=1)
                + a * np.abs(U.sum(axis=1)) - width_mean_var(d, ell, a)[0])
    mu = sqrt(2 / pi)
    sigma = sqrt(1 - 3 / pi)
    omega = sqrt((ell - a) ** 2 * sigma ** 2 + a ** 2)
    alpha = a / ((ell - a) * sigma)
    target = skewnorm(alpha, loc=-a * mu, scale=omega)
    ks = kstest(centered, target.cdf).statistic
    print("d=800 skew-normal KS distance:", round(float(ks), 6))
    assert ks < .05

    # The asymptotic variance has a strict interior optimizer.
    sigma2, tau2 = 1 - 3 / pi, 1 - 2 / pi
    star = ell * sigma2 / (sigma2 + tau2)
    f = lambda q: (ell - q) ** 2 * sigma2 + q ** 2 * tau2
    for q in (0, .01, .05, .3, .5, .8, ell):
        assert f(star) < f(q)
    assert abs(star / ell - (pi - 3) / (2 * pi - 5)) < 1e-14
    print("limiting optimizer a/ell=", round(star / ell, 9))
    print("ALL CHECKS PASSED (statistical checks corroborate, not prove, the theorem)")


if __name__ == "__main__":
    main()
