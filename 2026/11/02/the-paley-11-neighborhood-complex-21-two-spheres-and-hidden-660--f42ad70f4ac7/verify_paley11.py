#!/usr/bin/env python3
"""Self-contained exact finite checks for the 11-point biplane neighborhood complex.

Run with Python 3.10 or later; only the standard library is used.
"""
from collections import Counter, deque
from itertools import combinations
from math import lcm

N = 11
Q = {a*a % N for a in range(1, N)}
assert Q == {1, 3, 4, 5, 9}
blocks = tuple(frozenset((a + q) % N for q in Q) for a in range(N))
assert len(set(blocks)) == N
assert all(len(B) == 5 for B in blocks)
assert all(len(A & B) == 2 for i, A in enumerate(blocks)
           for B in blocks[i+1:])
faces = set()
for B in blocks:
    for k in range(1, 6):
        faces.update(tuple(s) for s in combinations(sorted(B), k))
ordered = tuple(sorted(faces, key=lambda s: (len(s), s)))
F = tuple(tuple(s for s in ordered if len(s) == d+1) for d in range(5))
assert tuple(map(len, F)) == (11, 55, 110, 55, 11)

# Lexicographically ordered vertex-toggle discrete Morse matching.
active = set(ordered)
pairs = []
for pivot in range(N):
    for lower in sorted(active, key=lambda s: (len(s), s)):
        if pivot in lower or lower not in active:
            continue
        upper = tuple(sorted(lower + (pivot,)))
        if upper in active:
            active.remove(lower)
            active.remove(upper)
            pairs.append((lower, upper))
assert len(pairs) == 110
assert Counter(len(s)-1 for s in active) == {0: 1, 2: 21}

# Fully traverse reversed matching Hasse graph to prove acyclicity.
idx = {s: i for i, s in enumerate(ordered)}
matched = set(pairs)
adj = [[] for _ in ordered]
indeg = [0]*len(ordered)
incidence_count = 0
for upper in ordered:
    if len(upper) <= 1:
        continue
    for j in range(len(upper)):
        lower = upper[:j] + upper[j+1:]
        if (lower, upper) in matched:
            x, y = idx[lower], idx[upper]
        else:
            x, y = idx[upper], idx[lower]
        adj[x].append(y)
        indeg[y] += 1
        incidence_count += 1
assert incidence_count == 715
queue = deque(i for i, degree in enumerate(indeg) if degree == 0)
visited = 0
while queue:
    i = queue.popleft()
    visited += 1
    for j in adj[i]:
        indeg[j] -= 1
        if indeg[j] == 0:
            queue.append(j)
assert visited == len(ordered), 'gradient cycle detected'

# Independent mod-two boundary-rank check (not used for the homotopy proof).
ranks = []
for d in range(1, 5):
    rows = {face: i for i, face in enumerate(F[d-1])}
    basis = {}
    for face in F[d]:
        column = 0
        for j in range(len(face)):
            column ^= 1 << rows[face[:j] + face[j+1:]]
        while column:
            h = column.bit_length()-1
            if h not in basis:
                basis[h] = column
                break
            column ^= basis[h]
    ranks.append(len(basis))
assert ranks == [10, 45, 44, 11]
assert [len(F[d])-(ranks[d-1] if d else 1)-
        (ranks[d] if d < 4 else 0) for d in range(5)] == [0,0,21,0,0]

# Exhaustive automorphism enumeration. For each new point image, test all
# newly completed faces of size at most five in both directions. This is
# equivalent to preserving every maximal five-point block.
aut = []
levels = [0]*12
def enumerate_automorphisms(img, used):
    k = len(img)
    levels[k] += 1
    if k == N:
        aut.append(tuple(img))
        return
    for v in range(N):
        if used & (1 << v):
            continue
        ok = True
        for j in range(min(k, 4)+1):
            for ii in combinations(range(k), j):
                source = tuple(sorted(ii + (k,)))
                target = tuple(sorted([img[i] for i in ii] + [v]))
                if (source in faces) != (target in faces):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            enumerate_automorphisms(img+[v], used | (1 << v))
enumerate_automorphisms([], 0)
assert len(aut) == len(set(aut)) == 660
assert levels == [1, 11, 110, 660, 660, 660, 660, 660, 660, 660, 660, 660]
assert all({frozenset(perm[x] for x in B) for B in blocks} == set(blocks)
           for perm in aut)

# Also check that the tournament-preserving subgroup consists precisely of
# the 55 oriented affine maps, not the additional biplane symmetries.
affine_maps = {tuple((a + b*x) % N for x in range(N))
               for a in range(N) for b in Q}
tournament_automorphisms = {p for p in aut if all(
    ((y-x) % N in Q) == ((p[y]-p[x]) % N in Q)
    for x in range(N) for y in range(N) if x != y)}
assert tournament_automorphisms == affine_maps and len(affine_maps) == 55

def group_order(perm):
    seen = set()
    n = 1
    for x in range(N):
        if x in seen:continue
        y = x
        k = 0
        while y not in seen:
            seen.add(y)
            y = perm[y]
            k += 1
        n = lcm(n, k)
    return n

def sign_of_permutation(values):
    inversions = sum(values[i] > values[j] for i in range(len(values))
                     for j in range(i+1, len(values)))
    return -1 if inversions & 1 else 1

def second_homology_trace(perm):
    # Integral simplicial Lefschetz trace. Since homology is only
    # H_0=Q and H_2=Q^21, trace(H_2)=Lefschetz-1.
    L = 0
    for face in ordered:
        image = [perm[x] for x in face]
        if tuple(sorted(image)) == face:
            L += ((-1) ** (len(face)-1)) * sign_of_permutation(image)
    return L - 1

spectrum = Counter()
scalar_product = 0
augmentation_product = 0
affine_traces = []
for perm in aut:
    chi = second_homology_trace(perm)
    fixed = sum(perm[i] == i for i in range(N))
    spectrum[(group_order(perm), fixed, chi)] += 1
    scalar_product += chi*chi
    augmentation_product += chi*(fixed-1)
assert dict(spectrum) == {
    (1,11,21):1, (2,3,-3):55, (3,2,0):110,
    (5,1,1):264, (6,0,0):110, (11,0,-1):120,
}
assert sum(chi*count for (_, _, chi), count in spectrum.items()) == 0
assert scalar_product == 2*660
assert augmentation_product == 0

# Natural orientation-preserving affine subgroup, order 11*5=55.
affine = set()
for t in range(N):
    for a in Q:
        perm = tuple((t+a*x) % N for x in range(N))
        assert perm in aut
        affine.add(perm)
assert len(affine) == 55
affine_distribution = Counter(second_homology_trace(p) for p in affine)
assert affine_distribution == {21:1, 1:44, -1:10}
assert sum(v*c for v, c in affine_distribution.items()) == 55
print('PALEY11_BIPLANE_21S2_FULL660_EQUIVARIANT_CHECKS_OK')
print('faces',tuple(map(len,F)),'matched_pairs',len(pairs),
      'critical',len(active),'Hasse',incidence_count,'F2_ranks',ranks)
print('automorphisms',len(aut),'spectrum',sorted(spectrum.items()))
print('invariants: full_group=0, affine_subgroup=1; character_squared_norm=2')
