#!/usr/bin/env python3
"""Recompute complete prime-field affine-code b-symbol enumerators independently.

Run: python verify_prime_rm.py
"""
from collections import Counter
from itertools import product
from random import Random


def predicted(p, m, b):
    n = p**m
    out = Counter({0: 1, n: p-1})
    for j in range(m):
        Q = p**j
        s = m-j-1
        B = p**s
        F = {0: 1}
        if s:
            for k in range(s):
                exponent = 1 if k == 0 else (p-1)*p**(k-1)
                G = Counter()
                for M, v in F.items():
                    G[M] += v*(p-1)
                    G[M+exponent] += v
                F = G
        for M, coefficient in F.items():
            if b <= Q:
                zero = B*(Q-b+1) + M*(b-1)
            elif b <= 2*Q:
                zero = M*(2*Q-b+1)
            else:
                zero = 0
            out[n-zero] += p*(p-1)*coefficient
    return +out


def actual(p, m, b):
    n=p**m
    digits=[[(i//p**j)%p for j in range(m)] for i in range(n)]
    out=Counter()
    for coef in product(range(p), repeat=m+1):
        w=[(coef[0]+sum(coef[j+1]*ds[j] for j in range(m)))%p for ds in digits]
        z=sum(all(w[(i+t)%n]==0 for t in range(b)) for i in range(n))
        out[n-z]+=1
    return +out


def checks():
    trials=0
    for p,m in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1),(5,2)]:
        for b in range(1,p**m+1):
            a=actual(p,m,b)
            e=predicted(p,m,b)
            assert a==e, (p,m,b,a,e)
            assert sum(e.values()) == p**(m+1)
            trials+=1
    r=Random(91385)
    for p,m in [(5,3),(7,2)]:
        for b in sorted({1,2,3,4,p,p+1,p**m//2,p**m-1,p**m}):
            if not (1<=b<=p**m):continue
            a=actual(p,m,b)
            e=predicted(p,m,b)
            assert a==e,(p,m,b,a,e)
            trials+=1
    print('PASS: '+str(trials)+' complete enumerator comparisons')
    for p,m in [(2,4),(3,3),(5,2)]:
        print('p,m,b= ',p,m,2,' spectrum=',dict(sorted(predicted(p,m,2).items())))

if __name__=='__main__': checks()
