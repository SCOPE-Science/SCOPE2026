#!/usr/bin/env python3
"""Finite independent checks for a general row-content identity."""
from math import comb, gcd, lcm
from functools import reduce


def test_sequence(seq, max_n):
    P=[1]
    for n in range(1,max_n+1): P.append(P[-1]*seq(n))
    L=1
    for n in range(1,max_n+1):
        prev=L
        L=lcm(L,seq(n))
        if n<2: continue
        values=[]
        for k in range(1,n):
            d=P[k]*P[n-k]
            assert P[n]%d==0,(seq,n,k)
            values.append(P[n]//d)
        g=reduce(gcd, values)
        assert g==L//prev,(n,g,L//prev)

def fibonacci():
    a,b=0,1
    while True:
        a,b=b,a+b
        yield a

def test_minimizing_columns(seq, max_n, primes):
    P=[1]
    for j in range(1,max_n+1): P.append(P[-1]*seq(j))
    def valuation(x,p):
        t=0
        while x%p==0:
            x//=p
            t+=1
        return t
    for p in primes:
        ranks=[]
        for j in range(1,max_n+1):
            v=valuation(seq(j),p)
            while len(ranks)<v: ranks.append(j)
        for n in range(2,max_n+1):
            proper=[r for r in ranks if r<n and n%r==0]
            k=max(proper) if proper else 1
            B=P[n]//(P[k]*P[n-k])
            assert valuation(B,p)==sum(r==n for r in ranks),(p,n,k,ranks)

if __name__ == '__main__':
    test_sequence(lambda n:n, 72)
    for q in [2,3,5]:
        test_sequence(lambda n,q=q:(q**n-1)//(q-1), 45)
    f=[0]
    it=fibonacci()
    for i in range(1,81): f.append(next(it))
    test_sequence(lambda n:f[n], 75)
    chains={2:(1,2,6,18,54),3:(3,9,27),5:(1,5,25),7:(7,14,28)}
    def artificial(n):
        v=1
        for p, ranks in chains.items():
            v*=p**sum(n%r==0 for r in ranks)
        return v
    test_sequence(artificial, 90)
    for seq, max_n in [(lambda n:n,60), (lambda n:(2**n-1),45), (lambda n:f[n],55), (artificial,75)]:
        test_minimizing_columns(seq,max_n,[2,3,5,7,11,13,17,19,23,31])
    for a in range(1,90):
        for b in range(1,90):
            assert gcd(artificial(a),artificial(b))==artificial(gcd(a,b))
    print('VERIFY_OK: ordinary 72 rows; Gaussian 3 x 45 rows; Fibonacci 75 rows; synthetic chained-rank 90 rows and 7,921 independent gcd pairs')
