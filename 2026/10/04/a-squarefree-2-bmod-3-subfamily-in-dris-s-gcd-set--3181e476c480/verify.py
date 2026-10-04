#!/usr/bin/env python3
from math import gcd, isqrt, log, sqrt, pi

LIMIT = 1_000_000

# Smallest-prime-factor sieve.
spf = list(range(LIMIT + 1))
for i in range(2, isqrt(LIMIT) + 1):
    if spf[i] == i:
        for j in range(i*i, LIMIT + 1, i):
            if spf[j] == j:
                spf[j] = i

def factor(n):
    out=[]
    while n>1:
        p=spf[n]
        e=0
        while n%p==0:
            n//=p
            e+=1
        out.append((p,e))
    return out

def in_B(n):
    return all(e==1 and p%3==2 for p,e in factor(n))

def sigma_square_from_factorization(fac):
    # For squarefree m, sigma(m^2)=product(p^2+p+1).
    s=1
    for p,e in fac:
        assert e==1
        s *= p*p+p+1
    return s

expected={1000:193,10000:1651,100000:14798,1000000:135052}
count=0
for n in range(1,LIMIT+1):
    if in_B(n):
        count+=1
        if n<=100000:
            fac=factor(n)
            s=sigma_square_from_factorization(fac)
            assert gcd(n,s)==1
            assert gcd(n*n,s)==1
    if n in expected:
        assert count==expected[n], (n,count,expected[n])

# Sieve primes for a stable truncation of the Euler product constant.
sieve=bytearray(b'\x01')*(LIMIT+1)
sieve[0:2]=b'\x00\x00'
for p in range(2,isqrt(LIMIT)+1):
    if sieve[p]:
        sieve[p*p:LIMIT+1:p]=b'\x00'*(((LIMIT-p*p)//p)+1)
prod=1.0
for p in range(2,LIMIT+1):
    if sieve[p] and p%3==2:
        prod *= 1.0-1.0/(p*p)
C=sqrt(2.0*sqrt(3.0)*prod)/pi
assert 0.49820 < C < 0.49822

# Observed normalized count is already close to the limiting constant.
normalized=count*sqrt(log(LIMIT))/LIMIT
assert 0.49 < normalized < 0.52

print('VERIFY_OK')
print('B(1000)=193')
print('B(10000)=1651')
print('B(100000)=14798')
print('B(1000000)=135052')
print('C_truncated_1e6=%.12f' % C)
print('normalized_B_1e6=%.12f' % normalized)
