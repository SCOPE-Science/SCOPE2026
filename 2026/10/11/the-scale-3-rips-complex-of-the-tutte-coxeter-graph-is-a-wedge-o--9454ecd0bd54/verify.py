#!/usr/bin/env python3
from itertools import combinations
from collections import deque, defaultdict

U=tuple(range(6))
DUADS=tuple(combinations(U,2))

def perfect_matchings(vertices):
    vertices=tuple(vertices)
    if not vertices:
        return [()]
    a=vertices[0]
    out=[]
    for i in range(1,len(vertices)):
        b=vertices[i]
        rest=vertices[1:i]+vertices[i+1:]
        for m in perfect_matchings(rest):
            out.append(tuple(sorted(((min(a,b),max(a,b)),)+m)))
    return out

SYNTHEMES=tuple(sorted(set(perfect_matchings(U))))
assert len(DUADS)==15 and len(SYNTHEMES)==15
D_index={e:i for i,e in enumerate(DUADS)}
S_index={m:15+i for i,m in enumerate(SYNTHEMES)}
N=30
adj=[set() for _ in range(N)]
for m in SYNTHEMES:
    sm=S_index[m]
    for e in m:
        de=D_index[e]
        adj[de].add(sm); adj[sm].add(de)
assert all(len(a)==3 for a in adj)
assert sum(map(len,adj))//2==45

# Exact graph distances.
dist=[[99]*N for _ in range(N)]
for s in range(N):
    dist[s][s]=0
    q=deque([s])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if dist[s][v]==99:
                dist[s][v]=dist[s][u]+1
                q.append(v)
assert max(max(r) for r in dist)==4

def disjoint_edges(e,f): return set(e).isdisjoint(f)
# Verify the distance dictionary used in the proof.
for i,e in enumerate(DUADS):
    for j,f in enumerate(DUADS):
        if i==j: assert dist[i][j]==0
        else: assert dist[i][j]==(2 if disjoint_edges(e,f) else 4)
for i,m in enumerate(SYNTHEMES):
    for j,n in enumerate(SYNTHEMES):
        a,b=15+i,15+j
        if i==j: assert dist[a][b]==0
        else: assert dist[a][b]==(2 if set(m)&set(n) else 4)
for i,e in enumerate(DUADS):
    for j,m in enumerate(SYNTHEMES):
        assert dist[i][15+j]==(1 if e in m else 3)

# Threshold-3 graph: all cross edges, plus disjointness on duads,
# plus common-duad adjacency on synthemes.
for u,v in combinations(range(N),2):
    edge=(dist[u][v] <= 3)
    if u<15 and v<15:
        expected=disjoint_edges(DUADS[u],DUADS[v])
    elif u>=15 and v>=15:
        expected=bool(set(SYNTHEMES[u-15]) & set(SYNTHEMES[v-15]))
    else:
        expected=True
    assert edge==expected

# Factor K_D: matching complex M(K6).
KD_edges=[]
KD_tri=[]
for a,b in combinations(range(15),2):
    if disjoint_edges(DUADS[a],DUADS[b]): KD_edges.append((a,b))
for tri in combinations(range(15),3):
    if all(disjoint_edges(DUADS[a],DUADS[b]) for a,b in combinations(tri,2)):
        KD_tri.append(tri)
assert (len(KD_edges),len(KD_tri))==(45,15)
edge_to_tri=defaultdict(int)
for t in KD_tri:
    for e in combinations(t,2): edge_to_tri[tuple(sorted(e))]+=1
assert set(edge_to_tri)==set(KD_edges)
assert all(c==1 for c in edge_to_tri.values())

# Factor K_S: clique complex of the graph of synthemes sharing a duad.
KS_edges=[]; KS_tri=[]
for a,b in combinations(range(15),2):
    if set(SYNTHEMES[a]) & set(SYNTHEMES[b]): KS_edges.append((a,b))
for tri in combinations(range(15),3):
    if all(set(SYNTHEMES[a]) & set(SYNTHEMES[b]) for a,b in combinations(tri,2)):
        KS_tri.append(tri)
