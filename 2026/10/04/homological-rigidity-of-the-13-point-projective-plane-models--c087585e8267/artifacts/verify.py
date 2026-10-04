#!/usr/bin/env python3
from itertools import combinations

# One of the two opposite 13-point minimal finite models of RP^2.
# A = vertices of K4, B = edges of K4, C = perfect matchings of K4.
# Covers are a<b for incidence, and b<c when b is NOT in matching c.
A = tuple(f"a{i}" for i in range(1,5))
pairs = tuple(combinations(range(1,5),2))
B = tuple(f"b{i+1}" for i in range(6))
edge_pair = dict(zip(B,pairs))
edge_name = {p:b for b,p in edge_pair.items()}
matchings = (
    frozenset(((1,2),(3,4))),
    frozenset(((1,3),(2,4))),
    frozenset(((1,4),(2,3))),
)
C = tuple(f"c{i+1}" for i in range(3))
nodes = A+B+C
covers=[]
for b,(i,j) in edge_pair.items():
    covers.extend(((f"a{i}",b),(f"a{j}",b)))
for c,M in zip(C,matchings):
    for p in pairs:
        if p not in M:
            covers.append((edge_name[p],c))

# Transitive closure.
le={(x,x) for x in nodes}|set(covers)
changed=True
while changed:
    changed=False
    for x,y in tuple(le):
        for u,v in tuple(le):
            if y==u and (x,v) not in le:
                le.add((x,v)); changed=True

# Order complex C_*(P;F2).
strict=tuple((x,y) for x in nodes for y in nodes if x!=y and (x,y) in le)
tri=tuple((x,y,z) for x in nodes for y in nodes for z in nodes
          if len({x,y,z})==3 and (x,y) in le and (y,z) in le)
idx0={x:i for i,x in enumerate(nodes)}
idx1={e:i for i,e in enumerate(strict)}

def rank_gf2(rows,ncols):
    rows=[sum((int(bit)&1)<<j for j,bit in enumerate(r)) for r in rows]
    r=0
    for c in range(ncols):
        p=next((i for i in range(r,len(rows)) if (rows[i]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(len(rows)):
            if i!=r and ((rows[i]>>c)&1): rows[i]^=rows[r]
        r+=1
    return r

# Boundary d1: C1 -> C0 and d2: C2 -> C1 over F2.
d1=[]
for x,y in strict:
    row=[0]*len(nodes); row[idx0[x]]=row[idx0[y]]=1; d1.append(row)
# d1 matrix is 13 x 36; rank equals rank of transpose rows above.
rank_d1=rank_gf2(d1,len(nodes))
d2_cols=[]
for x,y,z in tri:
    col=[0]*len(strict)
    for e in ((x,y),(y,z),(x,z)): col[idx1[e]]=1
    d2_cols.append(col)
rank_d2=rank_gf2(d2_cols,len(strict))
b1=len(strict)-rank_d1-rank_d2
assert (len(nodes),len(strict),len(tri),b1)==(13,36,24,1)

# The order complex is a closed connected triangulated surface with Euler characteristic 1.
tri_sets=[frozenset(t) for t in tri]
for e in strict:
    es=frozenset(e)
    assert sum(es <= T for T in tri_sets)==2
for v in nodes:
    nbr={u for e in strict if v in e for u in e if u!=v}
    link_edges=[]
    for T in tri_sets:
        if v in T:
            other=tuple(T-{v})
            link_edges.append(frozenset(other))
    deg={u:0 for u in nbr}
    adj={u:set() for u in nbr}
    for e in link_edges:
        u,w2=tuple(e); deg[u]+=1; deg[w2]+=1; adj[u].add(w2); adj[w2].add(u)
    assert all(d==2 for d in deg.values())
    seen=set(); stack=[next(iter(nbr))]
    while stack:
        u=stack.pop()
        if u in seen: continue
        seen.add(u); stack.extend(adj[u]-seen)
    assert seen==nbr
assert len(nodes)-len(strict)+len(tri)==1

# Compute an H^1 cocycle w not a coboundary by linear algebra over F2.
# delta0 columns are incidence vectors of vertices in edges; delta1 rows are triangle boundaries.
def rref_vectors(vectors,n):
    vs=list(vectors); piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,len(vs)) if (vs[i]>>c)&1),None)
        if p is None: continue
        vs[r],vs[p]=vs[p],vs[r]
        for i in range(len(vs)):
            if i!=r and ((vs[i]>>c)&1): vs[i]^=vs[r]
        piv.append(c); r+=1
    return vs,piv

