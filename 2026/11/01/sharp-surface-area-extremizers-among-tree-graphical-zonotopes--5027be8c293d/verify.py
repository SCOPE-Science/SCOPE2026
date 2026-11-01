#!/usr/bin/env python3
"""Deterministic verification of the tree-zonotope surface-area theorem.

Pure Python 3; no external packages.  Exact Gram minors and combinatorial
cut sizes are compared for all labeled trees on at most seven vertices.
"""
from itertools import product
from math import sqrt, pi


def prufer_edges(code):
    n = len(code)+2
    degrees = [1]*n
    for v in code:
        degrees[v] += 1
    edges=[]
    for v in code:
        leaf = next(i for i,d in enumerate(degrees) if d==1)
        edges.append((leaf,v))
        degrees[leaf]-=1
        degrees[v]-=1
    a,b = [i for i,d in enumerate(degrees) if d==1]
    edges.append((a,b))
    return edges


def det_bareiss(A):
    A = [list(row) for row in A]
    n=len(A)
    if not n: return 1
    sign=1; prior=1
    for k in range(n-1):
        if A[k][k]==0:
            ix=next((i for i in range(k+1,n) if A[i][k]!=0),None)
            if ix is None: return 0
            A[k],A[ix]=A[ix],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                top=A[i][j]*pivot-A[i][k]*A[k][j]
                assert top%prior==0
                A[i][j]=top//prior
        for i in range(k+1,n): A[i][k]=0
        prior=pivot
    return sign*A[-1][-1]


def gram(edges):
    def dot(e,f):
        a,b=e;c,d=f
        return (a==c)-(a==d)-(b==c)+(b==d)
    return [[dot(e,f) for f in edges] for e in edges]


def cut_products(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    out=[]
    for u,v in edges:
        seen={u}; stack=[u]
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if (x==u and y==v) or (x==v and y==u):continue
                if y not in seen:
                    seen.add(y);stack.append(y)
        s=len(seen)
        assert 0<s<n
        out.append(s*(n-s))
    return out


def surface(n,edges):
    products=cut_products(n,edges)
    return 2*sum(sqrt(x) for x in products)


def run():
    total=0
    for n in range(3,8):
        star=2*(n-1)*sqrt(n-1)
        path=2*sum(sqrt(k*(n-k)) for k in range(1,n))
        hi=0;lo=0
        for word in product(range(n),repeat=n-2):
            edges=prufer_edges(word)
            G=gram(edges)
            assert det_bareiss(G)==n  # same volume sqrt(n) for every tree
            cp=cut_products(n,edges)
            for omit,p in enumerate(cp):
                minor=[[G[i][j] for j in range(n-1) if j!=omit]
                       for i in range(n-1) if i!=omit]
                assert det_bareiss(minor)==p, (n,edges,omit,p)
            S=2*sum(sqrt(p) for p in cp)
            assert star-1e-10<=S<=path+1e-10,(n,word,S,star,path)
            is_star=max(sum(u in e for e in edges) for u in range(n))==n-1
            is_path=max(sum(u in e for e in edges) for u in range(n))<=2
            if abs(S-star)<1e-10:
                assert is_star
                lo+=1
            if abs(S-path)<1e-10:
                assert is_path
                hi+=1
            total+=1
        print('n=',n,'star=',format(star,'.12g'),'path=',format(path,'.12g'),
              'count_star=',lo,'count_path=',hi)
    assert total == sum(n**(n-2) for n in range(3,8))
    print('Checked',total,'labeled trees with all exact Gram minors.')
    for n in (50,100,250,500):
        ratio=2*sum(sqrt(k*(n-k)) for k in range(1,n))/(2*(n-1)*sqrt(n-1))
        assert abs(ratio/sqrt(n)-pi/8)<0.06
    print('ALL_TREE_ZONOTOPE_SURFACE_CHECKS_PASSED')

if __name__=='__main__':run()
