#!/usr/bin/env python3
"""Finite congruence tests for the prime-power zero-sum bound."""
from itertools import combinations_with_replacement
from math import gcd

def least_prime_factor(n):
    for p in range(2,n+1):
        if n%p==0:return p

def phi(n):
    return sum(1 for j in range(1,n+1) if gcd(j,n)==1)

def root_of_order(n,p,k):
    assert (p-1)%n==0
    z=None
    for a in range(2,p):
        if pow(a,n,p)==1 and all(pow(a,n//d,p)!=1 for d in range(2,n+1) if n%d==0 and all(d%e for e in range(2,__import__('math').isqrt(d)+1))):
            z=a;break
    if z is None:raise AssertionError(('root',n,p))
    for j in range(2,k+1):
        pj=p**(j-1)
        c=((pow(z,n,pj*p)-1)% (pj*p))//pj
        derivative=(n*pow(z,n-1,p))%p
        t=(-c*pow(derivative,-1,p))%p
        z+=t*pj
        assert pow(z,n,p**j)==1
    assert pow(z,n,p**k)==1
    assert all(pow(z,n//d,p)!=1 for d in range(2,n+1) if n%d==0 and all(d%e for e in range(2,__import__('math').isqrt(d)+1)))
    return z

def m_value(p,n,k):
    modulus=p**k; root=root_of_order(n,p,k); r=least_prime_factor(n)
    powers=[pow(root,j,modulus) for j in range(n)]
    for s in range(2,r):
        for J in combinations_with_replacement(range(n),s-1):
            if (1+sum(powers[j] for j in J))%modulus==0:
                return s
    return r

cases={ (5,11):[3,5,5],(5,61):[4,5],(7,29):[4,7],(7,43):[3,7],
        (11,23):[3,5,9,9,11],(11,67):[4,8,11],(13,53):[3,7,12,13] }
for (n,p),expected in cases.items():
    bound=(least_prime_factor(n)-1)**phi(n)
    K=1
    while p**K<=bound:K+=1
    got=[m_value(p,n,k) for k in range(1,len(expected)+1)]
    assert got==expected,(n,p,got,expected)
    assert len(expected)<=K, (n,p,K,expected)
    print('PASS',n,p,'K_bound',K,'m_sequence',got)
print('VERIFIER_OK',sum(len(s) for s in cases.values()),'prime-power instances')
