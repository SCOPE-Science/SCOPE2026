"""Independent exhaustive matching enumeration on labelled cycle edges.
The verified target is the eccentricity of the minimum-maximal-matching
single-edge-replacement graph, not a general matching reconfiguration claim.
Run: python verify_direct.py
"""
from itertools import combinations
from collections import deque
from math import ceil

def configs(n):
    k=(n+2)//3
    out=[]
    for c in combinations(range(n),k):
        mask=sum(1<<v for v in c)
        if any(((mask>>( (i-1)%n ))&1) and ((mask>>i)&1) for i in range(n)):
            continue
        if any(not (((mask>>( (i-1)%n ))&1) or ((mask>>i)&1) or ((mask>>((i+1)%n))&1)) for i in range(n)):
            continue
        out.append(mask)
    return out

def test(n):
    verts=configs(n); idx={v:i for i,v in enumerate(verts)}
    assert len(idx)==n*((n-1)//3)//2,(n,len(idx))
    adj=[set() for _ in verts]
    for a,v in enumerate(verts):
        for b in range(n):
            if v>>b&1:
                x=v^(1<<b)
                for c in range(n):
                    if not x>>c&1 and c!=b:
                        y=x|(1<<c)
                        if y in idx:
                            j=idx[y];adj[a].add(j)
                            assert (c-b)%n in (1,n-1),('nonadjacent exchange',n,b,c)
    assert all(i in adj[j] for i,ns in enumerate(adj) for j in ns)
    # Recover the older bracelet defect coordinates independently and
    # verify a complete vertex/edge bijection to the separated-pair model.
    k=(n-1)//3; h=k+1
    mapped=[]
    for mask in verts:
        deficits=[i for i in range(n) if not(mask>>i&1) and
                  (mask>>((i-1)%n)&1) and (mask>>((i+1)%n)&1)]
        assert len(deficits)==2
        p=tuple(sorted((-k*i)%n for i in deficits))
        assert h<=p[1]-p[0]<=n-h
        mapped.append(p)
    assert len(set(mapped))==len(verts)
    mapped_adj=set()
    for p in mapped:
        for which in (0,1):
            for step in (-1,1):
                q=list(p);q[which]=(q[which]+step)%n
                q=tuple(sorted(q))
                if q in set(mapped):mapped_adj.add(frozenset((p,q)))
    actual_adj={frozenset((mapped[i],mapped[j])) for i,ns in enumerate(adj) for j in ns}
    assert actual_adj==mapped_adj,(n,len(actual_adj),len(mapped_adj))
    ecc=[]
    for i in range(len(verts)):
        dist=[-1]*len(verts);dist[i]=0;Q=deque([i]);
        while Q:
            x=Q.popleft()
            for y in adj[x]:
                if dist[y]<0: dist[y]=dist[x]+1;Q.append(y)
        assert min(dist)>=0
        ecc.append(max(dist))
    assert set(ecc)=={n//2},('ecc',n,set(ecc))
    ds={len(ns) for ns in adj}
    assert ds <= {2,4},(n,ds)
    return len(verts),sum(map(len,adj))//2,dict((d,sum(len(x)==d for x in adj)) for d in ds),n//2

for n in (7,10,13,16,19,22):
    print(n,test(n))
print('CYCLE_MATCHING_DIRECT_ALL_PASS')
