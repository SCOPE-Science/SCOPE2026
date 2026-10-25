"""Numerical checks of the finite-cone intrinsic pair-distance tail.

Requires numpy. This is a quadrature cross-check, not a proof.
Run: OPENBLAS_NUM_THREADS=1 python checks/cone_tail_check.py
"""
from math import cos, pi, sin, tan, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss


def lead_coefficient(k):
    alpha = pi * k
    if k < 1/3 - 1e-12:
        return 4 * tan(alpha) / (3 * alpha)
    if k > 1/3 + 1e-12:
        return 2 / (3 * alpha * sin(alpha/2)**2 * cos(alpha/2))
    return 28 / (pi * sqrt(3))


def survival_near_endpoint(k, eps, nr=1000, na=300):
    alpha = pi*k
    diameter = max(1.0, 2*sin(alpha/2))
    threshold = diameter - eps
    roots, weights = leggauss(nr)
    radial = (roots + 1)/2
    radial_weight = weights/2
    aroots, aweights = leggauss(na)
    angles = (aroots + 1)*alpha/2
    angle_weight = aweights/2
    total = 0.0
    for delta, wt in zip(angles, angle_weight):
        c = cos(delta)
        discriminant = threshold**2 - radial**2*sin(delta)**2
        radical = np.sqrt(np.maximum(discriminant, 0.0))
        lo = np.clip(radial*c-radical, 0, 1)
        hi = np.clip(radial*c+radical, 0, 1)
        # Integrate the second radial coordinate exactly under density 2s.
        conditional = np.where(discriminant < 0, 1, 1+lo*lo-hi*hi)
        total += wt*np.dot(radial_weight, 2*radial*conditional)
    return total


def check():
    print('k epsilon P(D>diameter-eps)/eps^3 predicted relative_error')
    for k in (0.2, 1/3, 0.6, 0.85):
        c = lead_coefficient(k)
        for eps in (0.03, 0.015):
            p = survival_near_endpoint(k, eps)
            ratio = p/eps**3
            rel = abs(ratio/c-1)
            print(f'{k:.9f} {eps:.4f} {ratio:.9f} {c:.9f} {rel:.5f}')
            assert rel < 0.09
    rng = np.random.default_rng(294)
    u, v, w = rng.random((3, 500_000))
    r, s = np.sqrt(u), np.sqrt(v)
    k_low, k_high = 0.2, 0.72
    low2 = r*r+s*s-2*r*s*np.cos(pi*k_low*w)
    high2 = r*r+s*s-2*r*s*np.cos(pi*k_high*w)
    assert np.all(low2 < high2)
    for k in (0.2, 1/3, 0.6, 0.85):
        d2 = r*r+s*s-2*r*s*np.cos(pi*k*w)
        empirical = float(d2.mean())
        theoretical = 1-8*sin(pi*k)/(9*pi*k)
        error = abs(empirical-theoretical)
        print(f'moment k={k:.9f} observed={empirical:.8f} exact={theoretical:.8f} error={error:.6f}')
        assert error<0.0025
    print('All tests passed; asymptotic calculations require the separate analytic proof.')


if __name__ == '__main__':
    check()
