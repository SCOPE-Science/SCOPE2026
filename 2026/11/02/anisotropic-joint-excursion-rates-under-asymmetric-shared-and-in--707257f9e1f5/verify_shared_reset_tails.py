#!/usr/bin/env python3
"""Reproducible checks for a two-coordinate common/local Poisson-reset model.

Python 3 standard library only. Tests corroborate the mathematical proof; they do not
certify infinite-parameter assertions, publication priority, or independent review.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
from random import Random


def rate(a,b,c,x,y):
    A, B, L = a+c, b+c, a+b+c
    if x >= A*y/sqrt(B*b):
        return x + y*sqrt(b/B), 'independent-x-age'
    if y >= B*x/sqrt(A*a):
        return y + x*sqrt(a/A), 'independent-y-age'
    return sqrt(L*(x*x/A + y*y/B)), 'common-age'


def base_cost(a,b,c,x,y):
    return sqrt((a+b+c)*(x*x/(a+c) + y*y/(b+c)))


def minimize_golden(f,left,right):
    invphi = (sqrt(5)-1)/2
    u = right - invphi*(right-left)
    v = left + invphi*(right-left)
    fu, fv = f(u), f(v)
    for _ in range(105):
        if fu > fv:
            left=u;u=v;fu=fv;v=left+invphi*(right-left);fv=f(v)
        else:
            right=v;v=u;fv=fu;u=right-invphi*(right-left);fu=f(u)
    return min(f(left),f(right),fu,fv)


def independent_minimization(a,b,c,x,y):
    h = lambda X,Y:base_cost(a,b,c,X,Y)
    fx = lambda z: z+h(x-z,y)
    fy = lambda z: z+h(x,y-z)
    return min(h(x,y),fx(0),fy(0),minimize_golden(fx,0,x),minimize_golden(fy,0,y))


def characteristic(a,b,c,k,l):
    A,B,L=a+c,b+c,a+b+c
    return (c+a/(1+l*l)+b/(1+k*k))/(L+A*k*k+B*l*l)


def run():
    count=0
    # Independent exact-rational stationary generator identity and pair marginals.
    for a in range(1,5):
        for b in range(1,5):
            for c in range(1,5):
                a,b,c=Q(a),Q(b),Q(c)
                A,B,L=a+c,b+c,a+b+c
                for k,l in [(Q(0),Q(0)),(Q(1,2),Q(3,5)),(Q(2),Q(1,3)),(Q(3,4),Q(5,4))]:
                    p=characteristic(a,b,c,k,l)
                    assert (L+A*k*k+B*l*l)*p == c+a/(1+l*l)+b/(1+k*k)
                    assert characteristic(a,b,c,k,Q(0))==1/(1+k*k)
                    assert characteristic(a,b,c,Q(0),l)==1/(1+l*l)
                    # Mixture of a single exponential-aged Gaussian and Laplace additions.
                    h = L/(L+A*k*k+B*l*l)
                    assert p == h*(c+a/(1+l*l)+b/(1+k*k))/L
                    count+=4
    rng=Random(2026102701)
    # Generic 3-sector formula versus direct 1D infimal-convolution optimization.
    for _ in range(2100):
        a,b,c=[10**rng.uniform(-2,2) for j in range(3)]
        x,y=[10**rng.uniform(-2,2) for j in range(2)]
        v,region=rate(a,b,c,x,y)
        w=independent_minimization(a,b,c,x,y)
        assert isclose(v,w,rel_tol=3e-10,abs_tol=3e-9),(a,b,c,x,y,v,w,region)
        assert v>max(x,y)-1e-10
        count+=2
    # Strict common-rate monotonicity with BOTH marginal reset rates fixed.
    for _ in range(1600):
        A,B=[10**rng.uniform(-1,2) for j in range(2)]
        c1=min(A,B)*rng.uniform(.0005,.65)
        c2=c1+(min(A,B)-c1)*rng.uniform(.005,.95)
        x,y=[10**rng.uniform(-1,1) for j in range(2)]
        r1=rate(A-c1,B-c1,c1,x,y)[0]
        r2=rate(A-c2,B-c2,c2,x,y)[0]
        assert r2<r1,(A,B,c1,c2,r1,r2)
        count+=1
    # Along the diagonal with equal marginal reset rates, the exponent is sqrt(4-2c/mu).
    for _ in range(750):
        mu=10**rng.uniform(-2,2)
        c=mu*rng.uniform(0.0001,0.9999)
        assert isclose(rate(mu-c,mu-c,c,1,1)[0],sqrt(4-2*c/mu),rel_tol=2e-13)
        count+=1
    # Source-model symmetric batch reset is a covered subcase, used as a consistency check.
    for N in range(3,17):
        for m in range(2,N):
            r=Q(7,3)
            a=r*m*(N-m)/Q(N*(N-1))
            b=a
            c=r*m*(m-1)/Q(N*(N-1))
            A=a+c
            beta=Q(2*N-m-1,N-1)
            assert (a+b+c)/A==beta
            for k,l in [(Q(0),Q(0)),(Q(1,3),Q(3,4))]:
                formula=(Q(2)-beta+(beta-1)*(1/(1+k*k)+1/(1+l*l)))/(beta+k*k+l*l)
                assert characteristic(a,b,c,k,l)==formula
                count+=1
    print('PASSED:',count,'exact rational/numerical consistency assertions')

if __name__=='__main__':
    run()
