"""Exact finite tests for interval maximal variation with horizon cutoff.
This checks examples and small finite data sets, not an infinite proof.
"""
from fractions import Fraction
from itertools import product
from random import Random

def maximal(x, cap):
    n=len(x)
    assert n>=2 and 1<=cap<=n
    x=[abs(v) for v in x]
    best=[Fraction(0)]*n
    for a in range(n):
        s=0
        for b in range(a, min(n,a+cap)):
            s+=x[b]
            avg=Fraction(s,b-a+1)
            for i in range(a,b+1):
                if avg>best[i]: best[i]=avg
    return best

def variation(x):
    return sum(abs(x[j+1]-x[j]) for j in range(len(x)-1))

def prove_case(x, cap):
    n=len(x)
    v=variation(x)
    if v==0:return
    new=variation(maximal(x,cap))
    target=Fraction(n-1,n) if cap==n else Fraction(1)
    assert new<=target*v,(n,cap,x,new,v,target)

# Exhaustive three-level profiles for each R, small orders.
profiles=0
for n in range(2,9):
    for x in product(range(3),repeat=n):
        for cap in range(1,n+1):
            prove_case(x,cap); profiles+=1
        if n>=2:
            # input at first endpoint, exact sharpness for all caps
            pass
    delta=(1,)+(0,)*(n-1)
    for cap in range(1,n+1):
        r=variation(maximal(delta,cap))/variation(delta)
        expected=Fraction(n-1,n) if cap==n else Fraction(1)
        assert r==expected,(n,cap,r,expected)
print('exhaustive nonnegative ternary profile-cap checks:',profiles)

# Signed arbitrary fractions, both endpoints, random profiles.
rng=Random(1824)
checks=0
for n in (9,10,13,21,37):
    for _ in range(120):
        x=[Fraction(rng.randint(-13,13),rng.randint(1,8)) for j in range(n)]
        for cap in (1,2,max(1,n//2),n-1,n):
            prove_case(x,cap);checks+=1
print('signed rational profile-cap checks:',checks)
print('endpoint sharpness checks:',sum(range(2,9)))
print('ALL CHECKS PASSED')
