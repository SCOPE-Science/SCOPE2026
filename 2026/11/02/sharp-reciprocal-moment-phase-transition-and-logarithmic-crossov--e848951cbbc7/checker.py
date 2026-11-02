#!/usr/bin/env python3
"""Exact finite-state checks for minimal-walk occupancy reciprocal moments."""
from fractions import Fraction as F
from math import gamma, lgamma, log, exp

def law(p, nmax):
    a=[F(0), F(1)]
    for n in range(1,nmax):
        b=[F(0)]*(n+2)
        for k in range(1,n+1):
            prob=p*k/n
            b[k]+=a[k]*(1-prob)
            b[k+1]+=a[k]*prob
        a=b
        yield n+1,a

def check():
    checks=0
    for p in (F(1,3),F(1,2),F(2,3)):
        h=[F(0),F(1)]
        for n,a in [(1,h)]+list(law(p,34)):
            assert sum(a)==1;checks+=1
            assert a[1] == __import__('functools').reduce(lambda v,j:v*(1-p/F(j)),range(1,n),F(1));checks+=1
            lhs=sum((a[k]/F(k-1) for k in range(2,n+1)),F(0))
            rhs=p*a[1]*sum((1/(F(j)-p) for j in range(1,n)),F(0))
            assert lhs==rhs;checks+=1
            for u in (F(1,3),F(1,2),F(3,4)):
                vals=[F(0)]*(n+1)
                vals[1]=F(1)
                for k in range(1,n): vals[k+1]=vals[k]*(1-u/F(k))
                lhs=sum((a[k]*vals[k] for k in range(1,n+1)),F(0))
                rhs=__import__('functools').reduce(lambda v,j:v*(1-p*u/F(j)),range(1,n),F(1))
                assert lhs==rhs,(p,n,u,lhs,rhs)
                checks+=1
    assert checks==612,checks
    print('PASS',checks,'exact-rational assertions (three discounts, n=1..34)')
    # independent floating-point large-n recursion checks, no asymptotic proof claimed
    p=.5
    for nmax in (800,1600,3200):
        q=[0.0]*(nmax+2);q[1]=1.0
        for n in range(1,nmax):
            # only occupied prefix n. Avoid in-place spillover contamination.
            for k in range(n,0,-1):
                t=q[k]*p*k/n
                q[k]-=t
                q[k+1]+=t
        d1=sum(q[k]/k for k in range(1,nmax+1))
        target=p/ gamma(1-p)*nmax**(-p)*(log(nmax)-__import__('scipy').special.digamma(1-p))
        assert abs(d1/target-1)<.06,(nmax,d1,target)
        print('n',nmax,'inverse_mean',format(d1,'.10g'),'two_term_ratio',format(d1/target,'.7f'))
    print('PASS numerical consistency checks')
if __name__=='__main__':check()
