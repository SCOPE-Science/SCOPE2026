#!/usr/bin/env python3
"""Exact finite verification of the first order-20 prime-square collision.
No statistical or asymptotic claims are inferred from finite tests.
"""
from fractions import Fraction as Q
from math import comb, factorial

def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))

E = tuple(a for a in range(21) if a % 6 != 4)
assert E == (0,1,2,3,5,6,7,8,9,11,12,13,14,15,17,18,19,20)
assert len(E) == 18
exception=[]
for d in range(1,21):
    for q in range(5,1024):
        if prime(q) and (2**d-1) % (q*q) == 0:
            exception.append((d,q))
assert exception == [(20,5)], exception
primes=[p for p in range(5,180) if prime(p)]
for p in primes:
    rs=[pow(2,a,p*p) for a in E]
    assert len(set(rs)) == (17 if p==5 else 18), (p,rs)
    for k in range(19):
        T=E[:k]
        j=len(T)
        distinct=len({pow(2,a,p*p) for a in T})
        if p==5:
            assert distinct==j-int(k==18) # pair occurs in the full prefix
        else:
            assert distinct==j
# Check all subset cardinalities for the 5-square factor, including the pair.
for mask in range(1<<18):
    T=[E[i] for i in range(18) if mask>>i&1]
    j=len(T)
    r5=len({pow(2,a,25) for a in T})
    e=((mask&1)!=0 and (mask&(1<<17))!=0)
    assert r5==j-int(e)
    actual=Q(20-r5,20)
    fake=Q(20-j,20)
    assert actual == fake+Q(int(e),20)
# Exact finite-prime model: sixteen q>=7 are just enough for a
# collision at q=5 to cover 18 labels. Naive distinct classes cannot.
qs=[p for p in primes if p>=7][:16]
def H(j):
    ans=Q(20-j,20)
    for q in qs:
        ans*=Q(q*(q-1)-j,q*(q-1))
    return ans
naive=sum(((-1)**j)*comb(18,j)*H(j) for j in range(19))
correction=sum(((-1)**j)*comb(16,j-2)*H(j)/Q(20-j,1) for j in range(2,19))
witness=Q(factorial(16),20)
for q in qs:
    witness/=q*(q-1)
assert naive == 0, naive
assert correction == witness, (correction,witness)
assert correction>0
print('VERIFY_OK',len(E),len(exception),len(primes),1<<18,len(qs))
