#!/usr/bin/env python3
"""Standalone exhaustive permutation/Gray-code checks; Python stdlib only."""
import itertools
from collections import Counter, deque
from pathlib import Path

def states(n):
    return [p for p in itertools.permutations(range(n))
            if all(p[i] not in (i, (i+1)%n) for i in range(n))]

def neighbors(p):
    n = len(p)
    for i in range(n):
        for j in range(i+1,n):
            if p[j] not in (i,(i+1)%n) and p[i] not in (j,(j+1)%n):
                q=list(p);q[i],q[j]=q[j],q[i]
                yield tuple(q)

def cycles(n):
    ps=states(n);loc={p:i for i,p in enumerate(ps)}
    adj=[sorted(loc[q] for q in neighbors(p)) for p in ps]
    assert all(i in adj[j] for i,v in enumerate(adj) for j in v)
    seen=set();sizes=[];ecc=Counter()
    for i in range(len(ps)):
        if i not in seen:
            pool={i};queue=deque([i])
            while queue:
                for j in adj[queue.popleft()]:
                    if j not in pool:pool.add(j);queue.append(j)
            sizes.append(len(pool));seen|=pool
        queue=deque([i]);distance={i:0}
        while queue:
            u=queue.popleft()
            for v in adj[u]:
                if v not in distance:distance[v]=distance[u]+1;queue.append(v)
        ecc[(len(distance),max(distance.values()))]+=1
    return ps,adj,Counter(sizes),ecc

for n,num,edges,cc in [(3,1,0,{1:1}),(4,2,0,{1:2}), (5,13,15,{1:2,11:1}), (6,80,207,{80:1})]:
    ps,adj,sizes,ecc=cycles(n)
    assert len(ps)==num and sum(map(len,adj))//2==edges and dict(sizes)==cc
    if n==6:
        assert ecc==Counter({(80,5):48,(80,6):32})
        inds=[int(t) for t in Path(__file__).with_name('hamiltonian_cycle.txt').read_text().strip().split(',')]
        assert len(inds)==len(ps)==len(set(inds)) and set(inds)==set(range(80))
        assert all(inds[(k+1)%80] in adj[inds[k]] for k in range(80))
        assert Counter(sum(ps[i][a]>ps[i][b] for a in range(n) for b in range(a+1,n))%2 for i in inds)=={0:40,1:40}
    print(f'PERMUTATION_GRAPH_OK n={n} vertices={num} edges={edges} components={dict(sizes)} eccentricities={dict(ecc)}')
print('CYCLIC_MENAGE_GRAY_CODE_OK')
