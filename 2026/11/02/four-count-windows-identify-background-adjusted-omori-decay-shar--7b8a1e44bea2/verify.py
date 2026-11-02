"""Reproducible finite checks for four-bin identifiability of background-shifted Omori rates.

The global zero-count and interval integral arguments are analytical and are in RESULT.md.
Numerical checks do not certify the infinite-domain statements.
"""
import math
import random
from fractions import Fraction
import sympy as sp
import numpy as np


def binmean(mu, K, c, p, a, b):
    if abs(p-1.0) < 1e-11:
        decay = math.log((b+c)/(a+c))
    else:
        decay = ((b+c)**(1-p)-(a+c)**(1-p))/(1-p)
    return mu*(b-a)+K*decay


def rate(mu, K, c, p, t):
    return mu+K*(c+t)**(-p)


def jac(mu,K,c,p,a,b):
    # Jacobian entries: d_mu, d_K, d_c, d_p, with mpmath quadrature.
    import scipy.integrate as sint
    z=lambda t:t+c
    return np.array([
        b-a,
        sint.quad(lambda t:z(t)**(-p),a,b,epsabs=1e-13)[0],
        -K*p*sint.quad(lambda t:z(t)**(-p-1),a,b,epsabs=1e-13)[0],
        -K*sint.quad(lambda t:z(t)**(-p)*math.log(z(t)),a,b,epsabs=1e-13)[0],
    ])


def main():
    t=sp.symbols('t',real=True)
    f1=1+1/(t+1)
    f2=sp.Rational(111,100)+sp.Rational(7,2)/(t+2)**2
    cross=sp.factor((f1-f2)*(t+1)*(t+2)**2*100)
    assert sp.simplify(cross+(t-3)*(11*t**2-12*t+2))==0
    roots=[(6-sp.sqrt(14))/11,(6+sp.sqrt(14))/11,sp.Integer(3)]
    assert all(float(r)>0 for r in roots)
    assert all(sp.simplify((f1-f2).subs(t,r))==0 for r in roots)
    assert sp.expand((t+3)**2-sp.Rational(17,2)*(t+1))==sp.expand((2*t**2-5*t+1)/2)
    rng=random.Random(12349)
    checked=0
    for i in range(150):
        mu=10**rng.uniform(-1,1)
        K=10**rng.uniform(-1,1)
        c=10**rng.uniform(-.7,1)
        p=rng.uniform(.35,2.8)
        # disjoint positive-duration windows with arbitrary gaps and widths
        ends=[]; z=0.0
        for _ in range(4):
            a=z+rng.uniform(.05,.30); b=a+rng.uniform(.3,1.3)
            ends.append((a,b));z=b
        for a,b in ends:
            val=binmean(mu,K,c,p,a,b)
            from scipy.integrate import quad
            q=quad(lambda t:rate(mu,K,c,p,t),a,b,epsabs=1e-12)[0]
            assert abs(val-q)<2e-11*max(1.,abs(q))
            checked+=1
        # Jacobian full rank: scaling by column norms avoids huge dynamic ranges
        J=np.array([jac(mu,K,c,p,a,b) for a,b in ends])
        Jn=J/np.linalg.norm(J,axis=0)
        det=np.linalg.det(Jn)
        assert abs(det)>2e-14,(i,det,ends,(mu,K,c,p))
        checked+=1
        # Three-window rank nonzero, and two known-mu columns have rank two
        assert np.linalg.matrix_rank(J[:3,:3],tol=1e-13)==3
        assert np.linalg.matrix_rank(J[:2,1:3],tol=1e-13)==2
        checked+=2
    print('VERIFY_OK: exact 3-crossing polynomial and known-background 2-crossing witness; %d numerical integral/Jacobian/rank checks'%checked)

if __name__=='__main__':
    main()
