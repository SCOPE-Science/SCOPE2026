#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict, deque

N = 15
GENERATORS = [
    (0,1,3,7),(0,1,5,7),(0,2,3,7),
    (0,2,6,7),(0,4,5,7),(0,4,6,7)
]
FACETS = {
    tuple(sorted(((x+s) % N for x in g)))
    for g in GENERATORS for s in range(N)
}
V = tuple(range(N))

def faces(k):
    return sorted({
        tuple(sorted(c))
        for f in FACETS for c in combinations(f,k)
    })

E = faces(2)
T = faces(3)
Q = sorted(FACETS)
assert (len(V),len(E),len(T),len(Q)) == (15,105,180,90)

EI = {e:i for i,e in enumerate(E)}
TI = {t:i for i,t in enumerate(T)}

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

B2 = rref_basis(D2)
B3 = rref_basis(D3)
assert (len(B2),len(B3),len(T)-len(B2)-len(B3)) == (88,89,3)

TMASK = [sum(1<<v for v in t) for t in T]

def local_cycle_basis(mask):
    # Dependencies among the triangle-boundary columns, returned as
    # global triangle bit-vectors.
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

def image_h2_basis(mask):
    reps = []
    for z in local_cycle_basis(mask):
        r = reduce_mod(z,B3)
        if r:
            reps.append(r)
    return rref_basis(reps)

def induced_counts(S):
    ss = set(S)
    e = [x for x in E if set(x) <= ss]
    t = [x for x in T if set(x) <= ss]
    q = [x for x in Q if set(x) <= ss]
    return len(e),len(t),len(q),t

def orientable_closed_surface(S):
    ne,nt,nq,tris = induced_counts(S)
    if (ne,nt,nq) != (21,14,0):
        return False
    edge_inc = defaultdict(list)
    for i,(a,b,c) in enumerate(tris):
        for e,coef in [((b,c),1),((a,c),-1),((a,b),1)]:
            edge_inc[e].append((i,coef))
    if len(edge_inc) != 21 or any(len(v) != 2 for v in edge_inc.values()):
        return False
    sign = {}
    for start in range(len(tris)):
        if start in sign:
            continue
        sign[start] = 1
        dq = deque([start])
        while dq:
            i = dq.popleft()
            a,b,c = tris[i]
            for e,ci in [((b,c),1),((a,c),-1),((a,b),1)]:
                inc = edge_inc[e]
                j,cj = inc[0] if inc[1][0] == i else inc[1]
                want = -sign[i]*ci*cj
                if j in sign and sign[j] != want:
                    return False
                if j not in sign:
                    sign[j] = want
                    dq.append(j)
    return len(sign) == 14

# Exhaust all supports through size seven.
for k in range(1,7):
    for S in combinations(V,k):
        mask = sum(1<<v for v in S)
        assert len(image_h2_basis(mask)) == 0

supports = []
for S in combinations(V,7):
    mask = sum(1<<v for v in S)
    B = image_h2_basis(mask)
    if B:
        assert len(B) == 1
        assert orientable_closed_surface(S)
        supports.append((S,next(iter(B.values()))))

assert len(supports) == 60
assert all(induced_counts(S)[:3] == (21,14,0) for S,_ in supports)

# Four ambient nonzero H2 classes, fifteen supports each.
class_counts = Counter(c for _,c in supports)
assert len(class_counts) == 4
assert set(class_counts.values()) == {15}
classes = sorted(class_counts)
x = 0
for c in classes:
    x ^= c
assert x == 0

REP_A = (0,1,2,3,4,5,6)
REP_B = (0,1,2,3,8,9,10)
REP_C = (0,1,4,5,8,9,12)
REP_D = (0,2,4,6,8,10,12)
support_class = dict(supports)
a = support_class[REP_A]
b = support_class[REP_B]
c = support_class[REP_C]
d = support_class[REP_D]
assert len(rref_basis([a,b,c])) == 3
assert d == (a ^ b ^ c)

def coord(r):
    for bits in range(8):
        z = 0
        if bits & 1: z ^= a
        if bits & 2: z ^= b
        if bits & 4: z ^= c
        if z == r:
            return bits
    raise AssertionError("class outside chosen basis")

coord_counts = Counter(coord(r) for _,r in supports)
assert coord_counts == Counter({1:15,2:15,4:15,7:15})

# The published affine symmetry group A(1,Z_15).
MULT = [1,2,4,7,8,11,13,14]
AFF = [(u,v) for u in MULT for v in range(15)]
assert len(AFF) == 120

def image_set(S,u,v):
    return tuple(sorted(((u*x+v) % 15 for x in S)))

def image_facet(f,u,v):
    return tuple(sorted(((u*x+v) % 15 for x in f)))

for u,v in AFF:
    assert {image_facet(f,u,v) for f in FACETS} == FACETS

SUPPORT_SET = set(support_class)
orbit = {image_set(REP_A,u,v) for u,v in AFF}
assert orbit == SUPPORT_SET
for rep in (REP_A,REP_B,REP_C,REP_D):
    trans = [image_set(rep,1,v) for v in range(15)]
    assert len(set(trans)) == 15
    cls = {coord(support_class[s]) for s in trans}
    assert len(cls) == 1

print(
    "VERIFY_OK f=15,105,180,90 H2_F2_dim=3 "
    "min_vertex_support=7 supports7=60 "
    "all_supports_induced_orientable_tori=yes "
    "class_counts=15,15,15,15 classes=001|010|100|111 "
    "affine_auts_checked=120 support_orbit=60 "
    "translation_orbits=15_per_class"
)