# Kernel of delta1 = vectors on strict edges annihilating triangle boundaries.
triangle_masks=[]
for x,y,z in tri:
    m=0
    for e in ((x,y),(y,z),(x,z)): m ^= 1<<idx1[e]
    triangle_masks.append(m)
R,pivs=rref_vectors(triangle_masks,len(strict))
free=[c for c in range(len(strict)) if c not in pivs]
ker=[]
for f in free:
    v=1<<f
    for rr,p in enumerate(pivs):
        if (R[rr]>>f)&1: v ^= 1<<p
    ker.append(v)
# Coboundary span delta0.
cob=[]
for x in nodes:
    m=0
    for i,(u,v) in enumerate(strict):
        if x==u or x==v: m ^= 1<<i
    cob.append(m)
_,cob_pivs=rref_vectors(cob,len(strict)); cob_rank=len(cob_pivs)
def span_rank(vs): return len(rref_vectors(vs,len(strict))[1])
w=next(v for v in ker if span_rank(cob+[v])>cob_rank)

# A 6-edge loop in the K4-incidence layer; it pairs nontrivially with w.
z_edges=(("a1","b1"),("a2","b1"),("a2","b4"),("a3","b4"),("a3","b2"),("a1","b2"))
assert sum((w>>idx1[e])&1 for e in z_edges)%2==1

cover_up={x:[] for x in nodes}; cover_down={x:[] for x in nodes}
for x,y in covers:
    cover_up[x].append(y); cover_down[y].append(x)

def h1_action(assign):
    s=0
    for x,y in z_edges:
        fx,fy=assign[x],assign[y]
        if fx!=fy:
            assert (fx,fy) in le
            s ^= (w>>idx1[(fx,fy)])&1
    return s

def inverse_isotone(assign):
    inv={v:k for k,v in assign.items()}
    return all((inv[x],inv[y]) in le for x,y in le)

# Exact enumeration of isotone self-maps. MRV chooses the next domain point;
# checking cover constraints is sufficient because the order is their transitive closure.
assign={}; total=nonzero=bijective=bad_nonzero=0

def recurse():
    global total,nonzero,bijective,bad_nonzero
    if len(assign)==len(nodes):
        total+=1
        nz=h1_action(assign)
        bij=len(set(assign.values()))==len(nodes)
        if bij:
            bijective+=1
            assert inverse_isotone(assign)
        if nz:
            nonzero+=1
            if not bij: bad_nonzero+=1
        return
    best=None; bestcand=None
    for x in nodes:
        if x in assign: continue
        cand=[]
        for t in nodes:
            if all((assign[u],t) in le for u in cover_down[x] if u in assign) and \
               all((t,assign[v]) in le for v in cover_up[x] if v in assign):
                cand.append(t)
        if bestcand is None or len(cand)<len(bestcand):
            best,bestcand=x,cand
            if len(cand)<=1: break
    for t in bestcand:
        assign[best]=t; recurse(); del assign[best]

recurse()
assert total==562333
assert bijective==24
assert nonzero==24
assert bad_nonzero==0

# Structural automorphism count: every permutation of A extends uniquely by its action
# on 2-subsets B and on the three perfect matchings C.
from itertools import permutations
assert sum(1 for _ in permutations(A))==24

print("VERIFY_OK")
print(f"simplices={len(nodes)},{len(strict)},{len(tri)}")
print(f"dim_H1_F2={b1}")
print(f"isotone_self_maps={total}")
print(f"bijective_self_maps={bijective}")
print(f"H1_nonzero_self_maps={nonzero}")
print(f"H1_nonzero_nonhomeomorphisms={bad_nonzero}")
