#!/usr/bin/env python3
"""Independent numerical checks for marked Zipf coupon extremes."""
import math
import random


def finite_tail(n, alpha, x=0.0, cutoff=None):
    L=math.log(n)
    b=L-math.log(L)-math.log(alpha)
    threshold=b+x
    assert threshold>0
    total=0.0
    no_max=0.0
    restricted=0.0
    for k in range(1,n+1):
        rate=(n/k)**alpha
        p=math.exp(-rate*threshold)
        total+=p
        no_max+=math.log1p(-p)
        if cutoff is not None and alpha*L*(1-k/n)<=cutoff:
            restricted+=p
    return total,math.exp(no_max),restricted


def check():
    assertions=0
    # Ensure the proposed normalization and spatial mark are consistent.
    for alpha in (0.5,1.0,2.0):
        for x in (-0.5,0.0,0.6):
            for n in (2000,10000,50000,200000):
                mass,cdf,portion=finite_tail(n,alpha,x,cutoff=1.5)
                target=math.exp(-x)
                error=abs(mass-target)/target
                if n==200000:
                    assert error<0.28,(alpha,x,error)
                    assertions+=1
                    assert abs(cdf-math.exp(-target))<0.15,(alpha,x,cdf)
                    assertions+=1
                    if alpha==1.0 and x==0:
                        assert abs(portion/mass-(1-math.exp(-1.5)))<0.10,(portion/mass)
                        assertions+=1
    # Simulation provides a separate finite-sample sanity check of winner positions.
    rng=random.Random(721191)
    n=5000
    alpha=1.0
    trials=500
    marks=[]
    heights=[]
    b=math.log(n)-math.log(math.log(n))
    for _ in range(trials):
        m=-1.0
        ind=-1
        for k in range(1,n+1):
            t=rng.expovariate((n/k)**alpha)
            if t>m:
                m=t
                ind=k
        marks.append(alpha*math.log(n)*(1-ind/n))
        heights.append(m-b)
    mark_mean=sum(marks)/trials
    height_mean=sum(heights)/trials
    assert 0.72<mark_mean<1.22,mark_mean; assertions+=1
    assert 0.20<height_mean<1.05,height_mean; assertions+=1
    mark_cdf=sum(v<1 for v in marks)/trials
    assert abs(mark_cdf-(1-math.exp(-1)))<0.10,mark_cdf;assertions+=1
    print(f'PASS {assertions} checks. MC mark mean={mark_mean:.5f}, height mean={height_mean:.5f}, P(mark<1)={mark_cdf:.5f}.')

if __name__=='__main__':
    check()
