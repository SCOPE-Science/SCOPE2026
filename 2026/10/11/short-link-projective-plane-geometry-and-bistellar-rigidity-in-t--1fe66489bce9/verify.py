#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict, deque

# Köhler--Lutz Table 6 orbit representatives for the 13-vertex triangulation
# of SU(3)/SO(3), with labels 1,...,13.  The affine group 13:3 acts on
# residues 0,...,12 by x -> a*x+b, a in {1,3,9}; labels are residue+1.
REPS = [
    (1,2,3,4,5,8),
    (1,2,3,4,5,9),
    (1,2,3,4,7,9),
    (1,2,3,5,6,9),
    (1,2,3,5,8,10),
    (1,2,3,7,9,12),
]
EXPECTED_ORBIT_SIZES = [39,39,39,13,13,13]


def aff_perm(a,b):
    return {x: ((a*(x-1)+b) % 13)+1 for x in range(1,14)}

GROUP = [aff_perm(a,b) for a in (1,3,9) for b in range(13)]
assert len(GROUP)==39

def act(face,g):
    return tuple(sorted(g[x] for x in face))

def orbit(face):
    return {act(face,g) for g in GROUP}

facet_orbits = [orbit(r) for r in REPS]
assert [len(o) for o in facet_orbits] == EXPECTED_ORBIT_SIZES
for i,j in combinations(range(6),2):
    assert facet_orbits[i].isdisjoint(facet_orbits[j])
FACETS = set().union(*facet_orbits)
assert len(FACETS)==156

# All faces by cardinality.
faces = {k:set() for k in range(1,7)}
for F in FACETS:
    for k in range(1,7):
        faces[k].update(combinations(F,k))
fvec = tuple(len(faces[k]) for k in range(1,7))
assert fvec == (13,78,286,533,468,156), fvec
assert len(faces[2]) == 78 and len(faces[3]) == 286  # 3-neighborly

# Link of a face, as the full simplicial link represented by its facets.
def link_facets(sigma):
    S=set(sigma)
    raw=[]
    for F in FACETS:
        if S.issubset(F):
            raw.append(frozenset(set(F)-S))
    # inclusion-maximal residual faces only
    mx=[]
    for R in raw:
        if not any(R < T for T in raw):
            mx.append(R)
    return set(mx)

# Tetrahedron links in a closed 5-manifold are 1-spheres. Verify directly and census lengths.
tet_link_len = {}
for tet in sorted(faces[4]):
    lf = link_facets(tet)
    # each residual facet must be an edge; graph must be a connected 2-regular simple cycle
    assert all(len(e)==2 for e in lf), (tet,lf)
    V=set().union(*lf)
    deg=Counter()
    adj=defaultdict(set)
    for e in lf:
        u,v=tuple(e)
        deg[u]+=1;deg[v]+=1
        adj[u].add(v);adj[v].add(u)
    assert all(deg[v]==2 for v in V), (tet,deg)
    q=deque([next(iter(V))]); seen=set()
    while q:
        x=q.popleft()
        if x in seen: continue
        seen.add(x); q.extend(adj[x]-seen)
    assert seen==V
    assert len(lf)==len(V)
    tet_link_len[tet]=len(lf)
link_spectrum=Counter(tet_link_len.values())
assert link_spectrum == Counter({3:91,4:195,5:195,6:52}), link_spectrum

short = {t for t,L in tet_link_len.items() if L==3}
assert len(short)==91

# Group orbits on short-link tetrahedra.
unseen=set(short); short_orbits=[]
while unseen:
    r=min(unseen)
    o=orbit(r) & short
    assert orbit(r) <= short  # invariant property
    short_orbits.append((r,orbit(r)))
    unseen -= orbit(r)
short_orbits.sort(key=lambda ro:(len(ro[1]),ro[0]))
short_sizes=sorted(len(o) for _,o in short_orbits)
assert short_sizes == [13,39,39], short_sizes

# Canonical representatives from the exact reconstructed labeling.
short_by_size=defaultdict(list)
for r,o in short_orbits:
    short_by_size[len(o)].append((r,o))
assert len(short_by_size[13])==1 and len(short_by_size[39])==2
small_rep, small_orbit = short_by_size[13][0]
# The size-13 orbit contains the +1 relabeling of Kühnel's <0,1,4,6>.
assert (1,2,5,7) in small_orbit

# 2-(13,4,1) design check for this 13-block orbit.
pair_counts=Counter()
for B in small_orbit:
    for p in combinations(B,2):
        pair_counts[p]+=1
assert len(pair_counts)==78
assert set(pair_counts.values())=={1}

# Obtain exact link triangles for convenient representatives.
def link_vertices_of_tet(tet):
    lf=link_facets(tet)
    return tuple(sorted(set().union(*lf)))
canon_reps = [(1,2,3,10),(1,2,4,8),(1,2,5,7)]
for r in canon_reps:
    assert r in short
rep_links={r:link_vertices_of_tet(r) for r in canon_reps}
assert rep_links[(1,2,3,10)] == (5,6,8)
assert rep_links[(1,2,4,8)] == (3,5,13)
assert rep_links[(1,2,5,7)] == (9,12,13)
assert sorted(len(orbit(r)) for r in canon_reps)==[13,39,39]
assert set().union(*(orbit(r) for r in canon_reps))==short

# Exhaustive positive-index bistellar moves in dimension 5.
# A move of index i in {1,...,5} at a (5-i)-simplex sigma is legal iff
# lk(sigma) is exactly boundary(tau) for an i-simplex tau absent from K.
# Here boundary(tau) has i+1 vertices and maximal faces of cardinality i.

def full_link_faces(sigma):
    S=set(sigma)
    out={frozenset()}  # empty face
    for F in FACETS:
        if S.issubset(F):
            R=set(F)-S
            for k in range(1,len(R)+1):
                for c in combinations(R,k):
                    out.add(frozenset(c))
    return out

def boundary_faces(tau):
    T=tuple(tau)
    out={frozenset()}
    for k in range(1,len(T)):  # all proper nonempty subsets
        for c in combinations(T,k): out.add(frozenset(c))
    return out

def is_face(face):
    return tuple(sorted(face)) in faces[len(face)] if face else True

move_centers=defaultdict(list)
for i in range(1,6):
    sigma_card=6-i  # (5-i)-simplex has cardinality 6-i
    for sigma in sorted(faces[sigma_card]):
        lk=full_link_faces(sigma)
        verts=sorted(set().union(*(set(x) for x in lk))) if lk else []
        if len(verts)!=i+1:
            continue
        tau=tuple(verts)
        if is_face(tau):
            continue
        if lk == boundary_faces(tau):
            move_centers[i].append((sigma,tau))
assert {i:len(move_centers[i]) for i in range(1,6)} == {1:0,2:0,3:0,4:0,5:0}

# Extra cross-check: all codimension-one faces have exactly two containing facets.
for ridge in faces[5]:
    n=sum(set(ridge).issubset(F) for F in FACETS)
    assert n==2, (ridge,n)

print(
    "VERIFY_OK "
    f"f={','.join(map(str,fvec))} "
    "facet_orbits=39,39,39,13,13,13 "
    "tet_link_spectrum=3:91,4:195,5:195,6:52 "
    "short_orbits=13,39,39 "
    "pg23_blocks=13 pair_lambda=1 "
    "short_reps=1-2-3-10|1-2-4-8|1-2-5-7 "
    "short_links=5-6-8|3-5-13|9-12-13 "
    "positive_bistellar_moves=1:0,2:0,3:0,4:0,5:0"
)
