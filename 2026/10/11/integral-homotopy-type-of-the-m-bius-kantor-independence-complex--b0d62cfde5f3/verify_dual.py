#!/usr/bin/env python3
"""Exact eight-vertex Alexander-dual Morse certificate (standard library only)."""
from collections import Counter, defaultdict, deque
from functools import lru_cache

n=8
# Each mask is the neighborhood of a vertex on the opposite side of
# the 16-vertex cubic incidence graph. Every mask has three bits.
line_masks=(19,38,76,137,97,194,148,56)
assert len(set(line_masks))==8 and all(m.bit_count()==3 for m in line_masks)
# Verify these eight incidence triples directly from GP(8,3), rather than
# treating the asserted hypergraph-to-graph identification as an assumption.
G_edges=set()
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
        G_edges.add(tuple(sorted((a,b))))
left=sorted([i for i in range(8) if i%2==0]+[8+i for i in range(8) if i%2==1])
right=sorted([i for i in range(8) if i%2==1]+[8+i for i in range(8) if i%2==0])
assert left==[0,2,4,6,9,11,13,15]
assert right==[1,3,5,7,8,10,12,14]
assert len(G_edges)==24 and all(((a in left) != (b in left)) for a,b in G_edges)
derived=tuple(sum(1<<j for j,v in enumerate(left)
                  if tuple(sorted((v,r))) in G_edges) for r in right)
assert derived==line_masks, (derived,line_masks)
assert all(sum(bool(e&(1<<j)) for e in line_masks)==3 for j in range(n))
faces=tuple(mask for mask in range(1,1<<n) if any((mask&e)==0 for e in line_masks))
assert len(faces)==140
assert [sum(x.bit_count()==i for x in faces) for i in range(1,6)]==[8,28,56,40,8]
fset=set(faces)
remaining=set(faces)
pairs=[]
for i in range(n):
    bit=1<<i
    for lower in faces:
        upper=lower|bit
        if lower&bit==0 and lower in remaining and upper in remaining:
            remaining.remove(lower)
            remaining.remove(upper)
            pairs.append((lower,upper))
assert len(pairs)==67
assert sorted(remaining)==[1,14,22,82,164,204],sorted(remaining)
assert Counter(face.bit_count()-1 for face in remaining)=={0:1,2:4,3:1}
paired={a:b for a,b in pairs}
indegree={mask:0 for mask in faces}
outs=defaultdict(list)
incidences=0
for upper in faces:
    for i in range(n):
        if upper & (1<<i):
            lower=upper^(1<<i)
            if not lower:continue
            assert lower in fset
            u,v=(lower,upper) if paired.get(lower)==upper else (upper,lower)
            outs[u].append(v)
            indegree[v]+=1
            incidences+=1
q=deque(mask for mask in faces if indegree[mask]==0)
seen=0
while q:
    x=q.popleft();seen+=1
    for y in outs[x]:
        indegree[y]-=1
        if indegree[y]==0:q.append(y)
assert seen==len(faces), (seen,len(faces))
# The lone critical 3-cell could attach by nonzero degree to the 2-skeleton.
# Compute its full signed integral Morse boundary, not merely Betti numbers.
upper_of={upper:lower for lower,upper in pairs}
def boundary(m):
    verts=[i for i in range(n) if m & (1<<i)]
    for i,v in enumerate(verts):
        lower=m^(1<<v)
        if lower:yield lower,(-1 if i%2 else 1)
@lru_cache(None)
def eliminate(m):
    if m in remaining:return {m:1}
    if m in upper_of:return {}
    assert m in paired
    upper=paired[m]
    sgns=dict(boundary(upper))
    entry=sgns.pop(m)
    assert abs(entry)==1
    result=defaultdict(int)
    for x,sgn in sgns.items():
        for target,mult in eliminate(x).items():
            result[target]-=entry*sgn*mult
    return {target:v for target,v in result.items() if v}
crit2=sorted(x for x in remaining if x.bit_count()==3)
crit3=next(x for x in remaining if x.bit_count()==4)
coeff=defaultdict(int)
for face,sign in boundary(crit3):
    for target,weight in eliminate(face).items():coeff[target]+=sign*weight
assert all(coeff.get(x,0)==0 for x in crit2),coeff
assert not any(coeff.values()),coeff
print('DUAL_VERIFY_OK 8_vertices 8_triples 140_faces')
print('DUAL_F_VECTOR 8,28,56,40,8')
print('DUAL_MORSE 67_pairs critical_0=1 critical_2=4 critical_3=1')
print('DUAL_DAG',seen,'nodes',incidences,'oriented_cover_incidences')
print('DUAL_CRITICAL_MASKS',sorted(remaining))
print('DUAL_INTEGRAL_MORSE_D3_TO_D2', [coeff.get(x,0) for x in crit2])
print('DUAL_HOMOTOPY=4xS2+1xS3 GRAPH_SUSPENSION=4xS3+1xS4')
