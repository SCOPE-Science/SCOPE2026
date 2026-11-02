#!/usr/bin/env python3
"""Reproducibility checks for the two-candidate sketched quotient law.

Dependencies: Python 3.10+, numpy, scipy, sympy, mpmath.
No external files, network, or hidden fixtures are needed.
"""
import math
import numpy as np
import sympy as sp
from scipy import integrate, special
import mpmath as mp


def exact(k: int, rho: float) -> float:
    mp.mp.dps = 55
    rr = mp.mpf(str(rho))
    kk = mp.mpf(k)
    c = mp.gamma((kk+1)/2)**2/(mp.pi*kk*mp.gamma(kk))
    return float(c * rr**k * mp.hyper([mp.mpf('0.5'),(kk+1)/2,kk/2],
                                      [kk,kk/2+1],rr*rr))


def integral(k: int, rho: float) -> float:
    if k == 1:
        return math.asin(rho)/math.pi
    a = (k-1)/2
    norm = special.beta(0.5,k/2)
    def fn(t):
        return (rho**k/norm*t**(k-1)*
                special.betainc(a,0.5,1-t*t)/
                math.sqrt(1-rho*rho*t*t))
    val, err = integrate.quad(fn, 0, 1, epsabs=1.e-13,
                              epsrel=1.e-12, limit=200)
    assert err < 1.e-9, (k, rho, err)
    return val


def checks():
    checks = 0
    # Algebraic cross-multiplication of both sketched Rayleigh quotients.
    a,b,U,Z,V,c,s = sp.symbols('a b U Z V c s', real=True)
    nx = a*c**2*U+b*s**2*Z+(a+b)*c*s*V
    ny = a*s**2*U+b*c**2*Z+(a+b)*c*s*V
    dx = c**2*U+s**2*Z+2*c*s*V
    dy = s**2*U+c**2*Z+2*c*s*V
    target = (a-b)*(c*c-s*s)*((c*c+s*s)*U*Z+c*s*V*(U+Z))
    assert sp.expand(nx*dy-ny*dx-target) == 0
    checks += 1
    # Exact beta integral, closed-form k=1 and k=2 limits, and positivity.
    for k in [1,2,3,4,5,6,8,12,20,32]:
        old = -1
        for rho in [0.05,0.2,0.45,0.7,0.92]:
            p = exact(k, rho)
            assert 0 < p < 0.5
            assert p > old
            old = p
            if k == 1:
                assert abs(p-math.asin(rho)/math.pi) < 3.e-13
            else:
                pi = integral(k,rho)
                assert abs(p-pi) < max(6.e-11,1.e-9*p), (k,rho,p,pi)
            if k == 2:
                p2 = 0.5-special.ellipe(rho*rho)/math.pi
                assert abs(p-p2) < 4.e-13, (rho,p,p2)
            checks += 1
    # Exact rational nonrandom examples establish event direction,
    # including some where the ranking is inverted.
    for (uv, zv, vv) in [(2, 5, -3), (4, 4, -3), (3, 2, -2),
                         (4, 6, 2), (10, 1, -2), (5, 8, -4)]:
        # Ensure Gram matrix is positive definite when required.
        if uv*zv<=vv*vv:
            continue
        for theta in [0.15,0.45,0.75]:
            cc,ss=math.cos(theta),math.sin(theta)
            for aa,bb in [(-2, 3),(0,1),(7,8)]:
                numerator_x=aa*cc**2*uv+bb*ss**2*zv+(aa+bb)*cc*ss*vv
                denominator_x=cc**2*uv+ss**2*zv+2*cc*ss*vv
                numerator_y=aa*ss**2*uv+bb*cc**2*zv+(aa+bb)*cc*ss*vv
                denominator_y=ss**2*uv+cc**2*zv+2*cc*ss*vv
                actual=numerator_x/denominator_x>numerator_y/denominator_y
                predicted=uv*zv+cc*ss*vv*(uv+zv)<0
                assert actual==predicted,(uv,zv,vv,theta,aa,bb)
                checks+=1
    # Large-k normalizing constant and hypergeometric ratio.
    rho=0.64
    for k in [24,48,96,192]:
        p=mp.mpf(str(exact(k,rho)))
        asy=(mp.sqrt(2/mp.pi)*(mp.mpf(str(rho))/2)**k /
             (mp.sqrt(k)*mp.sqrt(1-mp.mpf(str(rho))**2/2)))
        rel=float(p/asy)
        assert abs(rel-1)<11/k, (k,rel)
        checks+=1
    # Coupled direct Gaussian trials; reproducible fixed seed and wide tolerance.
    rng=np.random.default_rng(14912)
    for k,theta,rows in [(1,0.22,140000),(2,0.35,140000),
                         (3,0.51,180000),(6,0.65,240000)]:
        g=rng.standard_normal((rows,k))
        h=rng.standard_normal((rows,k))
        C,S=math.cos(theta),math.sin(theta)
        x=C*g+S*h
        y=S*g+C*h
        ax=-1.*C*g+2.*S*h
        ay=-1.*S*g+2.*C*h
        Qx=np.sum(x*ax,axis=1)/np.sum(x*x,axis=1)
        Qy=np.sum(y*ay,axis=1)/np.sum(y*y,axis=1)
        rho=math.sin(2*theta)
        U=np.sum(g*g,axis=1)
        Z=np.sum(h*h,axis=1)
        V=np.sum(g*h,axis=1)
        theoretical=U*Z+(rho/2)*V*(U+Z)<0
        assert np.array_equal((Qx>Qy),theoretical)
        prob=exact(k,rho)
        empirical=float(np.mean(theoretical))
        # Standard binomial uncertainty with 6-sigma allowance + sampling floor.
        bound=6*math.sqrt(prob*(1-prob)/rows)+0.001
        assert abs(empirical-prob)<bound,(k,prob,empirical,bound)
        checks+=rows+1
    print(f'PASS: {checks} exact/numerical/direct randomized checks')
    print('Verified: cross-multiplication, beta integral, k=1/2 forms,')
    print('monotonicity probes, large-k constants, shared-sketch event.')
    print('Limits: finite tests do not prove the general theorem; see proof.')

if __name__=='__main__':
    checks()
