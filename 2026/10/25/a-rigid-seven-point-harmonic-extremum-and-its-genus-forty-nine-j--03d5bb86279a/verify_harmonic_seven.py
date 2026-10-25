#!/usr/bin/env python3
"""Exact finite combinatorial and GF(9) checks for a seven-point harmonic configuration."""
from itertools import combinations, permutations

# Compatible harmonic four-sets never contain a common three-subset.
quadruples = tuple(combinations(range(7), 4))
qindex = {b: i for i, b in enumerate(quadruples)}
qsets = [set(b) for b in quadruples]
compatible = [{j for j in range(35) if i != j and len(qsets[i] & qsets[j]) <= 2}
              for i in range(35)]
cliques = []

def extend(prefix, available):
    if len(prefix) == 5:
        cliques.append(tuple(prefix))
        return
    for j in sorted(available):
        extend(prefix + [j], {k for k in available if k > j and k in compatible[j]})

extend([], set(range(35)))
assert len(cliques) == 1050, len(cliques)
reps = [
    ((0,1,2,5), (0,1,4,6), (0,3,5,6), (1,2,3,6), (2,3,4,5)),
    ((0,1,2,6), (0,1,4,5), (0,2,3,5), (1,2,3,4), (1,3,5,6)),
]
remaining = set(cliques)
orbit_sizes = []
for named_rep in reps:
    rep = tuple(sorted(qindex[q] for q in named_rep))
    orbit = set()
    for perm in permutations(range(7)):
        transported = tuple(sorted(qindex[tuple(sorted(perm[i] for i in quadruples[j]))]
                                   for j in rep))
        orbit.add(transported)
    assert orbit <= remaining
    remaining -= orbit
    orbit_sizes.append(len(orbit))
assert not remaining and orbit_sizes == [420, 630], (remaining, orbit_sizes)

# GF(9) = GF(3)[z]/(z^2-z-1), with z^2=z+1.
def fadd(a, b):
    return ((a[0]+b[0]) % 3, (a[1]+b[1]) % 3)
def fneg(a):
    return ((-a[0]) % 3, (-a[1]) % 3)
def fsub(a,b):
    return fadd(a,fneg(b))
def fmul(a,b):
    return ((a[0]*b[0]+a[1]*b[1]) % 3,
            (a[0]*b[1]+a[1]*b[0]+a[1]*b[1]) % 3)
def det(a,b):
    if a is None: return (1,0)
    if b is None: return (2,0)
    return fsub(a,b)
def harmonic(q):
    a,b,c,d=q
    return fadd(fmul(det(a,c),det(b,d)), fmul(det(a,d),det(b,c))) == (0,0)

z=(0,1)
B=(None,(0,0),(1,0),fsub((1,0),z),fneg(z),(2,0),z)
assert len(set(B))==7
labels=[Q for Q in quadruples if harmonic(tuple(B[i] for i in Q))]
assert len(labels)==5, labels
# The union of the five four-subsets reaches every deleted-point six-subset.
assert all(any(j not in Q for Q in labels) for j in range(7))

# Every seven-subset of PG(1,9) has five harmonic tetrads.
full=[(a,b) for a in range(3) for b in range(3)] + [None]
assert len(set(full))==10
seven_counts={sum(harmonic(tuple(full[j] for j in Q)) for Q in combinations(S,4))
              for S in combinations(range(10),7)}
assert seven_counts=={5},seven_counts

# The normalized nonextendible five-block equations reduce to
# w=-1, v=-z, u=1-z and z^2-z-1=0. Check the last condition.
one=(1,0)
assert fsub(fsub(fmul(z,z),z),one)==(0,0)
print('VERIFY_OK: 1050 compatible 5-block systems, S7 orbits 420+630; '
      'GF9 canonical septad 5 harmonic tetrads, all 120 septads of PG1(F9) have 5')
