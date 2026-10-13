#!/usr/bin/env python3
"""Exact verifier for the K8 qualitative-representation classification.

Pure Python standard library. It enumerates all one-factorizations of K8
containing one fixed 1-factor, quotients them under vertex relabeling, checks
trichromatic coverage, and classifies deletions of the unique good class.
"""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict

CHECKS = 0

def check(cond, msg="assertion failed"):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(msg)

V = tuple(range(8))
EDGES = tuple(combinations(V, 2))
EIDX = {e:i for i,e in enumerate(EDGES)}
ALL_EDGES = (1 << len(EDGES)) - 1


def mask_of_pairs(pairs):
    m = 0
    for a,b in pairs:
        if a>b: a,b=b,a
        m |= 1 << EIDX[(a,b)]
    return m


def pairs_of_mask(mask):
    return tuple(EDGES[i] for i in range(28) if (mask >> i) & 1)


def perfect_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        rest = vertices[1:j] + vertices[j+1:]
        for tail in perfect_matchings(rest):
            yield ((a,b),) + tail

PMS = tuple(mask_of_pairs(M) for M in perfect_matchings(V))
check(len(PMS) == 105, "K8 should have 105 perfect matchings")
check(len(set(PMS)) == 105)
for m in PMS:
    ps = pairs_of_mask(m)
    check(len(ps) == 4)
    flat = [x for e in ps for x in e]
    check(sorted(flat) == list(V))

F0_PAIRS = ((0,1),(2,3),(4,5),(6,7))
F0 = mask_of_pairs(F0_PAIRS)
REST = ALL_EDGES ^ F0
CAND = tuple(m for m in PMS if m != F0 and not (m & F0))
check(len(CAND) == 60)
BY_EDGE = {i: tuple(m for m in CAND if (m >> i) & 1) for i in range(28)}

FACTS = []
def enumerate_factorizations(used, chosen):
    if used == REST:
        FACTS.append(tuple(sorted(chosen)))
        return
    avail = REST & ~used
    bit = avail & -avail
    e = bit.bit_length() - 1
    for m in BY_EDGE[e]:
        if not (m & used):
            enumerate_factorizations(used | m, chosen + (m,))

enumerate_factorizations(0, ())
check(len(FACTS) == 416, "fixed-factor census")
check(len(set(FACTS)) == 416)
FULL = tuple(tuple(sorted((F0,) + f)) for f in FACTS)
for fs in FULL:
    check(len(fs) == 7)
    acc = 0
    for m in fs:
        check((acc & m) == 0)
        acc |= m
    check(acc == ALL_EDGES)


def edge_color_map(fs):
    d = {}
    for c,m in enumerate(fs):
        for e in pairs_of_mask(m):
            check(e not in d)
            d[e] = c
    check(len(d) == 28)
    return d


def triangle_color_sets(fs):
    d = edge_color_map(fs)
    out = set()
    for a,b,c in combinations(V,3):
        cols = tuple(sorted((d[tuple(sorted((a,b)))],
                             d[tuple(sorted((a,c)))],
                             d[tuple(sorted((b,c)))])))
        # A 1-factorization makes every triangle trichromatic.
        check(len(set(cols)) == 3)
        out.add(cols)
    return out


def cycle_lengths(m1, m2):
    adj = {v:[] for v in V}
    for a,b in pairs_of_mask(m1) + pairs_of_mask(m2):
        adj[a].append(b); adj[b].append(a)
    for v in V:
        check(len(adj[v]) == 2)
    seen = set(); lens=[]
    for v in V:
        if v in seen: continue
        stack=[v]; seen.add(v); n=0
        while stack:
            x=stack.pop(); n += 1
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        lens.append(n)
    return tuple(sorted(lens))


def is_p1f(fs):
    return all(cycle_lengths(a,b) == (8,) for a,b in combinations(fs,2))

