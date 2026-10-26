#!/usr/bin/env python3
"""Exact-rational verification of Möbius-ladder cut/cycle projector formulas.
No dependencies outside Python standard library."""
from fractions import Fraction as F
from math import isclose, log, sqrt

def exact_green(n):
    # Solve 4g_0-2g_1=1, 4g_j-g_{j-1}-g_{j+1}=0 (j>=1), g_n=-g_0.
    a0,b0=1,0
    a1,b1=0,1
    a,b=a0,b0; c,d=a1,b1
    for j in range(1,n):
        a,b,c,d=c,d,4*c-a,4*d-b
    # g_n=c*g0+d*g1, therefore (c+1)*g0+d*g1=0.
    det=4*d+2*(c+1)
    assert det != 0
    g0=F(d,det)
    g1=F(-(c+1),det)
    g=[g0,g1]
    for j in range(1,n):g.append(4*g[-1]-g[-2])
    assert g[n]==-g[0]
    assert all(g[j]>g[j+1] for j in range(n))
    assert all(g[n-j]==-g[j] for j in range(n+1))
    return g

def formulas(n):
    g=exact_green(n); h=(n-1)//2; t=F(1,2*n)
    pos=sum((max(F(0),g[j]-t) for j in range(1,h+1)),F(0))
    s=sum(g[1:h+1],F(0))
    qrim=2-F(2,n)+2*g[0]+4*pos
    qrung=6*g[0]+4*s
    crim=2-F(1,n)+2*g[1]+4*pos
    crung=1+2*g[0]+4*s
    return qrim,qrung,crim,crung

def inv(mat):
    d=len(mat)
    a=[[F(z) for z in row]+[F(i==j) for j in range(d)] for i,row in enumerate(mat)]
    for k in range(d):
        p=next(i for i in range(k,d) if a[i][k]!=0)
        a[k],a[p]=a[p],a[k]
        y=a[k][k];a[k]=[z/y for z in a[k]]
        for i in range(d):
            if i!=k and a[i][k]:
                y=a[i][k]
                a[i]=[a[i][j]-y*a[k][j] for j in range(2*d)]
    return [r[d:] for r in a]

def graph_direct(n):
    N=2*n
    rim=[(i,(i+1)%N) for i in range(N)]
    rung=[(i,i+n) for i in range(n)]
    edges=rim+rung
    mat=[[0]*(N-1) for _ in range(N-1)]
    for u,v in edges:
        if u<N-1:mat[u][u]+=1
        if v<N-1:mat[v][v]+=1
        if u<N-1 and v<N-1:mat[u][v]-=1;mat[v][u]-=1
    inverse=inv(mat)
    # Each edge has incidence vector b: 1 at u and -1 at v.
    vec=[]
    for u,v in edges:
        z=[F(0)]*(N-1)
        if u<N-1:z[u]=F(1)
        if v<N-1:z[v]=F(-1)
        vec.append(z)
    proj=[]
    for j in range(len(edges)):
        x=[sum(inverse[i][h]*vec[j][h] for h in range(N-1)) for i in range(N-1)]
        qcol=[sum(vec[k][i]*x[i] for i in range(N-1)) for k in range(len(edges))]
        assert sum(qcol[k]*qcol[k] for k in range(len(edges)))==qcol[j]
        proj.append(qcol)
    for j,qcol in enumerate(proj):
        assert all(proj[k][j]==qcol[k] for k in range(len(edges)))
    return (max(sum(map(abs,col)) for col in proj[:N]),
            max(sum(map(abs,col)) for col in proj[N:]),
            max(1+sum(map(abs,col))-2*col[j] for j,col in enumerate(proj[:N])),
            max(1+sum(map(abs,col))-2*col[N+j] for j,col in enumerate(proj[N:]))) ,len(edges)

def main():
    ncols=0
    for n in range(3,14):
        x=formulas(n)
        direct,m=graph_direct(n)
        assert x==direct,(n,x,direct)
        if n==3:assert x[0]==x[1] and x[2]==x[3]
        if n>=4:assert x[0]>x[1] and x[2]>x[3]
        print(n, 'cut_rim',x[0], 'cut_rung',x[1], 'cycle_rim',x[2], 'cycle_rung',x[3])
        ncols+=m
    print('PASS direct edge columns:',ncols)
    for n in [20,50,100,200,500,1000,3000]:
        q=formulas(n)[0]
        ratio=float((3-q)*n)/log(n)
        target=2/log(2+sqrt(3))
        print('asymptotic n',n,'ratio',round(ratio,8),'target',round(target,8))
        assert abs(float(3-q))<1
    print('ALL PASS')
if __name__=='__main__':main()
