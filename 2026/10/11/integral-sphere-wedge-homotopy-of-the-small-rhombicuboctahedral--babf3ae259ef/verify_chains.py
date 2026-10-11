"""Independent geometric graph construction and exact mod-two chain check."""
from itertools import product
from collections import Counter, defaultdict
from math import sqrt

# Vertex list is independent of the combinatorial edge recipe:
# each vertex has a long coordinate 1+sqrt(2), and two unit coordinates.
verts=[]
for long_axis in range(3):
    for signs in product((-1,1), repeat=3):
        point=tuple(signs[i]*(1+sqrt(2) if i==long_axis else 1) for i in range(3))
        verts.append(point)
assert len(verts)==24 and len(set(verts))==24
adj=[0]*24
for i in range(24):
    for j in range(i):
        sqdist=sum((x-y)**2 for x,y in zip(verts[i],verts[j]))
        if abs(sqdist-4)<1.e-8:
            adj[i]|=1<<j
            adj[j]|=1<<i
        else:
            assert sqdist>4+1.e-7
assert sum(x.bit_count() for x in adj)==96
assert all(x.bit_count()==4 for x in adj)

# Enumeration in increasing vertex order, with a graph-independent bit test.
faces=[0]
for k in range(24):
    fac=[m|(1<<k) for m in faces if not (m & adj[k])]
    faces.extend(fac)
levels=defaultdict(list)
for m in faces:
    if m:levels[m.bit_count()-1].append(m)
assert [len(levels[d]) for d in range(8)]==[24,228,1104,2940,4368,3536,1440,234]

# F_2 boundary ranks via sparse columns represented as arbitrary-precision integers.
rank=[]
for d in range(1,8):
    lower={m:i for i,m in enumerate(levels[d-1])}
    pivots={}
    for f in levels[d]:
        c=0
        for j in range(24):
            if f & (1<<j):c ^= 1 << lower[f^(1<<j)]
        while c:
            p=c.bit_length()-1
            if p not in pivots:
                pivots[p]=c
                break
            c ^= pivots[p]
    rank.append(len(pivots))
reduced=[len(levels[0])-1-rank[0]]
for d in range(1,7):
    reduced.append(len(levels[d])-rank[d-1]-rank[d])
reduced.append(len(levels[7])-rank[6])
assert reduced==[0,0,0,0,1,4,0,0],reduced
print('geometry',len(verts),sum(x.bit_count() for x in adj)//2)
print('face_vector',*[len(levels[d]) for d in range(8)])
print('boundary_ranks',rank)
print('reduced_F2_Betti',reduced)
