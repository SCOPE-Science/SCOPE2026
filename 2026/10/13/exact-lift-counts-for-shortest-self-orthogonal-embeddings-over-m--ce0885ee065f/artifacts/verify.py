#!/usr/bin/env python3
import itertools, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))

def rank2(M):
    A=[list(row) for row in M]
    if not A:
        return 0
    m=len(A); n=len(A[0]); rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]&1),None)
        if p is None:
            continue
        A[rr],A[p]=A[p],A[rr]
        for i in range(m):
            if i!=rr and A[i][c]&1:
                A[i]=[x^y for x,y in zip(A[i],A[rr])]
        rr+=1
        if rr==m:
            break
    return rr

def f_flat(B,U):
    k=len(B); r=len(B[0])
    out=[]
    for a in range(k):
        for b in range(k):
            z=0
            for j in range(r):
                z ^= (B[a][j]&U[b][j]) ^ (U[a][j]&B[b][j])
            out.append(z)
    return tuple(out)

def map_matrix(B):
    k=len(B); r=len(B[0])
    cols=[]
    for a in range(k):
        for j in range(r):
            U=[[0]*r for _ in range(k)]
            U[a][j]=1
            cols.append(f_flat(B,U))
    # transpose columns to rows
    return [list(x) for x in zip(*cols)] if cols else []

def kernel_count_bruteforce(B):
    k=len(B); r=len(B[0]); c=0
    for bits in itertools.product((0,1),repeat=k*r):
        U=[list(bits[i*r:(i+1)*r]) for i in range(k)]
        c += not any(f_flat(B,U))
    return c

def formula(k,r,t):
    e=k*(r-t)+t*(t+1)//2
    return e, 2**e, t*(2*k-t-1)//2

# Exhaust every B and every U through 3x3.
for k in range(1,CERT['verification']['exhaustive_k_max']+1):
    for r in range(1,CERT['verification']['exhaustive_r_max']+1):
        for bits in itertools.product((0,1),repeat=k*r):
            B=[list(bits[i*r:(i+1)*r]) for i in range(k)]
            t=rank2(B)
            e,cnt,mrank=formula(k,r,t)
            assert kernel_count_bruteforce(B)==cnt
            assert rank2(map_matrix(B))==mrank
            assert k*r-mrank==e

# Larger canonical forms: no U exhaustion needed; map rank is computed directly.
for k in range(1,CERT['verification']['canonical_k_max']+1):
    for r in range(1,CERT['verification']['canonical_r_max']+1):
        exps=[]
        for t in range(min(k,r)+1):
            B=[[0]*r for _ in range(k)]
            for i in range(t):
                B[i][i]=1
            e,cnt,mrank=formula(k,r,t)
            assert rank2(B)==t
            assert rank2(map_matrix(B))==mrank
            exps.append(e)
        for t in range(len(exps)-1):
            assert exps[t+1]-exps[t]==t+1-k

print('VERIFY_OK')
