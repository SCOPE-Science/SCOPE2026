#!/usr/bin/env python3
"""Finite independent spot-checks of a proved prime-square support theorem."""
from itertools import combinations
from math import isqrt


def prime_factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n%d == 0:
            out.append(d)
            while n%d == 0:
                n //= d
        d = 3 if d == 2 else d+2
    if n>1:
        out.append(n)
    return out


def sieve(limit):
    flags = bytearray(b'\x01') * (limit+1)
    flags[0:2] = b'\x00\x00'
    for i in range(2, isqrt(limit)+1):
        if flags[i]:
            flags[i*i:limit+1:i] = b'\x00'*((limit-i*i)//i+1)
    return [i for i in range(2, limit+1) if flags[i]]


def verify():
    ps = sieve(110)  # 29 primes
    checked = 0
    for triple in combinations(ps, 3):
        total = sum(p*p for p in triple)
        outsider = [l for l in prime_factors(total) if l%4 == 3 and l not in triple]
        assert outsider, (triple, total)
        checked += 1
    assert checked == 3654

    expected = {46206: (2, [2,3,17,151]), 72105:(69,[3,5,11,19,23])}
    for n,(q,f) in expected.items():
        assert prime_factors(n)==f
        assert n//sum(p*p for p in f)==q
        assert n%sum(p*p for p in f)==0

    N=300000
    spf=list(range(N+1))
    for p in range(2,isqrt(N)+1):
        if spf[p] == p:
            for m in range(p*p,N+1,p):
                if spf[m]==m:
                    spf[m]=p
    hits=0
    for n in range(2,N+1):
        m=n; f=[]
        while m>1:
            p=spf[m]; f.append(p)
            while m%p==0:
                m//=p
        if len(f) < 2:
            continue
        if n % sum(p*p for p in f) == 0:
            assert len(f)>=4, (n,f)
            if n%2:
                assert len(f)>=5, (n,f)
            hits+=1
    assert hits>0
    print(f'VERIFY_OK: {checked} distinct-prime triples, all n<=300000, two sharp witnesses, {hits} qualifying non-prime-powers')

if __name__=='__main__':
    verify()
