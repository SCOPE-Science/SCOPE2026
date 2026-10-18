#!/usr/bin/env python3
"""Independent finite tests for the denominator-density theorem (stdlib only)."""
from fractions import Fraction
from math import gcd, log, exp

def factors(n):
    f = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def h(n):
    out = 1
    for p,a in factors(n).items():
        out *= (p**(2*a+1)+1)//(p+1)
    return out

def v(n,p):
    c = 0
    while n % p == 0:
        c += 1
        n //= p
    return c

# Exact rational sum vs independently factored product.
for n in range(1,261):
    original = sum((Fraction(1,gcd(n,j)) for j in range(1,n+1)), Fraction())
    assert original == Fraction(h(n),n), n
    for ell in (2,3,5,7,11,13,17,19):
        assert (original.denominator % ell == 0) == (v(n,ell)>v(h(n),ell)), (n,ell)

# Small exact values, independently testing the simplified five-adic factor rule.
X=120000
sp=list(range(X+1))
for p in range(2,int(X**.5)+1):
    if sp[p]==p:
        for j in range(p*p,X+1,p):
            if sp[j]==j: sp[j]=p

def count_five(N):
    count=0
    for n in range(1,N+1):
        rem=n
        b=0
        cost=0
        while rem>1:
            p=sp[rem]
            a=0
            while rem%p==0:
                rem//=p
                a+=1
            if p==5: b=a
            elif p%5==4:
                m=2*a+1
                while m%5==0:
                    m//=5
                    cost+=1
        if b>cost: count+=1
    return count
assert count_five(1000)==200
assert count_five(10000)==1994
assert count_five(100000)==19928

# Convergent product approximation using a separate elementary prime sieve.
P=100000
isprime=bytearray(b'\x01')*(P+1)
isprime[:2]=b'\x00\x00'
for p in range(2,int(P**.5)+1):
    if isprime[p]:
        for k in range(p*p,P+1,p):isprime[k]=0
acc=0.0
for p in range(2,P+1):
    if not isprime[p] or p%5!=4: continue
    s=1.0
    pk=1.0
    for a in range(1,12):
        pk/=p
        m=2*a+1
        c=0
        while m%5==0:
            m//=5
            c+=1
        s+=pk*5.0**(-c)
    acc+=log((1-1/p)*s)
delta=exp(acc)/5
assert 0.19923 < delta < 0.19926,delta
print('VERIFY_OK', 'exact_sums',260,'five_denominator_count_100000',19928,'euler_approx',format(delta,'.10f'))
