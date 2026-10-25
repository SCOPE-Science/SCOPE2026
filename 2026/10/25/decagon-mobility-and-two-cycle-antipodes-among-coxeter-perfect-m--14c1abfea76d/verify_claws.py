#!/usr/bin/env python3
"""Independent graph model and cycle-by-cycle reconfiguration check for Coxeter 1-factors."""
from collections import Counter,deque
import json

# The Coxeter graph as seven 3-stars with three 7-cycle satellite rings.
# Outer hub indices 0..6; satellites 7..13,14..20,21..27.
neighbor=[set() for _ in range(28)]
def link(a,b):neighbor[a].add(b);neighbor[b].add(a)
for t in range(7):
    for ring,step in enumerate((1,2,4)):
        a=7+7*ring+t
        link(t,a)
        link(a,7+7*ring+(t+step)%7)
assert len([1 for u in range(28) for v in neighbor[u] if u<v])==42
assert set(map(len,neighbor))=={3}
def girth(graph):
    answer=100
    for src in range(len(graph)):
        d={src:0};parent={src:None};Q=deque([src])
        while Q:
            x=Q.popleft()
            for y in graph[x]:
                if y not in d:d[y]=d[x]+1;parent[y]=x;Q.append(y)
                elif parent[x]!=y:answer=min(answer,d[x]+d[y]+1)
    return answer
assert girth(neighbor)==7

# Exhaustive completion with the smallest still-unmatched index; no shared edges table.
solutions=[]
def complete(remaining,paired):
    if not remaining:
        solutions.append(frozenset(paired));return
    a=min(remaining)
    for b in sorted(neighbor[a]&remaining):
        complete(remaining-{a,b},paired+[(a,b)])
complete(set(range(28)),[])
assert len(solutions)==84
solset=set(solutions)
assert len(solset)==84

# Enumerate allowed alternating simple cycles by following matched and unmatched edges,
# not by comparing pairs of solutions. Record successor matchings, deduplicated.
def exchange_neighbors(matching,length):
    partner={a:b for a,b in matching}
    partner.update({b:a for a,b in matching})
    successors=set()
    for start in range(28):
        # Force the first edge unmatched, then alternating matched/unmatched.
        stack=[(start,(start,),frozenset(),True)]
        while stack:
            v,path,used,unmatched=stack.pop()
            for w in (neighbor[v]-{partner[v]} if unmatched else {partner[v]}):
                if w==start:
                    if len(path)==length and not unmatched:
                        eadd=frozenset(tuple(sorted((path[i],path[(i+1)%length]))) for i in range(0,length,2))
                        erem=frozenset(tuple(sorted((path[i],path[(i+1)%length]))) for i in range(1,length,2))
                        m2=(matching-erem)|eadd
                        if len(m2)==14 and m2 in solset:successors.add(m2)
                    continue
                if w in path or len(path)==length:continue
                stack.append((w,path+(w,),used,not unmatched))
    return successors

# Fix a common orientation: in length-even cycle started with unmatched edge,
# the closing edge is matched (last parity position odd).
flip8={m:exchange_neighbors(m,8) for m in solutions}
flip10={m:exchange_neighbors(m,10) for m in solutions}
assert all(len(flip8[m])==1 for m in solutions),Counter(map(len,flip8.values()))
assert all(len(flip10[m])==4 for m in solutions),Counter(map(len,flip10.values()))
assert all(m in flip8[n] for m in solutions for n in flip8[m])
assert all(m in flip10[n] for m in solutions for n in flip10[m])

def cycle_partition(m,n):
    d=m^n
    adjacent={}
    for a,b in d:
        adjacent.setdefault(a,[]).append(b)
        adjacent.setdefault(b,[]).append(a)
    assert all(len(nbrs)==2 for nbrs in adjacent.values())
    todo=set(adjacent);parts=[]
    while todo:
        seed=todo.pop();seen={seed};stack=[seed]
        while stack:
            v=stack.pop()
            for w in adjacent[v]:
                if w not in seen:seen.add(w);stack.append(w)
        todo-=seen;parts.append(len(seen))
    return tuple(sorted(parts))

profiles=[];antipodes=[];eight_distances=[]
for m in solutions:
    d={m:0};q=deque([m])
    while q:
        u=q.popleft()
        for w in flip10[u]:
            if w not in d:d[w]=d[u]+1;q.append(w)
    assert len(d)==84
    p=tuple(Counter(d.values())[k] for k in range(7))
    profiles.append(p)
    assert p==(1,4,12,25,28,13,1)
    fars=[s for s in solutions if d[s]==6]
    assert len(fars)==1
    antipodes.append(cycle_partition(m,fars[0]))
    eight_distances.append(d[next(iter(flip8[m]))])
assert Counter(antipodes)=={(8,16):84}
assert Counter(eight_distances)=={5:84}
part_pairs=[(i,j) for i in range(84) for j in range(i+1,84)
            if cycle_partition(solutions[i],solutions[j])==(8,16)]
assert len(part_pairs)==42
for a,b in part_pairs:
    dist={solutions[a]:0};q=deque([solutions[a]])
    while q:
        x=q.popleft()
        for y in flip10[x]:
            if y not in dist:dist[y]=dist[x]+1;q.append(y)
    assert dist[solutions[b]]==6
res={'graph_order':28,'graph_edges':42,'perfect_matchings':len(solutions),
    'flip8_edges':sum(map(len,flip8.values()))//2,
    'flip10_edges':sum(map(len,flip10.values()))//2,
    'flip8_components':42,'flip10_degree':4,'flip10_connected':True,
    'flip10_distance_distribution':[1,4,12,25,28,13,1],
    'flip10_radius':6,'flip10_diameter':6,
    'unique_antipodal_pairs':42,'antipodal_symmetric_difference_cycles':[8,16],
    'only_8_plus_16_pairs_are_antipodal':True,
    'all_8_cycle_flip_pairs_are_distance_5_under_10_flips':True}
print(json.dumps(res,sort_keys=True,separators=(',',':')))
