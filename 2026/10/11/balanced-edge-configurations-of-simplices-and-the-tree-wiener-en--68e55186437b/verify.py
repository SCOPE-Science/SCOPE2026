#!/usr/bin/env python3
"""Independent exact-rational checks of the simplex skeleton/tree correspondence.
Pure Python standard library, no network or external data.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import deque, Counter
import random
import math


def prufer_edges(n, code):
    degree=[1]*n
    for z in code: degree[z]+=1
    out=[]
    for z in code:
        leaf=next(i for i in range(n) if degree[i]==1)
        out.append((min(leaf,z), max(leaf,z)))
        degree[leaf]-=1;degree[z]-=1
    i,j=[i for i in range(n) if degree[i]==1]
    out.append((min(i,j),max(i,j)))
    return out


def bfs_dist(n,edges,root,skip=None):
    adj=[[] for _ in range(n)]
    for i,j in edges:
        if (i,j)==skip or (j,i)==skip: continue
        adj[i].append(j);adj[j].append(i)
    dist=[-1]*n;dist[root]=0
    q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1;q.append(v)
    return dist


def check(n,code):
    edges=prufer_edges(n,code)
    pts=[]
    cutsum=0
    for i,j in edges:
        d=bfs_dist(n,edges,i,skip=(i,j))
        k=sum(x>=0 for x in d)
        assert 1<=k<n
        ci=F(n-k,n);cj=F(k,n)
        p=[F(0)]*n;p[i]=ci;p[j]=cj
        pts.append(p)
        cutsum+=k*(n-k)
        assert ci>0 and cj>0 and ci+cj==1
    # Independent barycenter test using n coordinate affine embedding.
    assert all(sum(p[i] for p in pts)==F(n-1,n) for i in range(n))
    # Pairwise distances in centered regular simplex with edge s=1:
    # ||x-y||^2 = 1/2 * sum (barycentric-coordinate differences)^2.
    E=sum((sum((p[k]-q[k])**2 for k in range(n))/2
           for p,q in combinations(pts,2)),F(0))
    W=sum(sum(bfs_dist(n,edges,i)[j] for j in range(i+1,n)) for i in range(n))
    assert W==cutsum
    formula=F(n-1)* (F((n-1)**2,2*n)-F(W,n*n))
    assert E==formula,(n,edges,E,formula)
    assert F((n-1)**2*(n-2),3*n) <= E <= F((n-1)**3*(n-2),2*n*n)
    ds=Counter(sum(i in e for e in edges) for i in range(n))
    if E == F((n-1)**2*(n-2),3*n):
        assert max(ds)==2 or n==3
    if E == F((n-1)**3*(n-2),2*n*n):
        assert max(ds)==n-1 or n==3
    return tuple(sorted(edges)), E

for n in range(3,7):
    seen=set();vals=Counter()
    for code in product(range(n),repeat=n-2):
        key, E=check(n,code)
        assert key not in seen
        seen.add(key);vals[E]+=1
    assert len(seen)==n**(n-2)
    if n>=4:
        assert vals[min(vals)]==math.factorial(n)//2
        assert vals[max(vals)]==n
    print('EXHAUSTIVE',n,len(seen),'min',min(vals),'max',max(vals))

rng=random.Random(294731)
for n in (7,8,9,12,17,30):
    for r in range(150):
        check(n,tuple(rng.randrange(n) for _ in range(n-2)))
    print('RANDOM',n,150)
print('VERIFY_OK')
