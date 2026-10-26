#!/usr/bin/env python3
"""Exhaustive, label-sensitive exact-cover verification of order-nine Steiner systems.

Use: python3 verify_exact_cover.py
Only Python's standard library is needed.
"""
from collections import Counter, deque, defaultdict
from itertools import combinations
from hashlib import sha256

N=9
pairs=list(combinations(range(N),2))
triples=list(combinations(range(N),3))
pidx={p:i for i,p in enumerate(pairs)}
index={t:i for i,t in enumerate(triples)}
cover=[]
choices=[[] for _ in pairs]
for j,t in enumerate(triples):
    pids=[pidx[p] for p in combinations(t,2)]
    cover.append(sum(1<<k for k in pids))
    for k in pids:choices[k].append(j)
complete=(1<<len(pairs))-1
systems=[]
node_count=0

def search(used,chosen):
    global node_count
    node_count+=1
    if used==complete:
        assert len(chosen)==12
        systems.append(tuple(sorted(chosen)))
        return
    k=(((~used)&complete)&-((~used)&complete)).bit_length()-1
    for t in choices[k]:
        if (used&cover[t])==0:
            search(used|cover[t],chosen+[t])

search(0,[])
systems=sorted(systems)
assert len(systems)==len(set(systems))==840
masks=[sum(1<<t for t in sys) for sys in systems]
for s in systems:
    assert len(s)==12
    assert sum(cover[t] for t in s)==complete

adj=[[] for _ in systems]
common_pairs=Counter()
for i in range(len(systems)):
    for j in range(i+1,len(systems)):
        common=(masks[i]&masks[j]).bit_count()
        common_pairs[common]+=1
        if common==6:
            adj[i].append(j)
            adj[j].append(i)
assert sorted(common_pairs)==[0,1,2,3,4,6]
assert [len(a) for a in adj]==[36]*840
expected={12:0,6:1,4:2,3:2,2:2,1:3,0:3}
root_layers=None
for root in range(len(systems)):
    dist=[-1]*len(systems)
    dist[root]=0
    queue=deque([root])
    while queue:
        a=queue.popleft()
        for b in adj[a]:
            if dist[b]==-1:
                dist[b]=dist[a]+1
                queue.append(b)
    assert max(dist)==3 and min(dist)==0
    layer=tuple(Counter(dist)[d] for d in range(4))
    assert layer==(1,36,395,408)
    if root_layers is None:root_layers=layer
    for i in range(len(systems)):
        c=(masks[root]&masks[i]).bit_count()
        assert dist[i]==expected[c],(root,i,c,dist[i])
print('EXACT_COVER_OK')
print('points=9 triples=84 pair_constraints=36')
print('backtracking_nodes=',node_count,sep='')
print('labeled_systems=',len(systems),sep='')
print('possible_pair_intersections=',sorted(common_pairs),sep='')
print('unordered_pair_intersection_counts=',sorted(common_pairs.items()),sep='')
print('minimum_trade_volume=6')
print('degree=36 edges=',sum(map(len,adj))//2,sep='')
print('distance_layers=',root_layers,sep='')
print('all_840_roots_and_all_705600_ordered_pairs_checked=True')
print('diameter=3 radius=3')
