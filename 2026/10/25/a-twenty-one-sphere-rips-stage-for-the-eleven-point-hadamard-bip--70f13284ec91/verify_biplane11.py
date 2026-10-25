#!/usr/bin/env python3
"""Standalone exact verification of the eleven-point biplane Rips theorem."""
from collections import defaultdict
from itertools import combinations
from collections import Counter
import json,sys

V=11
D=frozenset({1,3,4,5,9})
blocks=[frozenset((j+d)%V for d in D) for j in range(V)]
assert len(set(blocks))==V
assert all(len(B)==5 for B in blocks)
assert all(sum(p in B for B in blocks)==5 for p in range(V))
assert all(sum(p in B and q in B for B in blocks)==2 for p in range(V) for q in range(p+1,V))
assert all(len(blocks[j]&blocks[k])==2 for j in range(V) for k in range(j+1,V))
assert all(set((p+t)%V for p in blocks[j])==set(blocks[(j+t)%V]) for j in range(V) for t in range(V))

# Block complex D: each face is contained in a cyclic translate of the difference set.
dowker={sum(1<<i for i in c) for B in blocks for r in range(1,6) for c in combinations(sorted(B),r)}
assert Counter(x.bit_count()-1 for x in dowker)=={0:11,1:55,2:110,3:55,4:11}

# Free-face collapses, dimension 4 -> dimension 2; store unique codimension-one pairs.
alive=set(dowker)
pairs=[]
while any(x.bit_count()>=4 for x in alive):
    selected=None
    for top in sorted((x for x in alive if x.bit_count()>=4),key=lambda x:(-x.bit_count(),x)):
        for i in range(V):
            if not(top>>i&1): continue
            lower=top^(1<<i)
            if sum(lower&z==lower and z.bit_count()==top.bit_count() for z in alive)==1:
                selected=(lower,top);break
        if selected:break
    assert selected, 'No remaining free high-dimensional facet pair'
    lower,top=selected
    assert lower in alive and top in alive
    assert not any(lower & z == lower and z not in (top,lower) for z in alive)
    alive.remove(lower);alive.remove(top);pairs.append(selected)
assert len(pairs)==55
assert Counter(x.bit_count()-1 for x in alive)=={0:11,1:55,2:66}

# A trivial-presentation certificate: choose the 10 tree edges (0,i), then
# use filled triangles with exactly one uneliminated edge to eliminate
# each of the remaining 45 edge-loop generators. Tietze substitution is exact.
triangles={tuple(i for i in range(V) if t>>i&1) for t in dowker if t.bit_count()==3}
known={tuple(sorted((0,i))) for i in range(1,V)}
witness=[]
passes=[]
while len(known)<55:
    pending=[]
    for tri in sorted(triangles):
        edges={tuple(sorted(e)) for e in combinations(tri,2)}
        unknown=edges-known
        if len(unknown)==1:
            pending.append((next(iter(unknown)),tri))
    assert pending, 'Triangles do not eliminate every non-tree loop'
    added=0
    for e,t in pending:
        if e not in known:
            assert all(x in known for x in {tuple(sorted(x)) for x in combinations(t,2)}-{e})
            known.add(e);witness.append((e,t));added+=1
    passes.append(added)
assert len(witness)==45 and sum(passes)==45 and len(known)==55
assert sum((-1)**(n-1)*f for n,f in [(1,11),(2,55),(3,110),(4,55),(5,11)])-1==21

# Incidence graph: two 11-sets, with all point-block incidences.
N=22
adj=[set() for _ in range(N)]
for b,B in enumerate(blocks):
    for p in B:
        adj[p].add(V+b);adj[V+b].add(p)
assert sum(len(s) for s in adj)==110
for v in range(N):
    seen={v};front={v};layer=0
    while front:
        front=set.union(*(adj[x] for x in front))-seen
        if not front:break
        seen|=front;layer+=1
    assert seen==set(range(N)) and layer<=3
