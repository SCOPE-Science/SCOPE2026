#!/usr/bin/env python3
"""Finite smoke checks of the explicit prefix retraction construction.
The infinite family and optimal lower bound are proved analytically in RESULT.md.
"""

def circle_dist(n, i, j):
    gap = abs(i-j)
    return min(gap, n-gap)


def construct(n):
    assert n >= 3
    if n == 3:
        order = [0,1,2]
        parents = {1:0,2:0}
        return order,parents
    a=(n+3)//4
    b=(n+1)//2
    c=(3*n+3)//4
    assert 0<a<b<c<n
    anchors={0,a,b,c}
    order=[0,a,b,c]+[v for v in range(n) if v not in anchors]
    parents={a:0,b:a,c:a}
    for v in range(1,n):
        if v in anchors: continue
        if v<a: parents[v]=0
        elif v<b: parents[v]=a
        elif v<c: parents[v]=b
        else: parents[v]=c
    return order,parents


def check(n):
    order,parents=construct(n)
    assert sorted(order)==list(range(n))
    rank={v:i for i,v in enumerate(order)}
    assert all(rank[parents[v]]<rank[v] for v in parents)
    K=(n+3)//4
    maps=[]
    for k in range(1,n+1):
        def project(v):
            while rank[v]>=k:
                v=parents[v]
            return v
        f=tuple(project(v) for v in range(n))
        assert set(f)==set(order[:k])
        assert all(f[x]==x for x in order[:k])
        assert all(circle_dist(n,f[i],f[(i+1)%n])<=K for i in range(n))
        maps.append(f)
    assert all(tuple(maps[k][maps[j][i]] for i in range(n))==maps[k]
               for k in range(n) for j in range(k+1,n))
    return K


if __name__=='__main__':
    for n in range(3,129):
        check(n)
    print('PASS: 126 cycle sizes (n=3,...,128), every prefix, all cycle edges, and commutation')
