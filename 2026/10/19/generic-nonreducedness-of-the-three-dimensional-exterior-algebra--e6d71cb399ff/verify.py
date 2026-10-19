#!/usr/bin/env python3
"""Exact modular enumeration for three-dimensional exterior-algebra representations.
Python 3 standard library only. No external inputs.
"""
from itertools import product

def mm(A,B,p):
    return tuple(sum(A[3*i+k]*B[3*k+j] for k in range(3))%p
                 for i in range(3) for j in range(3))
def add(A,B,p):
    return tuple((a+b)%p for a,b in zip(A,B))
def Z():return (0,)*9
def eye():return (1,0,0,0,1,0,0,0,1)
def e(i,j):
    l=[0]*9;l[3*i+j]=1;return tuple(l)
def zero_sq(X,p):return mm(X,X,p)==Z()
def rel(X,Y,p):return add(mm(X,Y,p),mm(Y,X,p),p)==Z()
def rank_mod(rows,p):
    if not rows:return 0
    A=[[v%p for v in row] for row in rows];m=len(A);n=len(A[0]);r=0
    for col in range(n):
        k=next((i for i in range(r,m) if A[i][col]),None)
        if k is None:continue
        A[k],A[r]=A[r],A[k]
        t=pow(A[r][col],-1,p)
        A[r]=[(a*t)%p for a in A[r]]
        for i in range(m):
            if i!=r and A[i][col]:
                t=A[i][col]
                A[i]=[(A[i][j]-t*A[r][j])%p for j in range(n)]
        r+=1
        if r==m:break
    return r

def tangent_dim(X,Y,p,quotient=False):
    cols=[]
    for a in (0,1):
        for i in range(3):
            for j in range(3):
                P=e(i,j) if a==0 else Z()
                Q=e(i,j) if a==1 else Z()
                xx=add(mm(X,P,p),mm(P,X,p),p)
                yy=add(mm(Y,Q,p),mm(Q,Y,p),p)
                xy=add(mm(P,Y,p),mm(X,Q,p),p)
                yx=add(mm(Y,P,p),mm(Q,X,p),p)
                eq=xx+yy+((xy+yx) if quotient else (add(xy,yx,p)))
                cols.append(eq)
    rows=list(zip(*cols))
    return 18-rank_mod(rows,p)

def inverse(M,p):
    A=[[M[3*i+j]%p for j in range(3)]+[int(i==j) for j in range(3)] for i in range(3)]
    for j in range(3):
        k=next(i for i in range(j,3) if A[i][j])
        A[k],A[j]=A[j],A[k];w=pow(A[j][j],-1,p)
        A[j]=[(x*w)%p for x in A[j]]
        for i in range(3):
            if i!=j:
                w=A[i][j];A[i]=[(a-w*b)%p for a,b in zip(A[i],A[j])]
    return tuple(A[i][3+j] for i in range(3) for j in range(3))

def conj(X,G,GI,p):return mm(mm(G,X,p),GI,p)

def check(p):
    S=[A for A in product(range(p),repeat=9) if zero_sq(A,p)]
    sol={(X,Y) for X in S for Y in S if rel(X,Y,p)}
    expect=p*p*(2*p**4+p**3-p-1)
    assert len(sol)==expect,(p,len(sol),expect)
    assert all(mm(X,Y,p)==Z() and mm(Y,X,p)==Z() for X,Y in sol)
    gens=[]
    for i in range(3):
        for j in range(3):
            if i!=j:
                g=add(eye(),e(i,j),p)
                gens.append((g,inverse(g,p)))
    if p>2:
        G=list(eye());G[0]=2
        G=tuple(G);gens.append((G,inverse(G,p)))
    left=set(sol); orbits=[]
    while left:
        seed=next(iter(left));seen={seed};queue=[seed]
        for X,Y in queue:
            for G,GI in gens:
                pair=(conj(X,G,GI,p),conj(Y,G,GI,p))
                if pair not in seen:
                    assert pair in sol
                    seen.add(pair);queue.append(pair)
        assert seen<=left
        orbits.append(len(seen));left-=seen
    assert len(orbits)==p+4,(p,len(orbits),p+4)
    for X,Y,td in ((e(0,1),e(0,2),8),(e(0,2),e(1,2),8),
                   (e(0,1),Z(),10),(Z(),Z(),18)):
        assert tangent_dim(X,Y,p)==td,(p,X,Y,tangent_dim(X,Y,p))
    for X,Y,td in ((e(0,1),e(0,2),6),(e(0,2),e(1,2),6),
                   (e(0,1),Z(),9),(Z(),Z(),18)):
        assert tangent_dim(X,Y,p,quotient=True)==td
    print(f'q={p}: square-zero matrices={len(S)}, points={len(sol)}, orbits={len(orbits)}, sizes={sorted(orbits)}, tangent profiles=(8,8,10,18), quotient tangent profiles=(6,6,9,18)')

if __name__=='__main__':
    check(2);check(3)
    print('VERIFY_OK')
