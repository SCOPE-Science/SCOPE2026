#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict
from functools import lru_cache

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,8),(1,4,7,8),(1,5,6,9),(1,5,7,9),(1,6,8,9),(1,7,8,9),(2,3,4,9),
(2,3,5,10),(2,3,9,10),(2,4,6,11),(2,4,9,11),(2,5,6,12),(2,5,8,12),
(2,5,8,13),(2,5,10,13),(2,6,11,14),(2,6,12,14),(2,8,12,14),(2,8,13,15),
(2,8,14,15),(2,9,10,13),(2,9,11,16),(2,9,13,16),(2,11,14,15),
(2,11,15,16),(2,13,15,16),(3,4,7,16),(3,4,9,15),(3,4,14,15),
(3,4,14,16),(3,5,7,11),(3,5,10,11),(3,7,11,13),(3,7,13,16),(3,8,9,10),
(3,8,9,15),(3,8,10,11),(3,8,11,12),(3,8,12,14),(3,8,14,15),
(3,11,12,13),(3,12,13,14),(3,13,14,16),(4,5,8,13),(4,5,8,16),
(4,5,10,13),(4,5,10,15),(4,5,14,15),(4,5,14,16),(4,6,8,13),(4,6,11,13),
(4,7,8,16),(4,9,11,12),(4,9,12,15),(4,10,12,13),(4,10,12,15),
(4,11,12,13),(5,6,9,12),(5,7,9,14),(5,7,11,14),(5,8,12,16),(5,9,12,16),
(5,9,14,16),(5,10,11,15),(5,11,14,15),(6,7,11,13),(6,7,11,14),
(6,7,12,14),(6,7,12,15),(6,7,13,15),(6,8,9,15),(6,8,13,15),(6,9,12,15),
(7,8,9,10),(7,8,10,16),(7,9,10,14),(7,10,12,14),(7,10,12,15),
(7,10,15,16),(7,13,15,16),(8,10,11,16),(8,11,12,16),(9,10,13,14),
(9,11,12,16),(9,13,14,16),(10,11,15,16),(10,12,13,14)
}
V = tuple(range(1,17))

def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
Q = sorted(FACETS)
assert (len(V),len(E),len(T),len(Q)) == (16,109,186,93)
EI = {e:i for i,e in enumerate(E)}
TI = {t:i for i,t in enumerate(T)}

# Boundary columns over F_2, stored as bit vectors.
D2 = []
for t in T:
    x = 0
    for e in combinations(t,2):
        x ^= 1 << EI[e]
    D2.append(x)
D3 = []
for q in Q:
    x = 0
    for t in combinations(q,3):
        x ^= 1 << TI[t]
    D3.append(x)

def rref_basis(rows):
    B = {}
    for x in rows:
        y = x
        for p in sorted(B, reverse=True):
            if (y >> p) & 1:
                y ^= B[p]
        if not y:
            continue
        p = y.bit_length()-1
        for q in list(B):
            if (B[q] >> p) & 1:
                B[q] ^= y
        B[p] = y
    return dict(sorted(B.items(), reverse=True))

def reduce_mod(x,B):
    y = x
    for p,row in B.items():
        if (y >> p) & 1:
            y ^= row
    return y

B2 = rref_basis(D2)
B3 = rref_basis(D3)
assert (len(B2),len(B3),len(T)-len(B2)-len(B3)) == (93,92,1)

TMASK = [sum(1 << (v-1) for v in t) for t in T]

def local_cycle_basis(mask):
    piv = {}
    cycles = []
    for i,bnd in enumerate(D2):
        if TMASK[i] & ~mask:
            continue
        y = bnd
        combo = 1 << i
        for p in sorted(piv, reverse=True):
            if (y >> p) & 1:
                y ^= piv[p][0]
                combo ^= piv[p][1]
        if y:
            piv[y.bit_length()-1] = (y,combo)
        else:
            cycles.append(combo)
    return cycles

def ambient_image_basis(S):
    mask = sum(1 << (v-1) for v in S)
    reps = []
    for z in local_cycle_basis(mask):
        r = reduce_mod(z,B3)
        if r:
            reps.append(r)
    return rref_basis(reps)

support_counts = {}
carriers = []
for k in range(1,10):
    count = 0
    for S in combinations(V,k):
        if ambient_image_basis(S):
            count += 1
            if k == 9:
                carriers.append(S)
    support_counts[k] = count
assert support_counts == {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:37}
assert len(carriers) == 37