tri_hist = Counter()
pair_hist = Counter()
good_flags=[]
for fs in FULL:
    t = len(triangle_color_sets(fs))
    tri_hist[t] += 1
    good = (t == 35)
    good_flags.append(good)
    p = Counter(cycle_lengths(a,b) for a,b in combinations(fs,2))
    key = tuple(sorted(p.items()))
    pair_hist[key] += 1
    check(good == is_p1f(fs), "qualitative iff perfect in exhaustive K8 census")

check(tri_hist == Counter({7:2, 11:42, 13:28, 17:168, 26:112, 35:64}), str(tri_hist))
check(sum(good_flags) == 64)
expected_pair_hist = Counter({
    (((4,4),21),): 2,
    (((4,4),13),((8,),8)): 42,
    (((4,4),9),((8,),12)): 28,
    (((4,4),7),((8,),14)): 168,
    (((4,4),3),((8,),18)): 112,
    (((8,),21),): 64,
})
check(pair_hist == expected_pair_hist, str(pair_hist))

# Finite C8 lemma used in the hand proof of P1F => qualitative.
A = mask_of_pairs(((0,1),(2,3),(4,5),(6,7)))
B = mask_of_pairs(((1,2),(3,4),(5,6),(7,0)))
CYCLE = A | B
na = {}
nb = {}
for x,y in pairs_of_mask(A): na[x]=y; na[y]=x
for x,y in pairs_of_mask(B): nb[x]=y; nb[y]=x
STEP2 = {tuple(sorted((na[v],nb[v]))) for v in V}
check(len(STEP2) == 8)
lemma_matchings=[]
for m in PMS:
    if m & CYCLE: continue
    if any(e in STEP2 for e in pairs_of_mask(m)): continue
    lemma_matchings.append(m)
    check(cycle_lengths(A,m) == (4,4) or cycle_lengths(B,m) == (4,4))
check(len(lemma_matchings) == 7)

# Vertex relabeling machinery.
def edge_map_for_perm(p):
    em=[]
    for a,b in EDGES:
        x,y = sorted((p[a],p[b]))
        em.append(EIDX[(x,y)])
    return tuple(em)

def trans_mask(m, em):
    out=0
    while m:
        bit=m & -m
        i=bit.bit_length()-1
        out |= 1 << em[i]
        m -= bit
    return out

# Stabilizer of fixed matching F0: C2 wr S4, order 384.
STABS=[]
for sig in permutations(range(4)):
    for flips in product((0,1), repeat=4):
        p=[None]*8
        for i,(a,b) in enumerate(F0_PAIRS):
            x,y = F0_PAIRS[sig[i]]
            if flips[i]: x,y=y,x
            p[a]=x; p[b]=y
        STABS.append(tuple(p))
check(len(STABS) == 384)
STAB_EMS=tuple(edge_map_for_perm(p) for p in STABS)
for em in STAB_EMS:
    check(trans_mask(F0,em) == F0)


def matching_to_F0(m):
    ps = sorted(pairs_of_mask(m))
    p=[None]*8
    for j,(a,b) in enumerate(ps):
        x,y=F0_PAIRS[j]
        p[a]=x; p[b]=y
    return tuple(p)

Q = {m: matching_to_F0(m) for m in PMS}
for m,p in Q.items():
    check(trans_mask(m, edge_map_for_perm(p)) == F0)


def canonical_factorization(fs):
    best=None
    for distinguished in fs:
        emq=edge_map_for_perm(Q[distinguished])
        qfs=tuple(trans_mask(m,emq) for m in fs)
        for ems in STAB_EMS:
            rep=tuple(sorted(trans_mask(m,ems) for m in qfs))
            if best is None or rep < best:
                best=rep
    return best

CANONS=[]
for fs in FULL:
    c=canonical_factorization(fs)
    CANONS.append(c)
    check(F0 in c)
check(len(set(CANONS)) == 6, "six K8 one-factorization classes")
class_info=defaultdict(lambda:[0,0,Counter()])
for fs,c,g in zip(FULL,CANONS,good_flags):
    class_info[c][0]+=1
    class_info[c][1]+=int(g)
    class_info[c][2][len(triangle_color_sets(fs))]+=1
