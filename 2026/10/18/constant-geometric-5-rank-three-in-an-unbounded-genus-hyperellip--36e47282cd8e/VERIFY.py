#!/usr/bin/env python3
"""Standalone exact checks for stable Cartier rank in characteristic five."""

def matrix(r):
    g=3**r
    coeff={2:1,2*g+2:2,4*g+2:1}
    a=[[0]*g for _ in range(g)]
    for i in range(1,g+1):
        for j in range(1,g+1):
            a[i-1][j-1]=coeff.get(5*i-j,0)
    return a

def stable_rank_edges(r):
    g=3**r
    a=matrix(r)
    edges={}
    for i,row in enumerate(a):
        nonzero=[j for j,v in enumerate(row) if v!=0]
        if len(nonzero)>1:
            raise AssertionError((r,i,nonzero))
        if nonzero:
            edges[i]=nonzero[0]
    assert len(edges.values())==len(set(edges.values()))
    cycles=set()
    for i in range(g):
        path=[];idx={};v=i
        while v in edges and v not in idx:
            idx[v]=len(path);path.append(v);v=edges[v]
        if v in idx:
            cycles.update(path[idx[v]:])
    return len(cycles),{2*i+1 for i in cycles}

def orbits(r):
    g=3**r; m=4*g; b=set(range(1,2*g,2)); visited=set();survive=set()
    for t in sorted(b):
        if t in visited:continue
        path=[];x=t
        while x not in path:
            path.append(x);x=5*x % m
        assert x==t
        visited.update(path)
        if set(path).issubset(b):survive.update(path)
    return survive

for r in range(1,7):
    actual,tset=stable_rank_edges(r)
    expected={3**r,3**(r-1),5*3**(r-1)}
    b=orbits(r)
    assert b==expected==(tset), (r,actual,b,tset,expected)
    print('r=',r,'genus=',3**r,'p_rank=',actual,'survivors=',sorted(b))
print('VERIFY_OK')
