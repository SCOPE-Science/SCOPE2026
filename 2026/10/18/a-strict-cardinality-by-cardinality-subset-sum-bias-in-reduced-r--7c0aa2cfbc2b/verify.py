#!/usr/bin/env python3
"""Independent finite arithmetic tests for fixed-cardinality unit subset sums."""
from math import comb, gcd

def primes_dividing(n):
    return [p for p in range(2,n+1) if n%p==0 and all(p%j for j in range(2,int(p**0.5)+1))]

def coefficient(p,m):
    c=[1]
    for _ in range(m):
        nxt=[0]*(len(c)+p-1)
        for i,a in enumerate(c):
            for j in range(p):
                nxt[i+j]+=a
        c=nxt
    return c

def dp_counts(units,p):
    d=[[0]*p for _ in range(len(units)+1)]
    d[0][0]=1
    j=0
    for a in units:
        j+=1
        for r in range(j,0,-1):
            for b in range(p):
                d[r][b]+=d[r-1][(b-a)%p]
    return d

def check(N):
    U=[a for a in range(1,N) if gcd(a,N)==1]
    for p in primes_dividing(N):
        m=len(U)//(p-1)
        assert all(sum(a%p==v for a in U)==m for v in range(1,p))
        coeff=coefficient(p,m)
        got=dp_counts(U,p)
        for r in range(len(U)+1):
            val=(-1)**r*coeff[r]
            assert coeff[r]>0
            assert all((comb(len(U),r)+((p-1) if b==0 else -1)*val)%p==0 for b in range(p))
            predicted=[(comb(len(U),r)+((p-1) if b==0 else -1)*val)//p for b in range(p)]
            assert got[r]==predicted,(N,p,r,got[r],predicted)
            assert got[r][0]-got[r][1]==val
    if N%2==1:
        # The nonempty-subset equidistribution of Gaitanas is distinct from fixed r.
        d=[[0]*N for _ in range(len(U)+1)]
        d[0][0]=1
        j=0
        for a in U:
            j+=1
            for r in range(j,0,-1):
                for b in range(N):
                    d[r][b]+=d[r-1][(b-a)%N]
        sums=[sum(d[r][b] for r in range(1,len(U)+1)) for b in range(N)]
        assert len(set(sums))==1,(N,sums)

if __name__=='__main__':
    for n in range(2,97):
        check(n)
    print('VERIFY_OK: 95 moduli; all prime-divisor/cardinality/residue counts; positivity; odd-modulus nonempty subset contrast')
