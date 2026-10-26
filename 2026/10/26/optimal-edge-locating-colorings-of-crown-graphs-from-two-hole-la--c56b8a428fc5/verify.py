#!/usr/bin/env python3
"""Independent finite checks for the edge-locating crown coloring theorem.
Run with Python 3, using only the standard library.
The infinite-family proof is mathematical; these are finite regression tests.
"""
from collections import deque

SMALL = {6:(1,2,3,5,0,4),7:(1,2,4,5,3,6,0),8:(4,3,5,6,7,0,1,2)}

def sigma(n):
    if n in SMALL:
        return list(SMALL[n])
    assert n >= 9
    a = [(j+3) % n for j in range(n)]
    if n % 3 == 2:
        k = (n-2)//3
        for x,y in ((k-3,k-2),(k-1,k)):
            a[x],a[y]=a[y],a[x]
    return a

def pairs(n):
    m=n+1; s=sigma(n)
    R=[frozenset(((i-1)%m,(i+s[i])%m)) for i in range(n)]
    C=[frozenset(((s[j]-1)%m,(j+s[j])%m)) for j in range(n)]
    return R+C

def fast_check(n):
    s=sigma(n); m=n+1
    assert sorted(s)==list(range(n))
    p=pairs(n)
    assert all(len(x)==2 for x in p), n
    assert len(set(p))==2*n, n


def graph_check(n):
    m=n+1; s=sigma(n)
    vertices=2*n
    edges=[(i,n+j,(i+s[j])%m) for i in range(n) for j in range(n) if i!=j]
    adj=[[] for _ in range(vertices)]
    for u,v,c in edges:
        adj[u].append(v);adj[v].append(u)
    assert all(len(x)==n-1 for x in adj)
    # All-pairs shortest paths, independently of the missing-color calculation.
    dist=[]
    for root in range(vertices):
        d=[-1]*vertices;d[root]=0;q=deque([root])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0:d[v]=d[u]+1;q.append(v)
        assert min(d)>=0
        dist.append(d)
    codes=[]
    for v in range(vertices):
        code=[]
        for c in range(m):
            relevant=[(a,b) for a,b,z in edges if z==c]
            assert relevant, (n,c)
            code.append(min(min(dist[v][a],dist[v][b]) for a,b in relevant))
        codes.append(tuple(code))
    assert len(set(codes))==vertices, n
    # Each color class is a matching.
    for c in range(m):
        ends=[u for a,b,z in edges if z==c for u in (a,b)]
        assert len(ends)==len(set(ends)), (n,c)
    # The zeros of the distance code recover the incident-color complement.
    assert [frozenset(c for c,d in enumerate(code) if d!=0) for code in codes]==pairs(n)

if __name__=='__main__':
    for n in range(6,5001):fast_check(n)
    for n in range(6,14):graph_check(n)
    print('PASS: 4,995 parameter instances and 8 independent graph-distance checks')
