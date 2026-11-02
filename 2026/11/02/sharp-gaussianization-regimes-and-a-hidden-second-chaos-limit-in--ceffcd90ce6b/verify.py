#!/usr/bin/env python3
"""Numerically reproducible checks for fractional-kernel diffusivity asymptotics.

Requires Python 3, NumPy and SciPy. No random numbers are used.
"""
import math
from scipy.integrate import quad
from scipy.special import beta, betainc

ETA = 0.6
MU = 1.3
C = 0.8


def exact_ng(p, t):
    """One-dimensional incomplete-beta formula; valid 0 < p < 1/2."""
    assert 0 < p < .5 and t > 0
    value = quad(lambda w: (1 + t * w) ** (-ETA)
                 * betainc(p, 1 - 2 * p, 1 - w),
                 0, 1, weight='alg', wvar=(2 * p - 1, 0),
                 epsabs=2e-10, epsrel=2e-10, limit=400)[0]
    return 2 * p * p * C * beta(p, 1 - 2 * p) * value / (MU * MU)


def independent_ng(p, t):
    """Double covariance integral in triangle coordinates, independently computed."""
    def inner(r):
        return quad(lambda q: (1 + t*r*(1-q))**(-ETA),
                    0, 1, weight='alg', wvar=(p-1, 0),
                    epsabs=2e-10, epsrel=2e-10, limit=200)[0]
    integral = quad(lambda r: inner(r), 0, 1,
                    weight='alg', wvar=(2*p-1, 0),
                    epsabs=3e-9, epsrel=3e-9, limit=200)[0]
    return 2 * p * p * C * integral / (MU * MU)


def long_constant(p):
    return 2 * p*p*C*beta(p, 1-ETA) / ((2*p-ETA)*MU*MU)


def critical_constant(p):
    return 2 * p*p*C*beta(p, 1-ETA) / (MU*MU)


def short_constant(p):
    return 2 * p*p*C*beta(p, 1-2*p)*beta(2*p, ETA-2*p)/(MU*MU)


def main():
    checks = 0
    for p in (.18, .30, .42):
        for t in (.35, 2.0, 8.0):
            x = exact_ng(p, t)
            y = independent_ng(p, t)
            assert x>0 and math.isclose(x,y,rel_tol=2e-7,abs_tol=1e-10),(p,t,x,y)
            checks += 1
    for p in (.18, .30, .42):
        f = exact_ng(p, 1e5)
        if 2*p<ETA:
            ratio = f*1e5**(2*p)/short_constant(p)
        elif 2*p == ETA or abs(2*p-ETA)<1e-12:
            ratio = f*1e5**ETA/math.log(1e5)/critical_constant(p)
        else:
            ratio = f*1e5**ETA/long_constant(p)
        print('asymptotic',p,round(ratio,8),'NG',round(f,11))
        assert .68 < ratio < 1.18,(p,ratio)
        checks += 1
    # For a squared stationary Gaussian diffusivity, evaluate the small-H second-chaos variance.
    delta=.6
    mean=1.1+delta
    p=.19
    var_limit = 4*delta**2*p**2*beta(p,1-2*p)*beta(2*p,ETA-2*p)
    ng_limit = 4*delta**2*p**2*beta(p,1-2*p)*beta(2*p,ETA-2*p)/(mean**2)
    assert math.isclose(var_limit/mean**2,ng_limit,rel_tol=1e-13) and var_limit>0
    checks+=1
    print('PASS', checks, 'independent covariance quadratures, asymptotic regimes and second-chaos variance checks')


if __name__ == '__main__':
    main()
