#!/usr/bin/env python3
"""Independent subgroup-lattice inclusion-exclusion verification.

Enumerates all 30 subgroups of S4, all binary matrices invariant under each,
then exact stabilizers by subtracting supergroup-fixed sets. No reliance on
matrix-by-matrix stabilizer detection, row reduction or graph DFS.
"""
from itertools import permutations
from collections import Counter
import json
P=tuple(permutations(range(4)))
inv={p:i for i,p in enumerate(P)}
e=inv[(0,1,2,3)]
prod=[[inv[tuple(p[q[i]] for i in range(4))] for q in P] for p in P]

def gen(H,g):
    K=set(H)|{g}
    while True:
        newer=set(K)
        for x in K:
            for y in K:
                newer.add(prod[x][y])
        if newer==K:return frozenset(K)
        K=newer

subgroups={frozenset([e])}
queue=list(subgroups)
for H in queue:
    for g in range(24):
        if g in H:continue
        K=gen(H,g)
        if K not in subgroups:
            subgroups.add(K);queue.append(K)
assert len(subgroups)==30

def types(H):
    k=len(H)
    if k==1:return 'trivial'
    if k==2:return 'C2'
    if k==3:return 'C3'
    if k==4:
        for i in H:
            p=P[i]; q=tuple(range(4))
            for _ in range(4):q=tuple(p[t] for t in q)
            # check if some order-four element via square not identity
            q2=tuple(p[p[t]] for t in range(4))
            if q2 != tuple(range(4)):return 'C4'
        return 'V4'
    return {6:'S3',8:'D8',12:'A4',24:'S4'}[k]

def edges_for(H):
    seen=set();res=[]
    for i in range(16):
        if i in seen:continue
        r,c=divmod(i,4)
        orbit=set(4*P[h][r]+P[h][c] for h in H)
        assert i in orbit
        seen|=orbit;res.append(sum(1<<t for t in orbit))
    return res

def determinant(A):
    # Leibniz expansion over F2: sign irrelevant
    v=0
    for p in P:
        z=1
        for i in range(4):z&=(A>>(4*i+p[i]))&1
        v^=z
    return v

def simple(A):
    for subset in range(1,15):
        union=0
        for i in range(4):
            if (subset>>i)&1:union|=(A>>(4*i))&15
        if (union&~subset)==0:return False
    return True

def fixed(H):
    orb=edges_for(H)
    total=0
    for t in range(1<<len(orb)):
        A=0
        for j,cells in enumerate(orb):
            if (t>>j)&1:A|=cells
        if determinant(A) and simple(A):total+=1
    return total

F={H:fixed(H) for H in subgroups}
exact={}
for H in sorted(subgroups,key=len,reverse=True):
    exact[H]=F[H]-sum(exact[K] for K in exact if H<K)
    assert exact[H]>=0
labeled=Counter()
for H,v in exact.items():labeled[types(H)]+=v
EXPECTED={'trivial':11064,'C2':540,'C3':24,'C4':12,'V4':6,'S3':8,'D8':3,'S4':1}
assert {k:v for k,v in labeled.items() if v}==EXPECTED
assert labeled["A4"]==0
assert sum(labeled.values())==11658
print(json.dumps({'status':'VERIFY_OK','subgroup_count':len(subgroups),
  'labeled_simple':sum(labeled.values()),
  'exact_automorphism_group_labeled_counts':dict(sorted(labeled.items())),
  'max_cell_orbits':max(map(lambda h:len(edges_for(h)),subgroups)),
  'calculation':'supergroup Möbius subtraction of exact fixed subgroup counts'},indent=2))
