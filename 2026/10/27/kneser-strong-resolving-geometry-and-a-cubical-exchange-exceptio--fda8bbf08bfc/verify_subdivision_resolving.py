#!/usr/bin/env python3
"""Direct strong-geodesic enumeration, without strong-resolving-graph theorem."""
from itertools import combinations
from collections import Counter,deque
from math import comb
for n in (4,5):
    edgepairs=list(combinations(range(n),2)); size=n+len(edgepairs)
    neighbors=[set() for _ in range(size)]
    for i,(u,v) in enumerate(edgepairs):
        neighbors[u].add(n+i);neighbors[v].add(n+i)
        neighbors[n+i].update((u,v))
    dist=[[999]*size for _ in range(size)]
    for u in range(size):
        dist[u][u]=0; q=deque([u])
        while q:
            a=q.popleft()
            for b in neighbors[a]:
                if dist[u][b]==999:dist[u][b]=dist[u][a]+1;q.append(b)
    # For each pair, list all direct strong resolvers from exact geodesic equalities.
    requirements=[]
    for a,b in combinations(range(size),2):
        resolves=sum(1<<w for w in range(size) if dist[w][a]==dist[w][b]+dist[a][b] or dist[w][b]==dist[w][a]+dist[a][b])
        requirements.append(resolves)
        assert resolves
    valid=[]
    hist=Counter()
    for selected in range(1<<size):
        if all(selected & r for r in requirements):
            valid.append(selected);hist[selected.bit_count()]+=1
    m=comb(n,2)
    indep=[1,comb(n,2),n*comb(n-1,2)]+[n*comb(n-1,j)+(comb(n,3) if j==3 else 0) for j in range(3,n)]
    expected=Counter()
    for q,a in enumerate(indep):
        for t in range(n+1):expected[m-q+t]+=a*comb(n,t)
    assert dict(hist)==dict(expected),(n,hist,expected)
    s=min(hist); bases=[v for v in valid if v.bit_count()==s]
    assert len(bases)==(8 if n==4 else n)
    single_edges=[]
    for i,j in combinations(range(len(bases)),2):
        if (bases[i]^bases[j]).bit_count()==2:single_edges.append((i,j))
    assert len(single_edges)==(12 if n==4 else 0)
    print(f'n={n} direct_strong_resolving_sets={len(valid)} all_set_size_histogram={dict(sorted(hist.items()))} strong_dimension={s} minimum_bases={len(bases)} single_exchange_edges={len(single_edges)}')
print('PASS: independently checked all geodesic strong-resolving inequalities.')
