#!/usr/bin/env python3
"""Reproducibility checks for two-point inverse of the ideal ponded Green-Ampt law.
The infinite-domain theorem is proved analytically in RESULT.md, not by sampling."""
import math
import random
from fractions import Fraction


def g(u):
    if u <= 0.2:
        s = 0.0
        term = u*u
        sign = 1.0
        for n in range(2,200):
            add = sign*term/n
            s += add
            if abs(add) <= max(abs(s), 1.e-290)*1.e-17:
                break
            sign = -sign
            term *= u
        return s
    return u-math.log1p(u)


def ratio(r,u):
    return g(r*u)/g(u)


def infer(F1,F2,t1,t2):
    r = F2/F1
    q = t2/t1
    if not (F1>0 and t1>0 and r>1 and r<q<r*r):
        return None
    lo=1.e-12
    hi=1.e12
    assert ratio(r,lo)>q>ratio(r,hi)
    for _ in range(180):
        mid=math.sqrt(lo*hi)
        if ratio(r,mid)>q:
            lo=mid
        else:
            hi=mid
    u=math.sqrt(lo*hi)
    B=F1/u
    K=F1*g(u)/(u*t1)
    return (K,B,u)


def prove_rational_derivative_identity():
    for numer in range(1,40):
        x=Fraction(numer,11)
        a=2*x/(x+2)-x*x/(x+2)**2-1+1/(1+x)
        b=x*x/((1+x)*(x+2)**2)
        assert a==b


def main():
    prove_rational_derivative_identity()
    rng=random.Random(77883)
    for i in range(4000):
        F1=math.exp(rng.uniform(-4,4))
        rho=math.exp(rng.uniform(0.05,2.5))
        u=math.exp(rng.uniform(-5,6))
        K=math.exp(rng.uniform(-4,4))
        B=F1/u
        F2=rho*F1
        t1=B*g(u)/K
        t2=B*g(rho*u)/K
        rec=infer(F1,F2,t1,t2)
        assert rec is not None
        K2,B2,u2=rec
        assert abs(K2/K-1)<4e-10,(i,K,K2)
        assert abs(B2/B-1)<4e-10,(i,B,B2)
        assert abs(u2/u-1)<4e-10,(i,u,u2)
        assert (rho < t2/t1 < rho*rho)
    for q in (1,2,4,8):
        assert infer(1,2,1,q) is None
    F1,F2,K,B=1.0,2.0,1.0,1.0
    t1=1-math.log(2)
    t2=2-math.log(3)
    assert max(abs(a-b) for a,b in zip(infer(F1,F2,t1,t2)[:2],(K,B)))<1e-12
    rho=2.0
    for u in (1e-5, 1e-4, 1e-3):
        delta=rho*rho-ratio(rho,u)
        approximated_u=3*delta/(2*rho*rho*(rho-1))
        assert abs(approximated_u/u-1)<0.005
    for u in (1e7,1e9,1e11):
        epsilon=ratio(rho,u)-rho
        approx= (rho-1)*math.log(u)/u
        assert abs(approx/epsilon-1)<0.12
    print('PASS: exact fraction checks, 4000 inverse trials, boundary and asymptotic tests')

if __name__=='__main__':main()
