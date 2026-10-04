#!/usr/bin/env python3
import json,itertools,sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
cert=json.loads((HERE/'certificate.json').read_text(encoding='utf-8'))
V=cert['vertices']; idx={v:i for i,v in enumerate(V)}
parts=[]
for j,P in enumerate(cert['parts']):
    for v in P: parts.append((idx[v],j))
part=[None]*len(V)
for i,j in parts: part[i]=j
E=[(u,v) for u in range(len(V)) for v in range(u+1,len(V)) if part[u]!=part[v]]
prefs=[cert['preferences_best_to_worst'][v] for v in V]
pos=[{c:i for i,c in enumerate(p)} for p in prefs]

def proper(phi):
    return all(phi[u]!=phi[v] for u,v in E)

def envy_arcs(phi):
    A=set()
    for u,v in E:
        if pos[u][phi[v]] < pos[u][phi[u]]: A.add((u,v))
        if pos[v][phi[u]] < pos[v][phi[v]]: A.add((v,u))
    return A

def acyclic(A):
    adj=[[] for _ in V]; indeg=[0]*len(V)
    for u,v in A: adj[u].append(v); indeg[v]+=1
    q=[i for i,d in enumerate(indeg) if d==0]; seen=0
    while q:
        u=q.pop(); seen+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return seen==len(V)

# Exhaust every map V -> {1,...,5}; this includes colorings using fewer than five colors.
proper_list=[]
stable=[]
for phi in itertools.product(cert['colors'], repeat=len(V)):
    if not proper(phi): continue
    proper_list.append(phi)
    A=envy_arcs(phi)
    if acyclic(A): stable.append(phi)
assert len(proper_list)==2940, len(proper_list)
assert not stable, stable[:1]
assert cert['proper_coloring_count']==len(proper_list)
assert cert['stable_coloring_count']==0

# Check that the certificate has exactly one entry for every proper coloring and every displayed cycle is blocking.
rows=cert['blocking_cycle_witnesses']
assert len(rows)==len(proper_list)
rowmap={tuple(r['coloring']):r['blocking_cycle'] for r in rows}
assert len(rowmap)==len(rows)
assert set(rowmap)==set(proper_list)
for phi,cycle_names in rowmap.items():
    cyc=[idx[x] for x in cycle_names]
    assert len(cyc)>=3 and cyc[0]==cyc[-1]
    assert len(set(cyc[:-1]))==len(cyc)-1
    A=envy_arcs(phi)
    for u,v in zip(cyc,cyc[1:]): assert (u,v) in A

# Upper-bound orientation: C -> B -> A.  It is acyclic, and its reachable-set sizes are 1, 4, or 6.
adj=[[] for _ in V]
for u,v in E:
    if part[u]>part[v]: adj[u].append(v)
    else: adj[v].append(u)
reach=[]
for s in range(len(V)):
    seen={s}; stack=[s]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen: seen.add(v); stack.append(v)
    reach.append(len(seen))
assert max(reach)==6, reach
print('ALL CHECKS PASSED; proper_5_colorings=2940; stable_5_colorings=0; blocking_cycles=2940; orientation_max_reach=6')
