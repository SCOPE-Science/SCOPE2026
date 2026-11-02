#!/usr/bin/env python3
"""Finite exact checks of the combinatorial identities used in the theorem.
No simulation is presented as proof of asymptotic convergence.
"""
from math import comb, factorial
from collections import Counter
from fractions import Fraction
import argparse

def safe_choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def catalan(n):
    return comb(2*n,n)//(n+1)

def noncrossing(blocks):
    membership={x:i for i,b in enumerate(blocks) for x in b}
    n=sum(len(b) for b in blocks)
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            for c in range(b+1,n+1):
                if membership[a]!=membership[c]:continue
                for d in range(c+1,n+1):
                    if membership[b]==membership[d] and membership[a]!=membership[b]:return False
    return True

def partitions(n):
    if n==0:
        yield ()
        return
    for p in partitions(n-1):
        yield p + ((n,),)
        for i in range(len(p)):
            q=list(p)
            q[i]=q[i]+(n,)
            yield tuple(q)

def factorial_moment(n, rs):
    # Ordered distinct marked block occurrences of specified sizes.
    a=len(rs);R=sum(rs)
    if R>n:return Fraction(0)
    falling=1
    for z in range(a):falling*=n+1-z
    return Fraction(falling*safe_choose(2*n-R-a,n-a),comb(2*n,n))

def pos_probability(m,t,k):
    if t==0:return Fraction(int(k==0))
    return Fraction(safe_choose(m,k)*safe_choose(t-1,k-1),safe_choose(m+t-1,m-1))

def test():
    checks=0
    for n in range(1,9):
        obs=Counter()
        cross=0
        for p in partitions(n):
            if noncrossing(p):
                cross+=1
                profile=Counter(map(len,p))
                obs[tuple(profile.get(r,0) for r in range(1,n+1))]+=1
        assert cross==catalan(n),(n,cross,catalan(n));checks+=1
        total=catalan(n)
        for r in range(1,n+1):
            got=Fraction(sum(c*x[r-1] for x,c in obs.items()),total)
            assert got==factorial_moment(n,[r]),(n,r,got,factorial_moment(n,[r]));checks+=1
            for s in range(1,n+1):
                got2=Fraction(sum(c*x[r-1]*(x[s-1]-(r==s)) for x,c in obs.items()),total)
                expected=factorial_moment(n,[r,s])
                assert got2==expected,(n,r,s,got2,expected);checks+=1
        for k in range(1,n+1):
            empirical=sum(c for profile,c in obs.items() if sum(profile)==k)
            expected=safe_choose(n,k)*safe_choose(n,k-1)//n
            assert empirical==expected,(n,k,empirical,expected);checks+=1
    # Verify general factorial moments and Palm positive-count law by independent weak compositions.
    for m in range(2,10):
        for t in range(1,10):
            dp=Counter()
            def compositions(rem, slots, positives):
                if slots==0:
                    if rem==0:dp[positives]+=1
                    return
                for z in range(rem+1):compositions(rem-z,slots-1,positives+(z>0))
            compositions(t,m,0)
            den=safe_choose(m+t-1,m-1)
            assert sum(dp.values())==den
            checks+=1
            for k in range(m+1):
                assert Fraction(dp[k],den)==pos_probability(m,t,k),(m,t,k)
                checks+=1
    # Numerically inspect factorial moment scaling along powers of two.
    for n in (64,128,256,512,1024,2048):
        r=n.bit_length()-1
        f=float(factorial_moment(n,[r]))
        assert 0.25<f<1.0,(n,r,f)
        checks+=1
    print('PASS',checks-6,'exact finite assertions and 6 numerical scale checks; asymptotic argument is analytic')

if __name__=='__main__':test()
