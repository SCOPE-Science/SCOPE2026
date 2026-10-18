#!/usr/bin/env python3
"""Exact finite diagnostics for two-subset Peter-Weyl projection constants."""
from fractions import Fraction
from math import factorial
from itertools import permutations

def q_no_short_cycles(limit):
    q = [Fraction(0) for _ in range(limit+1)]
    q[0] = 1
    for n in range(2,limit):
        q[n+1] = (n*q[n] + q[n-2])/(n+1)
    return q

def coefficients(n):
    d = n*(n-3)//2
    return d

def kernel(n, fixed, two):
    d=coefficients(n)
    return 1+(n-1)*(fixed-1)+d*(fixed*(fixed-1)//2+two-fixed)

def cycle_counts(p):
    n=len(p)
    seen=[False]*n
    f=t=0
    for i in range(n):
        if seen[i]: continue
        j=i;k=0
        while not seen[j]:
            seen[j]=True
            j=p[j]
            k+=1
        if k==1:f+=1
        elif k==2:t+=1
    return f,t

def exact_formula(n,q):
    d=coefficients(n)
    return 1+2*((n-2)*q[n]+(d-1)*q[n-1]+Fraction(d-n,2)*q[n-2])

def single_block(n,q):
    return n*(n-3)*(q[n-1]+q[n-2]/2)

def run():
    q=q_no_short_cycles(35)
    assert (q[3],q[4],q[5],q[6]) == (Fraction(1,3),Fraction(1,4),Fraction(1,5),Fraction(2,9))
    checks=0
    for n in range(4,9):
        neg_mass=0
        abs_sum=0
        mean_sum=0
        neg_count=0
        for p in permutations(range(n)):
            f,t=cycle_counts(p)
            k=kernel(n,f,t)
            must_negative=(t==0 and (f<=1 or (f==2 and n>=6)))
            assert (k<0)==must_negative, (n,p,k)
            abs_sum+=abs(k)
            mean_sum+=k
            if k<0:
                neg_mass-=k;neg_count+=1
            checks+=1
        assert mean_sum==factorial(n)
        assert Fraction(abs_sum,factorial(n))==exact_formula(n,q)
        assert Fraction(neg_mass,factorial(n))==(exact_formula(n,q)-1)/2
        assert exact_formula(n,q)>single_block(n,q)
        print(n, 'lambda', exact_formula(n,q), 'single', single_block(n,q), 'negative permutations',neg_count)
    for n in range(6,35):
        assert Fraction(1,5)<=q[n]<=Fraction(1,4)
        assert exact_formula(n,q)>single_block(n,q)
        checks+=2
    print('PASS',checks,'exact permutation and recurrence assertions')

if __name__=='__main__':run()
