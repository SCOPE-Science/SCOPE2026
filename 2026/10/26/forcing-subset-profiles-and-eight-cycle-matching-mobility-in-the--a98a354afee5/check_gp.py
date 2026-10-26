#!/usr/bin/env python3
"""Exact forcing-subset and alternating-eight-switch enumeration for the dodecahedral graph.
Python 3 standard library only. All perfect matchings and all their 2^10 subsets are examined.
"""
from itertools import combinations
from collections import Counter,defaultdict,deque
import json
N=20
E=sorted({tuple(sorted(x)) for i in range(10) for x in ((i,(i+1)%10),(i,i+10),(i+10,10+(i+2)%10))})
assert len(E)==30
adj=[[] for _ in range(N)]
for e,(u,v) in enumerate(E):adj[u].append((v,e));adj[v].append((u,e))
M=[]
def walk(free, m):
    if not free:
        M.append(tuple(sorted(m)));return
    u=(free & -free).bit_length()-1
    for v,e in adj[u]:
        if (free>>v)&1:walk(free & ~(1<<u) & ~(1<<v),m+[e])
walk((1<<N)-1,[])
M=sorted(set(M));assert len(M)==36
poly=[]
for matching in M:
    counts=[]
    for k in range(11):
        count=0
        for sub in combinations(matching,k):
            count+=sum(all(x in other for x in sub) for other in M)==1
        counts.append(count)
    poly.append(tuple(counts))
profiles=Counter(poly)
F={24:(0,0,0,24,122,216,204,120,45,10,1),20:(0,0,0,20,110,202,200,120,45,10,1)}
assert profiles==Counter({F[24]:30,F[20]:6})
G=[set() for _ in M]
for i,j in combinations(range(len(M)),2):
    if len(set(M[i])^set(M[j]))==8:G[i].add(j);G[j].add(i)
assert sum(map(len,G))==240
seen=set();components=[]
for i in range(36):
    if i in seen:continue
    q=[i];seen.add(i)
    for x in q:
        for y in G[x]:
            if y not in seen:seen.add(y);q.append(y)
    components.append(len(q))
assert components==[36]
ecc=[]
for s in range(36):
    D={s:0};q=deque([s])
    while q:
        u=q.popleft()
        for v in G[u]:
            if v not in D:D[v]=D[u]+1;q.append(v)
    assert len(D)==36
    ecc.append(max(D.values()))
assert min(ecc)==max(ecc)==3
out={"representation":"GP(10,2)","graph_vertices":20,"graph_edges":len(E),"perfect_matchings":len(M),"forcing_polynomial_orbits":sorted([{"multiplicity":v,"coefficients":list(k)} for k,v in profiles.items()],key=lambda d:d['multiplicity']),"flip8_vertices":36,"flip8_edges":sum(map(len,G))//2,"flip8_components":components,"flip8_radius":min(ecc),"flip8_diameter":max(ecc),"flip8_degree_profile":dict(sorted(Counter(map(len,G)).items())),"flip8_orbit_cross_degree":{str(c):dict(Counter(sum(poly[j][3]!=c for j in G[i]) for i in range(36) if poly[i][3]==c)) for c in (20,24)}}
print(json.dumps(out,sort_keys=True))
