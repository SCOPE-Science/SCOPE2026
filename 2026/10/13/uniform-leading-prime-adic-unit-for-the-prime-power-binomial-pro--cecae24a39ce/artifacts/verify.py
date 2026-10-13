#!/usr/bin/env python3
"""Exact independent checks for a prime-power binomial congruence."""
from math import comb, factorial

def primes_leq(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]

def digit_sum(x,p):
    out=0
    while x:out+=x%p;x//=p
    return out

def vfac(x,p):
    total=0
    while x:x//=p;total+=x
    return total

def digit_factorial_product(x,p):
    out=1
    while x:out=out*factorial(x%p)%p;x//=p
    return out

checks=0
for p in primes_leq(31):
    a=1
    while p**a<=150:
        A=p**a; K=A-1
        for q in range(2,A+1):
            N=q*K; M=(q-1)*K
            exponent=vfac(N,p)-vfac(K,p)-vfac(M,p)
            assert exponent==a,(p,a,q,'valuation',exponent)
            B=comb(N,K)
            assert B % (p*A)==(p-1)*A,(p,a,q,'congruence')
            unit_fact=(digit_factorial_product(N,p)*pow(digit_factorial_product(K,p),-1,p)*pow(digit_factorial_product(M,p),-1,p))%p
            ratio=(-1 if a&1 else 1)*unit_fact % p
            assert ratio==(p-1)%p,(p,a,q,'unit_digit_factorials',ratio)
            assert B//A%p==ratio,(p,a,q,'independent_comparison')
            checks+=1
        a+=1
print('VERIFY_OK',checks,'triples, direct binomials/Legendre exponents/digit-factorial units')
