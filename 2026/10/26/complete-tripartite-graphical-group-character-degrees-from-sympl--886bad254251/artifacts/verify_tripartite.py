#!/usr/bin/env python3
"""Standalone tests for exact rank distributions of full tripartite alternating matrices.
All computations here are finite-field arithmetic and do not certify the infinite theorem.
"""
from itertools import product
from math import prod

def gauss(n,k,q):
    if not 0<=k<=n: return 0
    numerator=prod(q**(n-i)-1 for i in range(k))
    denominator=prod(q**(k-i)-1 for i in range(k))
    return numerator//denominator

def rank_maps(a,b,k,q):
    if not 0<=k<=min(a,b):return 0
    return gauss(a,k,q)*prod(q**b-q**i for i in range(k))

def spord(m,q):
    return q**(m*m)*prod(q**(2*i)-1 for i in range(1,m+1))

def isotropic(m,u,q):
    if not 0<=u<=m:return 0
    num=prod(q**(2*m-i)-q**i for i in range(u))
    den=prod(q**u-q**i for i in range(u))
    return num//den

def nondeg(m,t,q):
    if not 0<=t<=m:return 0
    return spord(m,q)//(spord(t,q)*spord(m-t,q))

def pullback(m,h,t,q):
    return sum(isotropic(m,u,q)*nondeg(m-u,t,q)*prod(q**h-q**i for i in range(2*t+u))
               for u in range(min(m,h-2*t)+1)) if 0<=t<=min(m,h//2) else 0

def distribution(a,b,c,q):
    ans={}
    for r in range(min(a,b)+1):
        cr=rank_maps(a,b,r,q)
        for s in range(min(a+b-2*r,c)+1):
            cs=rank_maps(a+b-2*r,c,s,q)
            for t in range(min(r,(c-s)//2)+1):
                ct=pullback(r,c-s,t,q)
                j=r+s+t
                ans[j]=ans.get(j,0)+cr*cs*q**(2*r*s)*ct
    return {k:v for k,v in ans.items() if v}

def rank_matrix(A,q):
    A=[list(row) for row in A]
    rows=len(A); cols=len(A[0]) if rows else 0
    r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if A[i][j]%q),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][j],-1,q)
        A[r]=[(v*inv)%q for v in A[r]]
        for i in range(r+1,rows):
            t=A[i][j]
            if t:A[i]=[(v-t*w)%q for v,w in zip(A[i],A[r])]
        r+=1
        if r==rows:break
    return r

def brute(a,b,c,q):
    n=a+b+c
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)
           if (i<a and j>=a) or (a<=i<a+b and j>=a+b)]
    d={}
    for w in product(range(q),repeat=len(pairs)):
        mat=[[0]*n for _ in range(n)]
        for (i,j),v in zip(pairs,w): mat[i][j]=v;mat[j][i]=-v%q
        rk=rank_matrix(mat,q)
        if rk%2:raise AssertionError('alternating odd rank')
        d[rk//2]=d.get(rk//2,0)+1
    return d

def pullbrute(m,h,t,q):
    # rectangular P with 2m rows and h columns; J pairs adjacent rows
    d=0
    for vals in product(range(q),repeat=2*m*h):
        P=[[vals[i*h+j] for j in range(h)] for i in range(2*m)]
        K=[[sum(P[2*v][i]*P[2*v+1][j]-P[2*v+1][i]*P[2*v][j] for v in range(m))%q
            for j in range(h)] for i in range(h)]
        if rank_matrix(K,q)==2*t:d+=1
    return d

def f4mul(a,b):
    # Modulo the irreducible polynomial T^2+T+1 over F_2.
    v=0
    while b:
        if b&1:v^=a
        b>>=1
        a<<=1
        if a&4:a^=7
    return v

def rank_f4(A):
    A=[list(row) for row in A]
    rows=len(A); cols=len(A[0]) if rows else 0
    r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=next(t for t in (1,2,3) if f4mul(t,A[r][j])==1)
        A[r]=[f4mul(inv,v) for v in A[r]]
        for i in range(r+1,rows):
            t=A[i][j]
            if t:A[i]=[v^f4mul(t,w) for v,w in zip(A[i],A[r])]
        r+=1
        if r==rows:break
    return r

def brute_f4(a,b,c):
    q=4;n=a+b+c
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)
           if (i<a and j>=a) or (a<=i<a+b and j>=a+b)]
    d={}
    for w in product(range(q),repeat=len(pairs)):
        mat=[[0]*n for _ in range(n)]
        for (i,j),v in zip(pairs,w):mat[i][j]=v;mat[j][i]=v
        rk=rank_f4(mat)
        assert rk%2==0
        d[rk//2]=d.get(rk//2,0)+1
    return d

def run():
    configs=[(1,1,1,2),(1,1,2,2),(1,1,3,2),(1,2,2,2),(1,2,3,2),
             (2,2,2,2),(1,1,1,3),(1,1,2,3),(1,2,2,3),
             (2,2,2,3),(1,1,1,5),(1,1,2,5)]
    for a,b,c,q in configs:
        pred=distribution(a,b,c,q)
        direct=brute(a,b,c,q)
        assert pred==direct,(a,b,c,q,pred,direct)
        assert sum(pred.values())==q**(a*b+a*c+b*c)
        print('PASS',a,b,c,q,pred)
    for q in (2,3):
        for m in range(3):
            for h in range(4):
                if 2*m*h>11:continue
                for t in range(min(m,h//2)+1):
                    assert pullback(m,h,t,q)==pullbrute(m,h,t,q),(m,h,t,q)
                assert sum(pullback(m,h,t,q) for t in range(min(m,h//2)+1))==q**(2*m*h)
    for a,b,c in [(1,1,1),(1,1,2),(1,2,2)]:
        pred=distribution(a,b,c,4)
        direct=brute_f4(a,b,c)
        assert pred==direct,(a,b,c,4,pred,direct)
        print('PASS_F4',a,b,c,pred)
    print('VERIFY_OK_TRIPARTITE_RANK_DISTRIBUTION')

if __name__=='__main__':run()
