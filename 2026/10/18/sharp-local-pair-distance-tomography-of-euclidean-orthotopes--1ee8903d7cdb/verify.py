"""Numerical diagnostics for local distance tomography of orthotopes.

Uses only Python's standard library. Finite checks corroborate, not prove, the theorem.
"""
import math
import random
from itertools import combinations

def omega(d):
    return math.pi**(d/2) / math.gamma(1+d/2)

def e_all(b):
    e=[1.0]+[0.0]*len(b)
    for q in b:
        for k in range(len(b),0,-1):
            e[k]+=q*e[k-1]
    return e

def coefficients(a):
    d=len(a)
    R=(math.prod(a)/omega(d))**(1/d)
    b=[R/x for x in a]
    e=e_all(b)
    c=[(-1)**k*math.gamma(1+d/2)/(math.pi**(k/2)*math.gamma(1+(d+k)/2))*e[k] for k in range(d+1)]
    assert abs(c[0]-1)<1e-12
    assert abs(e[-1]-1/omega(d))<1e-10
    return R,b,c

def cdfpoly(a,rho):
    d=len(a)
    R,b,c=coefficients(a)
    assert rho*R<min(a)
    return sum(c[k]*rho**(d+k) for k in range(d+1))

def numeric_cdf(a,rho,n=180000,seed=0):
    """Separate sampling using uniform-ball radius and normalised Gaussian direction."""
    rng=random.Random(seed)
    d=len(a)
    R,b,_=coefficients(a)
    v=omega(d)*rho**d
    acc=0.0
    for _ in range(n):
        q=[rng.gauss(0,1) for _ in a]
        z=rho*rng.random()**(1/d)/math.sqrt(sum(y*y for y in q))
        prod=1.0
        for y,bb in zip(q,b):
            prod*=max(0.0,1-bb*abs(y)*z)
        acc+=prod
    return v*acc/n / omega(d)

def sample_inversion(a):
    R,b,c=coefficients(a)
    d=len(a)
    e=[1.0]+[(-1)**k*c[k]*math.pi**(k/2)*math.gamma(1+(d+k)/2)/math.gamma(1+d/2) for k in range(1,d)]
    e.append(1/omega(d))
    expected=e_all(b)
    assert max(abs(x-y) for x,y in zip(e,expected))<1e-10


def test():
    for a in ([1,2,3],[1,1,1],[1,1.5,2.1,3.5],[1]*5):
        d=len(a); R,b,c=coefficients(a)
        sample_inversion(a)
        rho=0.3*min(a)/R
        analytic=cdfpoly(a,rho)
        numeric=numeric_cdf(a,rho,n=55000,seed=d*47)
        assert abs(numeric-analytic)<0.004*analytic, (a,analytic,numeric)
    # Independent direct pair sampling for 3D at a non-negligible threshold.
    a=[1,1.2,1.5]; d=3
    R,b,c=coefficients(a)
    rho=0.7*min(a)/R
    target=cdfpoly(a,rho)
    rng=random.Random(431)
    n=170000
    count=0
    for _ in range(n):
        norm=0
        for v in a:
            norm+=(v*(rng.random()-rng.random()))**2
        count+=(norm<(rho*R)**2)
    assert abs(count/n-target)<0.008, (count/n,target)
    # Coefficient product constraint and the cube boundary (equal repeated roots).
    for d in range(3,8):
        a=[1]*d
        _,b,c=coefficients(a)
        assert len(c)==d+1
        assert abs(e_all(b)[-1]-1/omega(d))<1e-12
    print('VERIFY_OK')

if __name__=='__main__':
    test()
