import itertools, json, pathlib, collections
HERE=pathlib.Path(__file__).resolve().parent
expected=json.loads((HERE/'CENSUS.json').read_text())
V=tuple(range(6))
FACETS=tuple(tuple(int(c) for c in s) for s in expected['facets'])
FACETSET={frozenset(t) for t in FACETS}
FACES={frozenset()}
for F in FACETSET:
    for r in (1,2,3):
        for s in itertools.combinations(F,r): FACES.add(frozenset(s))
# Surface checks.
edges=tuple(itertools.combinations(V,2)); eidx={e:i for i,e in enumerate(edges)}
assert all(frozenset(e) in FACES for e in edges)
edge_deg={e:sum(set(e)<=set(T) for T in FACETS) for e in edges}
assert set(edge_deg.values())=={2}
for v in V:
    nbr={u for u in V if u!=v and frozenset((u,v)) in FACES}
    link_edges={tuple(sorted((a,b))) for a,b in itertools.combinations(nbr,2) if frozenset((v,a,b)) in FACETSET}
    deg={u:sum(u in e for e in link_edges) for u in nbr}
    assert len(nbr)==5 and len(link_edges)==5 and set(deg.values())=={2}
assert 6-len(edges)+len(FACETS)==1
# Exhaustive simplicial maps.
def simplicial(f):
    return all(frozenset(f[i] for i in T) in FACES for T in FACETS)
maps=[f for f in itertools.product(V,repeat=6) if simplicial(f)]
assert len(maps)==expected['simplicial_self_maps']
image_dist=collections.Counter(len(set(f)) for f in maps)
assert {str(k):image_dist.get(k,0) for k in range(1,7)}==expected['image_size_distribution']
M=set(maps)
# Automorphisms independently as permutations preserving the facet set.
autos=[]
for p in itertools.permutations(V):
    img={frozenset(p[i] for i in T) for T in FACETS}
    if img==FACETSET: autos.append(p)
A=set(autos)
assert len(A)==expected['automorphisms']==60
assert A=={f for f in M if len(set(f))==6}
# GF(2) rank.
def gf2_rank(rows):
    rows=[sum((int(x)&1)<<j for j,x in enumerate(row)) for row in rows]
    rank=0; col=0
    while col and False: pass
    # Gaussian elimination over bit-packed rows, pivoting by highest available column.
    for c in range(max((r.bit_length() for r in rows), default=0)-1,-1,-1):
        p=next((i for i in range(rank,len(rows)) if (rows[i]>>c)&1),None)
        if p is None: continue
        rows[rank],rows[p]=rows[p],rows[rank]
        for i in range(len(rows)):
            if i!=rank and ((rows[i]>>c)&1): rows[i]^=rows[rank]
        rank+=1
    return rank
# d1: vertices x edges, d2: edges x triangles.
d1=[[0]*len(edges) for _ in V]
for j,(a,b) in enumerate(edges): d1[a][j]=d1[b][j]=1
d2=[[0]*len(FACETS) for _ in edges]
for j,T in enumerate(FACETS):
    for e in itertools.combinations(sorted(T),2): d2[eidx[e]][j]=1
assert gf2_rank(d1)==5
assert gf2_rank(d2)==9
assert len(edges)-5-9==expected['h1_f2_dimension']==1
# Explicit H1 generator and dual cocycle.
cycle=[tuple(map(int,s)) for s in expected['cycle_generator_edges']]
coc={tuple(map(int,s)) for s in expected['cocycle_support_edges']}
# cycle has zero boundary mod 2.
par={v:0 for v in V}
for a,b in cycle: par[a]^=1; par[b]^=1
assert not any(par.values())
# cocycle vanishes on every triangle boundary.
assert all(sum(tuple(sorted(e)) in coc for e in itertools.combinations(T,2))%2==0 for T in FACETS)
assert sum(tuple(sorted(e)) in coc for e in cycle)%2==1
# Induced H1 bit on the generator.
def h1bit(f):
    z=0
    for a,b in cycle:
        x,y=f[a],f[b]
        if x!=y and tuple(sorted((x,y))) in coc: z^=1
    return z
ones={f for f in M if h1bit(f)}
assert ones==A
assert len(M-A)==expected['zero_h1_action_maps']
# Contiguity graph reduced to one-coordinate moves.
def contiguous(f,g):
    return all(frozenset([f[i] for i in T]+[g[i] for i in T]) in FACES for T in FACETS)
def neigh(f):
    a=list(f)
    for i in V:
        old=a[i]
        for y in V:
            if y==old: continue
            a[i]=y; g=tuple(a)
            if g in M and contiguous(f,g): yield g
        a[i]=old
edge_count=sum(1 for f in maps for g in neigh(f) if f<g)
assert edge_count==expected['one_coordinate_contiguity_edges']
start=(0,0,0,0,0,0)
seen={start}; stack=[start]
while stack:
    f=stack.pop()
    for g in neigh(f):
        if g not in seen: seen.add(g); stack.append(g)
assert len(seen)==6336
assert seen==M-A
assert all(not any(True for _ in neigh(a)) for a in A)
assert sorted([len(seen)]+[1]*len(A),reverse=True)==sorted(expected['contiguity_component_sizes'],reverse=True)
print('VERIFY_OK maps=6396 image=6,930,5400,0,0,60 autos=60 edges=40860 components=6336+60x1 h1=6336zero+60identity')