# Collapse machinery on the induced subcomplex, always keeping all nine vertices.
def induced_maximal_facets(S):
    ss = set(S)
    simplices = set()
    for q in Q:
        for k in range(1,5):
            for c in combinations(q,k):
                if set(c) <= ss:
                    simplices.add(tuple(c))
    return frozenset(s for s in simplices if not any(set(s) < set(t) for t in simplices))

def all_simplices(maxs):
    out = set()
    for m in maxs:
        for k in range(1,len(m)+1):
            out.update(combinations(m,k))
    return out

def surface_profile(maxs):
    sims = all_simplices(maxs)
    vs = sorted({x for s in sims for x in s})
    es = sorted(s for s in sims if len(s)==2)
    ts = sorted(s for s in sims if len(s)==3)
    qs = [s for s in sims if len(s)==4]
    if qs:
        return None
    inc = Counter()
    links = {v:[] for v in vs}
    for t in ts:
        for e in combinations(t,2):
            inc[tuple(sorted(e))] += 1
        a,b,c = t
        links[a].append(tuple(sorted((b,c))))
        links[b].append(tuple(sorted((a,c))))
        links[c].append(tuple(sorted((a,b))))
    manifold = bool(ts) and len(inc)==len(es) and all(x==2 for x in inc.values())
    if manifold:
        gadj = defaultdict(list)
        for a,b in es:
            gadj[a].append(b); gadj[b].append(a)
        gseen = {vs[0]}
        gstack = [vs[0]]
        while gstack:
            u = gstack.pop()
            for w in gadj[u]:
                if w not in gseen:
                    gseen.add(w); gstack.append(w)
        if gseen != set(vs):
            manifold = False
    if manifold:
        for v in vs:
            ledges = links[v]
            verts = {x for e in ledges for x in e}
            deg = Counter(x for e in ledges for x in e)
            if not verts or len(ledges)!=len(verts) or any(deg[x]!=2 for x in verts):
                manifold = False
                break
            adj = defaultdict(list)
            for a,b in ledges:
                adj[a].append(b); adj[b].append(a)
            seen = {next(iter(verts))}
            stack = list(seen)
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if w not in seen:
                        seen.add(w); stack.append(w)
            if seen != verts:
                manifold = False
                break
    return (len(vs),len(es),len(ts),len(vs)-len(es)+len(ts),manifold)

def collapse_pairs(maxs):
    out = []
    for m in maxs:
        if len(m) <= 1:
            continue
        for f in combinations(m,len(m)-1):
            if len(f)==1:
                continue  # preserve the nine-vertex support
            if sum(set(f) <= set(M) for M in maxs) == 1:
                out.append((m,f))
    out.sort(key=lambda z:(-len(z[0]),z[0],z[1]))
    return out

def collapse_once(maxs,m,f):
    sims = all_simplices(maxs)
    rem = sims - {m,f}
    return frozenset(s for s in rem if not any(set(s)<set(t) for t in rem))

@lru_cache(maxsize=None)
def collapse_to_N3(maxs):
    prof = surface_profile(maxs)
    if prof == (9,30,20,-1,True):
        return ()
    for m,f in collapse_pairs(maxs):
        nxt = collapse_once(maxs,m,f)
        tail = collapse_to_N3(nxt)
        if tail is not None:
            return ((f,m),) + tail
    return None

already_surface = 0
collapse_lengths = []
for S in carriers:
    start = induced_maximal_facets(S)
    if surface_profile(start) == (9,30,20,-1,True):
        already_surface += 1
    cert = collapse_to_N3(start)
    assert cert is not None
    cur = start
    for f,m in cert:
        assert (m,f) in collapse_pairs(cur)
        cur = collapse_once(cur,m,f)
    assert surface_profile(cur) == (9,30,20,-1,True)
    # A closed connected surface with chi=-1 is the nonorientable genus-3 surface N_3.
    # Its mod-two fundamental cycle is the sum of all triangles and must carry ambient H_2.
    final_triangles = [s for s in all_simplices(cur) if len(s)==3]
    z = 0
    for t in final_triangles:
        z ^= 1 << TI[t]
    assert reduce_mod(z,B3) != 0
    collapse_lengths.append(len(cert))

assert already_surface == 4
assert len(collapse_lengths) == 37
assert max(collapse_lengths) <= 10

print(
    "VERIFY_OK f=16,109,186,93 H2_F2_dim=1 "
    "min_vertex_support=9 carriers9=37 "
    "already_induced_N3=4 collapse_to_9vertex_N3=37 "
    "ambient_fundamental_class_nonzero=37 "
    "support_counts_le9=0,0,0,0,0,0,0,0,37"
)
