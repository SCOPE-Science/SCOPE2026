#!/usr/bin/env python3
"""Exact-rational finite verification of clique-cycle join projection formulas.
Run with Python 3 and its standard library; no external packages are required.
The finite sample is not a substitute for the all-parameter proof.
"""
from fractions import Fraction as F


def inverse(a):
    n=len(a)
    m=[[F(t) for t in a[i]]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next((i for i in range(k,n) if m[i][k]),None)
        assert p is not None
        m[k],m[p]=m[p],m[k]
        z=m[k][k]
        m[k]=[t/z for t in m[k]]
        for i in range(n):
            if i==k: continue
            z=m[i][k]
            if z: m[i]=[x-z*y for x,y in zip(m[i],m[k])]
    return [row[n:] for row in m]


def matvec(A,v):
    return [sum((a*b for a,b in zip(row,v)), F(0)) for row in A]


def check(h,n):
    N=h+n
    E=[]
    E += [(i,j,'hub') for i in range(h) for j in range(i+1,h)]
    E += [(i,h+j,'spoke') for i in range(h) for j in range(n)]
    E += [(h+i,h+((i+1)%n),'rim') for i in range(n)]
    L=[[0]*N for _ in range(N)]
    for u,v,typ in E:
        L[u][u]+=1;L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
    A=inverse([row[:-1] for row in L[:-1]])
    C=[[h+2 if i==j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        C[i][(i-1)%n]-=1; C[i][(i+1)%n]-=1
    g=[row[0] for row in inverse(C)]
    f=n//2
    S=sum((abs(z-F(1,h*N)) for z in g),F(0))
    Q={
       'hub':F(2)-F(2,N),
       'rim': 4*(g[0]-g[1])+2*h*(g[0]-g[f]),
       'spoke':F(1)+(h-1)*S+2*(g[0]-g[f])}
    P={
       'hub':F(3)-F(6,N),
       'rim':F(1)+2*h*(g[0]-g[f]),
       'spoke':F(2)+(h-1)*S-2*g[f]-F(2*(h-1),h*N)}
    assert sum(g)==F(1,h)
    assert all(g[i]>=g[i+1] for i in range(n//2))
    ecount=0
    for u,v,typ in E:
        b=[F(0)]*(N-1)
        if u<N-1: b[u]+=1
        if v<N-1: b[v]-=1
        pot=matvec(A,b)+[F(0)]
        qcolumn=[pot[i]-pot[j] for i,j,_ in E]
        qs=sum(map(abs,qcolumn),F(0))
        i0=E.index((u,v,typ))
        ps=sum((abs(F(k==i0)-z) for k,z in enumerate(qcolumn)),F(0))
        assert qs==Q[typ],(h,n,u,v,typ,qs,Q[typ])
        assert ps==P[typ],(h,n,u,v,typ,ps,P[typ])
        assert qs-ps==2*qcolumn[i0]-1
        ecount+=1
    return ecount, Q,P

if __name__=='__main__':
    cases=0;columns=0
    for h in (2,3,4,5):
        for n in range(4,11):
            c,_,_=check(h,n)
            cases+=1;columns+=c
    for h,n in [(2,15),(3,13),(5,12)]:
        c,_,_=check(h,n);cases+=1;columns+=c
    print(f'CLIQUE_CYCLE_JOIN_CERTIFICATE_OK cases={cases} exact_columns={columns}')
