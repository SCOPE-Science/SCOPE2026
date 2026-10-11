#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque

ROWS=COLS=3
K=5
V=tuple(range(ROWS*COLS))
adj={v:set() for v in V}
for v in V:
    r,c=divmod(v,COLS)
    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
        rr,cc=r+dr,c+dc
        if 0<=rr<ROWS and 0<=cc<COLS:
            adj[v].add(rr*COLS+cc)

def connected(S):
    S=set(S)
    if not S:
        return False
    start=next(iter(S)); seen={start}; stack=[start]
    while stack:
        u=stack.pop()
        for w in adj[u] & S:
            if w not in seen:
                seen.add(w); stack.append(w)
    return len(seen)==len(S)

facets=[]
for S in combinations(V,K):
    if not connected(S):
        facets.append(frozenset(set(V)-set(S)))
assert len(facets)==77
faces={frozenset()}
for F in facets:
    ff=tuple(sorted(F))
    for j in range(1,len(ff)+1):
        for T in combinations(ff,j):
            faces.add(frozenset(T))
assert len(faces)==203
assert Counter(len(s)-1 for s in faces if s)==Counter({2:80,3:77,1:36,0:9})

# Sequential element matching, leaving the empty face outside the Morse matching.
unmatched=set(faces); unmatched.remove(frozenset())
pairs=[]
for v in V:
    # At a fixed stage, toggling v partitions eligible faces into disjoint pairs.
    lows=[s for s in unmatched if v not in s and (s|{v}) in unmatched]
    lows.sort(key=lambda s:(len(s),tuple(sorted(s))))
    for s in lows:
        t=s|{v}
        if s in unmatched and t in unmatched:
            unmatched.remove(s); unmatched.remove(t); pairs.append((s,t))
assert len(pairs)==88
critical=Counter(len(s)-1 for s in unmatched)
assert critical==Counter({3:25,0:1})

# Verify this is a matching of Hasse cover relations.
partner={}
for lo,hi in pairs:
    assert len(hi)==len(lo)+1 and lo < hi
    assert lo in faces and hi in faces
    assert lo not in partner and hi not in partner
    partner[lo]=hi; partner[hi]=lo

# Forman orientation: unmatched cover high -> low; matched cover low -> high.
nodes=[s for s in faces if s]
out={s:set() for s in nodes}; indeg={s:0 for s in nodes}
matched_edges={(lo,hi) for lo,hi in pairs}
for hi in nodes:
    if len(hi)<=1: continue
    for x in hi:
        lo=hi-{x}
        if not lo: continue
        if lo not in faces: continue
        if (lo,hi) in matched_edges:
            a,b=lo,hi
        else:
            a,b=hi,lo
        if b not in out[a]:
            out[a].add(b); indeg[b]+=1
q=deque([s for s in nodes if indeg[s]==0]); seen=0
while q:
    s=q.popleft(); seen+=1
    for t in out[s]:
        indeg[t]-=1
        if indeg[t]==0:q.append(t)
assert seen==len(nodes), 'directed Hasse orientation contains a cycle'

# Independent Euler check: one component and reduced Euler characteristic -25.
f=Counter(len(s)-1 for s in faces if s)
chi=sum(((-1)**d)*c for d,c in f.items())
assert chi==-24 and chi-1==-25
print('VERIFY_OK')
print('facets=77')
print('faces_including_empty=203')
print('f_vector=(9,36,80,77)')
print('matched_pairs=88')
print('critical_cells={0:1,3:25}')
print('hasse_orientation_acyclic=true')
print('euler_characteristic=-24')
print('reduced_euler_characteristic=-25')
