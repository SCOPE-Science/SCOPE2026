#!/usr/bin/env python3
"""Reproduce the analytic Steele--Beer optical-depth optimizer checks.
Uses only the Python standard library. All tests are finite checks, not proofs.
"""
import math
import random


def mean_prod(q, t):
    if t == 0.0:
        return q * math.exp(1.0-q)
    y = q * math.exp(-t)
    return math.e * math.exp(-y) * (-math.expm1(y-q)) / t


def stationary(q, t):
    y = q * math.exp(-t)
    return t*y + math.expm1(y-q)


def optimum(q):
    if q <= 1.0:
        return 0.0
    lo = math.log(q)
    hi = max(2., 2. * lo)
    while stationary(q, hi) > 0:
        hi *= 2.
    for _ in range(120):
        mid = (lo+hi)/2
        if stationary(q, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def simpson(q, t, n=400):
    h = t/n
    def f(u):
        v = q*math.exp(-u)
        return math.e*v*math.exp(-v)
    s = f(0)+f(t)
    for i in range(1,n):
        s += (4 if i%2 else 2)*f(i*h)
    return s*h/(3*t)


def check():
    rng = random.Random(453662)
    for _ in range(400):
        q=10**rng.uniform(-1.,1.7)
        t=rng.uniform(.1,3.)
        assert abs(mean_prod(q,t)-simpson(q,t)) < 6e-9
    for q in (.1,.2,.5,.9,1.):
        vals=[mean_prod(q,t) for t in (0.,.02,.1,.3,1.,3.,10.)]
        assert all(x>y for x,y in zip(vals,vals[1:]))
    last=-1.
    for q in (1.001,1.01,1.1,1.2,1.5,2,3,5,10,30,100,1000):
        t=optimum(q)
        assert t > math.log(q)
        assert t > last
        assert stationary(q, t-.01*min(1.,t-math.log(q))) > 0
        assert stationary(q, t+.01) < 0
        if t > .02:
            assert mean_prod(q,t) > mean_prod(q,t-.01*min(t/2,1))
        assert mean_prod(q,t) > mean_prod(q,t+.01)
        last=t
    t=optimum(2.)
    assert abs(t-1.0818888323121851) < 5e-11
    assert abs(mean_prod(2,t)-.9355216078872733) < 5e-11
    for d in (1e-1,1e-2,1e-3):
        z=optimum(1+d)
        assert abs(z/d-1.5) < 8*d
    for q in (1e2,1e3,1e5,1e8):
        t=optimum(q)
        y=q*math.exp(-t)
        assert abs(y*t-1)<3e-12
        if q>=1e5:
            assert abs(t-math.log(q)-math.log(math.log(q)))<.3
    print('PASS: 400 Simpson quadrature comparisons, 5 no-inhibition regimes, 12 optima and monotonicity checks, 3 threshold asymptotics, 4 strong-light checks.')
    print(f'Illustration q=2: t*={t!r}' if False else f'Illustration q=2: t*={optimum(2.):.15f}, max={mean_prod(2,optimum(2.)):.15f}, zero-attenuation={mean_prod(2,0.):.15f}')

if __name__=='__main__':
    check()
