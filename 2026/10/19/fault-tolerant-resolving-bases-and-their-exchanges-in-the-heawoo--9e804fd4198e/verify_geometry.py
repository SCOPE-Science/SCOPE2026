#!/usr/bin/env python3
"""Independent incidence-only classification and adjacency certificate checker."""
from itertools import combinations
from collections import Counter, deque
import json

points=set(range(7)); lines=set(range(7))
L=[frozenset(((i+j)%7) for j in (0,1,3)) for i in range(7)]
assert len(set(L))==7 and all(sum(a in x and b in x for x in L)==1 for a,b in combinations(points,2))
assert all(sum(p in L[j] and p in L[k] for p in points)==1 for j,k in combinations(lines,2))

def satisfies(A,B):
    for p,q in combinations(range(7),2):
        if (p in A)+(q in A)+sum(((p in L[l])!=(q in L[l])) for l in B)<2:return False
    for j,k in combinations(range(7),2):
        if (j in B)+(k in B)+sum(((p in L[j])!=(p in L[k])) for p in A)<2:return False
    return True

# Generate the predicted classification from Fano geometry, not from distance BFS.
expected=set()
peripheral_expected=set()
for A3 in combinations(points,3):
    A=frozenset(A3)
    if A in L:continue
    level={k:frozenset(j for j in lines if len(L[j]&A)==k) for k in range(3)}
    assert tuple(len(level[k]) for k in range(3))==(1,3,3)
    for j in level[0]|level[2]:
        B=level[1]|{j}
        expected.add(sum(1<<i for i in A)+sum(1<<(7+l) for l in B))
    B=level[0]|level[2]
    expected.add(sum(1<<i for i in A)+sum(1<<(7+l) for l in B))
    B=level[0]|level[1]
    peripheral_expected.add(sum(1<<i for i in A)+sum(1<<(7+l) for l in B))
for B3 in combinations(lines,3):
    B=frozenset(B3)
    if any(set(B)==set(j for j in lines if p in L[j]) for p in points):continue
    level={k:frozenset(p for p in points if sum(p in L[j] for j in B)==k) for k in range(3)}
    assert tuple(len(level[k]) for k in range(3))==(1,3,3)
    for p in level[0]|level[2]:
        A=level[1]|{p}
        expected.add(sum(1<<i for i in A)+sum(1<<(7+j) for j in B))
    A=level[0]|level[2]
    expected.add(sum(1<<i for i in A)+sum(1<<(7+j) for j in B))
    A=level[0]|level[1]
    peripheral_expected.add(sum(1<<i for i in A)+sum(1<<(7+j) for j in B))
expected.update([sum(1<<p for p in points),sum(1<<(7+j) for j in lines)])
assert len(expected)==282

# Exhaustively compare to an independent arithmetic pair-incidence test on all subsets.
observed=set()
count_by_size=[]
for size in range(8):
    count=0
    for A_size in range(size+1):
        B_size=size-A_size
        if A_size>7 or B_size>7:continue
        for aa in combinations(range(7),A_size):
            A=frozenset(aa)
            for bb in combinations(range(7),B_size):
                B=frozenset(bb)
                if satisfies(A,B):
                    count+=1
                    observed.add(sum(1<<i for i in A)+sum(1<<(7+j) for j in B))
    count_by_size.append(count)
assert count_by_size==[0,0,0,0,0,0,0,282]
assert observed==expected

# Construct exchange edges by checking set intersection, independent of bit-toggling.
state_sets={s:frozenset(i for i in range(14) if s&(1<<i)) for s in expected}
S=sorted(state_sets)
Edges=[]
for i in range(len(S)):
    for j in range(i+1,len(S)):
        if len(state_sets[S[i]]&state_sets[S[j]])==6:Edges.append((i,j))
assert len(Edges)==784
Adj=[set() for _ in S]
for i,j in Edges:Adj[i].add(j);Adj[j].add(i)
assert Counter(map(len,Adj))=={0:2,4:56,6:224}
comps=[];seen=set()
for i in range(len(S)):
    if i in seen:continue
    q=[i];seen.add(i)
    for j in q:
        for k in Adj[j]:
            if k not in seen:seen.add(k);q.append(k)
    comps.append(q)
assert sorted(map(len,comps))==[1,1,280]
large=next(c for c in comps if len(c)==280)
Ecc={}
for s in large:
    d={s:0};Q=deque([s])
    while Q:
        i=Q.popleft()
        for j in Adj[i]:
            if j not in d:d[j]=d[i]+1;Q.append(j)
    assert len(d)==280
    Ecc[s]=max(d.values())
assert Counter(Ecc.values())=={6:224,7:56}
assert {S[i] for i,e in Ecc.items() if e==7}==peripheral_expected
assert len(peripheral_expected)==56
with open('reconfiguration_certificate.json',encoding='utf-8') as f:C=json.load(f)
assert C['states_hex']==[f'{s:04x}' for s in S]
assert C['exchange_edges']==[list(p) for p in Edges]
assert C['giant_component_indices']==sorted(large)
assert C['eccentricities_giant']==[Ecc[i] for i in sorted(large)]
print('FANO_TRIANGLES_NONCOLLINEAR',28)
print('CLASSIFIED_SEVEN_SETS',len(expected))
print('ALL_MINIMUM_SIZE_COUNTS',count_by_size)
print('VALID_PROFILES',sorted(Counter((s&127).bit_count() for s in expected).items()))
print('SWAP_COMPONENT_SIZES',sorted(map(len,comps)))
print('SWAP_EDGES',len(Edges),'GIANT_ECCENTRICITIES',sorted(Counter(Ecc.values()).items()))
print('GEOMETRIC_PERIPHERAL_CLASSIFICATION',len(peripheral_expected))
print('CERTIFICATE_AGREEMENT_OK')
print('VERIFY_OK')
