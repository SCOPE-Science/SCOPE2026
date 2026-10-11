#!/usr/bin/env python3
import itertools, json, collections, sys
from functools import lru_cache

ORDER=(0,20,23,1,8,22,11,3,2,21,5,4,16,17,7,14,15,19,13,10,12,6,9,18)
ORDER2=(0,2,14,5,1,23,17,13,8,19,20,3,21,10,12,11,15,9,22,4,16,7,6,18)
ORDER3=(19,13,5,0,2,9,15,20,16,14,1,8,7,23,4,17,3,12,21,11,6,18,22,10)
EXPECTED_F=(24,228,1112,3042,4848,4592,2592,822,112)
EXPECTED_CRIT={0:1,4:5,5:2}

# Vertices of the regular truncated octahedron, indexed lexicographically.
V=[]
for perm in sorted(set(itertools.permutations((0,1,2)))):
    for signs in itertools.product((-1,1), repeat=2):
        a=[]; k=0
        for x in perm:
            if x==0: a.append(0)
            else: a.append(x*signs[k]); k+=1
        V.append(tuple(a))
V=sorted(set(V))
assert len(V)==24

# Edge graph: nearest Euclidean neighbors (squared distance 2).
adj=[set() for _ in V]
for i,j in itertools.combinations(range(24),2):
    if sum((V[i][t]-V[j][t])**2 for t in range(3))==2:
        adj[i].add(j); adj[j].add(i)
assert all(len(a)==3 for a in adj) and sum(map(len,adj))//2==36

# All-pairs graph distances.
dist=[]
for s in range(24):
    ds=[None]*24; ds[s]=0; q=collections.deque([s])
    while q:
        u=q.popleft()
        for w in adj[u]:
            if ds[w] is None: ds[w]=ds[u]+1; q.append(w)
    assert all(x is not None for x in ds)
    dist.append(ds)
assert max(max(r) for r in dist)==6

# Graph power at radius 4.
pow_adj=[set() for _ in V]
for i,j in itertools.combinations(range(24),2):
    if dist[i][j] <= 4:
        pow_adj[i].add(j); pow_adj[j].add(i)
assert sum(map(len,pow_adj))//2==228

# Maximal cliques by Bron-Kerbosch.
max_cliques=[]
def bronk(R,P,X):
    if not P and not X:
        max_cliques.append(tuple(sorted(R))); return
    # Pivot chosen deterministically.
    U=P|X
    u=max(U, key=lambda x: len(P & pow_adj[x])) if U else None
    for v in sorted(P - (pow_adj[u] if u is not None else set())):
        bronk(R|{v}, P & pow_adj[v], X & pow_adj[v])
        P.remove(v); X.add(v)
bronk(set(),set(range(24)),set())
max_cliques=sorted(set(max_cliques))
facet_sizes=collections.Counter(map(len,max_cliques))
assert facet_sizes==collections.Counter({9:112,8:30,7:24,6:52})

# Every nonempty simplex from maximal cliques.
faces=set()
for c in max_cliques:
    for k in range(1,len(c)+1):
        faces.update(itertools.combinations(c,k))
bydim=collections.Counter(len(s)-1 for s in faces)
fvec=tuple(bydim[d] for d in range(max(bydim)+1))
assert fvec==EXPECTED_F and len(faces)==17372

# Repeated-toggle matching.
alive=set(faces); pairs=[]
for v in ORDER:
    candidates=[]
    for s in sorted(alive,key=lambda x:(len(x),x)):
        if v not in s:
            up=tuple(sorted(s+(v,)))
            if up in alive: candidates.append((s,up))
    for lo,up in candidates:
        if lo in alive and up in alive:
            alive.remove(lo); alive.remove(up); pairs.append((lo,up))
assert len(pairs)==8682
crit=collections.Counter(len(s)-1 for s in alive)
assert dict(crit)==EXPECTED_CRIT
lo2up={a:b for a,b in pairs}; up2lo={b:a for a,b in pairs}
assert len(lo2up)==len(up2lo)==len(pairs)

# Verify every pair is a Hasse cover.
for lo,up in pairs:
    assert len(up)==len(lo)+1 and set(lo)<set(up) and lo in faces and up in faces

# Verify global acyclicity of the oriented Hasse graph.
# Unmatched covers point from coface down; matched covers point up.
nodes=list(faces); indeg={s:0 for s in nodes}; out={s:[] for s in nodes}
matched=set(pairs); covers=0
for up in nodes:
    if len(up)==1: continue
    for i in range(len(up)):
        lo=up[:i]+up[i+1:]; covers+=1
        if (lo,up) in matched: a,b=lo,up
        else: a,b=up,lo
        out[a].append(b); indeg[b]+=1
q=collections.deque([s for s in nodes if indeg[s]==0]); seen=0
while q:
    a=q.popleft(); seen+=1
    for b in out[a]:
        indeg[b]-=1
        if indeg[b]==0:q.append(b)
assert seen==len(nodes)

# Exact integral Morse boundary C5^M -> C4^M.
def incidence(face,cell):
    for i in range(len(cell)):
        if cell[:i]+cell[i+1:]==face:
            return 1 if i%2==0 else -1
    raise AssertionError('not a facet')