profile=sorted((n,g,tuple(sorted(h.items()))) for n,g,h in class_info.values())
check(profile == sorted([
    (2,0,((7,2),)),
    (42,0,((11,42),)),
    (28,0,((13,28),)),
    (168,0,((17,168),)),
    (112,0,((26,112),)),
    (64,64,((35,64),)),
]))
check(sum(1 for n,g,h in class_info.values() if g) == 1)

GOOD = FULL[good_flags.index(True)]
GOOD_CANON = canonical_factorization(GOOD)
check(is_p1f(GOOD))
check(len(triangle_color_sets(GOOD)) == 35)

# Automorphism group allowing permutation of factor/color classes.
AUT=[]
for p in permutations(V):
    em=edge_map_for_perm(p)
    image=tuple(sorted(trans_mask(m,em) for m in GOOD))
    if image == GOOD:
        AUT.append(tuple(p))
check(len(AUT) == 42, "automorphism group order")
remaining=set(V); vertex_orbits=[]
while remaining:
    v=min(remaining)
    orb={p[v] for p in AUT}
    vertex_orbits.append(tuple(sorted(orb)))
    remaining -= orb
check(sorted(map(len,vertex_orbits)) == [1,7], str(vertex_orbits))

# Directly classify the eight vertex deletions under S7 and color relabeling.
E7=tuple(combinations(range(7),2)); E7IDX={e:i for i,e in enumerate(E7)}
def restrict_delete(fs, dv):
    old=[v for v in V if v != dv]
    mp={v:i for i,v in enumerate(old)}
    classes=[]
    for m in fs:
        out=0
        for a,b in pairs_of_mask(m):
            if a==dv or b==dv: continue
            x,y=sorted((mp[a],mp[b]))
            out |= 1 << E7IDX[(x,y)]
        classes.append(out)
    return tuple(sorted(classes))

def canonical_7(rep):
    best=None
    for p in permutations(range(7)):
        em=[]
        for a,b in E7:
            x,y=sorted((p[a],p[b]))
            em.append(E7IDX[(x,y)])
        trans=[]
        for m0 in rep:
            m=m0; out=0
            while m:
                bit=m & -m; i=bit.bit_length()-1
                out |= 1 << em[i]; m -= bit
            trans.append(out)
        r=tuple(sorted(trans))
        if best is None or r<best: best=r
    return best

DEL_CANONS=[canonical_7(restrict_delete(GOOD,v)) for v in V]
mult=sorted(Counter(DEL_CANONS).values())
check(len(set(DEL_CANONS)) == 2)
check(mult == [1,7], str(mult))

# Sanity: explicit P1F factorization is a partition with full triple coverage.
explicit = (
    ((0,5),(1,7),(2,6),(3,4)),
    ((0,4),(1,6),(2,5),(3,7)),
    ((0,3),(1,5),(2,7),(4,6)),
    ((0,6),(1,2),(3,5),(4,7)),
    ((0,7),(1,3),(2,4),(5,6)),
    ((0,2),(1,4),(3,6),(5,7)),
    ((0,1),(2,3),(4,5),(6,7)),
)
EX=tuple(sorted(mask_of_pairs(x) for x in explicit))
check(is_p1f(EX))
check(len(triangle_color_sets(EX)) == 35)
check(canonical_factorization(EX) == GOOD_CANON)

print("fixed_factor_factorizations=416")
print("isomorphism_classes=6")
print("triangle_triple_histogram=" + repr(dict(sorted(tri_hist.items()))))
print("qualitative_fixed_factor_instances=64")
print("qualitative_isomorphism_classes=1")
print("good_automorphism_group_order=42")
print("good_vertex_orbit_sizes=[1, 7]")
print("seven_point_deletion_classes=2")
print("seven_point_deletion_multiplicities=[1, 7]")
print(f"VERIFY_OK {CHECKS} exact assertions")
