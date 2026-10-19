#!/usr/bin/env python3
"""Exact checks for two-level randomly pivoted Cholesky capture law.
Run using Python 3 standard library: python verify.py
"""
from fractions import Fraction
from math import comb, factorial, log, sqrt
from collections import defaultdict
from functools import lru_cache
import random


def laplace(r,a,j):
    product = Fraction(1)
    for h in range(1,r+1):
        product *= Fraction(a*h,a*h+j)
    return product

def pmf_exact(n,r,a):
    m=n-r
    return [comb(m,l)*sum(((-1)**j)*comb(l,j)*laplace(r,a,m-l+j)
                            for j in range(l+1)) for l in range(m+1)]

def pmf_markov(n,r,a):
    m=n-r
    @lru_cache(None)
    def proceed(h,l):
        if h==r: return {l:Fraction(1)}
        w=Fraction(a*(r-h),a*(r-h)+m-l)
        ans=defaultdict(Fraction)
        for end,p in proceed(h+1,l).items(): ans[end]+=w*p
        if l<m:
            for end,p in proceed(h,l+1).items(): ans[end]+=(1-w)*p
        return ans
    law=proceed(0,0)
    return [law.get(l,Fraction(0)) for l in range(m+1)]

def mean_formula(n,r,a):
    return (n-r)*(1-laplace(r,a,1))

def var_formula(n,r,a):
    m=n-r; q=laplace(r,a,1); q2=laplace(r,a,2)
    mean=m*(1-q)
    fact2=m*(m-1)*(1-2*q+q2)
    return fact2+mean-mean*mean

def main():
    checks=0
    for n in range(2,11):
      for r in range(1,n):
       for a in (2,3,4,7):
        p=pmf_exact(n,r,a)
        q=pmf_markov(n,r,a)
        assert p==q,(n,r,a,p,q)
        checks+=len(p)
        assert sum(p)==1
        assert sum(l*t for l,t in enumerate(p))==mean_formula(n,r,a)
        assert sum((l*l)*t for l,t in enumerate(p))-mean_formula(n,r,a)**2==var_formula(n,r,a)
        checks+=3
    # The critical-window centering has asymptotically Poisson-scale variance.
    for n,r,a in ((1000,10,1000),(10000,100,10000),(100000,2000,100000)):
        H=sum(1/h for h in range(1,r+1))
        mu=(n-r)*H/n
        # direct stable logarithmic products: laplace moments, cancellation avoided
        import math
        log1=sum(math.log1p(1/(a*h)) for h in range(1,r+1))
        expmean=(n-r)*(-math.expm1(-log1))
        assert abs(expmean-mu)<0.5,(expmean,mu)
        checks+=1
    print(f'PASS {checks} exact-rational identities and asymptotic-centering checks')

if __name__=='__main__': main()
