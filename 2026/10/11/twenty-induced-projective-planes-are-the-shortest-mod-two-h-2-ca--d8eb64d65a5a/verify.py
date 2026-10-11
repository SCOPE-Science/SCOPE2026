#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,7),(1,5,6,7),(2,3,4,8),(2,3,5,9),(2,3,8,9),(2,4,6,10),
(2,4,8,10),(2,5,6,11),(2,5,9,11),(2,6,10,11),(2,7,8,9),(2,7,8,10),
(2,7,9,11),(2,7,10,11),(3,4,7,11),(3,4,8,11),(3,5,7,10),(3,5,9,10),
(3,6,8,9),(3,6,8,11),(3,6,9,10),(3,6,10,11),(3,7,10,11),(4,5,8,10),
(4,5,8,11),(4,5,9,10),(4,5,9,11),(4,6,7,9),(4,6,9,10),(4,7,9,11),
(5,6,7,8),(5,6,8,11),(5,7,8,10),(6,7,8,9)
}
V = tuple(range(1,12))

def faces(k):
    return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
Q = sorted(FACETS)
assert (len(V),len(E),len(T),len(Q)) == (11,51,80,40)

EI = {e:i for i,e in enumerate(E)}
TI = {t:i for i,t in enumerate(T)}

D2 = []
for t in T:
    x = 0
    for e in combinations(t,2):
        x ^= 1 << EI[tuple(sorted(e))]
    D2.append(x)

D3 = []
for q in Q:
    x = 0
    for t in combinations(q,3):
        x ^= 1 << TI[tuple(sorted(t))]
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
assert (len(B2),len(B3),len(T)-len(B2)-len(B3)) == (40,39,1)

TMASK = [sum(1<<v for v in t) for t in T]

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

def image_h2_basis(S):
    mask = sum(1<<v for v in S)
    reps = []
    for z in local_cycle_basis(mask):
        r = reduce_mod(z,B3)
        if r:
            reps.append(r)
    return rref_basis(reps)

support_counts = {}
supports6 = []
for k in range(1,7):
    n = 0
    for S in combinations(V,k):
        B = image_h2_basis(S)
        if B:
            n += 1
            if k == 6:
                supports6.append(S)
                assert len(B) == 1
    support_counts[k] = n

assert support_counts == {1:0,2:0,3:0,4:0,5:0,6:20}

def induced_profile(S):
    ss = set(S)
    es = [e for e in E if set(e) <= ss]
    ts = [t for t in T if set(t) <= ss]
    qs = [q for q in Q if set(q) <= ss]
    inc = Counter()
    links = {v:[] for v in S}
    for t in ts:
        for e in combinations(t,2):
            inc[tuple(sorted(e))] += 1
        a,b,c = t
        links[a].append(tuple(sorted((b,c))))
        links[b].append(tuple(sorted((a,c))))
        links[c].append(tuple(sorted((a,b))))
    assert (len(es),len(ts),len(qs)) == (15,10,0)
    assert set(inc.values()) == {2} and len(inc) == 15
    # Every vertex link is a single cycle.
    for v in S:
        ledges = links[v]
        verts = sorted({x for e in ledges for x in e})
        deg = Counter(x for e in ledges for x in e)
        assert len(ledges) == len(verts)
        assert all(deg[x] == 2 for x in verts)
        adj = defaultdict(list)
        for a,b in ledges:
            adj[a].append(b); adj[b].append(a)
        seen = {verts[0]}
        stack = [verts[0]]
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        assert len(seen) == len(verts)
    # Connected complete one-skeleton and chi=1 imply RP^2.
    assert len(es) == 15
    assert len(S)-len(es)+len(ts) == 1

for S in supports6:
    induced_profile(S)

# Exhaust full simplicial automorphism group by degree-preserving,
# triangle-preserving backtracking, then verify facets at leaves.
TSET = set(T)
FSET = set(Q)
deg = {v:sum(v in e for e in E) for v in V}
groups = defaultdict(list)
for v in V:
    groups[deg[v]].append(v)
order = sorted(V,key=lambda v:(len(groups[deg[v]]),v))

AUT = []
used = set()
mp = {}

def rec(i):
    if i == len(order):
        image = {tuple(sorted(mp[x] for x in f)) for f in FSET}
        if image == FSET:
            AUT.append(tuple(mp[v] for v in V))
        return
    v = order[i]
    for w in groups[deg[v]]:
        if w in used:
            continue
        mp[v] = w
        used.add(w)
        ok = True
        for a,b in combinations(order[:i],2):
            src = tuple(sorted((a,b,v))) in TSET
            dst = tuple(sorted((mp[a],mp[b],w))) in TSET
            if src != dst:
                ok = False
                break
        if ok:
            rec(i+1)
        used.remove(w)
        del mp[v]

rec(0)
assert len(AUT) == 48

def image_set(S,p):
    return tuple(sorted(p[v-1] for v in S))

remaining = set(supports6)
orbits = []
while remaining:
    rep = min(remaining)
    orb = {image_set(rep,p) for p in AUT}
    assert orb <= set(supports6)
    orbits.append((rep,len(orb)))
    remaining -= orb

assert orbits == [
    ((2,3,4,5,10,11),12),
    ((2,3,4,9,10,11),8)
]

print(
    "VERIFY_OK f=11,51,80,40 H2_F2_dim=1 "
    "min_vertex_support=6 carriers6=20 "
    "all_carriers_induced_RP2=yes "
    "aut=48 carrier_orbits=12,8 "
    "reps=23451011|23491011"
)
