#!/usr/bin/env python3
"""Exact reproducibility checks for the Euclidean geometry of the cut-metric simplex.
Only Python's standard library is required. Finite tests illustrate a separate
algebraic argument valid for every integer n >= 3.
"""
from fractions import Fraction as Q
from math import factorial


def inverse(A):
    k=len(A)
    T=[[Q(x) for x in row]+[Q(i==j) for j in range(k)] for i,row in enumerate(A)]
    for j in range(k):
        p=next(i for i in range(j,k) if T[i][j])
        T[j],T[p]=T[p],T[j]
        t=T[j][j]
        T[j]=[x/t for x in T[j]]
        for i in range(k):
            if i==j:continue
            t=T[i][j]
            if t:T[i]=[u-t*v for u,v in zip(T[i],T[j])]
    return [row[k:] for row in T]


def det(A):
    k=len(A)
    T=[[Q(x) for x in row] for row in A]
    d=Q(1)
    for j in range(k):
        p=next((i for i in range(j,k) if T[i][j]),None)
        if p is None:return Q(0)
        if p!=j:T[j],T[p]=T[p],T[j];d=-d
        pivot=T[j][j];d*=pivot
        for i in range(j+1,k):
            t=T[i][j]/pivot
            if t:
                for c in range(j+1,k):T[i][c]-=t*T[j][c]
                T[i][j]=Q(0)
    return d


def dot(x,y):return sum((u*v for u,v in zip(x,y)),Q(0))


def verify(n):
    assert n>=3
    m=n-1
    w=[a*(n-a) for a in range(1,n)]
    W=sum(w)
    assert W==n*(n*n-1)//6
    vertices=[]
    for a in range(1,n):
        vertices.append([Q(int((i<a)!=(j<a)),2*a*(n-a))
                         for i in range(n) for j in range(n)])
    G=[[dot(u,v) for v in vertices] for u in vertices]
    for i in range(m):
        for j in range(m):
            bridge=min(i+1,j+1)*(n-max(i+1,j+1))
            assert G[i][j]==Q(bridge,2*w[i]*w[j])
    H=inverse(G)
    for i in range(m):
        for j in range(m):
            L=2 if i==j else (-1 if abs(i-j)==1 else 0)
            assert H[i][j]==Q(2*w[i]*w[j]*L,n)
    rowsums=[sum(row) for row in H]
    S=sum(rowsums)
    assert S==Q(2*(n*n-1),3)
    Bdiag=[H[i][i]-rowsums[i]**2/S for i in range(m)]
    for i in range(m):
        assert Bdiag[i]==Q(4*w[i]**2,n)*(1-Q(6,n*(n*n-1)))
    lam_in=[Q(v,W) for v in w]
    c_in=[sum(lam_in[a]*vertices[a][j] for a in range(m)) for j in range(n*n)]
    for i in range(n):
        for j in range(n):
            assert c_in[i*n+j]==Q(3*abs(i-j),n*(n*n-1))
    r2=Q(9,(n*n-1)*(n*(n*n-1)-6))
    for a in range(m):
        assert lam_in[a]**2/Bdiag[a]==r2
    lam_out=[Q((n-1)*(int(a==0)+int(a==m-1)),2*n)
             + lam_in[a]/n for a in range(m)]
    assert sum(lam_out)==1 and all(t>0 for t in lam_out)
    c_out=[sum(lam_out[a]*vertices[a][j] for a in range(m)) for j in range(n*n)]
    R2=Q((n-2)*(n*n+2*n+3),4*n*n*(n*n-1))
    for v in vertices:
        assert dot([x-y for x,y in zip(v,c_out)],
                   [x-y for x,y in zip(v,c_out)])==R2
    differences=[[vertices[a][i]-vertices[-1][i] for i in range(n*n)]
                 for a in range(m-1)]
    edgegram=[[dot(x,y) for y in differences] for x in differences]
    volume2=det(edgegram)/factorial(n-2)**2
    expected=Q(n**(n-2)*(n*n-1),
               3*2**(n-2)*factorial(n-1)**4*factorial(n-2)**2)
    assert volume2==expected
    return (n,r2,R2,volume2)


if __name__=='__main__':
    for n in range(3,11):
        n,r2,R2,v2=verify(n)
        print(f'n={n}: inradius^2={r2}; circumradius^2={R2}; volume^2={v2}')
    print('PASS: all independently constructed exact rational checks n=3..10')
