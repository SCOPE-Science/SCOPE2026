#!/usr/bin/env python3
import itertools
from collections import Counter, defaultdict

ALPHABET = tuple(range(4))  # A,C,G,T
DNA = ("A","C","G","T")
COMP = (3,2,1,0)
N = 4
D = 3
W = 2

def gc_content(x):
    return sum(a in (1,2) for a in x)

def rc(x):
    return tuple(COMP[a] for a in reversed(x))

def hamming(x,y):
    return sum(a != b for a,b in zip(x,y))

def fmt(x):
    return "".join(DNA[a] for a in x)

ALL_GC = tuple(x for x in itertools.product(ALPHABET, repeat=N) if gc_content(x) == W)
assert len(ALL_GC) == 96

# The reverse-complement constraint is imposed also for x=y.
ELIGIBLE = tuple(x for x in ALL_GC if hamming(x, rc(x)) >= D)
assert len(ELIGIBLE) == 72
EIDX = {x:i for i,x in enumerate(ELIGIBLE)}
AIDX = {x:i for i,x in enumerate(ALL_GC)}

# Build the constrained compatibility graph in two equivalent ways.
adj = [0]*len(ELIGIBLE)
adj_alt = [0]*len(ELIGIBLE)
for i,x in enumerate(ELIGIBLE):
    for j,y in enumerate(ELIGIBLE):
        if i == j:
            continue
        if hamming(x,y) >= D and hamming(x,rc(y)) >= D:
            adj[i] |= 1 << j
        # Equivalent formulation: all four words x,RC(x),y,RC(y)
        # form an ordinary distance-D code.
        four = {x, rc(x), y, rc(y)}
        if len(four) == 4 and all(hamming(a,b) >= D for a,b in itertools.combinations(four,2)):
            adj_alt[i] |= 1 << j
assert adj == adj_alt

def maximal_cliques(adj):
    n=len(adj)
    full=(1<<n)-1
    best=0
    maxima=set()
    def bronk(R,P,X):
        nonlocal best,maxima
        if not P and not X:
            C=tuple(i for i in range(n) if (R>>i)&1)
            s=len(C)
            if s>best:
                best=s; maxima={C}
            elif s==best:
                maxima.add(C)
            return
        U=P|X
        if U:
            cand=[u for u in range(n) if (U>>u)&1]
            pivot=max(cand,key=lambda u:(P&adj[u]).bit_count())
            Q=P & ~adj[pivot]
        else:
            Q=P
        while Q:
            vb=Q & -Q
            v=vb.bit_length()-1
            bronk(R|vb, P&adj[v], X&adj[v])
            P &= ~vb
            X |= vb
            Q &= ~vb
    bronk(0,full,0)
    return best,maxima

best, maxima = maximal_cliques(adj)
assert best == 6
assert len(maxima) == 512

# Independent fixed-size clique census.
def k_cliques(adj,k):
    n=len(adj)
    out=set()
    def rec(prefix,cand,need):
        if need==0:
            out.add(tuple(prefix)); return
        if cand.bit_count() < need:
            return
        while cand:
            vb=cand & -cand
            v=vb.bit_length()-1
            cand ^= vb
            rec(prefix+[v], cand & adj[v], need-1)
    rec([], (1<<n)-1, k)
    return out

six = k_cliques(adj,6)
assert six == maxima
assert len(k_cliques(adj,7)) == 0

# Ordinary constant-GC graph.
oadj=[0]*len(ALL_GC)
for i,x in enumerate(ALL_GC):
    for j,y in enumerate(ALL_GC):
        if i!=j and hamming(x,y) >= D:
            oadj[i] |= 1 << j

obest, ordinary_maxima = maximal_cliques(oadj)
assert obest == 12
assert len(ordinary_maxima) == 128

def ordinary_tuple_to_words(C):
    return tuple(ALL_GC[i] for i in C)

def ordinary_rc_invariant(C):
    S={ALL_GC[i] for i in C}
    return {rc(x) for x in S} == S

rc_parents_all = {C for C in ordinary_maxima if ordinary_rc_invariant(C)}
assert len(rc_parents_all) == 16
rc_parents = {
    C for C in rc_parents_all
    if all(x != rc(x) for x in ordinary_tuple_to_words(C))
}
assert len(rc_parents) == 8

# Every constrained optimum doubles to an RC-invariant ordinary optimum.
parent_to_children=defaultdict(set)
for C in maxima:
    S={ELIGIBLE[i] for i in C}
    parent_words=S | {rc(x) for x in S}
    assert len(parent_words) == 12
    parent=tuple(sorted(AIDX[x] for x in parent_words))
    assert parent in rc_parents
    parent_to_children[parent].add(C)

