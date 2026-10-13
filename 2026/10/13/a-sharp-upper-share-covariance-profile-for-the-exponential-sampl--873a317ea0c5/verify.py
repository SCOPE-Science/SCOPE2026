#!/usr/bin/env python3
"""Reproduce exact Gini/top-share covariance for normalized exponential samples.
Requires Python 3 standard library only; optional NumPy not used.
"""
from fractions import Fraction
from math import isclose, log, sqrt
import random

def harmonic(n):
    return sum((Fraction(1,j) for j in range(1,n+1)), Fraction())

def explicit_cov(n,k):
    h = harmonic(n)-harmonic(k)
    return Fraction(k,2*n*n*(n+1))*((n+1)*h-(n-k))

def dirichlet_cov(n,k):
    # Independent calculation from exact second moments of Z~Dirichlet(1,...,1).
    a=[Fraction(j-1,n) for j in range(1,n+1)]
    b=[min(Fraction(1),Fraction(k,n-j+1)) for j in range(1,n+1)]
    sa=sum(a); sb=sum(b)
    return (n*sum((a[j]*b[j] for j in range(n)),Fraction())-sa*sb)/Fraction(n*n*(n+1))

def delta_sign(n,k):
    return (n+1)*(harmonic(n)-harmonic(k))-2*(n-k)

def gini_top(sample,k):
    xs=sorted(sample)
    t=sum(xs)
    n=len(xs)
    g=sum((2*j-n-1)*xs[j-1] for j in range(1,n+1))/(n*t)
    top=sum(xs[-k:])/t
    return g,top

def independent_linear_rep(sample,k):
    xs=sorted(sample); n=len(xs); total=sum(xs)
    y=[(n-j+1)*(xs[j-1]-(xs[j-2] if j>1 else 0.)) for j in range(1,n+1)]
    z=[yy/total for yy in y]
    g=sum((j-1)*z[j-1] for j in range(1,n+1))/n
    t=sum(min(1.0,k/(n-j+1))*z[j-1] for j in range(1,n+1))
    return g,t

def exhaustive_algebra():
    count=0
    for n in range(2,151):
        H=harmonic(n)
        c=[]
        for k in range(1,n+1):
            x=explicit_cov(n,k)
            assert x==dirichlet_cov(n,k),(n,k,x)
            assert x > 0 if k<n else x==0
            c.append(x)
            count+=1
        if n>2:
            diffs=[c[k]-c[k-1] for k in range(1,n)]
            for k,delta in enumerate(diffs,1):
                assert delta == delta_sign(n,k)/Fraction(2*n*n*(n+1))
        threshold=next(k for k in range(1,n) if delta_sign(n,k)<=0)
        for j in range(1,n+1):
            assert c[j-1]<=c[threshold-1]
        ties=[j for j in range(1,n+1) if c[j-1]==c[threshold-1]]
        assert ties==([threshold,threshold+1] if delta_sign(n,threshold)==0 else [threshold])
        if n in (2,3,5,6,10,50,100,150):
            print('n',n,'maximizers',ties,'cov',float(c[threshold-1]))
    print('EXACT_CASES',count)

def monte_carlo():
    rng=random.Random(20261008)
    reps=40000
    for n,k in [(2,1),(3,1),(6,2),(10,2),(20,4)]:
        sg=st=sgt=0.
        for _ in range(reps):
            xs=[rng.expovariate(1) for i in range(n)]
            g,t=gini_top(xs,k)
            a,b=independent_linear_rep(xs,k)
            assert isclose(g,a,rel_tol=1e-10,abs_tol=1e-12)
            assert isclose(t,b,rel_tol=1e-10,abs_tol=1e-12)
            sg+=g;st+=t;sgt+=g*t
        cv=sgt/reps-(sg/reps)*(st/reps)
        exact=float(explicit_cov(n,k))
        print('MC',n,k,'empirical',cv,'exact',exact,'relative_err',abs(cv-exact)/exact)
        assert abs(cv-exact)<max(0.001,0.06*exact)

def asymptotic():
    import math
    a=0.2
    for _ in range(20):
        a -= (math.log(a)-2*a+2)/(1/a-2)
    assert 0.203<a<0.204
    print('alpha',a,'limiting_n_cov',a*(1-a)/2)
    for n in (100,400,1000):
        H=[0.0]*(n+1)
        for j in range(1,n+1): H[j]=H[j-1]+1/j
        vals=[k*((n+1)*(H[n]-H[k])-(n-k))/(2*n*n*(n+1)) for k in range(1,n+1)]
        ki=max(range(1,n+1),key=lambda k:vals[k-1])
        print('ASYM',n,ki,ki/n,n*vals[ki-1])
        assert abs(ki/n-a)<0.03

if __name__=='__main__':
    exhaustive_algebra(); monte_carlo(); asymptotic(); print('VERIFY_OK')
