#!/usr/bin/env python3
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CERT = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def rank(M,q):
    A=[[x%q for x in row] for row in M]
    if not A: return 0
    m,n=len(A),len(A[0]); rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]%q),None)
        if p is None: continue
        A[rr],A[p]=A[p],A[rr]
        z=pow(A[rr][c]%q,-1,q)
        A[rr]=[(z*x)%q for x in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]%q:
                z=A[i][c]%q
                A[i]=[(A[i][j]-z*A[rr][j])%q for j in range(n)]
        rr+=1
        if rr==m: break
    return rr

def transpose(A): return [list(x) for x in zip(*A)]

def matmul(A,B,q):
    if not A: return []
    return [[sum(A[i][t]*B[t][j] for t in range(len(B)))%q
             for j in range(len(B[0]))] for i in range(len(A))]

def vecmul(u,G,q):
    return [sum(u[i]*G[i][j] for i in range(len(u)))%q for j in range(len(G[0]))]

def span_basis(V,q):
    B=[]
    for v in V:
        if rank(B+[list(v)],q)>len(B): B.append(list(v))
    return B

def null_basis(M,q):
    k=len(M); V=[]
    for u in itertools.product(range(q),repeat=k):
        if not any(u): continue
        if all(sum(u[i]*M[i][j] for i in range(k))%q==0 for j in range(k)): V.append(u)
    return span_basis(V,q)

def subspaces(k,r,q):
    for piv in itertools.combinations(range(k),r):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv) for c in range(p+1,k) if c not in P]
        for vals in itertools.product(range(q),repeat=len(free)):
            B=[[0]*k for _ in range(r)]
            for i,p in enumerate(piv): B[i][p]=1
            for (i,c),v in zip(free,vals): B[i][c]=v
            yield B

def support(B,G,q):
    rows=[vecmul(u,G,q) for u in B]
    return sum(any(row[j] for row in rows) for j in range(len(G[0]))) if rows else 0

def ghw(G,q):
    return [min(support(B,G,q) for B in subspaces(len(G),r,q)) for r in range(1,len(G)+1)]

def systematic(q,k,n):
    tail=n-k
    for vals in itertools.product(range(q),repeat=k*tail):
        G=[[1 if i==j else 0 for j in range(k)] for i in range(k)]
        for i in range(k): G[i].extend(vals[i*tail:(i+1)*tail])
        yield G

def check(G,q):
    k=len(G)
    Gram=matmul(G,transpose(G),q)
    ell=k-rank(Gram,q)
    H=null_basis(Gram,q)
    assert len(H)==ell
    T=[x[:] for x in H]
    for j in range(k):
        e=[1 if i==j else 0 for i in range(k)]
        if rank(T+[e],q)>len(T): T.append(e)
    assert rank(T,q)==k
    Gp=matmul(T,G,q)
    add=[]
    for i in range(k):
        row=[0]*ell
        if i<ell: row[i]=1
        add.append(row)
    GT=[Gp[i]+add[i] for i in range(k)]
    assert rank(matmul(GT,transpose(GT),q),q)==k
    assert rank(add,q)==ell
    K=Gp[ell:]
    assert len(K)==k-ell
    dC=ghw(Gp,q); dT=ghw(GT,q); dK=ghw(K,q) if K else []
    for r in range(1,k+1):
        lo=max(0,r-k+ell); hi=min(r,ell)
        terms=[]
        for t in range(lo,hi+1):
            s=r-t
            dk=0 if s==0 else dK[s-1]
            terms.append(t+max(dC[r-1],dk))
        assert dT[r-1]>=min(terms)
        assert dT[r-1]>=dC[r-1]+lo
        assert dT[r-1]<=dC[r-1]+ell
    assert dT[-1]==dC[-1]+ell
    if ell==k:
        for r in range(1,k+1): assert dT[r-1]>=dC[r-1]+r
    return ell

tested=0; hulls=set()
for q,maxk,maxn in ((2,3,4),(3,2,4)):
    for k in range(1,maxk+1):
        for n in range(k,maxn+1):
            for G in systematic(q,k,n):
                ell=check(G,q); hulls.add((q,k,ell)); tested+=1
assert tested>100
assert any(ell==k for q,k,ell in hulls)
assert any(0<ell<k for q,k,ell in hulls)
print("VERIFY_OK")
