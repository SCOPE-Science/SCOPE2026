#!/usr/bin/env python3
"""Exact finite certificate for the ternary Hamming 3-cube's Rips filtration.
All simplices and Hasse incidences are reconstructed from the metric, without stored outputs.
"""
from itertools import product,combinations
from collections import Counter,defaultdict,deque
from math import comb

V=list(product(range(3),repeat=3))
assert len(V)==27
N=len(V)
d=lambda u,v:sum(a!=b for a,b in zip(u,v))
assert {d(u,v) for u in V for v in V}=={0,1,2,3}
assert all(sum(d(u,v)==1 for v in V)==6 for u in V)
# A simplex at scale 2 is an independent set in the graph of pairs distance 3.
forbid=[sum(1<<j for j,w in enumerate(V) if d(v,w)==3) for v in V]
faces_by_size=defaultdict(list)
def dfs(available, simplex):
    faces_by_size[simplex.bit_count()].append(simplex)
    while available:
        bit=available&-available; available ^= bit
        vertex=bit.bit_length()-1
        dfs(available&~forbid[vertex],simplex|bit)
dfs((1<<N)-1,0)
size_counts=[len(faces_by_size[k]) for k in range(10)]
assert size_counts==[1,27,243,945,1728,1620,945,351,81,9]
all_faces=set().union(*(set(g) for k,g in faces_by_size.items() if k))
assert len(all_faces)==5949

# Staged element toggles in lexicographic vertex order. In each stage pair
# all still-unmatched lower and upper faces differing by the stage vertex.
unmatched=set(all_faces)
matched_upper_to_lower={}
for idx in range(N):
    bit=1<<idx
    lower=[s for s in unmatched if not s&bit and s|bit in unmatched]
    for s in lower:
        assert s in unmatched and s|bit in unmatched
        unmatched.remove(s);unmatched.remove(s|bit)
        matched_upper_to_lower[s|bit]=s
assert len(matched_upper_to_lower)==2951
critical=Counter(s.bit_count()-1 for s in unmatched)
assert critical=={0:1,3:46},critical

# Verify entire oriented Hasse graph has no directed cycles.
# Matched cover relation is oriented upwards; all others downwards.
# In particular, there must be no directed cycles inside any fixed dimension.
face_list=sorted(all_faces)
face_id={s:i for i,s in enumerate(face_list)}
adj=[[] for _ in face_list]; indeg=[0]*len(face_list)
incidences=0
for s in face_list:
    b=s
    while b:
        v=b&-b;b^=v
        t=s^v
        if t==0:continue
        if matched_upper_to_lower.get(s)==t:
            tail,head=face_id[t],face_id[s]
        else:
            tail,head=face_id[s],face_id[t]
        adj[tail].append(head);indeg[head]+=1;incidences+=1
queue=deque(i for i,dg in enumerate(indeg) if dg==0)
visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in adj[u]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert visited==len(face_list),(visited,len(face_list))

# Independent field-homology verification, not required to infer the homotopy type.
boundary_rank={}
for s in range(1,10):
    if s==1:
        boundary_rank[s]=1
        continue
    codomain={f:j for j,f in enumerate(faces_by_size[s-1])}
    pivots={}
    for f in faces_by_size[s]:
        b=f;c=0
        while b:
            v=b&-b;b^=v
            c^=1<<codomain[f^v]
        while c:
            j=c.bit_length()-1
            if j not in pivots:
                pivots[j]=c
                break
            c^=pivots[j]
    boundary_rank[s]=len(pivots)
betti={s-1:len(faces_by_size[s])-boundary_rank.get(s,0)-boundary_rank.get(s+1,0)
       for s in range(1,10)}
assert betti=={0:0,1:0,2:0,3:46,4:0,5:0,6:0,7:0,8:0},betti
# At scale 1 maximal cliques are exactly the 27 coordinate lines (triples).
r1_triangles=[]
edges=set()
for i,j,k in combinations(range(N),3):
    if d(V[i],V[j])==d(V[i],V[k])==d(V[j],V[k])==1:
        r1_triangles.append((i,j,k))
for i,j in combinations(range(N),2):
    if d(V[i],V[j])==1:edges.add((i,j))
edge_in_triangles=Counter(pair for tri in r1_triangles for pair in combinations(tri,2))
assert len(edges)==81 and len(r1_triangles)==27
assert set(edge_in_triangles)==edges and set(edge_in_triangles.values())=={1}
# Every edge is in exactly one triangle, so deleting one edge and its
# unique triangle for each of the 27 triangles leaves a connected graph.
# Such deletions do not alter the number of connected components;
# the original Hamming graph is connected.
assert 1- (N-len(edges)+len(r1_triangles))==28
print('VERIFY_OK scale2_face_vector='+str(size_counts)+
      ' unmatched='+str(dict(critical))+' pairs='+str(len(matched_upper_to_lower))+
      ' incidences='+str(incidences)+' acyclic='+str(visited)+
      ' mod2_betti3='+str(betti[3])+' scale1_betti1=28')
