#!/usr/bin/env python3
"""Exact finite boundary verification for global prime-counting root inequality."""
from math import isqrt

def prime_counts(limit):
    sieve=bytearray(b'\x01')*(limit+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if sieve[p]: sieve[p*p:limit+1:p]=b'\x00'*((limit-p*p)//p+1)
    counts=[0]*(limit+1)
    for j in range(1,limit+1): counts[j]=counts[j-1]+sieve[j]
    return counts

def exact_sign(c,n,k):
    a,b=c[n*k],c[n*(k+1)]
    return (a**(k+1)>b**k)-(a**(k+1)<b**k)

def run():
    # The analytic proof covers n>=2, nk>=17 except n=3,
    # which is covered only for nk>=128.
    pairs=[(n,k) for n in range(2,17) for k in range(1,18//n+1)
           if n*k<17]
    pairs += [(3,k) for k in range(1,43)]
    pairs=sorted(set(pairs))
    c=prime_counts(max(n*(k+1) for n,k in pairs))
    nonpositive=[]
    for n,k in pairs:
        sg=exact_sign(c,n,k)
        if sg!=1: nonpositive.append((n,k,sg,c[n*k],c[n*(k+1)]))
    want=[(2,1,-1,1,2),(2,2,-1,2,3),(4,1,0,2,4)]
    assert nonpositive==want, (nonpositive,want)
    assert len(pairs)==len(set(pairs))
    print('BOUNDARY_CHECK_OK',len(pairs), 'nonpositive',nonpositive)

if __name__=='__main__':run()