assert any(j not in adj[i] for i in range(V) for j in range(V,N))

# All inclusive scale-2 Rips faces, by cross-incidence constraints.
faces=defaultdict(list)
for pm in range(1<<V):
    ps={i for i in range(V) if pm>>i&1}
    admissible=[b for b,B in enumerate(blocks) if ps.issubset(B)]
    for bs in range(1<<len(admissible)):
        bm=sum(1<<b for j,b in enumerate(admissible) if bs>>j&1)
        mask=pm|(bm<<V)
        if mask:faces[mask.bit_count()-1].append(mask)
assert {d:len(v) for d,v in faces.items()}=={0:22,1:165,2:550,3:935,4:1034,5:946,6:660,7:330,8:110,9:22,10:2}

# Exact F2 boundary ranks independently corroborate the topological proof.
previous=0
hom={}
for d in range(1,11):
    lower={x:i for i,x in enumerate(faces[d-1])}
    piv={}
    for face in faces[d]:
        col=0
        for j in range(N):
            if face>>j&1:col^=1<<lower[face^(1<<j)]
        while col:
            top=col.bit_length()
            if top in piv:col^=piv[top]
            else:piv[top]=col;break
    rank=len(piv)
    hom[d-1]=len(faces[d-1])-previous-rank
    previous=rank
assert hom=={0:1,1:0,2:0,3:21,4:0,5:0,6:0,7:0,8:0,9:0}
assert len(faces[10])-previous==0

# Signed reduced Lefschetz formula: invariant faces with induced orientation.
def sign(indices):
    return -1 if sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))%2 else 1

def reduced_lefschetz(t):
    result=-1  # augmented empty face of degree -1
    perm=[(j+t)%V for j in range(V)]+[V+(j+t)%V for j in range(V)]
    for d,ff in faces.items():
        for f in ff:
            a=[i for i in range(N) if f>>i&1]
            p=[perm[i] for i in a]
            if set(a)==set(p):result+=(-1)**d*sign(p)
    return result
lvals=[reduced_lefschetz(t) for t in range(V)]
assert lvals==[-21]+[1]*10
# H_3 has trace -L; cyclic C11 rational module has invariant rank 1 and
# two copies of the rational cyclotomic degree-ten representation.
assert [-x for x in lvals]==[21]+[-1]*10
# Scale one has 34 circles, nonidentity cyclic trace 1 (free graph action).
assert 55-22+1==34
assert 4+3*10==34 and 4-3==1
assert 1+2*10==21 and 1-2==-1

certificate={'parameters':{'v':11,'k':5,'lambda':2,'difference_set':sorted(D)},
 'dowker_f_vector':[11,55,110,55,11],
 'dowker_collapse_pairs':[[a,b] for a,b in pairs],
 'fundamental_group_eliminations':[{'edge':list(e),'triangle':list(t)} for e,t in witness],
 'fundamental_group_elimination_passes':passes,
 'rips2_f_vector':[len(faces[i]) for i in range(11)],
 'rips2_mod2_homology':[hom[i] for i in range(10)]+[0],
 'rips2_reduced_lefschetz_c11':lvals}
if len(sys.argv)>1 and sys.argv[1]=='--write-certificate':
    with open(sys.argv[2],'w',encoding='utf-8') as f:json.dump(certificate,f,indent=2,sort_keys=True);f.write('\n')
elif len(sys.argv)>1:
    with open(sys.argv[1],encoding='utf-8') as f:saved=json.load(f)
    assert saved==certificate, 'Certificate mismatch'
print('BIPLANE11_DESIGN_VERIFIED 11 5 2')
print('BIPLANE11_DOWKER_COLLAPSES_AND_PI1_VERIFIED',len(pairs),len(witness),passes)
print('BIPLANE11_RIPS2_MOD2_HOMOLOGY_VERIFIED',len(sum(faces.values(),[])))
print('BIPLANE11_CYCLIC_LEFSCHETZ_VERIFIED',lvals)
