#!/usr/bin/env python3
"""Independent subset-inclusion model and exhaustive S5 orbit and parity checks."""
from itertools import combinations, permutations
from collections import Counter, deque

T=list(combinations(range(5),2))
U=list(combinations(range(5),3))
allowed=[[j for j,u in enumerate(U) if set(t)<=set(u)] for t in T]
assert len(T)==len(U)==10 and all(len(row)==3 for row in allowed)

M=[]
def complete(i,used,choices):
    if i==10:
        M.append(tuple(choices))
        return
    for j in allowed[i]:
        if j not in used:
            complete(i+1,used|{j},choices+[j])
complete(0,set(),[])
assert len(M)==len(set(M))==60
# DP permanent is a third check of total matching count.
dp={0:1}
for row in allowed:
    nxt={}
    for mask,count in dp.items():
        for j in row:
            if not mask>>j & 1:
                nxt[mask | (1<<j)]=nxt.get(mask | (1<<j),0)+count
    dp=nxt
assert dp == {(1<<10)-1:60}

# Different choices at 3 or 4 lines give a single alternating 6-/8-cycle:
# A 4-cycle would require two distinct 2-subsets in two common 3-subsets,
# impossible since two distinct 2-subsets have at most one 3-superset.
E6=set();E8=set()
for a,b in combinations(range(len(M)),2):
    d=sum(M[a][i]!=M[b][i] for i in range(10))
    if d==3:E6.add((a,b))
    if d==4:E8.add((a,b))
assert len(E6)==120 and len(E8)==60
# Compare exact labelled states and all transitions to the supplied certificate.
from json import loads
from pathlib import Path
certificate_path=Path(__file__).resolve().with_name('state_transition_certificate.json')
if certificate_path.is_file():
    data=loads(certificate_path.read_text(encoding='utf-8'))
    assert [list(x) for x in M]==data['states']
    assert {tuple(x) for x in data['six_cycle_edges']}==E6
    assert {tuple(x) for x in data['eight_cycle_edges']}==E8

def adjacency(edges):
    result=[set() for _ in M]
    for a,b in edges:result[a].add(b);result[b].add(a)
    return result
N6=adjacency(E6);N8=adjacency(E8);N=adjacency(E6|E8)
assert Counter(map(len,N6))=={0:6,4:30,5:24}
assert Counter(map(len,N8))=={0:24,2:30,10:6}
assert all({len(N6[i]),len(N6[j])}=={4,5} for i,j in E6)
hubs={i for i in range(60) if not N6[i]}
assert hubs=={i for i in range(60) if len(N8[i])==10}
assert all(len(N8[i]&N8[j])==2 for i,j in combinations(sorted(hubs),2))
assert all(len(N8[i]&hubs)==2 for i in range(60) if len(N6[i])==4)
assert all(not N8[i] for i in range(60) if len(N6[i])==5)

# Sign of the point-line permutation: changing three assignments gives an
# even three-cycle; a four-assignment change gives an odd four-cycle.
def parity(p):
    return sum(p[i]>p[j] for i in range(10) for j in range(i+1,10))%2
sign=[parity(m) for m in M]
assert Counter((sign[i],len(N6[i])) for i in range(60)) == {
    (0,0):6,(1,4):30,(1,5):24}
assert all(sign[i]==sign[j] for i,j in E6)
assert all(sign[i]!=sign[j] for i,j in E8)

# Action of all 120 permutations of the five symbols on matchings.
TI={t:i for i,t in enumerate(T)};UI={u:i for i,u in enumerate(U)}
actions=[]
for p in permutations(range(5)):
    a=[TI[tuple(sorted(p[x] for x in t))] for t in T]
    b=[UI[tuple(sorted(p[x] for x in u))] for u in U]
    actions.append((a,b))
Mset=set(M);remaining=set(M);orbit_stats=[]
while remaining:
    representative=min(remaining)
    orbit=set()
    for a,b in actions:
        transformed=[-1]*10
        for i,j in enumerate(representative):transformed[a[i]]=b[j]
        orbit.add(tuple(transformed))
    assert orbit<=Mset
    sizes={len(N6[M.index(x)]) for x in orbit}
    assert len(sizes)==1
    orbit_stats.append((len(orbit),next(iter(sizes))))
    remaining-=orbit
assert set(orbit_stats)=={(6,0),(30,4),(24,5)}

# Complete shortest-path profiles, not a random collection of root tests.
profiles6=Counter()
for i in range(60):
    dist={i:0};q=deque([i])
    while q:
        a=q.popleft()
        for b in N6[a]:
            if b not in dist:dist[b]=dist[a]+1;q.append(b)
    layers=tuple(Counter(dist.values())[k] for k in range(max(dist.values())+1))
    profiles6[(len(N6[i]),len(dist),layers)]+=1
assert profiles6=={
    (0,1,(1,)):6,
    (4,54,(1,4,12,16,16,4,1)):30,
    (5,54,(1,5,10,20,12,5,1)):24,
}
profiles=Counter()
for i in range(60):
    dist={i:0};q=deque([i])
    while q:
        a=q.popleft()
        for b in N[a]:
            if b not in dist:dist[b]=dist[a]+1;q.append(b)
    assert len(dist)==60
    layers=tuple(Counter(dist.values())[k] for k in range(5))
    profiles[(len(N6[i]),layers)]+=1
assert profiles=={
    (0,(1,10,25,20,4)):6,
    (4,(1,6,21,24,8)):30,
    (5,(1,5,15,25,14)):24,
}
print('model=2-subset_vs_3-subset_inclusion_of_five_points')
print('matching_permanent=60;matching_enumeration=60')
print('six_flips=120;eight_flips=60;all_flips_leq8=180')
print('S5_orbits=(6_frozen,30_degree4,24_degree5)')
print('matching_sign_6flip_invariant=TRUE;eight_flip_sign_reversing=TRUE')
print('combined_graph_all60_connected;eccentricity4_for_all')
print('VERIFY_OK')
