#!/usr/bin/env python3
"""Exact finite checks for uniform spanning-tree degree covariance on wheels.
No external packages or network access are needed.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def inverse(a):
    n = len(a)
    z = [[F(a[i][j]) for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k,n) if z[i][k])
        z[k], z[p] = z[p], z[k]
        d = z[k][k]
        z[k] = [v/d for v in z[k]]
        for i in range(n):
            if i != k and z[i][k]:
                v = z[i][k]
                z[i] = [x-v*y for x,y in zip(z[i],z[k])]
    return [v[n:] for v in z]

def wheel(m):
    return [(i,(i+1)%m) for i in range(m)] + [(i,m) for i in range(m)]

def green(m):
    a = [[3*int(i==j)-int((j-i)%m in (1,m-1)) for j in range(m)] for i in range(m)]
    return inverse(a)

def edge_kernel(m,h,edges):
    vectors = []
    for u,v in edges:
        vec = [0]*m
        if u < m:vec[u] += 1
        if v < m:vec[v] -= 1
        vectors.append(vec)
    return [[sum(F(vectors[e][i]*vectors[f][j])*h[i][j] for i in range(m) for j in range(m))
             for f in range(2*m)] for e in range(2*m)]

def cov_kernel(m,h,edges):
    k = edge_kernel(m,h,edges)
    incident = [[ei for ei,(u,v) in enumerate(edges) if a in (u,v)] for a in range(m+1)]
    return [[sum((k[e][e]*(1-k[e][e]) if e==f else -k[e][f]**2)
                 for e in incident[u] for f in incident[v]) for v in range(m+1)]
            for u in range(m+1)]

def is_tree(m,edges,indices):
    parent = list(range(m+1))
    def root(a):
        while parent[a]!=a:a=parent[a]
        return a
    for ei in indices:
        u,v=edges[ei];u=root(u);v=root(v)
        if u==v:return False
        parent[u]=v
    return True

def covariance_enumeration(m,edges):
    n=m+1; cnt=0
    sums=[0]*n; prods=[[0]*n for _ in range(n)]
    for indices in combinations(range(len(edges)),m):
        if not is_tree(m,edges,indices):continue
        cnt += 1
        d=[0]*n
        for ei in indices:
            u,v=edges[ei]; d[u]+=1;d[v]+=1
        for i in range(n):
            sums[i]+=d[i]
            for j in range(n):prods[i][j]+=d[i]*d[j]
    cov=[[F(prods[i][j],cnt)-F(sums[i]*sums[j],cnt*cnt)
          for j in range(n)] for i in range(n)]
    return cov,cnt

def main():
    assertions=0; graph_count=0
    for m in range(3,16):
        edges=wheel(m)
        h=green(m)
        x=h[0][0]
        c=cov_kernel(m,h,edges)
        target=-(57*x*x-50*x+11)/2
        assert c[0][1]==target and target<0;assertions+=2
        # The hub is distinguished; covariance sum constraint and rotation symmetry.
        hubvar=c[m][m]
        assert hubvar>0;assertions+=1
        for u in range(m):
            assert c[u][m]==-hubvar/m; assertions+=1
            for v in range(u+1,m):
                assert c[u][v]<0; assertions+=1
        # The two deterministic kernel inverse relations used in the proof.
        d1=h[0][1];d2=h[0][2];d3=h[0][3%m]
        assert 3*x-2*d1==1; assertions+=1
        assert d2==3*d1-x;assertions+=1
        assert d3==3*d2-d1;assertions+=1
        if m<=8:
            brute,cnt=covariance_enumeration(m,edges)
            graph_count+=cnt
            for i in range(m+1):
                for j in range(m+1):
                    assert brute[i][j]==c[i][j]
                    assertions+=1
    print('VERIFY_OK',assertions,'exact identities; enumerated',graph_count,'wheel spanning trees')

if __name__=='__main__':main()
