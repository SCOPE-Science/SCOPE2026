#!/usr/bin/env python3
"""Independent numerical checks of pinned-interface reset inversion.

Dependencies: scipy >= 1.7.  Run: python3 verify.py
All physics statements and proof are in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import erf


def prediction(nu, mu, reset, noise, ell):
    a = reset + 2.0 * mu
    covariance_at_zero = noise / math.sqrt(2.0 * nu * a)
    ratio = math.exp(-ell * math.sqrt(a / (2.0 * nu)))
    y = math.sqrt(1.0 + reset / (2.0 * mu))
    excess = 3.0 * (4.0 / math.pi * y * math.atan(1.0 / y) - 1.0)
    return covariance_at_zero, ratio, excess


def inverse(nu, ell, variance, corr_ratio, excess):
    max_excess = 12.0 / math.pi - 3.0
    assert nu > 0 and ell > 0 and variance > 0
    assert 0.0 < corr_ratio < 1.0
    assert 0.0 < excess < max_excess
    def kurtosis_in_y(y):
        return 3.0 * (4.0 / math.pi * y * math.atan(1.0/y) - 1.0)
    lower = 1.0
    upper = 2.0
    while kurtosis_in_y(upper) <= excess:
        upper *= 2.0
    y = brentq(lambda v: kurtosis_in_y(v) - excess, lower, upper,
               xtol=1e-13, rtol=1e-14)
    z = y*y - 1.0
    total = 2.0 * nu * (math.log(corr_ratio) / ell) ** 2
    reset = total*z/(1.0+z)
    mu = total/(2.0*(1.0+z))
    noise = variance*math.sqrt(2.0*nu*total)
    return mu, reset, noise


def numerical_moments(nu, mu, reset, noise, ell):
    # Direct age-mixture integration, independent of Laplace-transform identities.
    eq_variance = noise/(2.0*math.sqrt(nu*mu))
    def v_age(age):
        return eq_variance*erf(math.sqrt(2.0*mu*age))
    v2 = quad(lambda t: reset*math.exp(-reset*t)*v_age(t),
              0.0, math.inf, epsabs=1e-11, epsrel=2e-10)[0]
    v4 = 3.0*quad(lambda t: reset*math.exp(-reset*t)*v_age(t)**2,
                  0.0, math.inf, epsabs=1e-11, epsrel=2e-10)[0]
    kurtosis = v4/v2**2-3.0
    a = reset + 2.0*mu
    # Different route: Laplace integral of spatial heat kernel.
    c_ell = 2.0*noise/math.sqrt(8.0*math.pi*nu)*quad(
        lambda u: math.exp(-a*u-ell*ell/(8.0*nu*u))/math.sqrt(u) if u>0 else 0.0,
        0.0, math.inf, epsabs=1e-11, epsrel=2e-10)[0]
    return v2, c_ell/v2, kurtosis


def run():
    examples = [
        (1.0, 0.5, 0.7, 2.0, 0.8),
        (0.37, 1.6, 0.08, 0.31, 2.2),
        (3.0, 0.11, 12.0, 0.65, 0.2),
        (0.82, 4.1, 2.9, 3.7, 1.25),
        (1.4, 0.3, 15.0, 0.9, 0.4),
    ]
    for nu, mu, reset, noise, ell in examples:
        c0, q, kappa = prediction(nu, mu, reset, noise, ell)
        n0, nq, nk = numerical_moments(nu, mu, reset, noise, ell)
        assert abs(c0/n0-1.0) < 1e-8, (c0, n0)
        assert abs(q/nq-1.0) < 1e-8, (q, nq)
        assert abs(kappa-nk) < 1e-8, (kappa, nk)
        m2, r2, d2 = inverse(nu, ell, c0, q, kappa)
        assert abs(m2/mu-1.0) < 2e-9, (m2, mu)
        assert abs(r2/reset-1.0) < 2e-9, (r2, reset)
        assert abs(d2/noise-1.0) < 2e-9, (d2, noise)
        print(f'PASS nu={nu:g} mu={mu:g} reset={reset:g} noise={noise:g} ell={ell:g} '
              f'excess={kappa:.12f}')
    print('PASS: five independent moment/covariance quadratures and inverse reconstructions')


if __name__ == '__main__':
    run()
