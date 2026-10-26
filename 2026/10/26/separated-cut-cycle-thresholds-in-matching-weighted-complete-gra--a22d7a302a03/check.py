"""Exact rational independent grounded-Laplacian checks for a weighted complete-graph family.
Run with Python 3 standard library: python check.py
"""
from fractions import Fraction as F


def inverse(a):
    n = len(a)
    t = [[F(z) for z in a[i]] + [F(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k,n) if t[i][k])
        t[k],t[pivot] = t[pivot],t[k]
        q=t[k][k]
        t[k]=[z/q for z in t[k]]
        for j in range(n):
            if j != k:
                c=t[j][k]
                if c: t[j]=[t[j][h]-c*t[k][h] for h in range(2*n)]
    return [row[n:] for row in t]


def theoretical(N,x):
    b=N-2+2*x*x
    qm=(2*x*x+2*(N-2)*x)/b
    pm=1+(-2*x*x+2*(N-2)*x)/b
    if x >= 1:
        qc=2-F(4,N)+2*x/b
        pc=3-F(6,N)+2*(x-1)/b
    else:
        qc=F(2,N)+(2*N-6+2*x)/b
        pc=1+(2*N-8+2*x)/b
    return qm,qc,pm,pc


def check(N,x):
    vertices=range(N)
    edges=[(u,v) for u in vertices for v in range(u+1,N)]
    root=N-1
    L=[[F(0) for _ in range(N-1)] for __ in range(N-1)]
    weights=[]
    for u,v in edges:
        c=x*x if u//2==v//2 else F(1)
        t=x if u//2==v//2 else F(1)
        weights.append(t)
        if u!=root:L[u][u]+=c
        if v!=root:L[v][v]+=c
        if u!=root and v!=root:
            L[u][v]-=c;L[v][u]-=c
    U=inverse(L)
    assert all(sum(L[i][k]*U[k][j] for k in range(N-1)) == (i==j)
               for i in range(N-1) for j in range(N-1))
    qm,qc,pm,pc=theoretical(N,x)
    cols=0
    for idx,(u,v) in enumerate(edges):
        t=weights[idx]
        pu=[t*(U[j][u] if u!=root else F(0))-t*(U[j][v] if v!=root else F(0)) for j in range(N-1)]
        pu.append(F(0))
        qcol=[weights[j]*(pu[r]-pu[s]) for j,(r,s) in enumerate(edges)]
        pcol=[F(j==idx)-qcol[j] for j in range(len(edges))]
        is_match=u//2==v//2
        assert sum(map(abs,qcol)) == (qm if is_match else qc), (N,x,u,v,'cut')
        assert sum(map(abs,pcol)) == (pm if is_match else pc), (N,x,u,v,'cycle')
        assert qcol[idx] == (2*x*x/(N-2+2*x*x) if is_match else F(1,N)+1/(N-2+2*x*x))
        cols+=1
    return cols

if __name__=='__main__':
    graphs=0; columns=0; ties=0
    for N in (8,10,12,14):
        xp=F(N*N-6*N+6,3*(N-2))
        xq=F((N-2)**2,N-4)
        assert 1 < xp < xq
        xs=(F(1,4),F(3,4),F(1),F(11,10), xp, (xp+xq)/2, xq, 2*xq)
        for x in xs:
            qm,qc,pm,pc=theoretical(N,x)
            if 0<x<1: assert qc>qm and pc>pm
            if 1<x<xp: assert qm>qc and pm>pc
            if xp<x<xq: assert qm>qc and pc>pm
            if x>xq: assert qc>qm and pc>pm
            if x==1: assert qc==qm and pc==pm
            if x==xp: assert pc==pm
            if x==xq: assert qc==qm
            columns+=check(N,x);graphs+=1
            ties+=(x==1 or x==xp or x==xq)
    print('MATCHING_WEIGHTED_COMPLETE_EXACT_OK graphs=%d full_columns=%d boundary_graphs=%d'%(graphs,columns,ties))
