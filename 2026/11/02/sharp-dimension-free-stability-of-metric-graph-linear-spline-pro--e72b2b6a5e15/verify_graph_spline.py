#!/usr/bin/env python3
"""Standalone exact-rational spot checks for metric-graph affine projection formulae.

This program tests finite cases; the proofs for arbitrary graphs and dimensions
are in RESULT.md and do not rely on extrapolation from these computations.
"""
from fractions import Fraction as F
from math import comb
from random import Random

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def invert(A):
    n=len(A)
    T=[[F(A[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next((i for i in range(k,n) if T[i][k]), None)
        check(p is not None, 'singular matrix')
        T[k],T[p]=T[p],T[k]
        v=T[k][k]
        T[k]=[x/v for x in T[k]]
        for i in range(n):
            if i!=k:
                v=T[i][k]
                if v:
                    T[i]=[T[i][j]-v*T[k][j] for j in range(2*n)]
    return [r[n:] for r in T]

def absolute_segment(a,b):
    a,b=F(a),F(b)
    if a*b>=0:
        return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))

def norm_graph(n,edges):
    # edges: (u,v,mass) with positive integral density over each edge
    G=[[F(0) for _ in range(n)] for _ in range(n)]
    D=[F(0) for _ in range(n)]
    for u,v,m in edges:
        m=F(m)
        check(m>0 and u!=v, 'invalid edge')
        D[u]+=m;D[v]+=m
        G[u][v]+=m;G[v][u]+=m
    M=[[F(2*D[i]+G[i][i],6) if i==j else G[i][j]/6 for j in range(n)] for i in range(n)]
    H=invert(M)
    # Check exact mass-matrix inversion.
    for i in range(n):
        for j in range(n):
            check(sum(M[i][k]*H[k][j] for k in range(n))==int(i==j), 'inverse')
    vals=[]
    for i in range(n):
        val=sum(F(m)*absolute_segment(H[i][u],H[i][v]) for u,v,m in edges)
        vals.append(val)
        check(val < 3, 'bound 3')
    return max(vals), vals

def radial(d):
    B=[[F(0) for _ in range(d+1)] for _ in range(d+1)]
    for k in range(d+1):
        B[k][k]=2*d
        if k:B[k][k-1]=-k
        if k<d:B[k][k+1]=-(d-k)
    a=[row[0] for row in invert(B)]
    for k in range(d+1):
        lhs=2*d*a[k]-(k*a[k-1] if k else 0)-((d-k)*a[k+1] if k<d else 0)
        check(lhs==int(k==0),'radial Green equation')
        check(a[k]>0,'positivity')
        if k:
            check(a[k]<=a[k-1],'radial monotonicity')
            check(a[k]/a[k-1] <= F(k,d),'radial ratio bound')
    m0=sum(comb(d,k)*a[k] for k in range(d+1))
    m1=sum(k*comb(d,k)*a[k] for k in range(d+1))
    m2=sum(k*k*comb(d,k)*a[k] for k in range(d+1))
    check(m0==F(1,d),'zeroth moment')
    check(m1==F(1,d+2),'first moment')
    check(m2==F(3*d+2,(d+2)*(d+4)),'second moment')
    norm=3*sum(comb(d,k)*(d-k)*(a[k]**2+a[k+1]**2)/(a[k]+a[k+1]) for k in range(d))
    gap=3-norm
    d_formula=6*sum(comb(d,k)*(d-k)*a[k]*a[k+1]/(a[k]+a[k+1]) for k in range(d))
    check(gap==d_formula,'exact norm deficit')
    check(0<gap<=F(6,d+2),'first order bound')
    check(F(6,d+2)-gap<=F(6*(3*d+2),d*(d+2)*(d+4)),'second order remainder')
    return norm,a

def main():
    target={1:F(5,3),2:F(17,9),3:F(24877,12075),4:F(7397,3381)}
    for d in range(1,17):
        nr,a=radial(d)
        if d<=4:
            check(nr==target[d],'exact sample fraction')
            es=[(x,y,F(1)) for x in range(2**d) for j in range(d) for y in [x^(1<<j)] if x<y]
            ng,vertex=norm_graph(2**d,es)
            check(ng==nr,'full graph vs radial exact kernel')
            check(all(v==nr for v in vertex),'cube symmetry')
    rng=Random(24017)
    for n in range(2,7):
        for _ in range(12):
            edges=[(i,i+1,F(rng.randint(1,9),rng.randint(1,9))) for i in range(n-1)]
            edges += [(i,j,F(rng.randint(1,9),rng.randint(1,9)))
                      for i in range(n) for j in range(i+2,n) if rng.randrange(3)==0]
            norm_graph(n,edges)
    print('PASS:',CHECKS,'exact-rational assertions; cube dimensions 1..16;')
    print('      full hypercubes dimensions 1..4; 60 weighted connected graphs.')

if __name__=='__main__':
    main()
