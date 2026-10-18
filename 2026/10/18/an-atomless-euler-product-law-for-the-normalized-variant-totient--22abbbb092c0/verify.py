#!/usr/bin/env python3
"""Independent finite checks for a summatory estimate of a recently defined arithmetic function."""
from math import gcd, log
from fractions import Fraction
from itertools import product

def omega(n):
    z = 0
    p=2
    while p*p<=n:
        if n%p==0:
            z+=1
            while n%p==0:n//=p
        p += 1 if p==2 else 2
    return z + (n>1)

def b_value(n):
    r=Fraction(1)
    if n%2==0:
        r/=2
        while n%2==0:n//=2
    p=3
    while p*p<=n:
        if n%p==0:
            r*=Fraction(p-2,p)
            while n%p==0:n//=p
        p+=2
    if n>1:r*=Fraction(n-2,n)
    return r

def T(n):
    if n==1:return 0
    return sum(gcd(k,n)==1 and gcd(2*k+1,n)==1 for k in range((n+1)//2))

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,int(n**.5)+1):
        if sieve[p]:sieve[p*p::p]=b'\x00'*((n-p*p)//p+1)
    return [i for i in range(n+1) if sieve[i]]

if __name__=='__main__':
    for n in range(1,1201):
        t,b=T(n),b_value(n)
        assert abs(Fraction(2*t)-n*b) <= 3**omega(n)
        if n%4==0:assert Fraction(2*t)==n*b
    unique = set()
    for bits in product((0,1), repeat=9):
        z = Fraction(1)
        for p, bit in zip(primes_upto(23), bits):
            if bit:
                z *= Fraction(1,2) if p==2 else Fraction(p-2,p)
        assert z not in unique
        unique.add(z)
    print('finite Euler-product factors: PASS, 512 distinct exact rational products')
    ps=primes_upto(200000)
    c=0.1875
    for p in ps:
        if p>2:c*=1-2/p**2
    print('finite direct checks: PASS 1..1200')
    print('Euler constant approximate through p<=200000:', format(c,'.12f'))
    for x in (100,300,1000,2000):
        total=sum(T(n) for n in range(1,x+1))
        print('x',x,'sum',total,'sum/x²',format(total/x**2,'.9f'),'limit approx',format(c,'.9f'), 'scaled err', format((total-c*x*x)/(x*(log(x)**2)),'.5f'))
