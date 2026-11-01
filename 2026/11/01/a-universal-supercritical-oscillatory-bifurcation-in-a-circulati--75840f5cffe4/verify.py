#!/usr/bin/env python3
"""Reproduce algebraic and finite numerical checks for a circulating logistic triad.
Requires Python 3.10+ and SymPy. Experiments corroborate, but do not prove, the local theorem.
"""
from __future__ import annotations
import math
import random
import cmath
import sympy as sp


def symbolic_normal_form():
    k = sp.symbols("k", real=True, positive=True)
    t = 2/(1+k**2)
    r = 1+t
    lam = sp.simplify(1-t+sp.I*k*t)
    beta = -r*(1+sp.I*k)
    gamma = (-2*r*r/t)*(-2+sp.I*k)
    p = sp.simplify(beta/(sp.conjugate(lam)**2-lam))
    assert sp.simplify(p - ((k**2+1)*(k**2+3)/(2*(3*k**2-1)))) == 0
    assert sp.simplify(sp.conjugate(lam)*lam-1) == 0
    first = sp.simplify(sp.re((gamma+2*beta*sp.conjugate(p))/lam))
    expected = -((k*k+3)**3)/(k*k+1)**2
    assert sp.simplify(first-expected) == 0
    assert sp.simplify(lam-(k+sp.I)/(k-sp.I)) == 0
    assert sp.simplify(first.subs(k,sp.sqrt(3))+sp.Rational(27,2)) == 0
    return first


def map_point(x, r, c):
    raw = [r*x[j]*(1-x[j]+c*(x[(j+1)%3]-x[(j-1)%3])) for j in range(3)]
    return [min(1.0,max(0.0,z)) for z in raw]


def check_fourier_polynomial():
    rng = random.Random(20261029)
    omega = cmath.exp(2j*math.pi/3)
    for _ in range(500):
        r = 1.01 + 1.7*rng.random()
        c = 0.01 + 1.6*rng.random()
        k = math.sqrt(3)*c
        t = r-1.0
        q = 1-1/r
        u = .03*(2*rng.random()-1)
        z = complex(.015*(2*rng.random()-1), .015*(2*rng.random()-1))
        x = [q+u+z*omega**j+z.conjugate()*omega**(-j) for j in range(3)]
        y = [r*x[j]*(1-x[j]+c*(x[(j+1)%3]-x[(j-1)%3])) for j in range(3)]
        up = sum(yy-q for yy in y)/3
        zp = sum((y[j]-q)*omega**(-j) for j in range(3))/3
        uh = (1-t)*u-r*u*u-2*r*abs(z)**2
        zh = (1-t+1j*k*t)*z+r*(-2+1j*k)*u*z-r*(1+1j*k)*z.conjugate()**2
        assert abs(up-uh)<5e-13, (up, uh)
        assert abs(zp-zh)<5e-13, (zp, zh)
    return 500


def check_linear_crossing():
    rng=random.Random(20261030)
    for _ in range(150):
        c=.02+2.5*rng.random()
        k=math.sqrt(3)*c
        rc=1+2/(1+k*k)
        q=1-1/rc
        assert 0<q<1
        for r, want in [(1+(rc-1)*.95,False),(rc+1e-3,True)]:
            rho=abs(2-r+1j*k*(r-1))
            assert (rho>1)==want
            if not want:
                assert abs(2-r)<1
    return 300


def check_asymptotic_amplitude():
    # At c=1, the coefficient is exactly -27/2 in Fourier amplitude.
    # This convergence check is only diagnostic; a numerical orbit is not a proof.
    out=[]
    w=cmath.exp(2j*math.pi/3)
    for mu,steps in [(0.001,30000),(0.0004,80000)]:
        r=1.5+mu
        q=1-1/r
        x=[q+.015*math.cos(2*math.pi*j/3) for j in range(3)]
        for _ in range(steps):
            x=map_point(x,r,1.0)
        z=sum((x[j]-q)*w**(-j) for j in range(3))/3
        predicted=math.sqrt(mu/13.5)
        ratio=abs(z)/predicted
        assert 0.92<ratio<1.08, (mu, ratio)
        assert all(0<v<1 for v in x)
        out.append((mu,ratio))
    return out


def main():
    l1=symbolic_normal_form()
    n1=check_fourier_polynomial()
    n2=check_linear_crossing()
    amp=check_asymptotic_amplitude()
    print('symbolic center-manifold/normal-form identity: PASS')
    print('exact first Lyapunov coefficient:', sp.sstr(l1))
    print('exact Fourier polynomial identities: %d random cases PASS' % n1)
    print('Schur crossing checks: %d parameter cases PASS' % n2)
    print('sample emergent circle Fourier radii vs leading prediction:', amp)
    print('all tests PASS; finite computations do not establish existence or priority')

if __name__=='__main__':
    main()
