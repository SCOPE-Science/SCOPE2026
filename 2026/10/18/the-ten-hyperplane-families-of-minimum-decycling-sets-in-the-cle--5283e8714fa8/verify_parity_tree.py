#!/usr/bin/env python3
"""Independent graph representation, forest DFS and geometric classification."""
import json
from collections import Counter,deque
from itertools import combinations

words=[x for x in range(32) if x.bit_count()%2==0]
assert len(words)==16
edges={x:{y for y in words if (x^y).bit_count()==4} for x in words}
assert {len(n) for n in edges.values()}=={5}


def is_forest(U):
    # Recursive traversal detects any edge back to a nonparent vertex.
    U=set(U)
    seen=set()
    def visit(v,parent):
        seen.add(v)
        for w in (edges[v] & U):
            if w==parent:
                continue
            if w in seen or not visit(w,v):
                return False
        return True
    for v in U:
        if v not in seen and not visit(v,None):
            return False
    return True

forests=[]
for k in (10,9):
    found=[]
    for comb in combinations(words,k):
        if is_forest(comb):
            found.append(frozenset(comb))
    if k==10:
        assert not found
    else:
        forests=found
assert len(forests)==80

halves={frozenset(x for x in words if (x>>i)&1==b) for i in range(5) for b in range(2)}
assert len(halves)==10
predicted={frozenset((set(words)-set(H)) | {x}) for H in halves for x in H}
assert set(forests)==predicted

# Encode minimum deletion sets as hashable frozensets of parity-5-bit words.
F=[frozenset(set(words)-set(U)) for U in forests]
assert len(set(F))==80

def graph(k,slide=False):
    A={f:set() for f in F}
    for a,b in combinations(F,2):
        if len(a-b)<=k and (not slide or (len(a-b)==1 and next(iter(a-b)) in edges[next(iter(b-a))])):
            A[a].add(b)
            A[b].add(a)
    seen=set();parts=[]
    for a in F:
        if a in seen:continue
        component={a};todo=[a];seen.add(a)
        for v in todo:
            for w in A[v]:
                if w not in seen:seen.add(w);todo.append(w);component.add(w)
        parts.append(component)
    return A,parts

A1,C1=graph(1)
A2,C2=graph(2)
A3,C3=graph(3)
AS,CS=graph(1,slide=True)
assert sorted(map(len,C1))==[8]*10
assert sorted(map(len,C2))==[8]*10
assert sorted(map(len,C3))==[80]
assert sorted(map(len,CS))==[2]*40
assert all(len(v)==23 for v in A3.values())

profiles=Counter()
for root in F:
    d={root:0};todo=deque([root])
    while todo:
        v=todo.popleft()
        for w in A3[v]:
            if w not in d:
                d[w]=d[v]+1;todo.append(w)
    assert len(d)==80
    profiles[tuple(Counter(d.values())[i] for i in range(4))]+=1
assert profiles=={(1,23,48,8):80}

# The inactive 9-set induces a 4-arm subdivided star.
for U in forests:
    degree=Counter(len(edges[x]&U) for x in U)
    assert degree==Counter({4:1,2:4,1:4})

print(json.dumps({
    'graph':'five-regular Clebsch even five-bit words',
    'forest9':80,'forest10':0,'minimum_fvs':7,'minimum_fvs_count':80,
    'hyperplanes':10,'forest_degree_sequence':[4]+[2]*4+[1]*4,
    'exchange1_edges':sum(map(len,A1.values()))//2,'exchange1_components':sorted(map(len,C1)),
    'exchange2_edges':sum(map(len,A2.values()))//2,'exchange2_components':sorted(map(len,C2)),
    'exchange3_edges':sum(map(len,A3.values()))//2,'exchange3_components':sorted(map(len,C3)),
    'exchange3_distance_profile':list(next(iter(profiles))),
    'slide_edges':sum(map(len,AS.values()))//2,'slide_components':sorted(map(len,CS)),
},sort_keys=True))
