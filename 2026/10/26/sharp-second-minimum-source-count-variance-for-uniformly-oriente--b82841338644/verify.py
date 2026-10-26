#!/usr/bin/env python3
"""Independent exact finite checks for a theorem about random edge orientations."""
from itertools import product
from fractions import Fraction as F
from collections import defaultdict

def edges_from_prufer(n, code):
    degree = [1]*n
    for x in code: degree[x]+=1
    out=[]
    for x in code:
        leaf=next(v for v,d in enumerate(degree) if d==1)
        out.append((leaf,x))
        degree[leaf]-=1;degree[x]-=1
    u,v=[i for i,d in enumerate(degree) if d==1]
    out.append((u,v))
    return out

def exact_form(n, edges):
    d=[0]*n
    for x,y in edges:d[x]+=1;d[y]+=1
    a=[F(1,2**k) for k in d]
    return sum(((a[x]-a[y])**2 for x,y in edges),F(0))+sum((F(2**k-k-1,4**k) for k in d),F(0))

def brute_orientation(n, edges):
    sums=sums2=0
    for mask in range(1<<len(edges)):
        indeg=[0]*n
        for j,(x,y) in enumerate(edges):
            indeg[x if (mask>>j)&1 else y]+=1
        s=sum(z==0 for z in indeg)
        sums+=s;sums2+=s*s
    m=1<<len(edges)
    return F(sums2,m)-F(sums,m)**2

for n in range(4,8):
    best=None
    min_count=0
    for code in product(range(n),repeat=n-2):
        edges=edges_from_prufer(n,code)
        d=[0]*n
        for u,v in edges:d[u]+=1;d[v]+=1
        stat=exact_form(n,edges)
        if n<=6:assert stat==brute_orientation(n,edges)
        gap=stat-F(n,16)
        assert gap>=0
        if max(d)>=3:
            assert gap>=F(3,64)
            if gap==F(3,64):
                assert d.count(3)==1 and max(d)==3
                branch=d.index(3)
                neighbors={i:[] for i in range(n)}
                for u,v in edges:neighbors[u].append(v);neighbors[v].append(u)
                for endpoint in (v for v in range(n) if d[v]==1):
                    frontier=[(branch,-1,0)]
                    while frontier:
                        x,old,dist=frontier.pop()
                        if x==endpoint:
                            assert dist>=2;break
                        frontier.extend((w,x,dist+1) for w in neighbors[x] if w!=old)
                    else:raise AssertionError('missing path')
            if best is None or gap<best:best=gap;min_count=1
            elif gap==best:min_count+=1
    if n==7:assert best==F(3,64)
    else:assert best>F(3,64)
    print('PRUFER_EXHAUSTIVE_PASS',n,'min_nonpath_gap',best,'labeled_minimizers',min_count)
for d in range(3,1001):
    a=F(1,2**d)
    g=(F(1,4)-a)**2
    b=F(2**d-d-1,4**d)
    delta=F(1,16)-b
    assert g>=F(1,64) and delta<=F(d-2,64)
    if d>=4: assert g>=F(9,256)
print('LOCAL_DEGREE_BOUNDS_PASS d=3..1000 (finite consistency only)')
print('VERIFY_OK')
