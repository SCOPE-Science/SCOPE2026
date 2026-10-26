"""Reproducible numerical diagnostics for a two-patch Hill-response allocation theorem.

This program supplements, and does not replace, its analytic proof.
Run with Python 3 using only the standard library.
"""
import math
import random


def response(x, p):
    y = x ** p
    return y / (1.0 + y)


def derivative(x, p):
    if x == 0:
        return 0.0
    y = x ** p
    return p * x ** (p - 1.0) / (1.0 + y) ** 2


def payoff(x, n, p):
    return response(x, p) + response(max(0.0, n-x), p)


def critical_local(p):
    return 2.0 * ((p - 1.0) / (p + 1.0)) ** (1.0/p)


def critical_global(p):
    return (2.0**p - 2.0) ** (1.0/p)


def log_sinh(x):
    if x <= 0:
        raise ValueError('positive input required')
    if x < 20:
        return math.log(math.sinh(x))
    return x - math.log(2.0) + math.log1p(-math.exp(-2.0*x))


def log_cosh(x):
    if x < 20:
        return math.log(math.cosh(x))
    return x - math.log(2.0) + math.log1p(math.exp(-2.0*x))


def log_stationary_budget(z, p):
    a = (p - 1.0) / 2.0
    b = (p + 1.0) / 2.0
    return (math.log(2.0) + log_cosh(z)
            + (log_sinh(a*z)-log_sinh(b*z))/p)


def off_center_minimum(n, p):
    if n <= critical_local(p):
        return None
    target = math.log(n)
    lo, hi = 1.0e-10, 1.0
    while log_stationary_budget(hi, p) < target:
        hi *= 2.0
    for _ in range(85):
        mid = (lo+hi)/2.0
        if log_stationary_budget(mid, p) < target:
            lo = mid
        else:
            hi = mid
    z = (lo+hi)/2.0
    x = n/(1.0+math.exp(2.0*z))
    return x, z


def test():
    rng = random.Random(20261023)
    samples = 1500
    for _ in range(samples):
        p = 1.05 + 14.0*rng.random()
        l, g = critical_local(p), critical_global(p)
        assert 0 < l < g
        regime = rng.randrange(3)
        if regime == 0:
            n = l*(0.15+0.8*rng.random())
        elif regime == 1:
            n = l+(g-l)*(0.1+0.8*rng.random())
        else:
            n = g*(1.05+1.1*rng.random())
        # Predicted candidates are always the only possible global maxima.
        opt = max(payoff(0.0,n,p), payoff(n/2.0,n,p))
        for j in range(401):
            x = n*j/400.0
            assert payoff(x,n,p) <= opt+3.0e-12, (p,n,x)
        if n < g:
            assert payoff(0.0,n,p)>payoff(n/2.0,n,p)
        else:
            assert payoff(0.0,n,p)<payoff(n/2.0,n,p)
        root = off_center_minimum(n,p)
        if n <= l:
            assert root is None
            for j in range(1,200):
                x = n*j/400.0
                assert derivative(x,p)<derivative(n-x,p)
        else:
            assert root is not None
            x,z = root
            assert 0<x<n/2.0 and z>0
            assert abs(derivative(x,p)-derivative(n-x,p)) < 4.0e-10
            assert payoff(x,n,p)<min(payoff(0.0,n,p),payoff(n/2.0,n,p))
            assert log_stationary_budget(z*(1+1e-5),p)>math.log(n)
            assert log_stationary_budget(z*(1-1e-5),p)<math.log(n)

    # Analytic p=2 tie and both noncentral local minima.
    n=math.sqrt(2.0); p=2.0
    x=(math.sqrt(2.0)-math.sqrt(4*math.sqrt(3.0)-6.0))/2.0
    min_exact=(3-math.sqrt(3.0))/2.0
    gap_exact=(3*math.sqrt(3.0)-5.0)/6.0
    assert abs(payoff(0.0,n,p)-2.0/3.0)<1e-14
    assert abs(payoff(n/2,n,p)-2.0/3.0)<1e-14
    assert abs(payoff(x,n,p)-min_exact)<1e-14
    assert abs(payoff(0.0,n,p)-payoff(x,n,p)-gap_exact)<1e-14

    # Universal pitchfork coefficient for multiple real Hill exponents.
    for p in [1.15,1.5,2.0,3.0,5.0,10.0,18.0]:
        for eps in [1.0e-2,1.0e-3,1.0e-4]:
            n=critical_local(p)*(1.0+eps)
            x,z = off_center_minimum(n,p)
            coef=((0.5-x/n)/math.sqrt(eps))
            target=math.sqrt(3.0)/2.0
            assert abs(coef-target)<0.065, (p,eps,coef)

    # Direct checks for log-budget monotonicity across exponents.
    for p in [1.01,1.2,1.7,2.0,3.5,7,30]:
        for j in range(1,300):
            z=0.0001*j
            assert log_stationary_budget(z+0.0001,p)>log_stationary_budget(z,p)

    print('PASS: 1500 seeded parameter configurations, 601500 grid comparisons,')
    print('      local-minimum crossings, seven-exponent onset checks, p=2 exact example,')
    print('      and 2093 strict monotonicity comparisons.')
    print('p=2 local threshold:',critical_local(2.0))
    print('p=2 global threshold:',critical_global(2.0))
    print('p=2 coexistence barrier:',gap_exact)


if __name__ == '__main__':
    test()
