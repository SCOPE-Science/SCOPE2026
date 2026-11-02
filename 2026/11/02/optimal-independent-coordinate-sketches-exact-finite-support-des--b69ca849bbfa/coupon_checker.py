"""Numerical and exact-enumeration checks for independent coordinate sketches.

The proof of the infinite-dimensional result is analytical; these checks
validate finite-dimensional reductions and asymptotic numerical predictions.
Run: python coupon_checker.py
"""
from __future__ import annotations
import itertools
import math
import random


def power_tail(s: float, start: int):
    """Euler-Maclaurin tail, with an explicit high-order remainder scale."""
    count=2000
    a=start+count
    finite=math.fsum(j**(-s) for j in range(start,a))
    tail=(a**(1-s)/(s-1)+a**(-s)/2+s*a**(-s-1)/12
          -s*(s+1)*(s+2)*a**(-s-3)/720
          +s*(s+1)*(s+2)*(s+3)*(s+4)*a**(-s-5)/30240)
    return finite+tail


def design(rho: float, samples: int):
    assert rho > 1 and samples >= 2
    delta = rho / (samples - 1)
    def f(t):
        # The support of the KKT optimum is precisely i < t.
        m = max(0, math.ceil(t) - 1)
        return sum(-math.expm1(delta * math.log(i/t)) for i in range(1,m+1))
    lo, hi = 1.0, float(max(4,samples*4))
    while f(hi) <= 1:hi *= 2
    for _ in range(75):
        mid = (lo+hi)/2
        if f(mid)>1:hi=mid
        else:lo=mid
    t=(lo+hi)/2
    m=math.ceil(t)-1
    q=[1 - (i/t)**delta for i in range(1,m+1)]
    exactcost=(m-1)*t**(-rho)+power_tail(rho,m+1)
    return t,q,exactcost


def brute_expected(rho, probs, samples):
    n=len(probs)
    out=0.0
    for indices in itertools.product(range(n),repeat=samples):
        pr=math.prod(probs[i] for i in indices)
        subset=set(indices)
        out+=pr*sum((j+1)**(-rho) for j in range(n) if j not in subset)
    return out


def run():
    checks=0
    random.seed(1709)
    # Exact finite sample-space enumeration, no simulation.
    for samples in range(2,5):
        for rho in [1.25, 2.0, 3.5]:
            probs=[random.random()+0.1 for _ in range(4)]
            probs=[p/sum(probs) for p in probs]
            formula=sum((i+1)**(-rho)*(1-probs[i])**samples for i in range(4))
            enum=brute_expected(rho,probs,samples)
            assert abs(formula-enum)<1e-12,(formula,enum)
            checks+=1
    # Full-support iid laws approximate the finite-support KKT infimum.
    for rho in [1.1,1.25,1.5,2.0,2.5,3.0,5.0]:
        for samples in [2,3,4,5,10,20,50,100]:
            t,q,cost=design(rho,samples)
            assert abs(sum(q)-1)<2e-12
            lam=samples*t**(-rho)
            for i,p in enumerate(q,1):
                assert p>0
                assert abs(samples*i**(-rho)*(1-p)**(samples-1)-lam)<1e-9
            m=len(q)
            assert (m+1)**(-rho)*samples <=lam*(1+1e-10)
            assert abs(sum((j+1)**(-rho)*(1-q[j])**samples for j in range(m))+power_tail(rho,m+1)-cost)<2e-9
            checks+=1
    for rho in [1.3,2.0,2.5,3.0,4.5]:
        ratios=[]
        for samples in [100,400,1600,6400]:
            t,q,cost=design(rho,samples)
            ratio=cost/power_tail(rho,samples+1)
            ratios.append(ratio)
            assert abs(t*rho/samples-1)<0.16
            assert abs(ratio/rho**rho-1)<0.45
            checks+=1
        assert abs(ratios[-1]/rho**rho-1)<0.015,(rho,ratios)
        print('rho',rho,'ratios', [round(x,6) for x in ratios], 'limit',round(rho**rho,6))
    # Exact two-draw law for spectra sigma_i^2=i^-rho.
    for rho in [1.1,1.5,2,3,5]:
        t,q,cost=design(rho,2)
        assert len(q)==2,(rho,t,q)
        a=2**(-rho)
        assert abs(q[0]-1/(1+a))<1e-11
        assert abs(q[1]-a/(1+a))<1e-11
        assert abs(cost-(power_tail(rho,3)+a/(1+a)))<1e-11
        checks+=1
    print('All checks passed:',checks)
if __name__=='__main__':run()
