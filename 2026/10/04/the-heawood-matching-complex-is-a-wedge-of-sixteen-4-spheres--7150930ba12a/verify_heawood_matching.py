#!/usr/bin/env python3
import json, os
from collections import Counter, deque

HERE=os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE,'morse_certificate.json'),encoding='utf-8') as fh:
    C=json.load(fh)

# Fano plane presentation.  L_i={i,i+1,i+3} modulo 7.
edges=[]
for i in range(7):
    for p in (i,(i+1)%7,(i+3)%7):
        edges.append((p,7+i))
assert len(edges)==21 and len(set(edges))==21
# Every graph vertex has degree three.
deg=[0]*14
for u,v in edges:
    deg[u]+=1; deg[v]+=1
assert deg==[3]*14
# Fano condition: every pair of point vertices lies on exactly one line.
for a in range(7):
    for b in range(a+1,7):
        common=0
        for i in range(7):
            line={i,(i+1)%7,(i+3)%7}
            common += int(a in line and b in line)
        assert common==1

# Conflict mask for graph edges: a face of the matching complex is a set of
# edge indices with pairwise disjoint endpoints.
conf=[]
for u,v in edges:
    m=0
    for j,(x,y) in enumerate(edges):
        if u in (x,y) or v in (x,y):
            m |= 1<<j
    conf.append(m)

faces=[]
def enumerate_faces(start,mask):
    if mask:
        faces.append(mask)
    for e in range(start,21):
        if mask & conf[e]:
            continue
        enumerate_faces(e+1,mask|(1<<e))
enumerate_faces(0,0)
face_set=set(faces)
assert len(faces)==C['expected_nonempty_face_count']
fc=Counter(m.bit_count()-1 for m in faces)
fvec=[fc[d] for d in range(max(fc)+1)]
assert fvec==C['expected_f_vector']
# The final coefficient independently checks the classical 24 perfect matchings.
assert fvec[-1]==24

# Deterministic sequential element matching. At each edge-index x, pair each
# still-unmatched lower face sigma not containing x with sigma union {x}, if
# the latter remains unmatched. Sorting makes the certificate byte-independent
# of Python set iteration.
unmatched=set(faces)
pairs=[]
for x in C['toggle_order']:
    bit=1<<x
    for lo in sorted(unmatched):
        if lo & bit:
            continue
        hi=lo|bit
        if hi in unmatched:
            assert hi in face_set and hi.bit_count()==lo.bit_count()+1
            unmatched.remove(lo); unmatched.remove(hi)
            pairs.append((lo,hi))
assert len(pairs)==C['expected_matching_pairs']
crit=sorted(tuple(i for i in range(21) if m>>i&1) for m in unmatched)
expected=sorted(tuple(x) for x in C['expected_critical_faces'])
assert crit==expected
crit_dims=Counter(len(x)-1 for x in crit)
assert crit_dims==Counter({4:16,0:1})

# Full acyclicity check on the nonempty face-poset Hasse graph. Unmatched cover
# relations point upward; matched cover relations are reversed.
idx={m:i for i,m in enumerate(faces)}
matched=set(pairs)
out=[[] for _ in faces]
indeg=[0]*len(faces)
hasse_edges=0
for lo in faces:
    for e in range(21):
        if lo>>e & 1:
            continue
        hi=lo|(1<<e)
        if hi not in face_set:
            continue
        if (lo,hi) in matched:
            a,b=idx[hi],idx[lo]
        else:
            a,b=idx[lo],idx[hi]
        out[a].append(b); indeg[b]+=1; hasse_edges+=1
assert hasse_edges==C['expected_hasse_edges']
q=deque(i for i,d in enumerate(indeg) if d==0)
seen=0
while q:
    a=q.popleft(); seen+=1
    for b in out[a]:
        indeg[b]-=1
        if indeg[b]==0:
            q.append(b)
assert seen==len(faces), 'oriented Hasse graph contains a directed cycle'

# Independent mod-2 homology cross-check from simplicial boundary matrices.
bydim={d:[m for m in faces if m.bit_count()-1==d] for d in range(max(fc)+1)}
def gf2_rank(columns):
    piv={}; rank=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p]=x; rank+=1; break
    return rank
ranks={}
for d in range(1,max(fc)+1):
    lower={m:i for i,m in enumerate(bydim[d-1])}
    columns=[]
    for m in bydim[d]:
        x=0
        for e in range(21):
            if m>>e & 1:
                x ^= 1<<lower[m^(1<<e)]
        columns.append(x)
    ranks[str(d)]=gf2_rank(columns)
assert ranks==C['expected_mod2_boundary_ranks']
betti={}
for d in range(max(fc)+1):
    b=len(bydim[d])-ranks.get(str(d),0)-ranks.get(str(d+1),0)
    if d==0:
        b-=1
    if b:
        betti[str(d)]=b
assert betti==C['expected_reduced_betti']
# Euler characteristic agrees with a wedge of sixteen even-dimensional spheres.
chi=sum((1 if d%2==0 else -1)*fc[d] for d in fc)
assert chi==17
print('VERIFY_OK')
