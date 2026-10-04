#!/usr/bin/env python3
from itertools import product
from collections import defaultdict

def leq(n,a,b):
    return a==b or (a%2==0 and b%2==1 and ((b-a)%(2*n) in (1,2*n-1)))

def is_map(m,n,f):
    return all(leq(n,f[e],f[(e-1)%(2*m)]) and leq(n,f[e],f[(e+1)%(2*m)]) for e in range(0,2*m,2))

def degree(m,n,f):
    cur=f[0]; total=0
    for i in range(2*m):
        v=f[(i+1)%(2*m)]
        opts=[d for d in (-1,0,1) if (cur+d-v)%(2*n)==0]
        assert len(opts)==1
        cur += opts[0]; total += opts[0]
    assert total%(2*n)==0
    return total//(2*n)

def all_maps(m,n):
    return [f for f in product(range(2*n), repeat=2*m) if is_map(m,n,f)]

def components(m,n,ms):
    index={f:i for i,f in enumerate(ms)}
    parent=list(range(len(ms)))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    neighbors={x:[y for y in range(2*n) if y!=x and (leq(n,x,y) or leq(n,y,x))] for x in range(2*n)}
    for i,f in enumerate(ms):
        g=list(f)
        for j,x in enumerate(f):
            for y in neighbors[x]:
                g[j]=y
                k=index.get(tuple(g))
                if k is not None: union(i,k)
            g[j]=x
    out=defaultdict(list)
    for i,f in enumerate(ms): out[find(i)].append(f)
    return list(out.values())

expected={(2,3):(48,1),(3,2):(200,3),(3,3):(234,7),(4,2):(1156,7),(4,3):(1248,3)}
for m,n in expected:
    ms=all_maps(m,n); cs=components(m,n,ms)
    assert (len(ms),len(cs))==expected[(m,n)]
    predicted=2*((m-1)//n)+1+(2*n if m%n==0 else 0)
    assert len(cs)==predicted
    for c in cs:
        assert len({degree(m,n,f) for f in c})==1
    if m%n==0:
        k=m//n
        for s in (-1,1):
            ext=[c for c in cs if degree(m,n,c[0])==s*k]
            assert len(ext)==n and all(len(c)==1 for c in ext)
    print(f"m={m} n={n} maps={len(ms)} components={len(cs)}")
print("VERIFY_OK")
