#!/usr/bin/env python3
"""Finite checks for the shifted-prime chain-density theorem (standard library)."""
import math


def sieve(bound):
    prime = bytearray(b'\x01') * (bound + 1)
    prime[0:2] = b'\x00\x00'
    for p in range(2, math.isqrt(bound) + 1):
        if prime[p]:
            start = p * p
            prime[start:bound+1:p] = b'\x00' * ((bound - start)//p + 1)
    return prime


def phi_sieve(bound):
    phi = list(range(bound+1))
    for p in range(2,bound+1):
        if phi[p] == p:
            for j in range(p,bound+1,p):
                phi[j] -= phi[j]//p
    return phi


def count_chains(X, prime):
    count=0
    contributions={}
    for p in range(2, math.isqrt(X)+1):
        if prime[p]:
            total=0
            for q in range(2*p+1, X//p+1, p+1):
                if prime[q]: total += 1
            count += total
            contributions[p]=total
    return count, contributions


def width_one_by_poset(p,q):
    vals={1,p+1,q+1,(p+1)*(q+1)}
    return all(a%b==0 or b%a==0 for a in vals for b in vals)


def main():
    bounds=[100,1000,10000,100000,1000000,10000000]
    P=sieve(max(bounds)//2)
    primes=[p for p in range(2,5001) if P[p]]
    tested=0
    for i,p in enumerate(primes):
        for q in primes[i+1:]:
            if p*q>10000: break
            assert width_one_by_poset(p,q) == ((q+1)%(p+1)==0)
            tested+=1
    phi=phi_sieve(100000)
    c=sum(1/(p*phi[p+1]) for p in range(2,100000) if P[p])
    assert .6328 < c < .6331, c
    print('finite equivalences:',tested)
    print('constant partial sum, primes <100000:',format(c,'.12f'))
    for X in bounds:
        ct, pp = count_chains(X,P)
        scale=ct*math.log(X)/X
        print('X:',X,'count:',ct,'scaled:',round(scale,8),'p=2:',pp.get(2,0),'p=3:',pp.get(3,0))
        if X<=10000:
            direct=sum(width_one_by_poset(p,q) for i,p in enumerate(primes) for q in primes[i+1:] if p*q<=X)
            assert direct == ct,(X,direct,ct)
    total, terms = count_chains(10000000,P)
    half,_ = count_chains(5000000,P)
    print('at X=10000000: share with n<=X/2:',round(half/total,8))
    print('at X=10000000: p=2 share:',round(terms[2]/total,8))
    print('VERIFY_OK')

if __name__=='__main__': main()
