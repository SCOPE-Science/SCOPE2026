#!/usr/bin/env python3
"""Finite-support sanity checks for exact asymptotic modulus formulas.

This numerical script is supplementary: infinite-dimensional claims follow
from tail estimates and quantifiers in the accompanying analytic proof.
"""
from math import sqrt, isclose


def bisect_root(fn, lo, hi, iterations=95):
    assert fn(lo)>0 and fn(hi)<0
    for _ in range(iterations):
        mid=(lo+hi)/2
        if fn(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def norm(vec, powers):
    assert len(vec)==len(powers)
    if not any(vec): return 0.0
    hi=sum(abs(v) for v in vec)+1
    return bisect_root(lambda z:sum((abs(v)/z)**p for v,p in zip(vec,powers))-1,
                       max(abs(v) for v in vec)*0.9999999,hi)


def predicted(x,p,t):
    assert isclose(sum(abs(v)**q for v,q in zip(x,p)),1.0,abs_tol=5e-13)
    return bisect_root(lambda L:sum(abs(v)**q/L**q for v,q in zip(x,p))+t/L-1,
                       max(1,t),2+t)


def run():
    for t in (.13,.75,1.,1.8):
        p=[2.]+[1.+1./n for n in range(2,4001)]
        x=[0.]*len(p);x[0]=1.
        root=predicted(x,p,t)
        for j in (4,20,100,1000,3000):
            v=x.copy();v[j]=t
            actual=norm(v,p)
            error=abs(actual-root)
            assert error<0.7/j, (t,j,error)
        low=bisect_root(lambda L:L**(-2)+t/L-1, max(1,t),2+t)
        assert isclose(root,low,abs_tol=1e-13)
        if t==1.:
            assert abs(root-(1+sqrt(5))/2)<1e-13
        for q in (1.001,1.01,1.1,1.5,2.):
            e=bisect_root(lambda L:L**(-q)+t/L-1,max(1,t),2+t)
            assert e<1+t and e>low-1e-13
        print(f't={t:.2f}; delta_root={root:.10f}; rho_sup={t:.10f}')

    p=[1.6,2.4,1.9]+[1+1/n for n in range(3,1503)]
    x=[0.]*len(p)
    x[0]=.6
    x[1]=(1-x[0]**p[0])**(1/p[1])
    assert abs(sum(abs(v)**q for v,q in zip(x,p))-1)<1e-14
    for t in (.1,.5,1.):
        root=predicted(x,p,t)
        for j in (10,100,300,1000):
            v=x.copy();v[j]=t
            actual=norm(v,p)
            assert abs(actual-root)<0.6/j, (t,j,actual,root)
    print('finite-support numerical checks PASS (not a proof of infinite quantifiers)')

if __name__=='__main__':run()
