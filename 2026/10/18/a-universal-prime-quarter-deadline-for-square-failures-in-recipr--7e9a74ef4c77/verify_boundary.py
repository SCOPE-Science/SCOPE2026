#!/usr/bin/env python3
"""Exact finite checks for the finite-field stopping-time bound and reciprocal sums."""
from math import gcd, isqrt
from fractions import Fraction

def primes_upto(n):
    a=[True]*(n+1);a[:2]=[False,False]
    for i in range(2,isqrt(n)+1):
        if a[i]:
            for j in range(i*i,n+1,i):a[j]=False
    return [i for i in range(n+1) if a[i]]

def first_hit(p,a):
    seen=set(); t=a; d=0
    while t not in seen and t:
        seen.add(t);t=(t+pow(t,-1,p))%p;d+=1
    return d if not t else None

def check_finite_fields():
    tested=0;hits=0;maxratio=(0,0)
    for p in primes_upto(2000):
        if p!=2 and p%4!=1: continue
        depth_counts={}
        for a in range(1,p):
            k=first_hit(p,a);tested+=1
            if k is not None:
                hits+=1;depth_counts[k]=depth_counts.get(k,0)+1
                if p==2: assert k==1
                assert p==2 or 4*k<=p+3,(p,a,k)
        H=sum(depth_counts.values())
        for k in depth_counts:
            if p!=2: assert H>=4*k-4,(p,k,H)
        if p==5: assert depth_counts=={1:2,2:2}
        if p==13: assert depth_counts=={1:2}
        if p==29: assert depth_counts=={1:2,2:4,3:2}
    return tested,hits

def integer_nonsquares(h,x0,max_n):
    # Generate direct reduced rational sequence independently.
    X=[Fraction(x0)];b=[]
    for n in range(1,max_n+1):
        X.append(Fraction(h*h,sum(X)))
        if n>=2:
            a,z=X[n].numerator,X[n].denominator
            val=Fraction(2*a,h)+z
            if isqrt(val.numerator)**2!=val.numerator or isqrt(val.denominator)**2!=val.denominator:
                b.append(n)
    return b

def predicted_bad(h,x0):
    out=[]
    for p in primes_upto(h):
        if h%p: continue
        e=0;z=h
        while z%p==0: e+=1;z//=p
        if x0%p**e:continue
        if (x0//p**e)%p==0:continue
        a=((x0//p**e)*pow(z,-1,p))%p
        k=first_hit(p,a)
        if k is not None:out.append(k+1)
    return sorted(set(out))

def check_recurrence():
    checks=0
    for h in range(1,41):
        ps=[p for p in primes_upto(h) if h%p==0]
        M=max([1]+([2] if 2 in ps else [])+[(p+7)//4 for p in ps if p%4==1])
        for x0 in range(1,min(2*h*h,120)+1):
            got=integer_nonsquares(h,x0,M+1)
            want=predicted_bad(h,x0)
            assert got==want,(h,x0,got,want)
            assert all(n<=M for n in got)
            checks+=1
    assert integer_nonsquares(5,5,5)==[3]
    return checks

if __name__=='__main__':
    print('FINITE_FIELDS',check_finite_fields())
    print('RECURRENCES',check_recurrence())
    print('SHARP_h5_x05',integer_nonsquares(5,5,5))
    print('VERIFY_OK')
