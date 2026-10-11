#!/usr/bin/env python3
"""Exact rational replay of finite tree Laplacian simplex checks.

The rigorous unbounded proof is in RESULT.md; this finite checker is corroborative.
Only the Python standard library is used.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, isfinite


def laplacian(n, edges):
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for u,v in edges:
        L[u][u] += 1
        L[v][v] += 1
        L[u][v] -= 1
        L[v][u] -= 1
    return L


def inverse_rational(a):
    n = len(a)
    b = [[F(a[i][j]) for j in range(n)] + [F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j,n) if b[k][j])
        b[j], b[k] = b[k], b[j]
        p = b[j][j]
        b[j] = [z/p for z in b[j]]
        for k in range(n):
            if k != j:
                p=b[k][j]
                if p:
                    b[k] = [b[k][h]-p*b[j][h] for h in range(2*n)]
    return [row[n:] for row in b]


def pseudo_inverse(n,edges):
    L=laplacian(n,edges)
    A=[[L[i][j]+F(1,n) for j in range(n)] for i in range(n)]
    inv=inverse_rational(A)
    D=[[inv[i][j]-F(1,n) for j in range(n)] for i in range(n)]
    for i in range(n):
        assert sum(D[i])==0
        for j in range(n):
            assert sum(L[i][k]*D[k][j] for k in range(n))==F(int(i==j))-F(1,n)
    return L,D


def prufer_tree(n,code):
    if n==2: return [(0,1)]
    degree=[1]*n
    for x in code:degree[x]+=1
    edges=[]
    for x in code:
        leaf=min(j for j in range(n) if degree[j]==1)
        edges.append((leaf,x))
        degree[leaf]-=1
        degree[x]-=1
    u,v=(j for j in range(n) if degree[j]==1)
    edges.append((u,v))
    return edges


def pairwise_dist(n,edges):
    nbr=[[] for _ in range(n)]
    for u,v in edges:nbr[u].append(v);nbr[v].append(u)
    out=[]
    for i in range(n):
        dist=[-1]*n;dist[i]=0;queue=[i]
        for u in queue:
            for v in nbr[u]:
                if dist[v]<0:dist[v]=dist[u]+1;queue.append(v)
        assert min(dist)>=0
        out.append(dist)
    return out


def path_norm2(n,i):
    z=F(2*i-n-1,2) # i is 1-indexed
    return (n**4+10*n*n-11+120*(n*n+1)*z*z-240*z**4)/F(720*n)


def path_explicit_column(n,i):
    a=F((n-i)*(n-i+1),2*n)-F(n*n-1,6*n)
    return [a+F(k*(k-1),2*n)-max(0,k-i) for k in range(1,n+1)]


def verify_tree(n,edges):
    L,D=pseudo_inverse(n,edges)
    norms2=[sum(D[k][i]**2 for k in range(n)) for i in range(n)]
    norms=[sqrt(float(x)) for x in norms2]
    S=sum(norms)
    assert S>0
    rho=1/S
    low=6/(sqrt(n)*(n*n-1))
    up=4*sqrt(2)*n/((n+2)*(n-1))
    assert low-2e-12 <=rho<=up+2e-12,(n,edges,rho,low,up)
    d=pairwise_dist(n,edges)
    W=sum(d[i][j] for i in range(n) for j in range(i+1,n))
    assert sum(D[i][i] for i in range(n))==F(W,n)
    assert W <= n*(n*n-1)//6
    # Center recovered from barycentric weights; every facet's clearance equal.
    lam=[si/S for si in norms]
    assert abs(sum(lam)-1)<1e-12
    c=[sum(float(L[j][i])*lam[i] for i in range(n)) for j in range(n)]
    assert abs(sum(c))<1e-10
    for i in range(n):
        raw=1/n + sum(float(D[j][i])*c[j] for j in range(n))
        assert abs(raw-lam[i])<1e-10
        assert abs(raw/norms[i]-rho)<1e-10
    return rho


number=0
for n in range(2,7):
    for code in product(range(n),repeat=n-2):
        edges=prufer_tree(n,code)
        verify_tree(n,edges)
        number+=1
for n in range(7,13):
    # Deterministic nontrivial Prufer sequences, no stochastic dependencies.
    for k in range(16):
        code=tuple((j*j+3*j*k+7*k+2)%n for j in range(n-2))
        verify_tree(n,prufer_tree(n,code))
        number+=1

for n in range(2,41):
    path=[(i,i+1) for i in range(n-1)]
    star=[(0,i) for i in range(1,n)]
    # The formula for each path column is exact in rational arithmetic.
    for i in range(1,n+1):
        v=path_explicit_column(n,i)
        assert sum(v)==0
        L=laplacian(n,path)
        for k in range(n):
            assert sum(L[k][j]*v[j] for j in range(n)) == F(int(k==i-1))-F(1,n)
        assert sum(z*z for z in v)==path_norm2(n,i)
    hub=F(n-1,n**3)
    leaf=F(n**3-n*n-n-1,n**3)
    assert hub>0 and leaf>0
    if n<=12:
        _,D=pseudo_inverse(n,star)
        assert sum(D[k][0]**2 for k in range(n))==hub
        for i in range(1,n):
            assert sum(D[k][i]**2 for k in range(n))==leaf
        verify_tree(n,path)
        verify_tree(n,star)

# Check the asymptotic constants by finite Riemann sums (not infinite proofs).
for n in (1000,5000):
    path_S=sum(sqrt(float(path_norm2(n,i))) for i in range(1,n+1))
    cpath=n**2.5/path_S
    assert abs(cpath-10.1708468399938)<0.03
    star_S=sqrt((n-1)/n**3)+(n-1)*sqrt((n**3-n*n-n-1)/n**3)
    assert abs(n/star_S-1)<0.01
print(f'VERIFY_OK tree-laplacian-inradius labeled_trees={number} exact_pseudoinverse=yes path_star_n=2..40 exact_columns=yes tree_bounds=yes asymptotics=yes')
