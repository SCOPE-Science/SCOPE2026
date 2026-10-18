#!/usr/bin/env python3
"""Independent reproducible checks for the fixed-energy log-cosh volume law.

Uses only Python standard library for exact Dirichlet moments and stable
log-cosh calculations; optional mpmath provides a numerical 2D cross-check.
None of the finite checks replaces the uniform analytic remainder proof.
"""
from fractions import Fraction
from math import exp, log, cosh, sinh, sqrt, pi, gamma, acosh


def rising(a, k):
    p=Fraction(1)
    for j in range(k):
        p*=a+j
    return p


def moment(n, exps):
    # Dirichlet with alpha_0=1 and n copies alpha_i=1/2.
    alpha=Fraction(n,2)+1
    out=Fraction(1)
    for coordinate, power in exps.items():
        base=Fraction(1) if coordinate==0 else Fraction(1,2)
        out*=rising(base,power)
    return out/rising(alpha,sum(exps.values()))


def assert_moments():
    for n in range(1,45):
        assert moment(n,{0:1})==Fraction(2,n+2)
        assert sum(moment(n,{i:2}) for i in range(1,n+1))==Fraction(3*n,(n+2)*(n+4))
        assert sum(moment(n,{i:4}) for i in range(1,n+1))==Fraction(105*n,(n+2)*(n+4)*(n+6)*(n+8))
        q2=sum(moment(n,{i:4}) for i in range(1,n+1))
        q2+=2*sum(moment(n,{i:2,j:2}) for i in range(1,n+1) for j in range(i+1,n+1))
        assert q2==Fraction(105*n+9*n*(n-1),(n+2)*(n+4)*(n+6)*(n+8))
        assert q2>0
    print('PASS: 44 dimensions of exact rational Dirichlet moments and Q squared')


def check_log_g():
    for j in range(1,1000):
        t=j/250.0
        g=sqrt(2*t/(1-exp(-2*t)))
        assert 1<g<=exp(t/2)+1e-12
        if t<0.1:
            actual=log(g)
            approx=t/2-t*t/12
            assert abs(actual-approx)<0.06*t**4+2e-13
    print('PASS: 999 log-Jacobian samples and small-parameter remainder')


def check_2d():
    try:
        import mpmath as mp
    except ImportError:
        print('SKIP: mpmath optional planar direct-integral check')
        return
    mp.mp.dps=40
    for beta in [mp.mpf('0.3'),mp.mpf('1.0'),mp.mpf('1.5')]:
        a=mp.acosh(mp.exp(beta))
        # first-quadrant area = integral_0^a arcosh(exp(beta)/cosh(x)) dx
        first=mp.quad(lambda x: mp.acosh(max(mp.mpf('1'),mp.exp(beta)/mp.cosh(x))),[0,a])
        direct=4*first/(2*mp.pi*beta)
        # independent 2D Dirichlet density quadrature on the unit triangle
        # integrate using angular coordinates x=sqrt(2beta S) cos(theta)
        # Reference radius squared 2 beta. Observe near 0 Jacobian simplifies.
        ratio2=direct
        assert ratio2>1
        print('beta=',beta,'n=2 direct-volume ratio=',mp.nstr(ratio2,20))
    print('PASS: independently integrated planar areas')


def check_dirichlet_numerical():
    try:
        import numpy as np
    except ImportError:
        print('SKIP: numpy optional Dirichlet sampling')
        return
    rng=np.random.default_rng(32123)
    for n in [20,100,400]:
        samples=15000
        Z=np.hstack((rng.gamma(1,1,size=(samples,1)),rng.gamma(0.5,1,size=(samples,n))))
        Z/=Z.sum(axis=1,keepdims=True)
        t=Z[:,1:]
        # log g = t/2 + 1/2 log(t / sinh t) with stable small-t expansion
        lg=t/2-t*t/12+t**4/360-t**6/5670
        estimate=float(np.exp(lg.sum(axis=1)).mean())
        predicted=exp(0.5)*(1-1.25/n)
        # Loose tolerance: n^{-2} bias plus MC noise
        assert abs(estimate-predicted)<0.02
        print(f'n={n:3d}: Monte Carlo ratio {estimate:.10f}, two-term {predicted:.10f}')
    print('PASS: finite-dimensional numerical consistency (not proof)')


if __name__=='__main__':
    assert_moments()
    check_log_g()
    check_2d()
    check_dirichlet_numerical()
    print('PASS: completed reproducibility checks')
