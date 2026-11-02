#!/usr/bin/env python3
"""Reproduce the complete constant-free semiring endomorphism census of UT_2(B).
Only Python standard library. Coordinates are bit masks: 1=E11, 2=E12, 4=E22.
"""
from collections import Counter
from itertools import product

S = range(8)
E, Z, F = 1, 2, 4

def multiply(x, y):
    a, b, c = x & 1, (x >> 1) & 1, (x >> 2) & 1
    d, e, f = y & 1, (y >> 1) & 1, (y >> 2) & 1
    return (a & d) | (((a & e) | (b & f)) << 1) | ((c & f) << 2)

def images(T, P, Q, R):
    return tuple(T | (P if x & 1 else 0) | (Q if x & 2 else 0)
                 | (R if x & 4 else 0) for x in S)

def preserves(f):
    return (all(f[x | y] == (f[x] | f[y]) for x in S for y in S)
            and all(f[multiply(x,y)] == multiply(f[x],f[y]) for x in S for y in S))

# Independent exhaustive check over every addition-preserving 8 -> 8 map:
# f(0), f(E11), f(E12), f(E22) determine the map by join.
full = set()
for t,p,q,r in product(S, repeat=4):
    if any(t | u != u for u in (p,q,r)):
        continue
    f = images(t,p,q,r)
    if preserves(f):
        full.add(f)
assert len(full) == 30

idempotents = tuple(x for x in S if multiply(x,x) == x)
assert idempotents == (0,1,3,4,5,6,7)

# Separate structural construction, with no brute-force multiplication test.
model = set()
# Case f(0)=f(E12)=0: orthogonal multiplicative idempotents.
for p in idempotents:
    for r in idempotents:
        if multiply(p,r) == multiply(r,p) == 0:
            model.add(images(0,p,0,r))
# Unique case f(E12) != 0.
model.add(images(0,E,Z,F))
# All positive f(0) constants, and four strict idempotent chains.
for t in idempotents:
    if t:
        model.add(images(t,t,t,t))
for t,u in ((1,5),(3,7),(4,5),(6,7)):
    model.add(images(t,t,t,u))
    model.add(images(t,u,t,t))
assert model == full

rank = lambda f: len(set(f))
composition = lambda f,g: tuple(f[g[x]] for x in S)
identity = tuple(S)
assert identity in full
assert all(composition(f,g) in full for f in full for g in full)
profile = Counter(rank(f) for f in full)
assert profile == {1:7,2:20,4:2,8:1}
retracts = tuple(f for f in full if composition(f,f)==f)
assert len(retracts) == 21
assert Counter(rank(f) for f in retracts) == {1:7,2:12,4:1,8:1}
assert len([f for f in full if rank(f)==8]) == 1

# The two rank-four maps form a local group of order 2, with identity projection.
rank4 = [f for f in full if rank(f)==4]
proj = images(0,1,0,4)
flip = images(0,4,0,1)
assert set(rank4) == {proj,flip}
assert composition(proj,flip) == composition(flip,proj) == flip
assert composition(flip,flip) == proj
assert composition(proj,proj) == proj

# No other nontrivial local subgroup: the image semirings of idempotent maps
# in ranks 1 and 2 each have trivial automorphisms; rank 8 has trivial units.
# Directly check all H_e = {g: g e=e g=g, and some h with gh=hg=e}.
for e in retracts:
    candidates = [g for g in full if composition(g,e)==g and composition(e,g)==g]
    group = [g for g in candidates if any(composition(g,h)==e and composition(h,g)==e for h in candidates)]
    assert len(group) == (2 if e==proj else 1)

# Corpus check: the five congruences in Jiao--Shao's Corollary 10.2
# give kernel class-counts 8,4,2,2,1, matching these complete image sizes.
kernels = {tuple(sorted(tuple(sorted(x for x in S if f[x]==v))
                          for v in set(f))) for f in full}
assert len(kernels) == 5
assert sorted((len(k),len([f for f in full if
    tuple(sorted(tuple(sorted(x for x in S if f[x]==v)) for v in set(f)))==k]))
    for k in kernels) == [(1,7),(2,10),(2,10),(4,2),(8,1)]
print('VERIFY_OK', 'endomorphisms',len(full),'rank_profile',dict(sorted(profile.items())),
      'retractions',len(retracts),'local_C2',len(rank4), 'kernels',len(kernels))
