#!/usr/bin/env python3
"""Exhaustive exact finite checks of a facet-normal covariance identity.

Requires only Python's standard library. All matrices use fractions.Fraction.
It enumerates rooted feasible integer potentials independently of the block law,
checks connectedness of their tight-edge graphs, and compares their empirical
covariance with the independently formed weighted graph Laplacian pseudoinverse.
"""
from fractions import Fraction as F
from collections import deque
from math import comb

def cactus(edges):
    assert len(set(tuple(sorted(e)) for e in edges))==len(edges)
    n=max(max(e) for e in edges)+1
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    order=[0]; par={0:None}
    for v in order:
        for w in adj[v]:
            if w not in par:
                par[w]=v;order.append(w)
    assert len(order)==n
    return n,adj,order,par

def facets(edges):
    n,adj,order,par=cactus(edges)
    vals=[None]*n; vals[0]=0; ans=[]
    def rec(k):
        if k==n:
            ta=[[] for _ in range(n)]
            for a,b in edges:
                if abs(vals[a]-vals[b])==1:
                    ta[a].append(b);ta[b].append(a)
            seen={0}; stack=[0]
            while stack:
                v=stack.pop()
                for w in ta[v]:
                    if w not in seen:
                        seen.add(w);stack.append(w)
            if len(seen)==n:
                ans.append(tuple(vals))
            return
        v=order[k];p=par[v]
        for delta in (-1,0,1):
            vals[v]=vals[p]+delta
            if all(vals[w] is None or abs(vals[v]-vals[w])<=1 for w in adj[v]):
                rec(k+1)
            vals[v]=None
    rec(1)
    return ans

def inv(A):
    n=len(A)
    z=[[F(A[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if z[i][k]),None)
        assert pivot is not None
        z[k],z[pivot]=z[pivot],z[k]
        scale=z[k][k]
        z[k]=[x/scale for x in z[k]]
        for i in range(n):
            if i!=k:
                a=z[i][k]
                if a: z[i]=[x-a*y for x,y in zip(z[i],z[k])]
    return [row[n:] for row in z]

def law(edges,cycles):
    n=max(max(e) for e in edges)+1
    for c in cycles:assert len(c)>=3
    cycleedges={}
    for c in cycles:
        for a,b in zip(c,c[1:]+c[:1]):
            key=tuple(sorted((a,b)))
            assert key not in cycleedges
            cycleedges[key]=len(c)
    assert set(cycleedges).issubset(set(tuple(sorted(e)) for e in edges))
    lap=[[F(0) for _ in range(n)] for _ in range(n)]
    for a,b in edges:
        r=cycleedges.get(tuple(sorted((a,b))),0)
        sigma=F(r,r-1) if r and r%2==0 else F(1)
        cond=1/sigma
        lap[a][a]+=cond;lap[b][b]+=cond
        lap[a][b]-=cond;lap[b][a]-=cond
    # Standard identity L^+ = (L+J/n)^{-1}-J/n.
    avg=F(1,n)
    mat=inv([[lap[i][j]+avg for j in range(n)] for i in range(n)])
    return [[mat[i][j]-avg for j in range(n)] for i in range(n)]

def determinant(A):
    n=len(A); B=[[F(v) for v in row] for row in A];out=F(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if B[i][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:B[k],B[pivot]=B[pivot],B[k];out=-out
        d=B[k][k];out*=d
        for i in range(k+1,n):
            ratio=B[i][k]/d
            for j in range(k+1,n):B[i][j]-=ratio*B[k][j]
            B[i][k]=0
    return out

def direct_cov(vectors):
    n=len(vectors[0]);N=len(vectors)
    out=[[F(0) for _ in range(n)] for _ in range(n)]
    for vec in vectors:
        mean=F(sum(vec),n)
        z=[F(v)-mean for v in vec]
        for i in range(n):
            for j in range(n):out[i][j]+=z[i]*z[j]
    return [[x/N for x in row] for row in out]

def facet_product(edges,cycles):
    cyc_edges=set()
    prod=1
    for cyc in cycles:
        m=len(cyc)
        prod*=comb(m,m//2) if m%2==0 else m*comb(m-1,(m-1)//2)
        for a,b in zip(cyc,cyc[1:]+cyc[:1]):cyc_edges.add(tuple(sorted((a,b))))
    bridges=len(set(tuple(sorted(x)) for x in edges)-cyc_edges)
    return prod*(2**bridges)

def check(label,edges,cycles):
    a=facets(edges)
    assert len(a)==facet_product(edges,cycles),(label,len(a),facet_product(edges,cycles))
    E=direct_cov(a);L=law(edges,cycles)
    assert E==L,(label,[(i,j,E[i][j],L[i][j]) for i in range(len(E)) for j in range(len(E)) if E[i][j]!=L[i][j]])
    n=len(E)
    # Ordered pair potential square differences = resistance distances.
    for i in range(n):
        for j in range(n):
            v=F(sum((v[i]-v[j])**2 for v in a),len(a))
            resistance=L[i][i]+L[j][j]-2*L[i][j]
            assert v==resistance
    kirchhoff=sum((L[i][i]+L[j][j]-2*L[i][j]) for i in range(n) for j in range(i+1,n))
    assert kirchhoff==n*sum(L[i][i] for i in range(n))
    det_restricted = n*determinant([row[:-1] for row in L[:-1]])
    product=F(1,n)
    for cyc in cycles:
        r=len(cyc); factor=F(r,r-1) if r%2==0 else F(1)
        product*=factor**(r-1)/r
    assert det_restricted==product, (label,det_restricted,product)
    print(label,'n',n,'m',len(edges),'facets',len(a),'trace',sum(L[i][i] for i in range(n)),'det',det_restricted,'OK')

def main():
    check('edge',[(0,1)],[])
    check('path-4',[(0,1),(1,2),(2,3)],[])
    check('triangle',[(0,1),(1,2),(2,0)],[[0,1,2]])
    check('square',[(0,1),(1,2),(2,3),(3,0)],[[0,1,2,3]])
    check('pentagon',[(0,1),(1,2),(2,3),(3,4),(4,0)],[[0,1,2,3,4]])
    check('hexagon',[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)],[[0,1,2,3,4,5]])
    check('triangle-square bouquet',[(0,1),(1,2),(2,0),(0,3),(3,4),(4,5),(5,0)],[[0,1,2],[0,3,4,5]])
    check('triangle-square bridge',[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,3)],[[0,1,2],[3,4,5,6]])
    check('two-square bouquet',[(0,1),(1,2),(2,3),(3,0),(0,4),(4,5),(5,6),(6,0)],[[0,1,2,3],[0,4,5,6]])
    check('two triangles with tail',[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3),(5,6)],[[0,1,2],[3,4,5]])
    print('ALL EXACT FINITE CHECKS PASSED')
if __name__=='__main__':main()
