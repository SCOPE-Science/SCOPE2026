from itertools import combinations
from collections import Counter

FACETS = [
(1,2,3,5),(1,2,3,15),(1,2,5,13),(1,2,7,13),(1,2,7,15),
(1,3,4,14),(1,3,4,15),(1,3,5,14),(1,4,11,12),(1,4,11,14),(1,4,12,15),
(1,5,9,13),(1,5,9,14),(1,7,10,12),(1,7,10,13),(1,7,12,15),
(1,9,10,11),(1,9,10,13),(1,9,11,14),(1,10,11,12),
(2,3,5,12),(2,3,6,12),(2,3,6,15),(2,5,11,12),(2,5,11,13),
(2,6,10,12),(2,6,10,14),(2,6,14,15),(2,7,8,13),(2,7,8,14),(2,7,14,15),
(2,8,10,11),(2,8,10,14),(2,8,11,13),(2,10,11,12),
(3,4,10,13),(3,4,10,14),(3,4,13,15),(3,5,8,12),(3,5,8,14),
(3,6,9,12),(3,6,9,13),(3,6,13,15),(3,8,9,10),(3,8,9,12),(3,8,10,14),(3,9,10,13),
(4,5,6,7),(4,5,6,11),(4,5,7,8),(4,5,8,12),(4,5,11,12),(4,6,7,10),(4,6,10,14),(4,6,11,14),
(4,7,8,13),(4,7,10,13),(4,8,12,15),(4,8,13,15),
(5,6,7,9),(5,6,9,13),(5,6,11,13),(5,7,8,14),(5,7,9,14),
(6,7,9,12),(6,7,10,12),(6,11,13,15),(6,11,14,15),
(7,9,12,15),(7,9,14,15),(8,9,10,11),(8,9,11,15),(8,9,12,15),(8,11,13,15),(9,11,14,15)
]
F = {tuple(sorted(f)) for f in FACETS}
assert len(F) == 75
faces = {k:set() for k in range(1,5)}
for f in F:
    for k in range(1,5):
        for s in combinations(f,k): faces[k].add(tuple(sorted(s)))
assert tuple(len(faces[k]) for k in range(1,5)) == (15,90,150,75)
vertices=sorted(faces[1]); edges=sorted(faces[2]); triangles=sorted(faces[3])
edge_index={e:i for i,e in enumerate(edges)}
vertex_index={v[0]:i for i,v in enumerate(vertices)}

def bitxor_basis(vectors):
    basis={}
    for x in vectors:
        y=x
        while y:
            p=y.bit_length()-1
            if p in basis: y ^= basis[p]
            else:
                basis[p]=y
                break
    return basis

def reduce_vec(x,basis):
    y=x
    for p in sorted(basis, reverse=True):
        if (y>>p)&1: y ^= basis[p]
    return y

def edge_chain(es):
    x=0
    for e in es: x ^= 1 << edge_index[tuple(sorted(e))]
    return x

def tri_boundary(t):
    return edge_chain(combinations(t,2))

def edge_boundary(e):
    return (1<<vertex_index[e[0]]) ^ (1<<vertex_index[e[1]])

B1_basis = bitxor_basis(tri_boundary(t) for t in triangles)
d1_basis = bitxor_basis(edge_boundary(e) for e in edges)
assert len(B1_basis)==74
assert len(d1_basis)==14
cycle_dim=len(edges)-len(d1_basis)
H1_dim=cycle_dim-len(B1_basis)
assert cycle_dim==76 and H1_dim==2

missing=[]; noncycles=[]
for t in combinations(range(1,16),3):
    if t in faces[3]: continue
    if all(tuple(sorted(e)) in faces[2] for e in combinations(t,2)): missing.append(t)
    else: noncycles.append(t)
assert len(missing)==120 and len(noncycles)==185
remainders=[reduce_vec(tri_boundary(t),B1_basis) for t in missing]
assert all(remainders)
class_counts=Counter(remainders)
assert sorted(class_counts.values()) == [40,40,40] and len(class_counts)==3
# Since any simple cycle has at least three edges, these are exactly the length-3 nonzero cycles.

# Published generators of action 15^15 = [3]A5 = GL(2,4).
def cycperm(cycles):
    p=list(range(1,16))
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): p[a-1]=b
    return tuple(p)
gens=[
    cycperm([(1,9,10,3,14),(2,15,7,12,6),(4,5,11,13,8)]),
    cycperm([(1,4,10),(2,5,8),(3,7,11),(6,9,15),(12,14,13)]),
    cycperm([(1,2,15),(4,5,6),(8,9,10),(12,13,14)]),
]
def compose(p,q): return tuple(p[q[i]-1] for i in range(15))
idp=tuple(range(1,16)); group={idp}; stack=[idp]
while stack:
    x=stack.pop()
    for g in gens:
        y=compose(g,x)
        if y not in group: group.add(y); stack.append(y)
assert len(group)==180
assert all({tuple(sorted(p[i-1] for i in f)) for f in F}==F for p in group)
remaining=set(missing); orbit_records=[]
while remaining:
    rep=min(remaining)
    orbit={tuple(sorted(p[i-1] for i in rep)) for p in group}
    assert orbit <= set(missing)
    counts=Counter(reduce_vec(tri_boundary(t),B1_basis) for t in orbit)
    orbit_records.append((rep,len(orbit),sorted(counts.values())))
    remaining -= orbit
orbit_records.sort(key=lambda x:x[1], reverse=True)
assert [(r,n,c) for r,n,c in orbit_records] == [((1,2,10),90,[30,30,30]),((1,2,12),30,[10,10,10])]
print('VERIFY_OK f=15,90,150,75 ranks_d1_d2=14,74 H1_F2=2 missing3=120 essential3=120 class_counts=40,40,40 systole=3 aut_group=180 orbit_sizes=90,30 orbit_reps=1-2-10,1-2-12 orbit_class_counts=30x3,10x3')
