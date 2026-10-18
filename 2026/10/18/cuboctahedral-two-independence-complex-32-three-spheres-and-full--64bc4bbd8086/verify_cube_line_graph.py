#!/usr/bin/env python3
"""Standalone exhaustive finite certificate for cuboctahedral 2-independence homotopy and symmetry."""
from itertools import permutations, product
from collections import Counter, defaultdict, deque
from math import factorial

# Cube coordinate integers 0..7, edge endpoints differ in one bit.
cube_edges = tuple((a,b) for a in range(8) for b in range(a+1,8)
                   if (a^b).bit_count()==1)
assert len(cube_edges)==12
edge_index={e:i for i,e in enumerate(cube_edges)}
N=12
adj=tuple(sum((1<<j) for j,f in enumerate(cube_edges) if i!=j and set(e)&set(f))
          for i,e in enumerate(cube_edges))

def independent_components_size_le2(s):
    return all((s & adj[v]).bit_count()<=1 for v in range(N) if s>>v&1)

faces=tuple(s for s in range(1,1<<N) if independent_components_size_le2(s))
assert faces == tuple(sorted(faces))
face_set=set(faces)
fvec=Counter(s.bit_count()-1 for s in faces)
assert fvec == {0:12,1:66,2:164,3:177,4:36},fvec
print('cuboctahedral_line_graph_cube_edge_list=',cube_edges)
print('face_vector=',dict(sorted(fvec.items())))
print('number_nonempty_faces=',len(faces))
# Deterministic sequence of maximal vertex toggles, with tie by vertex order.
unpaired=set(faces)
matched=[]
steps=[]
while True:
    choice=max(((sum(s|1<<v in unpaired and not (s>>v&1) for s in unpaired), -v, v)
              for v in range(N)))
    count,_,v=choice
    if count==0:break
    pairs=[(s,s|(1<<v)) for s in sorted(unpaired) if s & (1<<v)==0 and s|(1<<v) in unpaired]
    assert len(pairs)==count
    for lo,hi in pairs:
        unpaired.remove(lo);unpaired.remove(hi)
        matched.append((lo,hi))
    steps.append((v,count,len(unpaired)))
critical_by_dim=Counter(s.bit_count()-1 for s in unpaired)
print('matching_stages=',steps)
print('critical_by_dimension=',dict(sorted(critical_by_dim.items())))
assert critical_by_dim=={0:1,3:32}
assert len(matched)==(len(faces)-len(unpaired))//2
matched_edges=set(matched)

# Full Hasse orientation: normally high -> low; matched low -> high.
indeg={s:0 for s in faces};out=defaultdict(list)
cover_ct=0
for s in faces:
    bit=s
    while bit:
        b=bit & -bit;bit-=b
        t=s^b
        if t==0:continue
        assert t in face_set
        cover_ct+=1
        if (t,s) in matched_edges:
            a,b2=t,s
        else:
            a,b2=s,t
        out[a].append(b2);indeg[b2]+=1
queue=deque(s for s in faces if indeg[s]==0)
processed=0
while queue:
    s=queue.popleft();processed+=1
    for t in out[s]:
        indeg[t]-=1
        if indeg[t]==0:queue.append(t)
print('hasse_cover_relations=',cover_ct,'topological_sort_count=',processed)
assert processed==len(faces),'Morse matching is not acyclic'

# independent mod-two boundary ranks via bit-packed Gaussian elimination.
chains=defaultdict(list)
for s in faces:chains[s.bit_count()-1].append(s)
rank_by_degree={}
for k in sorted(chains):
    if k==0:continue
    below={s:i for i,s in enumerate(chains[k-1])}
    pivots={};rank=0
    for s in chains[k]:
        col=0;bit=s
        while bit:
            b=bit&-bit;bit-=b
            col ^=1<<below[s^b]
        while col:
            pivot=col.bit_length()-1
            if pivot in pivots:col^=pivots[pivot]
            else:pivots[pivot]=col;rank+=1;break
    rank_by_degree[k]=rank
betti={k:len(chains[k])-rank_by_degree.get(k,0)-rank_by_degree.get(k+1,0) for k in chains}
print('boundary_mod2_ranks=',rank_by_degree)
print('unreduced_mod2_betti=',betti)
assert betti=={0:1,1:0,2:0,3:32,4:0}

# Automorphisms act on x in (Z/2)^3 by permuting bits and complementing selected bits.
def transform_vertex(x,p,b):
    return b ^ sum(((x>>p[i])&1)<<i for i in range(3))
def to_edge_permutation(p,b):
    out=[]
    for a,c in cube_edges:
        aa=transform_vertex(a,p,b);cc=transform_vertex(c,p,b)
        out.append(edge_index[tuple(sorted((aa,cc)))])
    assert len(set(out))==12
    return tuple(out)

def sign_of_fixed_face(s,perm):
    pre=[i for i in range(N) if s>>i & 1]
    image=[perm[i] for i in pre]
    if {perm[i] for i in pre}!={i for i in pre}:return 0
    inv=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
    return -1 if inv%2 else 1

def trace_on_H3(perm):
    lefschetz=sum((-1)**(s.bit_count()-1)*sign_of_fixed_face(s,perm) for s in faces)
    return 1-lefschetz

# group conjugacy classes: multiset of (+ cycle length) and (- cycle length)
def signed_class(p,b):
    remaining=set(range(3));pos=[];neg=[]
    while remaining:
        v=min(remaining);cyc=[];u=v
        while u not in cyc:
            cyc.append(u);remaining.remove(u);u=p[u]
        assert u==v
        s=sum((b>>u)&1 for u in cyc)%2
        (neg if s else pos).append(len(cyc))
    return (tuple(sorted(pos)),tuple(sorted(neg)))

class_values=defaultdict(list)
all_traces=[]
for p in permutations(range(3)):
    for b in range(8):
        eperm=to_edge_permutation(p,b)
        t=trace_on_H3(eperm)
        klass=signed_class(p,b)
        class_values[klass].append(t)
        all_traces.append((p,b,klass,t))
assert len(all_traces)==48 and sum(map(len,class_values.values()))==48
assert len(class_values)==10
assert all(len(set(v))==1 for v in class_values.values())
print('signed_cycle_class (positive_lengths,negative_lengths) | size | trace_H3')
for k in sorted(class_values): print(k,len(class_values[k]),class_values[k][0])
print('dim_invariants_full_group=',sum(t for *_,t in all_traces)//48)
assert sum(t for *_,t in all_traces)%48==0
center=next(t for p,b,_,t in all_traces if p==(0,1,2) and b==7)
print('central_antipodal_trace=',center,'plus_minus_dimensions=',(32+center)//2,(32-center)//2)
print('total_automorphisms=',len(all_traces))

print("orientation_preserving_invariants=",sum(t for p,b,cls,t in all_traces if (((-1)**(sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)))) * ((-1)**(b.bit_count())))==1)//24)
