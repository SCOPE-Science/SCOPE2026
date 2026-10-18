#!/usr/bin/env python3
"""Exact check of a two-prime-support commutation classification."""
from math import gcd, isqrt

def factors(n):
    f={}; d=2
    while d*d<=n:
        while n%d==0:
            f[d]=f.get(d,0)+1;n//=d
        d+=1 if d==2 else 2
    if n>1:f[n]=f.get(n,0)+1
    return f

def derivative(n):
    if n==1:return 0
    f=factors(n)
    return sum((n//p)*k for p,k in f.items())

def totient(n):
    if n==1:return 1
    result=n
    for p in factors(n):result=result//p*(p-1)
    return result

def prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def check(limit):
    count=0
    for a in range(2,limit+1):
        for b in range(2,limit+1):
            n=2**a*3**b
            lhs=totient(derivative(n))
            rhs=derivative(totient(n))
            expected=(a%2==0 and prime(3*(a//2)+b))
            assert (lhs==rhs)==expected,(a,b,lhs,rhs)
            count+=1
    print('PASS: exact arithmetic for',count,'interior lattice pairs through',limit)
    for u,b in [(1,2),(2,2),(3,2),(1,3),(4,3),(7,9)]:
        n=2**(2*u)*3**b
        print('u,b,3u+b,commute',u,b,3*u+b,totient(derivative(n))==derivative(totient(n)))
    print('small index sequence check')
    known=[1,3,8,28,32,36,40,50,56,80,128,176,184,228,324,368,448,472,504,560,576,664,704,1328,1336,1512,1620,1686,1816,2048]
    found=[n for n in range(1,2049) if totient(derivative(n))==derivative(totient(n)) if derivative(n)>=1]
    # n=1 is in the public table by convention, but phi(D(1)) is undefined without phi(0).
    assert [n for n in found if n<=2048] ==known[1:]
    print('PASS: agreement with listed positive terms of OEIS A260961 through 2048, excluding 1 convention')
if __name__=='__main__':check(55)
