#!/usr/bin/env python3
"""Exact finite checks for ranks of U_0=0,U_1=1,U_{n+2}=s U_{n+1}-U_n.
All arithmetic uses Python integers. No external packages.
"""
from collections import Counter
from math import gcd

def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

def phi(n):
    return sum(gcd(i,n)==1 for i in range(1,n+1))

def theoretical_fibers(p,k):
    out=Counter({p**k:2*p**(k-1)})
    for A in ((p-1)//2,(p+1)//2):
        for d in divisors(A):
            if d==1: continue
            for j in range(k):
                r=d*p**j
                assert r not in out  # the two tame divisors are coprime
                out[r]=phi(r)
    assert sum(out.values())==p**k
    return out

def first_zero_rank(p,k,s):
    modulus=p**k
    a,b=0,1
    for n in range(1,modulus+2):
        if b==0:
            return n
        a,b=b,(s*b-a)%modulus
    raise AssertionError('No zero within p^k+1')

def main():
    total=0
    cases=[]
    for p,kmax in ((5,4),(7,3),(11,3),(13,3),(17,2),(19,2),(23,2),(29,2)):
        for k in range(1,kmax+1):
            m=p**k
            observed=Counter()
            for s in range(m):
                z=first_zero_rank(p,k,s)
                observed[z]+=1
                assert (z==m)==(s%p in (2,p-2)),(p,k,s,z)
            expected=theoretical_fibers(p,k)
            assert observed==expected,(p,k,observed,expected)
            total+=m
            cases.append((p,k,m,len(expected)))
            print('LEVEL_OK p=%d k=%d parameters=%d distinct_ranks=%d'%(p,k,m,len(expected)))
    print('VERIFY_OK fully_enumerated_parameters=%d levels=%d'%(total,len(cases)))
if __name__=='__main__': main()
