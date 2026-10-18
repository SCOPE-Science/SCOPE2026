#!/usr/bin/env python3
"""Independent exhaustive middle-levels representation of the Desargues Roman graph.

Only Python standard library; validates all state/transition certificate entries.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
D=json.loads((ROOT/'data'/'states_edges.json').read_text(encoding='utf-8'))
labels=list(combinations(range(5),2))+list(combinations(range(5),3))
assert len(labels)==20
N=[set() for _ in labels]
for i in range(10):
    for j in range(10,20):
        if set(labels[i]).issubset(labels[j]):
            N[i].add(j); N[j].add(i)
assert all(len(a)==3 for a in N)
# This explicit bijection can be independently checked using the 30 edge equations.
# Its target is u0,...,u9,v0,...,v9 of GP(10,3).
map_to_gp=[0,2,13,19,11,17,8,4,15,6,1,10,9,3,12,16,14,18,7,5]
assert sorted(map_to_gp)==list(range(20))
def gp_edge(a,b):
    if a>=10 and b>=10:
        return (a-b)%10 in (3,7)
    if a<10 and b<10:
        return (a-b)%10 in (1,9)
    return (a-b)%10==10 or (b-a)%10==0
for i in range(20):
    for j in range(i):
        assert (j in N[i])==gp_edge(map_to_gp[i],map_to_gp[j]), (i,j)

# Independent enumeration: a minimum label assignment is fully specified by
# the vertices carrying a 2, because every vertex outside their closed
# neighborhood must carry a 1. There can be no redundant 1 in a minimum.
# At 12 units, seven 2-labels are impossible, so k=0..6 is exhaustive
# both for proving the lower bound and for finding all minima.
C=[{i}|N[i] for i in range(20)]
best=21
states=[]
for k in range(7):
    for twos in combinations(range(20),k):
        protected=set(twos)
        for v in twos:protected.update(N[v])
        ones=set(range(20))-protected
        weight=2*k+len(ones)
        if weight<best:
            best=weight;states=[]
        if weight==best:
            f=['0']*20
            for v in twos:f[v]='2'
            for v in ones:f[v]='1'
            states.append(tuple(f))
assert best==12 and len(states)==340
assert len(set(states))==len(states)

def reindex(f):
    t=['']*20
    for a,b in enumerate(map_to_gp):t[b]=f[a]
    return ''.join(t)
S=[reindex(f) for f in states]
assert sorted(S)==D['states']
Ssorted=D['states']
J={f:i for i,f in enumerate(Ssorted)}
# Compare all pairs rather than generate moves from individual states.
# This is independent of the move-generating loop of verify_cyclic.py.
found=[]
for a in range(len(states)):
    f=states[a]
    for b in range(a+1,len(states)):
        g=states[b]
        diff=[i for i in range(20) if f[i]!=g[i]]
        if len(diff)!=2: continue
        i,j=diff
        old=(f[i],f[j]); new=(g[i],g[j]); typ=None
        if set(old)=={'0','2'} and set(new)=={'0','2'} and old==tuple(reversed(new)):
            typ='P1'
        elif set(old)=={'1','2'} and set(new)=={'1','2'} and old==tuple(reversed(new)):
            typ='P2'
        elif i in N[j] and ((old==('1','1') and set(new)=={'0','2'}) or (new==('1','1') and set(old)=={'0','2'})):
            typ='P3'
        if typ:
            lo,hi=sorted((J[S[a]],J[S[b]]))
            found.append((lo,hi,typ))
assert len(found)==len(set(found))
assert sorted(found)==sorted(tuple(z) for z in D['edges'])
nb=[set() for _ in states]
for a,b,t in found:nb[a].add(b);nb[b].add(a)
seen=set();comps=[]
for start in range(len(states)):
    if start in seen:continue
    todo=[start];seen.add(start)
    for v in todo:
        for w in nb[v]:
            if w not in seen:seen.add(w);todo.append(w)
    comps.append(todo)
assert Counter(map(len,comps))==Counter({1:100,48:5})

def dist(start):
    d={start:0};todo=[start]
    for v in todo:
        for w in nb[v]:
            if w not in d:d[w]=d[v]+1;todo.append(w)
    return d

ecc=Counter();deg=Counter();tiers=Counter();all_types=Counter(z[2] for z in found)
for comp in comps:
    if len(comp)!=48:continue
    for v in comp:
        dd=dist(v)
        assert len(dd)==48
        ecc[max(dd.values())]+=1
        deg[len(nb[v])]+=1
        tiers[(Ssorted[v].count('1'),len(nb[v]),max(dd.values()))]+=1
assert ecc==Counter({6:30,7:180,8:30})
assert deg==Counter({4:210,8:30})
assert all_types==Counter({'P1':180,'P3':360})
assert len(found)==540
print('VERIFY_OK')
print('incidence_graph','20 vertices 30 edges, explicit isomorphism to GP(10,3) checked')
print('weight',best,'states',len(S),'types',sorted(Counter((f.count('1'),f.count('2')) for f in S).items()))
print('all_edges',len(found),'edge_types',sorted(all_types.items()))
print('component_sizes',sorted(Counter(map(len,comps)).items()))
print('mobile_ecc_histogram',sorted(ecc.items()))
print('mobile_degrees',sorted(deg.items()))
print('mobile_profile_degree_ecc',sorted(tiers.items()))
print('state_and_transition_certificate','EXACT_MATCH')
