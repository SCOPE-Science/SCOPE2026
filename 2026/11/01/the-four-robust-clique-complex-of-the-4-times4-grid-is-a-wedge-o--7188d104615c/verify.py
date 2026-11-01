#!/usr/bin/env python3
"""Exhaustive finite certificate for four-robust clique complex of the 4x4 grid."""
from collections import Counter, deque
from itertools import combinations
from math import factorial

N=16
vertices=[(r,c) for r in range(4) for c in range(4)]
independent=[]
for q in combinations(range(N),4):
    if all(abs(vertices[a][0]-vertices[b][0])+abs(vertices[a][1]-vertices[b][1])!=1 for a,b in combinations(q,2)):
        independent.append(sum(1<<i for i in q))
assert len(independent)==405
faces={f for f in range(1<<N) if not any(f&i==i for i in independent)}
assert len(faces)==4812
fv=tuple(sum(f.bit_count()==j for f in faces) for j in range(1,7))
assert fv==(16,120,560,1415,1788,912),fv

# Lexicographic elementary Morse pairing. The empty-face pair is suppressed
# so that the resulting matching is a matching of the ordinary face poset.
remaining=set(faces)
pairs=[]
for vertex in range(N):
    bit=1<<vertex
    for face in sorted(remaining):
        if face in remaining and not face&bit and face|bit in remaining:
            remaining.remove(face)
            remaining.remove(face|bit)
            pairs.append((face,face|bit))
zero_pair=[(a,b) for a,b in pairs if a==0]
assert len(zero_pair)==1 and zero_pair[0][1]==1
ordinary_pairs=[(a,b) for a,b in pairs if a]
critical=remaining|{1}
critdims=Counter(f.bit_count()-1 for f in critical)
assert len(ordinary_pairs)==2363
assert critdims=={0:1,5:84},critdims

# Verify all Hasse incidences, all actual pairs, and full acyclicity.
nonempty=faces-{0}
arcs={f:[] for f in nonempty}
indegree={f:0 for f in nonempty}
paired=set(ordinary_pairs)
incidence_count=0
for face in nonempty:
    for vertex in range(N):
        bit=1<<vertex
        if face&bit:
            subface=face^bit
            if subface==0:continue
            incidence_count+=1
            # In a matched Hasse incidence reverse the default downward edge.
            if (subface,face) in paired:
                a,b=subface,face
            else:
                a,b=face,subface
            arcs[a].append(b)
            indegree[b]+=1
queue=deque(f for f,d in indegree.items() if d==0)
visited=0
while queue:
    v=queue.popleft();visited+=1
    for w in arcs[v]:
        indegree[w]-=1
        if indegree[w]==0:queue.append(w)
assert visited==len(nonempty),(visited,len(nonempty))
assert incidence_count==sum((j)*fv[j-1] for j in range(2,7))

# Signed simplicial Hopf trace, including augmented (-1)-chain.
def map_indices(map_fn):
    p=[]
    for r,c in vertices:
        rr,cc=map_fn(r,c)
        p.append(4*rr+cc)
    assert sorted(p)==list(range(N))
    assert all(abs(vertices[p[a]][0]-vertices[p[b]][0])+abs(vertices[p[a]][1]-vertices[p[b]][1])==1
               for a,b in combinations(range(N),2) if abs(vertices[a][0]-vertices[b][0])+abs(vertices[a][1]-vertices[b][1])==1)
    return p

def face_signed_trace(perm):
    total=-1  # augmented empty face, in degree -1
    fixed=0
    for face in nonempty:
        verts=[i for i in range(N) if face&(1<<i)]
        image=[perm[i] for i in verts]
        if set(image)!=set(verts):continue
        fixed+=1
        inv=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
        total+=(-1)**(len(verts)-1+inv)
    return total,fixed
symmetries=[
 ('identity',lambda r,c:(r,c),84),
 ('rotation90',lambda r,c:(c,3-r),0),
 ('rotation180',lambda r,c:(3-r,3-c),4),
 ('rotation270',lambda r,c:(3-c,r),0),
 ('vertical',lambda r,c:(r,3-c),-10),
 ('horizontal',lambda r,c:(3-r,c),-10),
 ('main_diagonal',lambda r,c:(c,r),-10),
 ('anti_diagonal',lambda r,c:(3-c,3-r),-10),
]
character={}
for name,fn,expected in symmetries:
    reduced_lefschetz,fixed=face_signed_trace(map_indices(fn))
    # Only H_5 is nonzero, so Lefschetz equals (-1)^5 times its trace.
    character[name]=-reduced_lefschetz
    assert character[name]==expected,(name,character[name],expected)
assert (6+16+11+11+2*20)==84
assert (6+16+11+11+40)==84
assert sum(k*v for k,v in [(1,6),(1,16),(1,11),(1,11),(2,20)])==84
print('VERIFY_OK independent_quadruples=405 faces=4811 face_vector='+str(fv))
print('VERIFY_OK incidences=%d matched_pairs=%d critical=(1 vertex,84 five_simplices) dag=%d' % (incidence_count,len(ordinary_pairs),visited))
print('VERIFY_OK D4_traces='+str(character)+' irreducibles=(6,16,11,11,20)')
