#!/usr/bin/env python3
"""Exact optimal Roman-domination and P1/P2/P3 exchange census of GP(10,3).

Uses only Python's standard library. Run from any directory.
The optional --create-certificate flag writes the complete canonical census.
"""
from __future__ import annotations
import collections
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
CERT = ROOT / 'data' / 'states_edges.json'
N = 20
WHOLE = (1 << N) - 1
adj = [set() for _ in range(N)]
for i in range(10):
    for u,v in [(i,(i+1)%10),(i,10+i),(10+i,10+(i+3)%10)]:
        adj[u].add(v); adj[v].add(u)
assert sum(map(len, adj)) == 60 and all(len(x)==3 for x in adj)
closed = [(1 << i) | sum(1 << j for j in adj[i]) for i in range(N)]

# F[T] = N[T], computed independently of any published gamma_R value.
coverage = [0] * (1 << N)
minw = 21
optimal_masks = []
for t in range(1 << N):
    if t:
        low = t & -t
        coverage[t] = coverage[t ^ low] | closed[low.bit_length() - 1]
    w = 2*t.bit_count() + (WHOLE ^ coverage[t]).bit_count()
    if w < minw:
        minw = w
        optimal_masks = []
    if w == minw:
        optimal_masks.append(t)

states = []
for t in optimal_masks:
    forced_ones = WHOLE ^ coverage[t]
    s = ''.join('2' if (t >> j) & 1 else '1' if (forced_ones >> j) & 1 else '0' for j in range(N))
    states.append(s)
states.sort()
assert len(states) == len(set(states))
position = {s: i for i,s in enumerate(states)}
profiles = collections.Counter((s.count('1'),s.count('2')) for s in states)

edges = set()
nonadjacent_P1 = []
for i,s in enumerate(states):
    for u in range(N):
        for v in range(N):
            if v == u:
                continue
            typ = None
            if s[u]=='2' and s[v]=='0':
                typ='P1'
                t = list(s);t[u]='0';t[v]='2'
            elif s[u]=='2' and s[v]=='1':
                typ='P2'
                t = list(s);t[u]='1';t[v]='2'
            elif s[u]=='1' and s[v]=='1' and v in adj[u]:
                typ='P3'
                t = list(s);t[u]='2';t[v]='0'
            else:
                continue
            j = position.get(''.join(t))
            if j is None:
                continue
            a,b = sorted((i,j))
            edges.add((a,b,typ))
            if typ == 'P1' and v not in adj[u]:
                nonadjacent_P1.append((i,j,u,v))
assert not nonadjacent_P1
assert len({(a,b) for a,b,_ in edges}) == len(edges)
edge_list=sorted((a,b,typ) for a,b,typ in edges)
links=[[] for _ in states]
for a,b,t in edge_list:
    links[a].append(b);links[b].append(a)

def bfs(start):
    dist={start:0}
    q=[start]
    for x in q:
        for y in links[x]:
            if y not in dist:
                dist[y]=dist[x]+1;q.append(y)
    return dist

components=[];seen=set()
for start in range(len(states)):
    if start in seen:continue
    block=sorted(bfs(start))
    seen.update(block)
    components.append(block)
mobile=[c for c in components if len(c)>1]
assert len(mobile)==5 and all(len(c)==48 for c in mobile)
assert len([c for c in components if len(c)==1])==100
center_hist=collections.Counter()
component_stats=[]
for block in mobile:
    ecc={i:max(bfs(i).values()) for i in block}
    center_hist.update(ecc.values())
    type_edges=collections.Counter(t for a,b,t in edge_list if a in block)
    component_stats.append((len(block),sum(type_edges.values()), min(ecc.values()), max(ecc.values()),
                            sorted(collections.Counter(ecc.values()).items()),sorted(type_edges.items())))
assert len(set(map(str,component_stats)))==1
# Cyclic rotation is an automorphism acting as a single 5-cycle on mobile components.
def rotate(s):
    return s[9]+s[:9]+s[19]+s[10:19]
component_of={v:k for k,c in enumerate(mobile) for v in c}
cycle={k:component_of[position[rotate(states[c[0]])]] for k,c in enumerate(mobile)}
assert len(set(cycle.values()))==5
k=0;orbit=[]
for _ in range(5):orbit.append(k);k=cycle[k]
assert k==0 and len(set(orbit))==5
assert all(sorted(position[rotate(states[i])] for i in c)==mobile[cycle[k]] for k,c in enumerate(mobile))

data={'object':'Roman P1/P2/P3 reconfiguration of GP(10,3)',
      'vertex_order':'u0,...,u9,v0,...,v9',
      'minimum_weight':minw,
      'states':states,
      'edges':[[a,b,t] for a,b,t in edge_list]}
canonical=json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n'
fingerprint=hashlib.sha256(canonical.encode('utf-8')).hexdigest()
if '--create-certificate' in sys.argv:
    CERT.write_text(canonical,encoding='utf-8')
else:
    stored=CERT.read_text(encoding='utf-8')
    assert stored==canonical, 'Package certificate disagrees with independent reconstruction'
print('VERIFY_OK')
print('gamma_R',minw,'minimum_functions',len(states),'profiles',sorted(profiles.items()))
print('reconfiguration_edges',len(edge_list),'move_types',sorted(collections.Counter(t for _,_,t in edge_list).items()))
print('components',sorted(collections.Counter(map(len,components)).items()))
print('frozen_profiles',sorted(collections.Counter((states[c[0]].count('1'),states[c[0]].count('2')) for c in components if len(c)==1).items()))
print('mobile_per_component',component_stats[0])
print('mobile_eccentricity_histogram_all',sorted(center_hist.items()))
print('rotation_component_cycle',orbit)
print('P1_nonadjacent_pairs',len(nonadjacent_P1))
print('certificate_sha256',fingerprint)
