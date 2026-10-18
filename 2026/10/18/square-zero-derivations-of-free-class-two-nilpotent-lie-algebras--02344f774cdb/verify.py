#!/usr/bin/env python3
"""Standalone finite-prime-field checks of derivation square-zero counts."""
from itertools import product,combinations
from math import prod

def rank(M,p):
    a=[row[:] for row in M]
    if not a:return 0
    R=len(a);C=len(a[0]);h=0
    for j in range(C):
        pivot=next((i for i in range(h,R) if a[i][j]%p),None)
        if pivot is None:continue
        a[h],a[pivot]=a[pivot],a[h]
        inv=pow(a[h][j],-1,p)
        a[h]=[v*inv%p for v in a[h]]
        for i in range(R):
            if i==h:continue
            c=a[i][j]%p
            if c:a[i]=[(x-c*y)%p for x,y in zip(a[i],a[h])]
        h+=1
        if h==R:break
    return h

def qbinom(n,k,q):
    if not 0<=k<=n:return 0
    return prod((q**(n-i)-1)//1 for i in range(k))//prod((q**(k-i)-1) for i in range(k))

def gl(r,q):
    return prod((q**r-q**i) for i in range(r))

def f(m,n,p,A):
    pairs=list(combinations(range(n),2));M=len(pairs)
    pairid={z:i for i,z in enumerate(pairs)}
    T=[[0]*M for _ in range(M)]
    def add(u,v,coeff,col):
        if u==v:return
        s=1
        if u>v:u,v=v,u;s=-1
        T[pairid[(u,v)]][col]=(T[pairid[(u,v)]][col]+s*coeff)%p
    for col,(i,j) in enumerate(pairs):
        for k in range(n):
            add(k,j,A[k][i],col)
            add(i,k,A[k][j],col)
    eq=[]
    for k in range(M):
        for j in range(n):
            row=[0]*(M*n)
            for h in range(M): row[h*n+j]=(row[h*n+j]+T[k][h])%p
            for h in range(n): row[k*n+h]=(row[k*n+h]+A[h][j])%p
            eq.append(row)
    return rank(T,p),M*n-rank(eq,p)

def matmul(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def enumeration(n,p):
    count=[0]*(n//2+1)
    samples={}
    for cells in product(range(p),repeat=n*n):
        A=[list(cells[i*n:(i+1)*n]) for i in range(n)]
        if any(matmul(A,A,p)[i][i] for i in range(n)): # fast rejection (some full multiply again)
            continue
        if any(x for row in matmul(A,A,p) for x in row):continue
        r=rank(A,p)
        count[r]+=1
        samples.setdefault(r,A)
    m=n*(n-1)//2
    result={}
    total=0
    for r,A in samples.items():
        induced_rank,h=f(m,n,p,A)
        sr=r*(n-r-1)
        hd=n*m-n*sr-m*r+2*r*sr
        predicted=qbinom(n,r,p)*qbinom(n-r,r,p)*gl(r,p)
        assert count[r]==predicted,(n,p,r,count[r],predicted)
        assert sr==induced_rank,(n,p,r,sr,induced_rank)
        assert h==hd,(n,p,r,hd,h)
        if p%2 and r>=2:raise AssertionError('odd rank >=2 square-zero on exterior square')
        result[r]=(count[r],induced_rank,h)
        total+=count[r]*p**h
    return total,result

if __name__=='__main__':
    for n,p in [(2,2),(2,3),(3,2),(3,3),(4,2)]:
        total,byrank=enumeration(n,p)
        m=n*(n-1)//2
        expr=sum(qbinom(n,r,p)*qbinom(n-r,r,p)*gl(r,p)*p**(n*m-n*r*(n-r-1)-m*r+2*r*r*(n-r-1)) for r in range((n//2+1) if p==2 else 2))
        assert total==expr
        print('n=',n,'p=',p,'N=',total,'by_rank=',byrank)
    print('VERIFY_OK')
