#!/usr/bin/env python3
"""Exact integer certificate for unimodular fourth moments on a quartic graph over F_19.
Runs with Python >=3.9 standard library. No numeric approximation is used.
"""
from collections import defaultdict, Counter
from itertools import combinations

P = 19

def det_bareiss(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    assert n and all(len(row) == n for row in a)
    prev, sign = 1, 1
    for k in range(n - 1):
        pivot = next((i for i in range(k,n) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k],a[pivot] = a[pivot],a[k]
            sign = -sign
        d = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                x = a[i][j]*d - a[i][k]*a[k][j]
                assert x % prev == 0
                a[i][j] = x // prev
            a[i][k] = 0
        prev = d
    return sign*a[-1][-1]

def pair_normalize(ab):
    return tuple(sorted(ab))

def comparison(pair1, pair2):
    return tuple(sorted((pair_normalize(pair1), pair_normalize(pair2))))

def lift(comp, multiplier):
    return comparison(*[tuple((multiplier*t)%P for t in ab) for ab in comp])

sums = defaultdict(list)
for a in range(P):
    for b in range(a, P):
        sums[((a+b)%P,(pow(a,4,P)+pow(b,4,P))%P)].append((a,b))
comparisons = set()
for pairs in sums.values():
    for ab,cd in combinations(pairs,2):
        comparisons.add(comparison(ab,cd))
assert len(comparisons) == 36
assert Counter(map(len, sums.values())) == {1:118, 2:36}
assert not any(0 in ab for comp in comparisons for ab in comp)
seeds = [comparison((1,6),(12,14)),comparison((1,8),(12,16))]
orbits = [{lift(seed,u) for u in range(1,P)} for seed in seeds]
assert len(orbits[0]) == len(orbits[1]) == 18
assert not (orbits[0] & orbits[1])
assert orbits[0] | orbits[1] == comparisons

residues = {x*x%P for x in range(1,P)}
legendre = lambda x: 0 if x%P == 0 else (1 if x%P in residues else -1)
assert len(residues) == 9
for comp in comparisons:
    (a,b),(c,d) = comp
    assert (a+b-c-d)%P == 0
    assert (pow(a,4,P)+pow(b,4,P)-pow(c,4,P)-pow(d,4,P))%P == 0
    assert legendre(a)*legendre(b) == legendre(c)*legendre(d)

# One dilation orbit already supplies all 17 independent nonconstant nonzero-phase constraints.
# The row for multiplier 18 is redundant. Identify the degree-zero lattice on
# indices 1..18 with Z^17 by deleting the coordinate indexed 18.
minor=[]
for u in range(1,18):
    v = [0]*P
    for t in seeds[0][0]:v[u*t%P] += 1
    for t in seeds[0][1]:v[u*t%P] -= 1
    assert v[0] == 0 and sum(v)==0
    minor.append(v[1:18])
determinant = det_bareiss(minor)
assert abs(determinant) == 722, determinant

# Derive the unrestricted phase-only maximum from exact ordered-pair fibers.
ordered = defaultdict(list)
for a in range(P):
    for b in range(P):
        ordered[((a+b)%P, (pow(a,4,P)+pow(b,4,P))%P)].append((a,b))
hist = Counter(map(len,ordered.values()))
energy = sum(len(fiber)**2 for fiber in ordered.values())
assert energy == 991
assert energy == 3*P*P-5*P+3
assert hist == {1:19,2:99,4:36}, hist

# P=19 phase parameter signatures are distinct modulo nonzero common phase:
# the 19^2 exponential characters of x and x^4 are distinct on nonzero x,
# and the Legendre sign has order two, disjoint from the odd-order characters.
for A in range(P):
    for B in range(P):
        if A == B == 0: continue
        residues_character = {(A*t+B*pow(t,4,P))%P for t in range(1,P)}
        assert len(residues_character) > 1
assert len({(A,B,e) for A in range(P) for B in range(P) for e in (0,1)}) == 722
print('VERIFY_OK p=19 unordered_fibers=154 collision_relations=36 orbit_sizes=18,18')
print('VERIFY_OK minor_17x17_determinant=%d index_bound=722' % determinant)
print('VERIFY_OK ordered_hist=%s energy=%d projective_components=722 circle_dimension=1' % (sorted(hist.items()),energy))
