#!/usr/bin/env python3
import json, math
from pathlib import Path
from fractions import Fraction
from collections import Counter
from itertools import permutations

DATA=Path(__file__).with_name('graph_atlas_connected_2to7.json')
EXPECTED_COUNTS={2:1,3:2,4:6,5:21,6:112,7:853}
EXPECTED_DIFF_CLASSES={2:0,3:0,4:0,5:0,6:3,7:22}
EXPECTED_UNIQUE_DIFF_CLASSES={2:0,3:0,4:0,5:0,6:0,7:2}
EXPECTED_SIX_TIE_ORBITS=sorted([360,180,360])
EXPECTED_SEVEN_UNIQUE_ORBITS=sorted([2520,2520])
EXPECTED_SEVEN_REPS=[
    [(0,3),(1,3),(1,4),(2,4),(2,5),(2,6)],
    [(0,4),(1,2),(1,3),(2,5),(2,6),(3,4),(5,6)],
]

def adj_from_edges(n,edges):
    a=[set() for _ in range(n)]
    for u,v in edges:
        a[u].add(v);a[v].add(u)
    return a

def dist_bfs(adj,s):
    n=len(adj); d=[None]*n; d[s]=0; q=[s]; qi=0
    while qi<len(q):
        v=q[qi]; qi+=1
        for w in adj[v]:
            if d[w] is None:
                d[w]=d[v]+1; q.append(w)
    assert all(x is not None for x in d)
    return d

def all_dist_bfs(adj):
    return [dist_bfs(adj,s) for s in range(len(adj))]

def all_dist_floyd(adj):
    n=len(adj); INF=99
    d=[[INF]*n for _ in range(n)]
    for i in range(n): d[i][i]=0
    for i in range(n):
        for j in adj[i]: d[i][j]=1
    for k in range(n):
        for i in range(n):
            dik=d[i][k]
            for j in range(n):
                z=dik+d[k][j]
                if z<d[i][j]: d[i][j]=z
    return d

def centers(D):
    n=len(D)
    far=[sum(D[v][u] for u in range(n) if u!=v) for v in range(n)]
    harm=[sum((Fraction(1,D[v][u]) for u in range(n) if u!=v),Fraction(0,1)) for v in range(n)]
    mf=min(far); mh=max(harm)
    C=tuple(v for v,x in enumerate(far) if x==mf)
    H=tuple(v for v,x in enumerate(harm) if x==mh)
    return far,harm,C,H

def aut_order(n,edges):
    E={tuple(sorted(e)) for e in edges}; c=0
    for p in permutations(range(n)):
        Ep={tuple(sorted((p[u],p[v]))) for u,v in E}
        if Ep==E: c+=1
    return c

rows=json.loads(DATA.read_text(encoding='utf-8'))
counts=Counter(); diffs=Counter(); udiffs=Counter()
six=[]; seven=[]
for r in rows:
    n=r['n']; edges=[tuple(e) for e in r['edges']]; counts[n]+=1
    adj=adj_from_edges(n,edges)
    D1=all_dist_bfs(adj); D2=all_dist_floyd(adj)
    assert D1==D2
    far,harm,C,H=centers(D1)
    if C!=H:
        diffs[n]+=1
        if n==6: six.append((edges,far,harm,C,H))
    if len(C)==len(H)==1 and C!=H:
        udiffs[n]+=1
        if n==7: seven.append((edges,far,harm,C,H))
assert dict(counts)==EXPECTED_COUNTS,counts
for n in EXPECTED_COUNTS:
    assert diffs[n]==EXPECTED_DIFF_CLASSES[n], (n,diffs[n])
    assert udiffs[n]==EXPECTED_UNIQUE_DIFF_CLASSES[n], (n,udiffs[n])

six_orbits=[]
for edges,far,harm,C,H in six:
    a=aut_order(6,edges); six_orbits.append(math.factorial(6)//a)
assert sorted(six_orbits)==EXPECTED_SIX_TIE_ORBITS
assert sum(six_orbits)==900

seven_orbits=[]; rep_edges=[]
profiles=[]
for edges,far,harm,C,H in seven:
    a=aut_order(7,edges); seven_orbits.append(math.factorial(7)//a); rep_edges.append(edges)
    c=C[0]; h=H[0]
    Dc=all_dist_bfs(adj_from_edges(7,edges))[c]
    Dh=all_dist_bfs(adj_from_edges(7,edges))[h]
    pc=tuple(sorted(Dc[u] for u in range(7) if u!=c))
    ph=tuple(sorted(Dh[u] for u in range(7) if u!=h))
    profiles.append((pc,ph,far[c],harm[c],far[h],harm[h]))
assert sorted(seven_orbits)==EXPECTED_SEVEN_UNIQUE_ORBITS
assert sum(seven_orbits)==5040
assert sorted(rep_edges)==sorted(EXPECTED_SEVEN_REPS)
expected_profile=((1,1,2,2,2,3),(1,1,1,2,3,4),11,Fraction(23,6),12,Fraction(49,12))
assert all(p==expected_profile for p in profiles), profiles

print('VERIFY_OK')
print('connected_unlabeled',dict(counts))
print('set_disagreement_classes',dict(diffs))
print('unique_unique_disagreement_classes',dict(udiffs))
print('six_vertex_tie_orbits',six_orbits,'total',sum(six_orbits))
print('seven_vertex_unique_orbits',seven_orbits,'total',sum(seven_orbits))
print('seven_representatives',rep_edges)
print('leader_profiles',profiles)
