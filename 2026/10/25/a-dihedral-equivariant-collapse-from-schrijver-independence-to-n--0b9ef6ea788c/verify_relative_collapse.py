#!/usr/bin/env python3
"""Complete, reproducible D8-orbit simplicial collapse for the natural
inclusion N(SG(3,2)) -> Ind(SG(3,2)). Python standard library only.
All graph vertices and simplex masks are reconstructed from definitions.
"""
from itertools import combinations
from collections import Counter

N = 8
V = [tuple(t) for t in combinations(range(N),3)
     if all((x+1)%N not in t for x in t)]
assert len(V)==16
adj = [[int(i!=j and set(V[i]).isdisjoint(V[j])) for j in range(16)] for i in range(16)]
assert sum(sum(row) for row in adj)==72
assert all(not(adj[i][j] and adj[j][k] and adj[k][i])
           for i,j,k in combinations(range(16),3))
F_ind = set()
for mask in range(1,1<<16):
    ids=[i for i in range(16) if mask>>i&1]
    if all(not adj[i][j] for i,j in combinations(ids,2)):
        F_ind.add(mask)
F_neigh=set()
for center in range(16):
    ngb=[i for i in range(16) if adj[center][i]]
    for length in range(1,len(ngb)+1):
        for ids in combinations(ngb,length):
            F_neigh.add(sum(1<<i for i in ids))
assert F_neigh <= F_ind
fvector = lambda fs: [sum(m.bit_count()==d+1 for m in fs)
                      for d in range(max(m.bit_count() for m in fs))]
assert fvector(F_ind)==[16,84,184,186,88,16]
assert fvector(F_neigh)==[16,68,88,42,8]

D=[]
for a in range(8):
    for reflection in (0,1):
        images=[V.index(tuple(sorted((a+(-x if reflection else x))%8 for x in t))) for t in V]
        assert sorted(images)==list(range(16))
        assert all(adj[i][j]==adj[images[i]][images[j]]
                   for i in range(16) for j in range(16))
        D.append(images)
assert len({tuple(p) for p in D})==16

def transform(mask,perm):
    return sum(1<<perm[i] for i in range(16) if mask>>i&1)

REPS = [
 (58624,60672), (52480,52544), (58368,60416), (57600,59648),
 (43010,59394), (52224,52288), (50432,50496), (40962,57346),
 (57344,59392), (50176,50240), (16648,49416), (16450,49218),
 (41216,43264), (40960,43008)]
ORBIT_SIZES=[8,8,16,16,8,16,8,16,16,16,8,16,8,16]
F=set(F_ind); count=0
for idx,(lower,upper) in enumerate(REPS):
    orbit={(transform(lower,p),transform(upper,p)) for p in D}
    assert len(orbit)==ORBIT_SIZES[idx],(idx,len(orbit))
    faces=[mask for pair in orbit for mask in pair]
    assert len(faces)==len(set(faces)),idx
    for a,b in orbit:
        assert a in F-F_neigh and b in F-F_neigh,(idx,a,b)
        assert b.bit_count()==a.bit_count()+1 and a&b==a
        cofaces=[a|(1<<i) for i in range(16)
                 if not a>>i&1 and a|(1<<i) in F]
        assert cofaces==[b],(idx,a,b,cofaces)
    for a,b in orbit:
        F.remove(a);F.remove(b)
    count+=len(orbit)
    assert {transform(x,p) for x in F for p in D}==F
assert F==F_neigh
assert count==176
assert len(F_ind-F_neigh)==352

# The published sphere theorem for the open-neighborhood complex
# supplies its homotopy type. Verify the common D8 homology character
# directly and independently by alternating traces on chains.
def signed_lefschetz(faces,perm):
    tr=0
    for mask in faces:
        indices=[i for i in range(16) if mask>>i&1]
        images=[perm[i] for i in indices]
        if sum(1<<i for i in images)!=mask:continue
        inversions=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
        tr+=(-1)**(len(indices)-1+inversions)
    return tr
for a in range(8):
    for reflection in (0,1):
        g=D[2*a+reflection]
        target=(-1)**(a+reflection)
        assert signed_lefschetz(F_ind,g)-1==target
        assert signed_lefschetz(F_neigh,g)-1==target
print('GRAPH vertices=16 edges=36 triangle_free=True')
print('FACE_VECTORS Ind=(16,84,184,186,88,16) N=(16,68,88,42,8)')
print('ORBIT_SIZES',ORBIT_SIZES)
print('EQUIVARIANT_ORBITS 14 ELEMENTARY_PAIRS 176 OUTSIDE_FACES 352')
print('FINAL_COMPLEX_EQUALS_OPEN_NEIGHBORHOOD True')
print('D8_H2_ORIENTATION_CHARACTER (-1)^(rotation_exponent+reflection_parity)')
print('VERIFY_OK_SCHRIJVER_SG32_RELATIVE_EQUIVARIANT_COLLAPSE')
