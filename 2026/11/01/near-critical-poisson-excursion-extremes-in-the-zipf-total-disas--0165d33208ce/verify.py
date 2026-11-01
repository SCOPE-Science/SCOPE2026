#!/usr/bin/env python3
"""Standalone numerical and exact checks for a near-critical Zipf disaster walk.
Finite checks illustrate the theorem; they do not prove its limiting assertions.
"""
import math
from fractions import Fraction
import mpmath as mp
import numpy as np


def a(c):
    return -math.expm1(-c)/c if c else 1.0


def intensity(c):
    return c/math.expm1(c) if c else 1.0


def truncated_mean(n, beta):
    return (mp.digamma(n+1)+mp.euler) if beta==1 else mp.zeta(beta) - mp.zeta(beta, n+1)


def walk_trial(n, c, rng):
    beta=1+c/math.log(n)
    total=0
    count=0
    maximum=0
    while total < n:
        # Rounding-down inverse CDF gives P(L >= k) = k^(-beta).
        u=rng.random(30000)
        L=np.floor(np.power(u,-1.0/beta)).astype(np.int64)
        cum=np.cumsum(L)
        j=int(np.searchsorted(cum,n-total,side='right'))
        if j:
            maximum=max(maximum,int(L[:j].max()-1))
            total+=int(cum[j-1]); count+=j
        if j<len(L):
            maximum=max(maximum, int(n-total))
            total=n
    return count, maximum


def main():
    checks=0
    for k in range(0,50):
        for beta in (1,2,3):
            pk=Fraction(k+1,k+2)**beta
            product=Fraction(1,1)
            for j in range(k+1):
                product*=Fraction(j+1,j+2)**beta
            assert product==Fraction(1,k+2)**beta
            checks+=1
            tail=Fraction(1,k+1)**beta
            assert (tail-Fraction(1,k+2)**beta)>=0
            checks+=1
    mp.mp.dps=65
    print('A(c), lambda(c), truncated-mean ratios and spike intensity checks')
    for c in (-2.0,-0.75,0.0,0.75,2.0):
        aa=a(c); la=intensity(c)
        assert abs(la-aa**(-1)*math.exp(-c))<1e-12
        checks+=1
        for n in (10**9,10**40,10**100):
            beta=mp.mpf(1)+mp.mpf(str(c))/mp.log(n)
            mu=truncated_mean(n,beta)
            approx=float(mu/mp.log(n))
            assert abs(approx-aa)<0.05
            checks+=1
            b=mp.mpf(n)/mp.log(n)
            m=mp.mpf(n)/(mp.mpf(str(aa))*mp.log(n))
            k=int(b)
            marktail=mp.power(k+2,-beta)
            rate=float(m*marktail)
            if n==10**100:
                assert abs(rate-la)/la <0.06
                checks+=1
            print('c=%5.2f n=1e%-3d truncated/logn=%0.8f A=%0.8f markrate=%0.8f lambda=%0.8f'%(c,len(str(n))-1,approx,aa,rate,la))
    rng=np.random.default_rng(20261027)
    n=400000
    reps=160
    print('simulated path horizon:',n,'replicates:',reps)
    for c in (-1.,0.,1.):
        data=np.array([walk_trial(n,c,rng) for _ in range(reps)],dtype=float)
        nn=n/math.log(n)
        expected_renewals=nn/a(c)
        expected_cdf=math.exp(-intensity(c))
        estimate=float(np.mean(data[:,1]/nn<=1.))
        print('c=%5.2f mean N/(n/logn)=%.6f limit=%.6f P(max<=n/logn)=%.5f limit=%.5f' %
             (c,float(data[:,0].mean()/nn),1/a(c),estimate,expected_cdf))
        assert 0.5*expected_renewals < data[:,0].mean()<1.6*expected_renewals
        checks+=1
    print('PASS: %d exact/numeric/seeded-simulation assertions; finite diagnostics are not infinite proofs'%checks)

if __name__=='__main__':
    main()
