#!/usr/bin/env python3
"""Reproduce the two-threshold investment phase diagram (standard library only).

The source adaptive-gradient equation is assumed; this program checks the
algebraically derived root formula against *direct* differentiated benefits.
Finite trials supplement, and cannot replace, the analytic proof.
"""
import math
import random


def g(t):
    return 1.0/(2.0+2.0*math.cosh(t))


def f(H, C):
    return (1.0+H*C)/(C+H)**2


def root_C(H, theta):
    disc = H*H-4.0*theta*(H*H-1.0)
    assert disc > 0.0
    return tuple(sorted(((H*(1.0-2.0*theta)-math.sqrt(disc))/(2.0*theta),
                         (H*(1.0-2.0*theta)+math.sqrt(disc))/(2.0*theta))))


def roots(H, L, theta):
    assert H > 2.0 and L > math.acosh(H)
    cs = root_C(H, theta)
    assert 1.0 < cs[0] < H-2.0/H < cs[1] < math.cosh(L)
    n = 2.0*L  # with beta=1
    return ((L-math.acosh(cs[1]))/n,
            (L-math.acosh(cs[0]))/n,
            (L+math.acosh(cs[0]))/n,
            (L+math.acosh(cs[1]))/n)


def bisection(fx, lo, hi):
    a = fx(lo)
    b = fx(hi)
    assert a*b < 0.0
    for _ in range(58):
        mid = (lo+hi)/2.0
        if fx(mid)*a > 0:
            lo = mid
            a = fx(mid)
        else:
            hi = mid
    return (lo+hi)/2.0


def verify(H, L, theta):
    h = math.acosh(H)
    rr = roots(H, L, theta)
    assert all(0.0 < rr[i] < rr[i+1] for i in range(3))
    assert 0.0 < rr[0] < rr[-1] < 1.0

    # Evaluate B'(nx)/(b beta) without using the rationalized identity.
    def direct(x):
        z = 2.0*L*(x-0.5)
        return g(z+h)+g(z-h)-theta

    # Independent location by direct sign-change bisection on a grid.
    M = 4096
    crossings = []
    xold, yold = 0.0, direct(0.0)
    for i in range(1, M+1):
        xnew = i/M
        ynew = direct(xnew)
        if ynew*yold < 0:
            crossings.append(bisection(direct, xold, xnew))
        xold, yold = xnew, ynew
    assert len(crossings) == 4, (H,L,theta,crossings)
    for expected, actual in zip(rr, crossings):
        assert abs(expected-actual) < 2e-12, (expected,actual)
        assert abs(direct(expected)) < 1e-12
        z = 2.0*L*(expected-0.5)
        assert abs((direct(expected)+theta)-f(H,math.cosh(z))) < 1e-12
    for i,expected_stability in enumerate(('repeller','attractor','repeller','attractor')):
        eps = min(1e-6, 0.01*min(rr[i]-(rr[i-1] if i else 0.0),
                                 (rr[i+1] if i<3 else 1.0)-rr[i]))
        left,right = direct(rr[i]-eps),direct(rr[i]+eps)
        if expected_stability == 'attractor':
            assert left > 0.0 and right < 0.0
        else:
            assert left < 0.0 and right > 0.0
    return rr


if __name__ == '__main__':
    H, L, theta = 3.0, 5.0, 17.0/64.0
    r = verify(H,L,theta)
    expected_C = ((45.0-16.0*math.sqrt(2.0))/17.0,
                  (45.0+16.0*math.sqrt(2.0))/17.0)
    for x,c in zip(root_C(H,theta),expected_C):
        assert abs(x-c)<1e-13
    print('Exact-parameter example: four investments',*[f'{v:.14f}' for v in r])
    print('Classification: repeller, attractor, repeller, attractor')

    random.seed(271828)
    good = 0
    for _ in range(140):
        H = random.uniform(2.12,7.0)
        h = math.acosh(H)
        L = h+random.uniform(0.75,3.0)
        Q = math.cosh(L)
        lower = max(1.0/(H+1.0),f(H,Q))
        upper = H*H/(4.0*(H*H-1.0))
        assert lower < upper
        theta = lower+(upper-lower)*random.uniform(0.12,0.88)
        verify(H,L,theta)
        good += 1
    print(f'PASS: {good} additional parameter triples; each checked by 4096 direct-benefit grid brackets')
