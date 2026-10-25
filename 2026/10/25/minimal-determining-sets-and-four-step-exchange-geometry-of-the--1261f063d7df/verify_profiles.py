#!/usr/bin/env python3
"""Coordinate-incidence certificate, using no automorphism enumeration."""
from itertools import combinations
from collections import Counter, deque
import json

N=16
D=(1,2,4,8,15)
# Each vector has a unique representation by at most two of five directions.
REP={0:0}
for r in (1,2):
    for ids in combinations(range(5),r):
        vec=0
        for i in ids: vec ^= D[i]
        assert vec not in REP
        REP[vec]=sum(1<<i for i in ids)
assert len(REP)==N

def members(mask):
    return tuple(i for i in range(N) if mask & (1<<i))

def base(mask):
    vertices=members(mask)
    if not vertices:return False
    x=vertices[0]
    # Five coordinate columns of the incidence matrix of the other vertices.
    signatures=[]
    for coord in range(5):
        signatures.append(tuple(bool(REP[x^v]&(1<<coord)) for v in vertices[1:]))
    return len(set(signatures)) == 5

base_table=[base(m) for m in range(1<<N)]
minimal=set()
for mask,b in enumerate(base_table):
    if b and all(not base_table[mask^(1<<x)] for x in members(mask)):
        minimal.add(mask)
count=Counter(m.bit_count() for m in minimal)
assert dict(count)=={4:560,5:192}
B4={m for m in minimal if m.bit_count()==4}
B5={m for m in minimal if m.bit_count()==5}

def induced_degree_seq(mask):
    xs=members(mask)
    return tuple(sorted(sum((x^y) in D for y in xs if x!=y) for x in xs))

assert Counter(induced_degree_seq(m) for m in B4)=={(0,0,0,0):80,(0,0,1,1):480}
assert all((lambda v: v[0]^v[1]^v[2]^v[3] != 0)(members(m)) for m in B4 if induced_degree_seq(m)==(0,0,0,0))
assert all(induced_degree_seq(m)==(2,2,2,2,2) for m in B5)
# Verify the converse over every candidate, not only the accepted ones.
for c in combinations(range(N),4):
    mask=sum(1<<x for x in c)
    degrees=induced_degree_seq(mask)
    expected=(degrees==(0,0,1,1) or (degrees==(0,0,0,0) and c[0]^c[1]^c[2]^c[3]!=0))
    assert (mask in B4)==expected
for c in combinations(range(N),5):
    mask=sum(1<<x for x in c)
    assert (mask in B5)==(induced_degree_seq(mask)==(2,2,2,2,2))

B=set(B4)
# Independent adjacency implementation: enumerate unordered pairs and test intersection size 3.
A={u:[] for u in B}
ordered=sorted(B)
for ii,u in enumerate(ordered):
    for v in ordered[ii+1:]:
        if (u&v).bit_count()==3:
            A[u].append(v);A[v].append(u)
assert sum(map(len,A.values()))==11840
assert Counter(map(len,A.values()))=={20:480,28:80}
seen=set()
components=[]
for st in ordered:
    if st in seen:continue
    q=[st];seen.add(st)
    for x in q:
        for y in A[x]:
            if y not in seen:seen.add(y);q.append(y)
    components.append(len(q))
assert components==[560]
E=Counter()
layers={}
for st in ordered:
    distances={st:0};q=deque([st])
    while q:
        x=q.popleft()
        for y in A[x]:
            if y not in distances:
                distances[y]=distances[x]+1;q.append(y)
    e=max(distances.values());E[e]+=1
    cls=sum(induced_degree_seq(st))//2
    v=tuple(Counter(distances.values())[i] for i in range(e+1))
    if cls in layers:assert layers[cls]==v
    else:layers[cls]=v
assert E=={4:560}
assert layers=={0:(1,28,126,220,185),1:(1,20,126,244,169)}
print(json.dumps({'method':'five_direction_incidence_signatures','subsets_tested':65536,
 'minimum_determining_number':4,'inclusion_minimal_size_counts':dict(sorted(count.items())),
 'minimum_set_types':{'one_edge':480,'independent_nonzero_xor':80},
 'minimal_five_sets_are_exactly_induced_five_cycles':True,
 'minimum_exchange_vertices':len(B),'minimum_exchange_edges':sum(map(len,A.values()))//2,
 'exchange_degree_counts':dict(sorted(Counter(map(len,A.values())).items())),
 'exchange_components':components,'eccentricity_distribution':dict(E),
 'distance_layers_by_induced_edges':{str(k):list(v) for k,v in sorted(layers.items())}},sort_keys=True))
