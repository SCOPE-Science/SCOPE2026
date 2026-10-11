#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter

FACETS = {tuple(sorted(x)) for x in [
(1,2,4,5,6),(2,3,5,6,4),(3,1,6,4,5),
(1,2,4,5,9),(2,3,5,6,7),(3,1,6,4,8),
(2,3,6,4,9),(3,1,4,5,7),(1,2,5,6,8),
(3,1,5,6,9),(1,2,6,4,7),(2,3,4,5,8),
(4,5,7,8,9),(5,6,8,9,7),(6,4,9,7,8),
(4,5,7,8,3),(5,6,8,9,1),(6,4,9,7,2),
(5,6,9,7,3),(6,4,7,8,1),(4,5,8,9,2),
(6,4,8,9,3),(4,5,9,7,1),(5,6,7,8,2),
(7,8,1,2,3),(8,9,2,3,1),(9,7,3,1,2),
(7,8,1,2,6),(8,9,2,3,4),(9,7,3,1,5),
(8,9,3,1,6),(9,7,1,2,4),(7,8,2,3,5),
(9,7,2,3,6),(7,8,3,1,4),(8,9,1,2,5)
]}
V = tuple(range(1,10))

def faces(k):
    return {tuple(sorted(c)) for f in FACETS for c in combinations(f,k)}

E = sorted(faces(2))
T = sorted(faces(3))
Q = sorted(faces(4))
assert (len(V),len(E),len(T),len(Q),len(FACETS)) == (9,36,84,90,36)
assert len(T) == len(list(combinations(V,3)))  # 3-neighborly

Ei={e:i for i,e in enumerate(E)}
Ti={t:i for i,t in enumerate(T)}

def gf2_rank(rows):
    basis={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in basis: x ^= basis[p]
            else:
                basis[p]=x
                break
    return len(basis)

def gf2_basis(rows):
    basis={}
    for x in rows:
        y=x
        while y:
            p=y.bit_length()-1
            if p in basis: y ^= basis[p]
            else:
                basis[p]=y
                break
    return basis

def gf2_reduce(x,basis):
    while x:
        p=x.bit_length()-1
        if p in basis: x ^= basis[p]
        else: break
    return x

# d2 columns: triangle boundaries in edge coordinates.
d2_cols=[]
for a,b,c in T:
    x=0
    for e in [(a,b),(a,c),(b,c)]:
        x ^= 1<<Ei[tuple(sorted(e))]
    d2_cols.append(x)
r2=gf2_rank(d2_cols)

# d3 columns: tetrahedron boundaries in triangle coordinates.
d3_cols=[]
for q in Q:
    x=0
    for t in combinations(q,3):
        x ^= 1<<Ti[tuple(sorted(t))]
    d3_cols.append(x)
r3=gf2_rank(d3_cols)
assert (r2,r3,84-r2-r3)==(28,55,1)

B3=gf2_basis(d3_cols)
def class2_from_tris(tris):
    x=0
    for t in tris: x ^= 1<<Ti[tuple(sorted(t))]
    return gf2_reduce(x,B3)

all4=set(combinations(V,4))
missing=sorted(all4-set(Q))
assert len(missing)==36
present=sorted(set(Q))
zero_present=[class2_from_tris(combinations(q,3)) for q in present]
nonzero_missing=[class2_from_tris(combinations(q,3)) for q in missing]
assert all(x==0 for x in zero_present)
assert all(x!=0 for x in nonzero_missing)
assert len(set(nonzero_missing))==1

# Integral 2-cocycle w on increasingly oriented triangles.
wp = {
(1,2,6),(1,4,5),(1,4,6),(1,4,8),(1,7,8),
(2,3,5),(2,4,5),(2,6,8),(2,7,8),(3,5,8),
(3,7,8),(4,5,7),(4,5,8),(4,5,9)
}
wm = {(1,3,4),(1,6,7),(2,5,6),(2,5,7),(3,4,7)}
def w(t):
    t=tuple(sorted(t))
    return 1 if t in wp else (-1 if t in wm else 0)

def boundary_eval(q):
    q=tuple(sorted(q))
    # oriented boundary [q1q2q3] - [q0q2q3] + [q0q1q3] - [q0q1q2]
    return sum(((-1)**i)*w(q[:i]+q[i+1:]) for i in range(4))

# Cocycle: evaluation on every oriented 3-simplex boundary is zero.
assert all(boundary_eval(q)==0 for q in present)
mev={q:boundary_eval(q) for q in missing}
assert Counter(mev.values())==Counter({1:18,-1:18})

# Automorphism group by complete permutation exhaustion.
def image_set(p,S):
    m={i:p[i-1] for i in V}
    return {tuple(sorted(m[x] for x in f)) for f in S}
AUT=[p for p in permutations(V) if image_set(p,FACETS)==FACETS]
assert len(AUT)==54

def image_tuple(q,p):
    return tuple(p[x-1] for x in q)
def sort_sign(seq):
    inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return -1 if inv%2 else 1

# Orbits of missing tetrahedral supports.
unseen=set(missing); orbit_sizes=[]
while unseen:
    q=next(iter(unseen))
    orb={tuple(sorted(image_tuple(q,p))) for p in AUT}
    assert orb <= set(missing)
    orbit_sizes.append(len(orb)); unseen-=orb
assert sorted(orbit_sizes)==[9,27]

# H2 action. Choose a primitive carrier with +1 cocycle evaluation.
q0=next(q for q in missing if mev[q]==1)
actions=[]
for p in AUT:
    seq=image_tuple(q0,p)
    qs=tuple(sorted(seq))
    val=sort_sign(seq)*mev[qs]  # w evaluated on the pushed-forward oriented carrier
    assert val in (-1,1)
    actions.append(val)
assert Counter(actions)==Counter({1:27,-1:27})

# Kernel action preserves the cohomology generator and has order 27.
KER=[p for p,s in zip(AUT,actions) if s==1]
assert len(KER)==27

print(
"VERIFY_OK f=9,36,84,90,36 H2_F2_dim=1 "
"missing4=36 present4=90 missing4_mod2_nonzero=36 "
"cocycle_nonzero=19 missing4_integral_evals=+1:18,-1:18 "
"aut=54 carrier_orbits=9,27 H2_action=+1:27,-1:27 kernel=27"
)
