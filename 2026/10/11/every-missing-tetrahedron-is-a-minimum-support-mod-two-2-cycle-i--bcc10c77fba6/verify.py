#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict

VERTS='123456789ab'
FACETS='''12346 12347 12369 12379 12458 12459 12468 12479
12568 12569 13467 13567 13569 1357a 1359b 135ab
1379a 139ab 1458a 1459b 145ab 1467b 1468a 146ab
1479b 15678 1578a 1678b 168ab 178ab 179ab 23468
23478 2357a 2357b 235ab 2368a 2369a 2378b 2379a
238ab 24589 24789 2568b 2569a 256ab 25789 2578b
2579a 268ab 3467b 3468a 3469a 3469b 3478b 3489a
3489b 3567b 3569b 389ab 4569a 4569b 456ab 4589a
4789b 5678b 5789a 789ab'''.split()
ORDER={v:i for i,v in enumerate(VERTS)}
def norm(s): return tuple(sorted(s,key=ORDER.get))
facets=[norm(x) for x in FACETS]
assert len(facets)==68 and len(set(facets))==68
faces=[]
for k in range(1,6):
    ss=set()
    for F in facets:
        ss.update(norm(c) for c in combinations(F,k))
    faces.append(sorted(ss,key=lambda x:tuple(ORDER[v] for v in x)))
assert tuple(map(len,faces))==(11,55,150,170,68)

edges,triangles,tetrahedra=faces[1],faces[2],faces[3]
eidx={e:i for i,e in enumerate(edges)}
tidx={t:i for i,t in enumerate(triangles)}

def bitvec(items,index):
    x=0
    for a in items: x ^= 1<<index[norm(a)]
    return x

def basis(vectors):
    B={}
    for x in vectors:
        y=x
        while y:
            p=y.bit_length()-1
            if p in B: y ^= B[p]
            else:
                B[p]=y
                break
    return B

def reducev(x,B):
    y=x
    for p in sorted(B,reverse=True):
        if (y>>p)&1: y ^= B[p]
    return y

def rank(vectors): return len(basis(vectors))

# Boundary d2: triangles -> edges; boundary d3: tetrahedra -> triangles.
d2=[bitvec(combinations(T,2),eidx) for T in triangles]
d3=[bitvec(combinations(Q,3),tidx) for Q in tetrahedra]
r2,r3=rank(d2),rank(d3)
assert (r2,r3)==(45,103)
h2_dim=len(triangles)-r2-r3
assert h2_dim==2

tri_set=set(triangles); tet_set=set(tetrahedra)
missing=[]
for Q in combinations(VERTS,4):
    Q=norm(Q)
    if all(norm(T) in tri_set for T in combinations(Q,3)) and Q not in tet_set:
        z=bitvec(combinations(Q,3),tidx)
        missing.append((Q,z))
assert len(missing)==58

B3=basis(d3)
# Every missing tetrahedral boundary is nonzero in H2, checked by rank increase.
for Q,z in missing:
    assert reducev(z,B3)!=0
    assert rank(d3+[z])==r3+1

# Equal homology classes iff z+w lies in im d3; obtain the basis-independent class partition.
unused=set(range(len(missing))); classes=[]
while unused:
    i=min(unused); zi=missing[i][1]
    cls=[]
    for j in sorted(unused):
        zj=missing[j][1]
        if reducev(zi^zj,B3)==0:
            cls.append(j)
    for j in cls: unused.remove(j)
    classes.append(cls)
sizes=sorted(len(c) for c in classes)
assert sizes==[6,24,28]
assert len(classes)==3==(2**h2_dim-1)

# Any nonzero 2-cycle on at most four vertices must use four vertices and be the
# full tetrahedral boundary. Thus these are exactly the minimum vertex supports.
# Verify computationally that the 58 supports exhaust all four-sets with a nonzero boundary class.
essential4=[]
for Q in combinations(VERTS,4):
    Q=norm(Q)
    if all(norm(T) in tri_set for T in combinations(Q,3)):
        z=bitvec(combinations(Q,3),tidx)
        if reducev(z,B3)!=0: essential4.append(Q)
assert set(essential4)=={Q for Q,_ in missing}

print('VERIFY_OK f=11,55,150,170,68 ranks_d2_d3=45,103 H2_F2=2 missing_tetrahedra=58 essential_missing=58 class_supports=6,24,28 min_vertex_support=4')
