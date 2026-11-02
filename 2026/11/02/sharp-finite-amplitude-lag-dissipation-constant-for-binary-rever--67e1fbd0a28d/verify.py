#!/usr/bin/env python3
"""Reproduce numerical checks of the sharp binary-state dissipation constant.

The analytic theorem is proved in RESULT.md; finite tests are supplementary.
Requires only Python's standard library.
"""
import math

COUNT = 0

def assert_close(a, b, *, rtol=1e-10, atol=1e-12):
    global COUNT
    assert math.isfinite(a) and math.isfinite(b)
    assert abs(a - b) <= atol + rtol * max(abs(a), abs(b)), (a, b)
    COUNT += 1

def check(condition, message):
    global COUNT
    assert condition, message
    COUNT += 1

def logit(x):
    return math.log(x) - math.log1p(-x)

def nvalue(x, q):
    return logit(x) - logit(q) - (x-q)/(x*(1-x))

def peak(q):
    if q > 0.5:
        return 1.0 - peak(1.0-q)
    if q == 0.5:
        return 0.5
    lo, hi = 0.5, 1.0-1e-13
    check(nvalue(lo, q)>0 and nvalue(hi, q)<0, 'root brackets')
    for _ in range(160):
        mid = (lo+hi)/2.0
        if nvalue(mid, q)>0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0

def bound_constant(q, s):
    x = peak(q)
    return x*(1-x)/s

def exact_sigma(q, s, x):
    return s*(x-q)*(logit(x)-logit(q))

def main():
    qs = [0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.4, 0.49, 0.5, 0.51, 0.6, 0.8, 0.9, 0.95, 0.99, 0.999]
    ss = [0.125, 1.0, 7.25]
    for q in qs:
        xstar = peak(q)
        check((xstar > 0.5 if q < 0.5 else (xstar < 0.5 if q > 0.5 else xstar == 0.5)), 'unique side')
        if q != 0.5:
            check(abs(nvalue(xstar, q))<1e-8, 'stationarity')
            check(xstar*(1-xstar)>q*(1-q), 'strict global amplification')
        assert_close(bound_constant(q, 1), bound_constant(1-q, 1), atol=1e-12)
        for s in ss:
            C = bound_constant(q,s)
            assert_close(s*C, xstar*(1-xstar))
            for i in range(1,1000):
                x = i/1000
                if abs(x-q)<1e-10:
                    continue
                sig = exact_sigma(q,s,x)
                check(sig > 0, 'positive dissipation')
                check((x-q)**2 <= C*sig + 2e-13, 'global sharp bound')
            if q != 0.5:
                sig = exact_sigma(q,s,xstar)
                assert_close((xstar-q)**2, C*sig, atol=5e-13)
                rate_forward = s*q
                rate_backward = s*(1-q)
                j = rate_forward*(1-xstar)-rate_backward*xstar
                force = math.log(rate_forward*(1-xstar)/(rate_backward*xstar))
                assert_close(j*force,sig)
    # Sharp rare-event expansion and its actual convergence trend.
    residuals = []
    for L in [20., 40., 80., 160.]:
        q = 1.0/(1.0+math.exp(L))
        x = peak(q)
        y = 1.0/(1-x)
        residual = abs(y-L-math.log(L))
        residuals.append(residual)
        check(residual < 0.25, 'rare-event y expansion')
        # Exact reciprocal-constant identity.
        assert_close(1.0/bound_constant(q,1.0),y*y/(y-1),atol=1e-11)
    check(all(a>b for a,b in zip(residuals,residuals[1:])), 'rare-event residual decreases')
    # Equilibrium autocovariance of the state-1 indicator: q(1-q)e^{-s t}.
    for q in [0.02,0.1,0.4]:
        for s in [0.5,1,5]:
            for t in [0.,0.1,1.,5.]:
                exact = q*(1-q)*math.exp(-s*t)
                expected = q*((q+(1-q)*math.exp(-s*t))-q)
                assert_close(exact,expected)
    print('PASS: %d deterministic checks; largest tested grid has 999 points per case.'%COUNT)
    print('Example q=0.1: x*=%.12f, s*C=%.12f, s*tau_m=0.09'%(peak(.1),bound_constant(.1,1.0)))
    print('Rare-event residuals |y-L-log L|:',residuals)

if __name__=='__main__':
    main()
