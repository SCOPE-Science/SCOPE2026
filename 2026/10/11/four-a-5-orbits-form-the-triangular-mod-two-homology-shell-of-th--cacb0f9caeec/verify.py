#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

FACETS = {
(1,2,3),(1,2,8),(1,3,7),(1,4,6),(1,4,10),(1,5,7),(1,5,9),(1,6,8),(1,9,10),
(2,3,6),(2,4,7),(2,4,9),(2,5,6),(2,5,10),(2,7,10),(2,8,9),(3,4,5),(3,4,10),
(3,5,9),(3,6,8),(3,7,9),(3,8,10),(4,5,8),(4,6,9),(4,7,8),(5,6,7),(5,8,10),
(6,7,10),(6,9,10),(7,8,9)
}
V=tuple(range(1,11))
ALL_EDGES=sorted(combinations(V,2))
assert len(ALL_EDGES)==45
E=set()
for f in FACETS:
    E.update(tuple(sorted(e)) for e in combinations(f,2))
assert E==set(ALL_EDGES)
assert (len(V),len(E),len(FACETS))==(10,45,30)
assert 10-len(E)+len(FACETS)==-5
# Closed surface checks.
for e in E:
    assert sum(set(e)<=set(f) for f in FACETS)==2
for v in V:
    lk=[]
    for f in FACETS:
        if v in f:
            a,b=sorted(set(f)-{v}); lk.append((a,b))
    deg=Counter(x for e in lk for x in e)
    verts=set(deg)
    assert len(lk)==len(verts) and all(deg[x]==2 for x in verts)
    adj={x:[] for x in verts}
    for a,b in lk: adj[a].append(b);adj[b].append(a)
    seen={next(iter(verts))}; stack=list(seen)
    while stack:
        u=stack.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w);stack.append(w)
    assert seen==verts

# Contract the star spanning tree T={(1,i):i=2..10}. Non-tree edges among 2..10 form cycle lattice basis.
NT=sorted(combinations(range(2,11),2))
NI={e:i for i,e in enumerate(NT)}
assert len(NT)==36

def tri_vec(t):
    x=0
    for e in combinations(sorted(t),2):
        if 1 not in e:
            x ^= 1<<NI[e]
    return x

def rref(rows):
    B={}
    for x in rows:
        y=x
        for p in sorted(B,reverse=True):
            if (y>>p)&1: y ^= B[p]
        if not y: continue
        p=y.bit_length()-1
        for q in list(B):
            if (B[q]>>p)&1: B[q]^=y
        B[p]=y
    return dict(sorted(B.items(),reverse=True))

def reduce_vec(x,B):
    y=x
    for p,row in B.items():
        if (y>>p)&1: y^=row
    return y

B=rref([tri_vec(f) for f in sorted(FACETS)])
assert len(B)==29
free=[i for i in range(36) if i not in B]
assert len(free)==7

def compact(x):
    r=reduce_vec(x,B)
    y=0
    for j,p in enumerate(free):
        if (r>>p)&1: y |= 1<<j
    return y

def expand_compact(y):
    x=0
    for j,p in enumerate(free):
        if (y>>j)&1: x |= 1<<p
    return x

ALL_TRI=sorted(combinations(V,3))
EMPTY=[t for t in ALL_TRI if t not in FACETS]
assert len(ALL_TRI)==120 and len(EMPTY)==90
classes=[compact(tri_vec(t)) for t in EMPTY]
assert all(classes)
cc=Counter(classes)
assert len(cc)==41
mult=Counter(cc.values())
assert mult==Counter({2:25,1:10,5:6})

# Exhaust all simplicial automorphisms with triple-incidence pruning.
FSET=set(FACETS)
order=V
AUT=[]
mp={}; used=set()
def rec(i):
    if i==len(order):
        image={tuple(sorted(mp[x] for x in f)) for f in FSET}
        if image==FSET:
            AUT.append(tuple(mp[v] for v in V))
        return
    v=order[i]
    for w in V:
        if w in used: continue
        mp[v]=w; used.add(w)
        ok=True
        assigned=order[:i]
        for a,b in combinations(assigned,2):
            if ((tuple(sorted((a,b,v))) in FSET) != (tuple(sorted((mp[a],mp[b],w))) in FSET)):
                ok=False; break
        if ok: rec(i+1)
        used.remove(w); del mp[v]
