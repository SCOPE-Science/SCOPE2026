#!/usr/bin/env python3
"""Exact small-field checks for the rank profile of derivations of F_p[x]/(x^m)."""
from itertools import product
from collections import Counter

def rank_mod_p(M, p):
    A=[row[:] for row in M]
    n=len(A); m=len(A[0]) if n else 0
    r=0
    for c in range(m):
        piv=next((i for i in range(r,n) if A[i][c] % p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(n):
            if i!=r and A[i][c]%p:
                a=A[i][c]%p
                A[i]=[(x-a*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==n: break
    return r

def predicted(p,q,m):
    end=m if m%p==0 else m-1
    out=Counter({0:1})
    for t in range(1,end+1):
        out[t-t//p]+=(q-1)*q**(t-1)
    return out

def actual(p,m):
    q=p
    out=Counter()
    for f in product(range(q), repeat=m):
        if m%p and f[0]!=0: continue
        # D(x^i)=i*x^(i-1)*f; columns are coordinates in basis 1,x,...,x^(m-1).
        M=[[0]*m for _ in range(m)]
        for i in range(1,m):
            for j in range(m-i+1):
                # term f[j] x^(i-1+j) survives iff exponent < m
                e=i-1+j
                if e<m:
                    M[e][i]=(i*f[j])%p
        out[rank_mod_p(M,p)]+=1
    return out

cases=[]
for p, max_m in [(2,7),(3,5),(5,4)]:
    for m in range(2,max_m+1):
        a=actual(p,m); e=predicted(p,p,m)
        if a!=e:
            raise SystemExit(f'MISMATCH p={p},m={m}: actual={dict(a)} expected={dict(e)}')
        cases.append((p,m,sum(a.values()),sorted(a.items())))
print('ALL_CASES_PASS',len(cases))
for c in cases: print(c)
