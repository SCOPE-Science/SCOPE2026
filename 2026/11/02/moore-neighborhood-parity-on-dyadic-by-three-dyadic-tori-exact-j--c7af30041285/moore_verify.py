#!/usr/bin/env python3
"""Reproduce rank and finite-state checks for Moore-neighbor parity on 2-power by 3*2-power tori.
Pure Python, no external dependencies. This verifies finite instances, not the infinite-family proof.
"""
from collections import Counter

def matrix(M,N):
    rows=[]
    for i in range(M):
        for j in range(N):
            z=0
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if (di,dj)!=(0,0):
                        z^=1<<(((i+di)%M)*N+(j+dj)%N)
            rows.append(z)
    return rows

def apply(rows,v):
    return sum(((v & row).bit_count()&1)<<i for i,row in enumerate(rows))

def mul(A,B):
    C=[]
    for row in A:
        out=0
        while row:
            k=(row&-row).bit_length()-1
            out^=B[k]
            row&=row-1
        C.append(out)
    return C

def rank(rows):
    pivot={}
    for r in rows:
        while r:
            j=r.bit_length()-1
            if j in pivot: r^=pivot[j]
            else:
                pivot[j]=r
                break
    return len(pivot)

def xorid(A):return [v^(1<<i) for i,v in enumerate(A)]

def check_ranks(M,d):
    N=3*d;n=M*N
    L=max(M,d)//2;c=2*min(M,d)
    A=matrix(M,N)
    P=[1<<i for i in range(n)]
    ranks=[]
    for k in range(L+2):
        observed=n-rank(P)
        expected=c*min(k,L)
        assert observed==expected,(M,d,'zero-kernel',k,observed,expected)
        ranks.append(observed)
        P=mul(A,P)
    P=A
    fixed=[]
    for j in range(d.bit_length()):
        observed=n-rank(xorid(P))
        expected=2*M*min(2**j,d)
        assert observed==expected,(M,d,'fixed-kernel',j,observed,expected)
        fixed.append(observed)
        P=mul(P,P)
    return {'M':M,'N':N,'L':L,'zero_blocks':c,'recurrent_blocks':2*M,'kerT':ranks,'kerTpow_minusI':fixed}

def check_exhaustive(M=4,d=1):
    N=3*d;n=M*N;assert n<=16
    rows=matrix(M,N)
    population=Counter()
    for x in range(1<<n):
        seen={};v=x;t=0
        while v not in seen:
            seen[v]=t
            v=apply(rows,v)
            t+=1
        entry=seen[v];p=t-entry
        population[(entry,p)]+=1
    L=max(M,d)//2;c=2*min(M,d)
    for entry in range(L+1):
        cnt=(1<<(2*M*d+c*entry))-(1<<(2*M*d+c*(entry-1))) if entry else 1<<(2*M*d)
        assert population[(entry,1)]==cnt,(entry,cnt,population)
    assert sum(population.values())==1<<n
    assert all(p==1 for _,p in population)
    return dict(sorted(population.items()))

if __name__=='__main__':
    total=0
    for M in (4,8,16,32):
        for d in (1,2,4,8):
            if 3*M*d>384:continue
            r=check_ranks(M,d)
            total+=1
            print('PASS',r)
    print('EXHAUSTIVE',check_exhaustive())
    print('ALL_TESTS_PASSED cases=',total)
