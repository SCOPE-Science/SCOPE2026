#!/usr/bin/env python3
"""Numerical checks of finite complete-multipartite bi-heat stability formula.
Requires Python 3 standard library only. These finite checks supplement, not replace, proof.
"""
import math
import random

CHECKS=0

def close(a,b,tol=1.5e-9):
    global CHECKS
    CHECKS+=1
    if abs(a-b)>tol*(1+abs(a)+abs(b)):
        raise AssertionError((a,b,abs(a-b)))

def mm(A,B):
    n=len(A)
    out=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for k, aik in enumerate(A[i]):
            if aik:
                for j,bkj in enumerate(B[k]): out[i][j]+=aik*bkj
    return out

def expmat(M):
    """Scaling and squaring Taylor exponential, with independently built matrix M."""
    n=len(M)
    infinity_norm=max(sum(abs(z) for z in row) for row in M)
    k=max(0, math.ceil(math.log2(infinity_norm/0.125))) if infinity_norm else 0
    A=[[z/(2**k) for z in row] for row in M]
    E=[[float(i==j) for j in range(n)] for i in range(n)]
    P=[[float(i==j) for j in range(n)] for i in range(n)]
    for z in range(1,28):
        P=mm(P,A)
        for i in range(n):
            for j in range(n):
                P[i][j]/=z
                E[i][j]+=P[i][j]
    for _ in range(k):E=mm(E,E)
    return E

def root(x):
    assert 0<x<1
    def F(u):return math.exp(-x*x*u)-(1-x)-x*math.exp(-u)
    lo=min(1e-5, 0.01*x)
    assert F(lo)>0, (x, lo, F(lo))
    hi=max(4,4/x)
    assert F(hi)<0, (x,hi,F(hi))
    for _ in range(100):
        mid=(lo+hi)/2
        if F(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def kernel_formula(parts,u):
    n=sum(parts)
    rows=[]
    for m in parts:
        x=(n-m)/n
        same=(1-x+x*math.exp(-u)-math.exp(-x*x*u))/m
        cross=(1-math.exp(-u))/n
        diag=1/n+(1/m-1/n)*math.exp(-u)+(1-1/m)*math.exp(-x*x*u)
        rows.append((same,cross,diag))
    return rows

def verify(parts):
    n=sum(parts)
    part_index=[i for i,m in enumerate(parts) for _ in range(m)]
    L=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:L[i][j]=n-parts[part_index[i]]
            elif part_index[i]!=part_index[j]:L[i][j]=-1
    L2=mm(L,L)
    top=max(parts)
    tau=root((n-top)/n)/n**2 if top>1 else 0.0
    sample=[0.0001,0.2*n*n*tau,0.6*n*n*tau,1.01*n*n*tau,1.8*n*n*tau]
    for u in sample:
        T=expmat([[-u*z/(n*n) for z in row] for row in L2])
        rowformula=kernel_formula(parts,u)
        norm_form=1+2*max((m-1)*max(0,-rowformula[k][0]) for k,m in enumerate(parts))
        norm_direct=max(sum(abs(v) for v in row) for row in T)
        close(norm_direct,norm_form,5e-9)
        for i in range(n):
            close(sum(T[i]),1,4e-9)
            for j in range(n):
                p=part_index[i]
                val=(rowformula[p][2] if i==j else rowformula[p][0] if p==part_index[j] else rowformula[p][1])
                close(T[i][j],val,4e-9)
        if top>1 and abs(u/n**2-tau)>tau*.01:
            minval=min(T[i][j] for i in range(n) for j in range(n) if i!=j)
            if u/n**2 < tau:
                assert minval < -1e-9, (parts,u,tau,minval)
            else:
                assert minval > -1e-9, (parts,u,tau,minval)
    return tau

def main():
    rng=random.Random(20423)
    tests=[[1,1],[1,2],[2,2],[2,1,1],[3,1,1,1],[3,2,2],[4,3,1],[5,4],[2,2,2,2],[2,1,1,1,1,1],[8,1],[1,1,1,1]]
    for n in range(3,17):
        for _ in range(5):
            k=rng.randrange(2,min(n,8)+1)
            dividers=sorted(rng.sample(range(1,n),k-1))
            parts=[y-x for x,y in zip([0]+dividers,dividers+[n])]
            tests.append(parts)
    for parts in tests:verify(parts)
    for n in range(4,50):
        ta=root(1/n)/n**2
        tb=root((n-2)/n)/n**2
        assert ta>=tb, (n,ta,tb)
        close(ta, -math.log1p(-1/n), 2.0/(n*n)*math.exp(-n/2))
    for n in [30,60,120,240,480]:
        star=root(1/n)/n**2
        near=root(1-2/n)/n**2
        close(n*star,1,0.03)
        close(n*n*near,root(1-1e-7),0.09)
    uhalf=root(.5)
    close(math.exp(-uhalf/4)*2,1+math.exp(-uhalf),3e-13)
    print('PASS',CHECKS,'numerical equalities;',len(tests),'graph designs;', 'half_size_u',format(uhalf,'.12f'))
if __name__=='__main__':main()
