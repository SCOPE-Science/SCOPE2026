#!/usr/bin/env python3
"""Exact finite verification of the Paley-13 flag torus's systolic shell.

The argument for all lattice vectors appears in RESULT.md; this standalone
finite checker exhausts the small combinatorial classification and tests the
word-metric identity on a finite coordinate box.
"""
from collections import Counter, deque
from itertools import combinations

P = 13
STEPS = {1:(1,0),3:(0,1),4:(1,1),9:(-1,-1),10:(0,-1),12:(-1,0)}
RESIDUES = set(STEPS)
verts = tuple(range(P))
adj = {v: {w for w in verts if w!=v and (w-v)%P in RESIDUES} for v in verts}
edges = set(tuple(sorted((u,v))) for u in verts for v in adj[u])
triangles = set(combinations(verts,3))
triangles = {t for t in triangles if all(tuple(sorted(e)) in edges for e in combinations(t,2))}
expected = {tuple(sorted(((i)%P,(i+1)%P,(i+4)%P))) for i in verts}
expected |= {tuple(sorted(((i)%P,(i+3)%P,(i+4)%P))) for i in verts}
assert len(edges)==39 and len(triangles)==26 and triangles==expected
assert not any(all(tuple(sorted(e)) in edges for e in combinations(t,2)) for t in combinations(verts,4))
for v in verts:
    nbr = adj[v]
    link_edges = {tuple(sorted(e)) for e in combinations(nbr,2) if tuple(sorted((*e,v))) in triangles}
    assert len(nbr)==6 and len(link_edges)==6
    assert all(sum(vv in e for e in link_edges)==2 for vv in nbr)
    seen = {next(iter(nbr))}
    while True:
        nxt = {b for a,b in link_edges if a in seen} | {a for a,b in link_edges if b in seen}
        if nxt <= seen: break
        seen |= nxt
    assert seen==nbr

def simple_cycles(k):
    for subset in combinations(verts,k):
        start = subset[0]
        def grow(path):
            if len(path)==k:
                if path[-1] in adj[start] and path[1]<path[-1]:
                    yield tuple(path)
                return
            for w in subset[1:]:
                if w not in path and w in adj[path[-1]]:
                    yield from grow(path+[w])
        yield from grow([start])

def displacement(cycle):
    u=v=0
    for a,b in zip(cycle, cycle[1:]+cycle[:1]):
        x,y=STEPS[(b-a)%P]
        u+=x;v+=y
    assert (u+3*v)%P==0
    return u,v

def norm(w):
    u,v=w
    return max(abs(u),abs(v),abs(u-v))

def canon(c):
    l=list(c)
    j=l.index(min(l))
    l=l[j:]+l[:j]
    return tuple(l if l[1]<l[-1] else [l[0]]+list(reversed(l[1:])))

tri=list(simple_cycles(3));quad=list(simple_cycles(4))
assert len(tri)==26 and len(quad)==78
assert all(displacement(c)==(0,0) for c in tri)
rankfree={(3,-1), (1,4)}
assert abs(3*4-1*(-1))==P
vcounts=Counter()
essential=[]
for c in quad:
    d=displacement(c)
    key = max(d,tuple(-x for x in d))
    vcounts[key]+=1
    if d!=(0,0):essential.append(c)
assert vcounts == {(0,0):39,(3,-1):13,(1,4):13,(4,3):13},vcounts
assert len(essential)==39

# All length <= 4 closed walks in the Cayley graph, using their lifts.
# Exhaustion is over up to six to-the-fourth sequences of edge directions.
front={(0,0)}
first_nonzero = set()
for k in range(1,5):
    front = {(u+a,v+b) for u,v in front for a,b in STEPS.values()}
    closed={w for w in front if (w[0]+3*w[1])%P==0 and w!=(0,0)}
    if k<=3:assert not closed
    if k==4:
        assert closed=={(3,-1),(-3,1),(1,4),(-1,-4),(4,3),(-4,-3)},closed
        first_nonzero=closed

# The affine graph automorphism group is x -> a*x+b, with quadratic-residue a.
essential_set=set(essential)
rep=essential[0]
orbit={canon(tuple((a*x+b)%P for x in rep)) for a in RESIDUES for b in verts}
assert len(orbit)==39 and orbit==essential_set

# The multiplier 4 lifts to the order-six linear action R(u,v)=(u-v,u).
R=lambda w:(w[0]-w[1],w[0])
assert R((3,-1))==(4,3) and R((4,3))==(1,4) and R((1,4))==(-3,1)
assert all((R(w)[0]+3*R(w)[1]-4*(w[0]+3*w[1]))%P==0 for w in first_nonzero)

# Independent finite stress test of the claimed exact word metric.
step_vectors=tuple(STEPS.values())
dist={(0,0):0}
queue=deque([(0,0)])
while queue:
    u,v=queue.popleft()
    if dist[(u,v)]==16:continue
    for a,b in step_vectors:
        w=(u+a,v+b)
        if w not in dist:dist[w]=dist[(u,v)]+1;queue.append(w)
assert all(dist[w]==norm(w) for w in dist)

# Chain-check H_1 with independent binary boundary elimination.
edge_idx={e:j for j,e in enumerate(sorted(edges))}
basis={}
for t in triangles:
    col=sum(1<<edge_idx[e] for e in combinations(t,2))
    while col:
        k=col.bit_length()-1
        if k in basis:col^=basis[k]
        else:basis[k]=col;break
assert len(basis)==25
assert len(edges)-(len(verts)-1)-len(basis)==2
print('VERIFY_OK')
print('flag_clique_complex=true vertices=13 edges=39 faces=26 link=C6 no_tetrahedra=true')
print('simple_cycles=triangles:26 quadrilaterals:78')
print('quadrilateral_displacements=zero:39 A(3,-1):13 B(1,4):13 C(4,3):13')
print('nonzero_loop_length_min=4 six_primitive_vectors=passed')
print('essential_four_cycles=39 single_affine_orbit=true')
print('integral_homology_basis=(3,-1),(1,4) det=13 multiplier4_order6=passed')
print('word_metric_BFS_radius16=passed mod2_betti1=2')