assert (len(KS_edges),len(KS_tri))==(45,15)
# No four synthemes are pairwise adjacent, so the clique complex has dimension 2.
for quad in combinations(range(15),4):
    assert not all(set(SYNTHEMES[a]) & set(SYNTHEMES[b]) for a,b in combinations(quad,2))
edge_to_triS=defaultdict(int)
for t in KS_tri:
    common=set(SYNTHEMES[t[0]]) & set(SYNTHEMES[t[1]]) & set(SYNTHEMES[t[2]])
    assert len(common)==1
    for e in combinations(t,2): edge_to_triS[tuple(sorted(e))]+=1
assert set(edge_to_triS)==set(KS_edges)
assert all(c==1 for c in edge_to_triS.values())

# Connectivity of both 1-skeleta.
def connected(n,edges):
    g=[set() for _ in range(n)]
    for a,b in edges:g[a].add(b);g[b].add(a)
    seen={0}; q=deque([0])
    while q:
        u=q.popleft()
        for v in g[u]:
            if v not in seen: seen.add(v);q.append(v)
    return len(seen)==n
assert connected(15,KD_edges) and connected(15,KS_edges)
# Each factor collapses one free edge from each of 15 triangles,
# leaving a connected graph with 15 vertices and 30 edges, hence rank 16.
assert 30-15+1==16

# Enumerate the full threshold-3 Rips complex as a join and cross-check its f-vector.
KD_faces={():True}
for i in range(15): KD_faces[(i,)]=True
for e in KD_edges: KD_faces[e]=True
for t in KD_tri: KD_faces[t]=True
KS_faces={():True}
for i in range(15): KS_faces[(15+i,)]=True
for a,b in KS_edges: KS_faces[(15+a,15+b)]=True
for t in KS_tri: KS_faces[tuple(15+x for x in t)]=True
faces_by_dim=defaultdict(set)
for a in KD_faces:
    for b in KS_faces:
        face=tuple(sorted(a+b))
        if face: faces_by_dim[len(face)-1].add(face)
fvec=tuple(len(faces_by_dim[d]) for d in range(max(faces_by_dim)+1))
assert fvec==(30,315,1380,2475,1350,225)

# Independently enumerate all cliques of the actual threshold-3 graph and compare
# with the join enumeration, so no higher-dimensional factor clique can be missed.
th_adj=[set() for _ in range(N)]
for u,v in combinations(range(N),2):
    if dist[u][v] <= 3:
        th_adj[u].add(v); th_adj[v].add(u)
actual_faces=set()
def extend(prefix,candidates):
    for k,v in enumerate(candidates):
        face=prefix+(v,)
        actual_faces.add(face)
        nxt=[w for w in candidates[k+1:] if w in th_adj[v]]
        if nxt: extend(face,nxt)
extend((),list(range(N)))
join_faces=set().union(*faces_by_dim.values())
assert actual_faces==join_faces

# Exact F2 boundary ranks and Betti numbers as an independent algebraic cross-check.
def rank_f2(columns):
    piv={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else: piv[p]=x; break
    return len(piv)

ranks={}
maxd=max(faces_by_dim)
for d in range(1,maxd+1):
    low=sorted(faces_by_dim[d-1]); idx={s:i for i,s in enumerate(low)}
    cols=[]
    for s in sorted(faces_by_dim[d]):
        x=0
        for f in combinations(s,d): x ^= 1<<idx[f]
        cols.append(x)
    ranks[d]=rank_f2(cols)
betti=[]
for d in range(maxd+1):
    betti.append(len(faces_by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0))
assert tuple(betti)==(1,0,0,256,0,0)

print('VERIFY_OK')
print('vertices=30 edges=45 diameter=4')
print('factor_fvector=(15,45,15) for both factors')
print('factor_homotopy=wedge^16 S^1 for both factors')
print('rips_scale3_fvector='+repr(fvec))
print('rips_scale3_betti_F2='+repr(tuple(betti)))
print('conclusion=VR_<=3(Tutte-Coxeter) ~= wedge^256 S^3')