crit4=sorted(s for s in alive if len(s)==5)
crit5=sorted(s for s in alive if len(s)==6)
@lru_cache(None)
def reduce4(s):
    if s in alive: return {s:1}
    if s in up2lo: return {}  # paired downward with a 3-cell
    if s in lo2up:
        u=lo2up[s]; a=incidence(s,u); ans={}
        for i in range(len(u)):
            t=u[:i]+u[i+1:]
            if t==s: continue
            c=-incidence(t,u)*a
            for q0,v0 in reduce4(t).items(): ans[q0]=ans.get(q0,0)+c*v0
        return {q0:v0 for q0,v0 in ans.items() if v0}
    raise AssertionError(('unclassified cell',s))
mb=[]
for s in crit5:
    ans={}
    for i in range(len(s)):
        t=s[:i]+s[i+1:]
        c=1 if i%2==0 else -1
        for q0,v0 in reduce4(t).items(): ans[q0]=ans.get(q0,0)+c*v0
    row=[ans.get(q0,0) for q0 in crit4]
    mb.append(row)
assert mb==[[0]*5,[0]*5]


# Verify the other nontrivial integer scales by the same construction.
def build_faces(scale):
    pa=[set() for _ in V]
    for i,j in itertools.combinations(range(24),2):
        if dist[i][j] <= scale:
            pa[i].add(j); pa[j].add(i)
    m=[]
    def bk(R,P,X):
        if not P and not X:
            m.append(tuple(sorted(R))); return
        U=P|X; u=max(U,key=lambda x:len(P & pa[x])) if U else None
        for v in sorted(P-(pa[u] if u is not None else set())):
            bk(R|{v},P & pa[v],X & pa[v]); P.remove(v); X.add(v)
    bk(set(),set(range(24)),set())
    fs=set()
    for c in m:
        for k in range(1,len(c)+1): fs.update(itertools.combinations(c,k))
    return fs

def toggle_critical(fs, order):
    a=set(fs); prs=[]
    for v in order:
        cand=[]
        for s0 in sorted(a,key=lambda x:(len(x),x)):
            if v not in s0:
                u0=tuple(sorted(s0+(v,)))
                if u0 in a: cand.append((s0,u0))
        for lo0,up0 in cand:
            if lo0 in a and up0 in a:
                a.remove(lo0); a.remove(up0); prs.append((lo0,up0))
    # global DAG check
    md=set(prs); indeg0={x:0 for x in fs}; out0={x:[] for x in fs}
    for up0 in fs:
        if len(up0)==1: continue
        for i0 in range(len(up0)):
            lo0=up0[:i0]+up0[i0+1:]
            x,y=(lo0,up0) if (lo0,up0) in md else (up0,lo0)
            out0[x].append(y); indeg0[y]+=1
    q0=collections.deque(x for x in fs if indeg0[x]==0); seen0=0
    while q0:
        x=q0.popleft(); seen0+=1
        for y in out0[x]:
            indeg0[y]-=1
            if indeg0[y]==0:q0.append(y)
    assert seen0==len(fs)
    return a,prs

f2=build_faces(2); c2,p2=toggle_critical(f2,ORDER2)
assert collections.Counter(len(x)-1 for x in c2)==collections.Counter({0:1,2:9})
f3=build_faces(3); c3,p3=toggle_critical(f3,ORDER3)
assert collections.Counter(len(x)-1 for x in c3)==collections.Counter({0:1,2:1})
# Scale 1 is the connected 24-vertex, 36-edge graph, hence cycle rank 13.
assert 36-24+1==13
# At scale 5 the only missing edges are the 12 antipodal pairs v,-v.
missing5=[]
for i,j in itertools.combinations(range(24),2):
    if dist[i][j]>5: missing5.append((i,j))
assert len(missing5)==12 and all(tuple(-a for a in V[i])==V[j] for i,j in missing5)
# Thus the scale-5 clique complex is the boundary of the 12-dimensional cross-polytope, S^11.
assert all(dist[i][j] <= 6 for i,j in itertools.combinations(range(24),2))

cert={
  'vertices':len(V),'edges':36,'diameter':6,'scale':4,'power_edges':228,
  'maximal_cliques':len(max_cliques),'facet_size_counts':dict(sorted(facet_sizes.items())),
  'face_vector':list(fvec),'nonempty_simplices':len(faces),'hasse_covers':covers,
  'matching_pairs':len(pairs),'critical_counts':dict(sorted(crit.items())),
  'critical_4_cells':[list(x) for x in crit4],
  'critical_5_cells':[list(x) for x in crit5],
  'morse_boundary_5_to_4':mb,'acyclic':True,
  'scale_1_homotopy':'wedge_13_S1',
  'scale_2_critical_counts':dict(sorted(collections.Counter(len(x)-1 for x in c2).items())),
  'scale_3_critical_counts':dict(sorted(collections.Counter(len(x)-1 for x in c3).items())),
  'scale_5_antipodal_pairs':len(missing5),'scale_5_homotopy':'S11','scale_6_homotopy':'contractible'
}
print(json.dumps(cert,sort_keys=True))
print('VERIFY_OK')
