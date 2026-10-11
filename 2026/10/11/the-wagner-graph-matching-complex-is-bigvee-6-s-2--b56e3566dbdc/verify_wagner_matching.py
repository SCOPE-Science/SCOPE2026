#!/usr/bin/env python3
"""Exact verifier for the ordinary matching complex of the Wagner graph M8."""
from collections import Counter, deque
import json

# M8: an 8-cycle plus four antipodal edges.
edges=[]
for i in range(8):
    e=tuple(sorted((i,(i+1)%8)))
    if e not in edges:
        edges.append(e)
for i in range(4):
    edges.append((i,i+4))
assert len(edges)==12 and len(set(edges))==12

def is_matching(mask):
    used=0
    for j,(a,b) in enumerate(edges):
        if (mask>>j)&1:
            bit=(1<<a)|(1<<b)
            if used & bit:
                return False
            used |= bit
    return True

faces=[m for m in range(1,1<<len(edges)) if is_matching(m)]
face_set=set(faces)
face_vector=Counter(m.bit_count()-1 for m in faces)
assert dict(sorted(face_vector.items())) == {0:12,1:42,2:44,3:7}

covers=[]
for lo in faces:
    for j in range(len(edges)):
        if not ((lo>>j)&1):
            hi=lo|(1<<j)
            if hi in face_set:
                covers.append((lo,hi))
assert len(covers)==244

# Sequential element matching: at stage j, pair every still-unmatched face F
# not containing edge j with F union {j}, whenever the latter is still unmatched.
unmatched=set(faces)
pairs=[]
for j in range(len(edges)):
    for lo in sorted(tuple(unmatched)):
        if lo not in unmatched or ((lo>>j)&1):
            continue
        hi=lo|(1<<j)
        if hi in unmatched:
            unmatched.remove(lo); unmatched.remove(hi); pairs.append((lo,hi))

assert len(pairs)==49
critical=Counter(m.bit_count()-1 for m in unmatched)
assert dict(sorted(critical.items())) == {0:1,2:6}

# Verify the discrete-Morse orientation is acyclic on the complete Hasse graph.
pairset=set(pairs)
adj={m:[] for m in faces}
indeg={m:0 for m in faces}
for lo,hi in covers:
    if (lo,hi) in pairset:
        a,b=lo,hi
    else:
        a,b=hi,lo
    adj[a].append(b); indeg[b]+=1
q=deque([m for m,d in indeg.items() if d==0])
seen=0
while q:
    a=q.popleft(); seen+=1
    for b in adj[a]:
        indeg[b]-=1
        if indeg[b]==0:
            q.append(b)
assert seen==len(faces)

# Independent mod-2 simplicial homology.
by_dim={d:sorted([m for m in faces if m.bit_count()-1==d]) for d in range(4)}
def rank_f2(cols):
    basis={}; rank=0
    for x in cols:
        while x:
            p=x.bit_length()-1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p]=x; rank+=1; break
    return rank
ranks={}
for k in range(1,4):
    target={m:i for i,m in enumerate(by_dim[k-1])}
    cols=[]
    for m in by_dim[k]:
        col=0
        for j in range(len(edges)):
            if (m>>j)&1:
                col ^= 1 << target[m^(1<<j)]
        cols.append(col)
    ranks[k]=rank_f2(cols)
assert ranks == {1:11,2:31,3:7}
betti={}
for k in range(4):
    b=len(by_dim[k])-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0)
    betti[k]=b
assert betti == {0:0,1:0,2:6,3:0}

out={
    "graph_edges": edges,
    "nonempty_faces": len(faces),
    "face_vector_by_dimension": dict(sorted(face_vector.items())),
    "hasse_covers": len(covers),
    "matched_pairs": len(pairs),
    "critical_cells_by_dimension": dict(sorted(critical.items())),
    "acyclic_matching": True,
    "boundary_ranks_mod2": ranks,
    "reduced_betti_mod2": betti,
    "conclusion": "Match(M8) is homotopy equivalent to a wedge of six 2-spheres",
    "status": "VERIFY_OK"
}
print(json.dumps(out,sort_keys=True,separators=(",",":")))
