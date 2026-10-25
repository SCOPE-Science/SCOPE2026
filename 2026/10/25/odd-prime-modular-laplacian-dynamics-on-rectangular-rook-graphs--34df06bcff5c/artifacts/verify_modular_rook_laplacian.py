#!/usr/bin/env python3
"""Reproducible finite-field checks for iterated graph Laplacian dynamics.

Standard library only: python3 verify.py
"""
from itertools import product
from collections import Counter


def laplacian_columns(m,n,p):
    """Column representation for L on K_m square K_n, reduced modulo p."""
    N=m*n
    cols=[]
    for j in range(N):
        a,b=divmod(j,n)
        z=[0]*N
        z[j]=(m+n-2)%p
        for i in range(m):
            if i!=a:z[i*n+b]=(z[i*n+b]-1)%p
        for k in range(n):
            if k!=b:z[a*n+k]=(z[a*n+k]-1)%p
        cols.append(z)
    return cols


def apply(m,n,p,x):
    row=[sum(x[i*n+j] for j in range(n))%p for i in range(m)]
    col=[sum(x[i*n+j] for i in range(m))%p for j in range(n)]
    return [((m+n)*x[i*n+j]-row[i]-col[j])%p for i in range(m) for j in range(n)]


def rank_columns(cols,p):
    basis={}
    for col in cols:
        v=col[:]
        while 1:
            pos=next((i for i,vv in enumerate(v) if vv),None)
            if pos is None: break
            if pos in basis:
                u=basis[pos];a=v[pos]
                v=[(vi-a*ui)%p for vi,ui in zip(v,u)]
            else:
                inv=pow(v[pos],-1,p)
                basis[pos]=[(z*inv)%p for z in v]
                break
    return len(basis)


def nilpotent_ranks(m,n,p):
    assert p >= 3 and p % 2 == 1
    a=m%p;b=n%p
    if a and b:
        h=1+(m-1)*(n-1) if (a+b)%p==0 else 1
        return [h,0,0,0]
    if a==0 and b:
        return [m,1,0,0]
    if a and b==0:
        return [n,1,0,0]
    return [m*n,m+n-2,1,0]


def periodic_dim(m,n,p,t):
    assert p >= 3 and p % 2 == 1
    a=m%p;b=n%p
    if a and b:
        return ((m-1) if pow(a,t,p)==1 else 0)+((n-1) if pow(b,t,p)==1 else 0)+((m-1)*(n-1) if ((a+b)%p) and pow((a+b)%p,t,p)==1 else 0)
    if a==0 and b:
        if pow(b,t,p)!=1:return 0
        return m*(n-1) if t%p==0 else (m-1)*(n-1)
    if a and b==0:
        if pow(a,t,p)!=1:return 0
        return n*(m-1) if t%p==0 else (n-1)*(m-1)
    return 0


def verify_matrix():
    checked=0
    for p in (3,5,7):
        for m in range(2,9):
            for n in range(2,9):
                N=m*n
                cols=laplacian_columns(m,n,p)
                for j in range(N):
                    x=[0]*N;x[j]=1
                    assert apply(m,n,p,x)==cols[j]
                r=nilpotent_ranks(m,n,p)
                # Stabilizes by step 3 at the latest; rank(L^t) = recurrent dimension + rank(N^t).
                d=N-r[0]
                power_cols=[[int(i==j) for i in range(N)] for j in range(N)]
                for t in range(4):
                    got=rank_columns(power_cols,p)
                    want=d+r[t]
                    assert got==want,(m,n,p,t,got,want)
                    power_cols=[apply(m,n,p,v) for v in power_cols]
                checked+=1
    print('MATRIX_RANK_CASES',checked)


def verify_periods():
    checked=0
    for p,m,n in [(3,2,2),(3,2,3),(3,3,3),(3,3,4),(3,4,5),(5,2,2),(5,5,2),(7,2,2)]:
        N=m*n
        I=[[int(i==j) for i in range(N)] for j in range(N)]
        cols=laplacian_columns(m,n,p)
        for t in range(1,18):
            M=[[(cols[j][i]-I[j][i])%p for i in range(N)] for j in range(N)]
            got=N-rank_columns(M,p)
            want=periodic_dim(m,n,p,t)
            assert got==want,(p,m,n,t,got,want)
            cols=[apply(m,n,p,v) for v in cols]
            checked+=1
    print('FIXED_ITERATE_RANK_CASES',checked)


def exact_depth(x,m,n,p):
    curr=tuple(x)
    seen={};t=0
    while curr not in seen:
        seen[curr]=t
        curr=tuple(apply(m,n,p,curr))
        t+=1
    return seen[curr],t-seen[curr]


def mobius(n):
    if n==1:return 1
    parity=0;k=2
    while k*k<=n:
        if n%k==0:
            parity+=1;n//=k
            if n%k==0:return 0
            while n%k==0:n//=k
        k+=1
    return -1 if (parity+(n>1))%2 else 1


def primitive_count(m,n,p,t):
    return sum(mobius(t//d)*p**periodic_dim(m,n,p,d)
               for d in range(1,t+1) if t%d==0)


def verify_exhaustive():
    cases=[(3,2,2),(3,3,2),(3,3,3),(3,4,2),(5,2,2),(7,2,2)]
    checked=0
    for p,m,n in cases:
        N=m*n
        assert p**N<=20000
        count=Counter(exact_depth(x,m,n,p) for x in product(range(p),repeat=N))
        nil=nilpotent_ranks(m,n,p)
        dim=N-nil[0]
        for t in range(4):
            cumulative=sum(q for (s,per),q in count.items() if s<=t)
            expected=p**(N-nil[t])
            assert cumulative==expected,(p,m,n,t,cumulative,expected)
        nil_dim=nil[0]
        for (depth,per),num in count.items():
            assert num>0 and depth<=3
            h=(1 if depth==0 else p**(nil_dim-nil[depth])-p**(nil_dim-nil[depth-1]))
            expected=h*primitive_count(m,n,p,per)
            assert num==expected,(p,m,n,depth,per,num,expected)
        max_period=max(per for depth,per in count)
        for per in range(1,max_period+1):
            actual=sum(num for (depth,t),num in count.items() if depth==0 and t==per)
            expected=primitive_count(m,n,p,per)
            assert actual==expected,(p,m,n,per,actual,expected)
        checked+=p**N
    print('FULL_STATE_CASES',len(cases),'STATES',checked)


if __name__=='__main__':
    verify_matrix()
    verify_periods()
    verify_exhaustive()
    print('MODULAR_LAPLACIAN_VERIFY_OK')
