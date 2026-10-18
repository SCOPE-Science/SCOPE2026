#!/usr/bin/env python3
"""Self-contained exhaustive certificate for a Fano-incidence higher-independence complex.
Run with Python 3.9 or later. No external packages required.
"""
from collections import Counter, deque
from itertools import combinations

N=14
NEIGH=[0]*N
for point in range(7):
    for line in range(7):
        if (point-line)%7 in (0,1,3):
            a,b=point,7+line
            NEIGH[a]|=1<<b
            NEIGH[b]|=1<<a

# A forbidden triple is precisely a three-vertex connected induced subgraph.
forbidden=set()
for center in range(N):
    for a,b in combinations([v for v in range(N) if NEIGH[center]>>v&1],2):
        forbidden.add((1<<center)|(1<<a)|(1<<b))
assert len(forbidden)==42

# Alternative elementary equivalence of membership: no selected vertex may have
# two selected neighbors. This equivalence is exact because induced components
# of size >=3 contain a three-vertex path.
faces=[]
for mask in range(1,1<<N):
    a=all((mask & t)!=t for t in forbidden)
    b=all((NEIGH[v]&mask).bit_count()<2 for v in range(N) if mask>>v&1)
    assert a==b
    if a:faces.append(mask)
F=set(faces)
fvector=Counter(m.bit_count()-1 for m in faces)
assert dict(sorted(fvector.items()))=={0:14,1:91,2:322,3:651,4:728,5:392,6:58}
assert len(F)==2256

# Deterministic sequence of vertex-toggle elementary matchings.
remaining=F.copy()
matching={}
for vertex in range(N):
    bit=1<<vertex
    for lower in sorted(remaining,key=lambda m:(m.bit_count(),m)):
        if lower not in remaining or lower & bit:continue
        upper=lower|bit
        if upper in remaining:
            matching[lower]=upper
            remaining.remove(lower)
            remaining.remove(upper)
assert len(matching)==1121
critical=Counter(m.bit_count()-1 for m in remaining)
assert critical=={0:1,5:13},critical

# Full directed Hasse graph, reverse matched incidences and verify it is a DAG.
indegree={m:0 for m in faces}
out={m:[] for m in faces}
cover_count=0
for coface in faces:
    bits=coface
    while bits:
        bit=bits&-bits;bits-=bit
        face=coface^bit
        if not face:continue
        if matching.get(face)==coface:
            a,b=coface,face
        else:
            a,b=face,coface
        out[a].append(b)
        indegree[b]+=1
        cover_count+=1
assert cover_count==10150
q=deque(m for m in faces if indegree[m]==0)
visited=0
while q:
    m=q.popleft();visited+=1
    for t in out[m]:
        indegree[t]-=1
        if indegree[t]==0:q.append(t)
assert visited==len(F)
assert sum((-1)**d*c for d,c in fvector.items())==1-13

# Rotation on the seven point labels and seven line labels, of exact order 7.
def shift(m,step):
    out=0
    for v in range(N):
        if m>>v&1:
            to=((v+step)%7) if v<7 else 7+((v-7+step)%7)
            out|=1<<to
    return out

def sign_on_face(m,step):
    order=[v for v in range(N) if m>>v&1]
    shifted=[((v+step)%7 if v<7 else 7+(v-7+step)%7) for v in order]
    inv=sum(a>b for i,a in enumerate(shifted) for b in shifted[i+1:])
    return (-1)**inv

traces=[]
for step in range(7):
    t=-1 # reduced augmentation: empty simplex has degree -1 and trace 1
    fixed=[]
    for m in faces:
        if shift(m,step)==m:
            t+=(-1)**(m.bit_count()-1)*sign_on_face(m,step)
            fixed.append(m)
    traces.append(t)
    if step:assert len(fixed)==2 and {m.bit_count() for m in fixed}=={7}
assert traces==[-13]+[1]*6,traces
# Since only reduced H_5 is nonzero, the homological traces are minus these.
character=[-t for t in traces]
assert character==[13]+[-1]*6
print('PASS: vertices=14 edges=21 forbidden_connected_triples=42')
print('PASS: nonempty_faces=2256 fvector=',dict(sorted(fvector.items())))
print('PASS: matched_pairs=1121 critical_cells=',dict(sorted(critical.items())))
print('PASS: oriented_Hasse_arcs=',cover_count,'topological_sort_vertices=',visited)
print('PASS: reduced_Lefschetz_rotation=',traces)
print('PASS: H5_rotation_character=',character,'Q-module=Q+2Q(zeta_7)')
print('PASS: homotopy_type=wedge_of_13_five_spheres')
