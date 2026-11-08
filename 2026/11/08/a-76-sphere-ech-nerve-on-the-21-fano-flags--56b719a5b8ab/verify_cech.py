#!/usr/bin/env python3
"""Reproducible exact finite certificate for the 3/2-ball Čech nerve of the Fano incidence line graph."""
from collections import Counter, deque
import json, hashlib

# The seven lines of the Fano plane are translates of {0,1,3} in Z/7Z.
incidences = tuple(sorted((p,ell) for ell in range(7) for p in (ell,(ell+1)%7,(ell+3)%7)))
assert len(incidences)==21
adj=[set() for _ in incidences]
for i,(p,L) in enumerate(incidences):
    for j,(q,M) in enumerate(incidences):
        if i!=j and (p==q or L==M):adj[i].add(j)
assert all(len(nb)==4 for nb in adj)
edges=tuple((i,j) for i in range(21) for j in sorted(adj[i]) if i<j)
assert len(edges)==42

def faces_for_scale(scale):
    # Use graph-vertex and edge-midpoint centres as geometric witnesses.
    if scale==2:
        generating=[sum(1<<v for v in ({i}|adj[i])) for i in range(21)]
    elif scale==3:
        generating=[sum(1<<v for v in ({i,j}|adj[i]|adj[j])) for i,j in edges]
    else:raise ValueError
    faces=set()
    for m in generating:
        s=m
        while s:
            faces.add(s)
            s=(s-1)&m
    return generating, faces

def morse(faces, vertex_order):
    # Patchwork: greedily match all presently unmatched faces toggleable at
    # each successive vertex; verify the global oriented Hasse graph below.
    rest=set(faces); matched=[]
    for v in vertex_order:
        bit=1<<v
        for f in sorted(rest):
            if not (f&bit) and f|bit in rest:
                rest.remove(f);rest.remove(f|bit);matched.append((f,f|bit))
    return matched,rest

def test_acyclic(faces,pairs):
    up={a:b for a,b in pairs}
    indegree={f:0 for f in faces}
    outs={f:[] for f in faces}
    incidences_count=0
    for high in faces:
        s=high
        while s:
            bit=s&(-s);low=high^bit;s-=bit
            if not low:continue # empty face excluded from ordinary Morse poset
            incidences_count+=1
            if up.get(low)==high:
                outs[low].append(high);indegree[high]+=1
            else:
                outs[high].append(low);indegree[low]+=1
    Q=deque(x for x in faces if indegree[x]==0)
    seen=0
    while Q:
        v=Q.popleft();seen+=1
        for u in outs[v]:
            indegree[u]-=1
            if indegree[u]==0:Q.append(u)
    assert seen==len(faces),(seen,len(faces))
    return incidences_count

def mod2_ranks(faces):
    levels={d: sorted(f for f in faces if f.bit_count()-1==d) for d in range(7)}
    ranks={}
    for d in range(1,7):
        ix={v:i for i,v in enumerate(levels[d-1])}
        basis={}
        for f in levels[d]:
            b=0;u=f
            while u:
                bit=u&(-u);u-=bit
                b ^= 1<<ix[f^bit]
            while b:
                pivot=b.bit_length()-1
                if pivot not in basis:
                    basis[pivot]=b
                    break
                b ^= basis[pivot]
        ranks[d]=len(basis)
    betti={d:len(levels[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(7)}
    betti[0]-=1
    return ranks,betti

generating,faces=faces_for_scale(3)
assert len(set(generating))==42
# Independent face-membership count by enumerating all 2^21 vertex subsets.
# Covers any potential missing face, even if it is not in the subset-enumerator.
facet_masks=set(generating)
native_faces=sum(1 for s in range(1,1<<21) if any(s&f==s for f in facet_masks))
assert native_faces==len(faces)
assert len(faces)==3395
vec=tuple(sum(x.bit_count()==d+1 for x in faces) for d in range(7))
assert vec==(21,210,854,1155,819,294,42)
assert sum((-1)**d*c for d,c in enumerate(vec))==77
ranks,betti=mod2_ranks(faces)
assert betti=={0:0,1:0,2:76,3:0,4:0,5:0,6:0}
for order in [list(range(21)),list(range(20,-1,-1))]:
    pairs,critical=morse(faces,order)
    assert len(pairs)==1659
    assert Counter(f.bit_count()-1 for f in critical)=={0:1,2:76}
    assert test_acyclic(faces,pairs)==sum((d+1)*vec[d] for d in range(1,7))

_,before=faces_for_scale(2)
oldpairs,oldcritical=morse(before,range(21))
assert len(oldpairs)==223
assert Counter(f.bit_count()-1 for f in oldcritical)=={0:1,1:8}
assert test_acyclic(before,oldpairs)==1323
oldranks,oldbetti=mod2_ranks(before)
assert oldbetti.get(1)==8
assert oldbetti.get(2)==0
result={
 'graph':'line graph of the Fano-plane Heawood incidence graph',
 'graph_vertices':len(incidences), 'graph_edges':len(edges),
 'scale_2_face_count':len(before), 'scale_2_morse_pairs':len(oldpairs), 'scale_2_hasse_incidences':1323, 'scale_2_reduced_mod2_betti':oldbetti,
 'scale_3_facets':len(facet_masks),'scale_3_f_vector':vec,'scale_3_face_count_nonempty':len(faces),
 'scale_3_hasse_incidences':test_acyclic(faces,morse(faces,range(21))[0]),
 'morse_pairs_each_order':1659,'morse_critical_cells':{'0':1,'2':76},
 'scale_3_mod2_boundary_ranks':ranks,'scale_3_reduced_mod2_betti':betti,
 'acyclic_matching_orders':2,'integral_homotopy':'wedge of 76 copies of S^2',
 'status':'HEAWOOD_LINE_CECH3_WEDGE76_VERIFIED'}
print(json.dumps(result,sort_keys=True,indent=2))
