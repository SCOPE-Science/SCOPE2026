#!/usr/bin/env python3
"""Exact, reproducible face-and-lattice certificate for a specified non-Fano matroid normal fan.
Requires Python 3.10+ and sympy. No external data or web access.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd, lcm
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

E = tuple(range(7))
H = (0, 1, 2)
LINES = ((0,1,2), (0,3,4), (0,5,6), (1,3,5),
         (1,4,6), (2,3,6), (2,4,5))
FORBIDDEN = tuple(L for L in LINES if L != H)
BASES = tuple(B for B in combinations(E, 3) if B not in FORBIDDEN)
assert len(BASES) == 29 and H in BASES
# The base-exchange axiom is checked independently of the geometric computation.
BB = frozenset(frozenset(B) for B in BASES)
for A in BB:
    for B in BB:
        for a in A-B:
            assert any(frozenset((A-{a})|{b}) in BB for b in B-A)

def rank_subset(S):
    return max(len(S & B) for B in BB)

all_flats=[]
for bits in range(1, (1<<7)-1):
    S=frozenset(i for i in E if bits>>i & 1)
    if all(rank_subset(S|{i}) > rank_subset(S) for i in E if i not in S):
        all_flats.append((S,rank_subset(S)))
rank_two = frozenset(S for S,r in all_flats if r==2)
assert rank_two == frozenset(map(frozenset,FORBIDDEN)) | frozenset(map(frozenset,combinations(H,2)))
assert frozenset(S for S,r in all_flats if r==1) == frozenset(frozenset([i]) for i in E)
P = tuple(tuple(int(i in B) for i in E) for B in BASES)

# Inequalities are a*x >= b for lower singleton facets,
# and a*x <= b for upper singleton and remaining six lines.
FACETS = tuple((frozenset([i]), 0, 1) for i in E) + \
         tuple((frozenset([i]), 1, -1) for i in E) + \
         tuple((frozenset(T), 2, -1) for T in FORBIDDEN)
assert len(FACETS) == 20
FULL = (1 << len(BASES)) - 1

def exact_rank(rows):
    rows = [[Fraction(v) for v in row] for row in rows]
    if not rows: return 0
    n = len(rows[0]); j = 0
    for col in range(n):
        t = next((i for i in range(j, len(rows)) if rows[i][col]), None)
        if t is None: continue
        rows[j], rows[t] = rows[t], rows[j]
        z = rows[j][col]
        for k in range(col, n): rows[j][k] /= z
        for i in range(j+1, len(rows)):
            z = rows[i][col]
            if z:
                for k in range(col, n): rows[i][k] -= z * rows[j][k]
        j += 1
        if j == len(rows): break
    return j

def vertices(mask):
    return [i for i in range(len(BASES)) if mask >> i & 1]

def dimension(mask):
    I = vertices(mask)
    return exact_rank([[P[j][k]-P[I[0]][k] for k in E] for j in I[1:]])

FMASK = []
RAYS = []
for subset, value, sign in FACETS:
    m = sum(1<<j for j,B in enumerate(BASES) if len(subset.intersection(B)) == value)
    FMASK.append(m)
    assert dimension(m) == 5
    # inward primitive normal, in coordinates dual to e_i-e_6 (i=0,...,5)
    a = [sign*(i in subset) for i in E]
    RAYS.append(tuple(int(a[i]-a[6]) for i in range(6)))

# Every nonempty face of a polytope is an intersection of facets.
faces = {FULL}
queue = [FULL]
while queue:
    current = queue.pop()
    for m in FMASK:
        nxt = current & m
        if nxt and nxt not in faces:
            faces.add(nxt)
            queue.append(nxt)

assert len(faces) == 801
FD = {}
for mask in faces:
    d = dimension(mask)
    active = tuple(j for j,m in enumerate(FMASK) if (m & mask) == mask)
    assert len(active) >= 6-d
    FD[mask] = (d,active)
assert Counter(int(d) for d,a in FD.values()) == {0:29,1:138,2:263,3:242,4:108,5:20,6:1}

non_simplicial = []
for mask,(d,active) in FD.items():
    if not active:
        assert d == 6
        continue
    R = Matrix([RAYS[j] for j in active])
    assert R.rank() == 6-d
    S = smith_normal_form(R,domain=ZZ)
    invariants = [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i] != 0]
    assert invariants == [1]*(6-d), (mask,d,active,invariants)
    if len(active)>6-d: non_simplicial.append(mask)
assert len(non_simplicial)==278
assert Counter(int(FD[m][0]) for m in non_simplicial) == {0:29,1:120,2:111,3:18}

# A toric orbit closure V(sigma_F) is a maximal irreducible singular
# component exactly when F is inclusion-maximal among singular faces.
maximal=[]
for mask in non_simplicial:
    if not any(other != mask and (other & mask)==mask for other in non_simplicial):
        maximal.append(mask)
assert len(maximal) == 58

spectrum=Counter()
for mask in maximal:
    d,active = FD[mask]
    R = Matrix([RAYS[j] for j in active])
    null = R.T.nullspace()
    assert len(null)==1 and len(active)==7-d
    v = null[0]
    t=lcm(*(int(x.q) for x in v))
    rel=[int(x*t) for x in v]
    common=gcd(*rel)
    rel=[x//common for x in rel]
    assert all(abs(x)==1 for x in rel)
    plus=sum(x>0 for x in rel)
    minus=sum(x<0 for x in rel)
    spectrum[(int(d),mask.bit_count(),min(plus,minus),max(plus,minus))]+=1

    # Face lattice indices in the saturated coordinate-difference lattice.
    I=vertices(mask)
    if len(I)>1:
        D=Matrix([[P[j][k]-P[I[0]][k] for k in E] for j in I[1:]])
        S=smith_normal_form(D,domain=ZZ)
        inv=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]!=0]
        assert inv==[1]*d, (mask,inv)
    if d==2 and len(I)==4:
        sums=Counter(tuple(P[a][k]+P[b][k] for k in E) for a,b in combinations(I,2))
        assert any(n==2 for n in sums.values())  # primitive parallelogram

assert spectrum == {(3,4,2,2):18,(2,3,2,3):24,(2,4,2,3):15,(0,1,3,4):1},spectrum
assert [BASES[vertices(m)[0]] for m in maximal if FD[m][0]==0] == [H]
print('VERIFY_OK')
print('vertices=29 facets=20 faces=801; f-vector=(29,138,263,242,108,20,1)')
print('nonsimplicial-cones=278; all 800 nonzero normal cones lattice-saturated')
print('maximal singular strata: 18 tetrahedral 3-faces [2x2];')
print('  24 triangular 2-faces [2x3], 15 parallelogram 2-faces [2x3],')
print('  1 isolated vertex (0,1,2) [3x4]; total=58')
