#!/usr/bin/env python3
"""Exact finite verification of the induced-degree-one complex of K2 x K3 x K3."""
from collections import Counter, deque
from itertools import combinations
N=18
mask_full=(1<<N)-1
coords=[(q,i,j) for q in range(2) for i in range(3) for j in range(3)]
adj=[0]*N
for u,(q,i,j) in enumerate(coords):
    for v,(r,k,l) in enumerate(coords):
        if q!=r and i!=k and j!=l:
            adj[u]|=1<<v
edges=[(u,v) for u in range(N) for v in range(u+1,N) if adj[u]>>v&1]
assert len(edges)==36 and all(x.bit_count()==4 for x in adj)
# Independent forbidden-triple characterization: selected vertices form a matching plus isolates.
forbid={((1<<u)|(1<<v)|(1<<w)) for v in range(N) for u,w in combinations([k for k in range(N) if adj[v]>>k&1],2)}
assert len(forbid)==108
faces=[]
for m in range(1,1<<N):
    a=m; ok=True
    while a:
        b=a&-a; a^=b
        v=b.bit_length()-1
        if (m&adj[v]).bit_count()>1:
            ok=False;break
    if ok:faces.append(m)
faces2=[m for m in range(1,1<<N) if all(m&t!=t for t in forbid)]
assert faces==faces2
F=set(faces)
assert len(F)==8564
facets=Counter(m.bit_count()-1 for m in F if not any(((m|(1<<v)) in F) for v in range(N) if not m>>v&1))
active=set(F);pairmap={};pairs=[];by_pivot=[]
for v in range(N):
    bit=1<<v; c=0
    for m in faces:
        if m in active and not (m&bit) and (m|bit) in active:
            active.remove(m);active.remove(m|bit)
            pairmap[m]=m|bit;pairs.append((m,m|bit));c+=1
    by_pivot.append(c)
assert len(pairs)==4273
crit=Counter(m.bit_count()-1 for m in active)
assert crit=={0:1,5:17},crit
# Verify exact directed cover relation acyclicity by topological sort.
indegree={m:0 for m in F};out={m:[] for m in F};edges_count=0
for top in F:
    r=top
    while r:
        bit=r&-r;r^=bit
        bottom=top^bit
        if not bottom:continue
        assert bottom in F
        u,v=(bottom,top) if pairmap.get(bottom)==top else (top,bottom)
        out[u].append(v);indegree[v]+=1;edges_count+=1
queue=deque(m for m in F if indegree[m]==0);visited=0
while queue:
    u=queue.popleft();visited+=1
    for v in out[u]:
        indegree[v]-=1
        if indegree[v]==0:queue.append(v)
assert visited==len(F),(visited,len(F))
# Direct independent F2 homology (every boundary, no Morse reduction).
by_dim={d:[m for m in faces if m.bit_count()-1==d] for d in range(9)}
ranks={}
for d in range(1,9):
    lookup={x:j for j,x in enumerate(by_dim[d-1])}
    piv={}
    for m in by_dim[d]:
        col=0;r=m
        while r:
            b=r&-r;r^=b
            col^=1<<lookup[m^b]
        while col:
            hi=col.bit_length()-1
            if hi not in piv:piv[hi]=col;break
            col^=piv[hi]
    ranks[d]=len(piv)
reduced={d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in range(9)}
assert reduced=={0:0,1:0,2:0,3:0,4:0,5:17,6:0,7:0,8:0},reduced
fvec={d:len(xs) for d,xs in by_dim.items()}
print('VERIFY_TRIPLE_PRODUCT_F1_EXACT_MORSE_OK')
print('vertices=18 edges=36 degree=4 forbidden_triples=108')
print('nonempty_faces=',len(F),'facets_by_dimension=',dict(sorted(facets.items())))
print('nonempty_faces_by_dimension=',fvec)
print('matching_pairs=',len(pairs),'pair_count_by_pivot=',by_pivot)
print('critical_cells=',dict(sorted(crit.items())))
print('hasse_incidences=',edges_count,'complete_acyclicity_vertices=',visited)
print('mod2_boundary_ranks=',dict(sorted(ranks.items())))
print('reduced_mod2_betti=',{k:v for k,v in reduced.items() if v})
print('homotopy_type=17 copies of S^5 by integral discrete Morse theory')