assert set(parent_to_children) == rc_parents
assert {len(v) for v in parent_to_children.values()} == {64}

# Conversely every one of the 2^6 transversals of every parent is valid,
# and they are exactly the direct 512-code census.
children_from_parents=set()
for parent in rc_parents:
    S={ALL_GC[i] for i in parent}
    unseen=set(S)
    pairs=[]
    while unseen:
        x=min(unseen)
        y=rc(x)
        assert y in unseen and y != x
        pairs.append((x,y))
        unseen.remove(x); unseen.remove(y)
    assert len(pairs)==6
    for bits in itertools.product((0,1), repeat=6):
        Cwords=tuple(sorted(pairs[k][bits[k]] for k in range(6)))
        C=tuple(sorted(EIDX[x] for x in Cwords))
        assert C in maxima
        children_from_parents.add(C)
assert children_from_parents == maxima

# Explicit 256-element constraint-preserving symmetry group.
# Coordinate permutations must commute with reversal.
position_perms=[
    p for p in itertools.permutations(range(4))
    if all(p[3-i] == 3-p[i] for i in range(4))
]
assert len(position_perms)==8

# At each mirrored coordinate pair independently swap A/T and/or C/G.
local_perms=[]
for swap_at in (0,1):
    for swap_cg in (0,1):
        p=list(range(4))
        if swap_at: p[0],p[3]=p[3],p[0]
        if swap_cg: p[1],p[2]=p[2],p[1]
        local_perms.append(tuple(p))
PAIR_SWAP=(1,0,3,2)  # globally exchange {A,T} with {C,G}

maps=[]
for pp in position_perms:
    for po in local_perms:
        for pi in local_perms:
            for swap_classes in (0,1):
                T=[]
                for x in ELIGIBLE:
                    u=tuple(x[pp[i]] for i in range(4))
                    v=list(u)
                    for i in (0,3): v[i]=po[v[i]]
                    for i in (1,2): v[i]=pi[v[i]]
                    if swap_classes:
                        v=[PAIR_SWAP[a] for a in v]
                    v=tuple(v)
                    assert v in EIDX
                    T.append(EIDX[v])
                maps.append(tuple(T))
maps=list(dict.fromkeys(maps))
assert len(maps)==256

# Every listed map must preserve the complete compatibility graph.
for T in maps:
    for i in range(len(ELIGIBLE)):
        mapped=0
        bits=adj[i]
        while bits:
            vb=bits & -bits
            j=vb.bit_length()-1
            mapped |= 1 << T[j]
            bits ^= vb
        assert mapped == adj[T[i]]

maxset={tuple(C) for C in maxima}
seen=set()
orbits=[]
for C in sorted(maxset):
    if C in seen: continue
    orbit={tuple(sorted(T[i] for i in C)) for T in maps}
    assert orbit <= maxset
    seen |= orbit
    orbits.append((len(orbit), 256//len(orbit), min(orbit)))
assert seen == maxset
orbits.sort()
assert [(a,b) for a,b,_ in orbits] == [(128,2)]*4

# The eight parents form one orbit under the same transformations.
# Extend each transformation from eligible words to all constant-GC words by
# reconstructing its generating action, rather than using the vertex map.
# It is enough here to verify parent transitivity by direct transformed child unions:
parent_orbit=set()
P0=min(rc_parents)
P0words={ALL_GC[i] for i in P0}
for C in parent_to_children[P0]:
    for T in maps:
        TC=tuple(sorted(T[i] for i in C))
        S={ELIGIBLE[i] for i in TC}
        parent=tuple(sorted(AIDX[x] for x in (S | {rc(x) for x in S})))
        parent_orbit.add(parent)
assert parent_orbit == rc_parents

print("AMBIENT_OK gc_words=96 eligible_rc_words=72 compatibility_formulations_agree=true")
print("RC_MAXIMUM=6 RC_LABELED_MAXIMA=512")
print("ORDINARY_MAXIMUM=12 ORDINARY_LABELED_MAXIMA=128 RC_INVARIANT=16 VIABLE_RC_PARENTS=8")
print("PARENT_LIFT children_per_parent=64 exact_cover=true")
print("SYMMETRY group_order=256 orbits=4 orbit_sizes=128,128,128,128 stabilizers=2,2,2,2")
for k,(size,stab,rep) in enumerate(orbits,1):
    print("REP",k,"orbit",size,"stabilizer",stab,
          "code",",".join(fmt(ELIGIBLE[i]) for i in rep))
print("VERIFY_OK maximum=6 labeled_maxima=512 parents=8 children_per_parent=64 "
      "orbits=4 orbit_sizes=128,128,128,128 stabilizers=2,2,2,2")