rec(0)
AUT=set(AUT)
assert len(AUT)==60

# Published generators: (1 3 5 7 9)(2 4 6 8 10) and (1 9)(3 4)(5 10)(6 7).
def perm_from_cycles(cycles):
    p=list(V)
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): p[a-1]=b
    return tuple(p)
g=perm_from_cycles([(1,3,5,7,9),(2,4,6,8,10)])
h=perm_from_cycles([(1,9),(3,4),(5,10),(6,7)])
def compose(p,q): return tuple(p[q[i]-1] for i in range(10))
G={tuple(V)}; todo=[tuple(V)]
while todo:
    a=todo.pop()
    for b in (g,h):
        c=compose(a,b)
        if c not in G: G.add(c);todo.append(c)
assert len(G)==60 and G==AUT

def pset(S,p): return tuple(sorted(p[v-1] for v in S))
remaining=set(EMPTY); carrier_orbits=[]
while remaining:
    rep=min(remaining)
    orb={pset(rep,p) for p in AUT}
    assert orb<=set(EMPTY)
    carrier_orbits.append((rep,orb))
    remaining-=orb
assert [(r,len(o)) for r,o in carrier_orbits]==[
    ((1,2,4),20),((1,2,6),30),((1,2,7),30),((1,2,10),10)
]

# Induced action on H1: realize quotient coordinate as graph cycle, permute its edge chain,
# then convert back to contracted-tree coordinates.
def graph_chain_from_nt(x):
    edges=set()
    for i,e in enumerate(NT):
        if (x>>i)&1:
            a,b=e; edges.symmetric_difference_update({e,(1,a),(1,b)})
    return edges

def nt_from_graph_cycle(edges):
    x=0
    for e in edges:
        e=tuple(sorted(e))
        if 1 not in e: x ^= 1<<NI[e]
    # The non-tree coordinates uniquely determine a cycle after tree contraction.
    return x

def act_class(y,p):
    x=expand_compact(y)
    edges=graph_chain_from_nt(x)
    pedges={tuple(sorted((p[a-1],p[b-1]))) for a,b in edges}
    return compact(nt_from_graph_cycle(pedges))

# Validate action on every triangular carrier.
for p in AUT:
    for t in EMPTY:
        assert act_class(compact(tri_vec(t)),p)==compact(tri_vec(pset(t,p)))

sigs=[]; seen_class_orbits=[]
for rep,orb in carrier_orbits:
    c=compact(tri_vec(rep))
    corb={act_class(c,p) for p in AUT}
    image={compact(tri_vec(t)) for t in orb}
    assert image==corb
    vals={cc[z] for z in corb}
    assert len(vals)==1
    fib=next(iter(vals))
    assert len(orb)==len(corb)*fib
    sigs.append((len(orb),len(corb),fib))
    seen_class_orbits.append(corb)
assert sigs==[(20,10,2),(30,6,5),(30,15,2),(10,10,1)]
assert sum(map(len,seen_class_orbits))==41
for i,a in enumerate(seen_class_orbits):
    for b in seen_class_orbits[i+1:]: assert a.isdisjoint(b)
# Orbit count on all 127 nonzero classes, for context.
rem=set(range(1,128)); all_orbits=[]
while rem:
    c=min(rem); o={act_class(c,p) for p in AUT}; all_orbits.append(o); rem-=o
assert len(all_orbits)==15

print('VERIFY_OK f=10,45,30 surface=N7 H1_F2_dim=7 graph_triangles=120 facial3=30 empty3=90 all_empty3_nonzero=yes simple_F2_1_systole=3 distinct_triangular_classes=41 class_multiplicity_profile=1x10,2x25,5x6 aut=A5_order60 carrier_orbits=20,30,30,10 class_orbits=10,6,15,10 fibers=2,5,2,1 all_nonzero_class_orbits=15')
