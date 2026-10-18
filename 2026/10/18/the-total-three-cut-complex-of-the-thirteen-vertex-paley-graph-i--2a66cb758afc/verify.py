#!/usr/bin/env python3
"""Reproduce an integral homotopy certificate and affine homology character.

All sets are encoded as masks on F_13, with bit i denoting vertex i.
The finite face-poset matching is checked by a complete directed-acyclicity test.
No mathematical package other than the Python standard library is required.
"""
from collections import Counter, deque
from itertools import combinations

P = 13
ALL = (1 << P) - 1
Q = {x*x % P for x in range(1, P)}
assert Q == {1, 3, 4, 9, 10, 12}


def vertices(mask):
    return [i for i in range(P) if (mask >> i) & 1]


def faces_and_facets():
    independent = []
    for triple in combinations(range(P), 3):
        if all((y-x) % P not in Q for x, y in combinations(triple, 2)):
            independent.append(sum(1 << v for v in triple))
    facets = [ALL ^ m for m in independent]
    faces = set()
    for f in facets:
        s = f
        while True:
            faces.add(s)
            if s == 0:
                break
            s = (s-1) & f
    return independent, facets, faces


independent, facets, faces = faces_and_facets()
assert len(independent) == len(facets) == 26
assert len(faces) == 6553
assert len(set(facets)) == 26
counts = Counter(m.bit_count()-1 for m in faces)
assert [counts[d] for d in range(-1, 10)] == [1,13,78,286,715,1287,1677,1469,780,221,26]

# Fixed, publicly specified element-matching sequence. At a stage, pair all
# currently unmatched cells differing exactly by the chosen vertex.
stages = [0, 2, 4, 12, 6, 3, 7]
U = set(faces)
pairs = []
counts_by_stage = []
for v in stages:
    bit = 1 << v
    stage_pairs = [(s, s | bit) for s in sorted(U)
                   if not (s & bit) and (s | bit) in U]
    counts_by_stage.append(len(stage_pairs))
    for low, high in stage_pairs:
        assert low in U and high in U and high ^ low == bit
        U.remove(low)
        U.remove(high)
    pairs.extend(stage_pairs)
assert counts_by_stage == [3012, 153, 71, 21, 9, 5, 5]
assert U == {sum(1 << v for v in (2,3,4,6,7,12))}
assert (0, 1) in pairs
pairs.remove((0, 1))
assert len(pairs) == 3275
U.update((0, 1))
assert sorted(Counter(m.bit_count()-1 for m in U).items()) == [(-1,1),(0,1),(5,1)]

# Check acyclicity of the augmented face-poset matching, including empty face.
# Every cover relation high -> low is reversed precisely when it is matched.
# A full topological sort tests *every* cover incidence, not just a sample.
matched = {hi:lo for lo,hi in pairs}
assert len(matched) == len(pairs)
assert len({x for pair in pairs for x in pair}) == 2*len(pairs)
adjacency = {m:[] for m in faces}
indegree = {m:0 for m in faces}
incidences = 0
for high in faces:
    for i in vertices(high):
        low = high ^ (1 << i)
        assert low in faces
        if matched.get(high) == low:
            src,dst = low,high
        else:
            src,dst = high,low
        adjacency[src].append(dst)
        indegree[dst] += 1
        incidences += 1
assert incidences == sum(m.bit_count() for m in faces)
ready = deque(m for m in faces if indegree[m] == 0)
visited = 0
while ready:
    m = ready.popleft()
    visited += 1
    for nxt in adjacency[m]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            ready.append(nxt)
assert visited == len(faces), 'Morse matching has an alternating directed cycle'

# Independently compute all augmented simplicial boundary ranks mod 2.
# This is corroboration only: the exact integral homotopy conclusion is from
# the complete acyclic matching, not from field computations.
by_dim = {d:sorted(m for m in faces if m.bit_count()-1==d)
          for d in range(-1, 10)}
ranks = {}
for d in range(0, 10):
    low_index = {m:i for i,m in enumerate(by_dim[d-1])}
    echelon = {}
    for high in by_dim[d]:
        col = 0
        for i in vertices(high):
            col ^= 1 << low_index[high ^ (1 << i)]
        while col:
            lead = col.bit_length()-1
            if lead not in echelon:
                echelon[lead] = col
                break
            col ^= echelon[lead]
    ranks[d] = len(echelon)
reduced_betti = {}
for d in range(-1, 10):
    value = len(by_dim[d]) - ranks.get(d,0) - ranks.get(d+1,0)
    if value:
        reduced_betti[d] = value
assert reduced_betti == {5:1}, reduced_betti

# Exact simplicial reduced Lefschetz trace for every affine symmetry.
# A map fixing a face setwise contributes the orientation permutation sign.
# The empty-face contribution is -1 in reduced Lefschetz theory.
characters = Counter()
for a in sorted(Q):
    for b in range(P):
        image = [(a*i+b)%P for i in range(P)]
        assert all(((image[j]-image[i])%P in Q) == ((j-i)%P in Q)
                   for i in range(P) for j in range(i+1,P))
        lefschetz = 0
        for face in faces:
            vs = vertices(face)
            ws = [image[i] for i in vs]
            if sorted(ws) != vs:
                continue
            inversions = sum(ws[i]>ws[j] for i in range(len(ws))
                             for j in range(i+1,len(ws)))
            parity = ((len(vs)-1) + inversions) % 2
            lefschetz += -1 if parity else 1
        # H~ is concentrated in degree 5, so trace = -L~.
        character = -lefschetz
        expected = 1 if pow(a,3,P)==1 else -1
        assert pow(a,3,P) in (1,P-1)
        assert character == expected, (a,b,character,expected)
        characters[(a,character)] += 1

print('VERIFIED')
print('independent_triples=',len(independent),'facets=',len(facets),'faces=',len(faces))
print('augmented_f_vector=',[counts[d] for d in range(-1,10)])
print('morse_stage_vertices=',stages,'morse_stage_pairs=',counts_by_stage)
print('critical_vertex=0 critical_dimension=5 critical_simplex=',[2,3,4,6,7,12])
print('morse_pairs=',len(pairs),'face_poset_incidences=',incidences,'dag_nodes=',visited)
print('mod2_reduced_betti=',reduced_betti,'boundary_ranks=',[ranks[d] for d in range(10)])
print('affine_group_size=',P*len(Q),'affine_character_by_multiplier=',
      [(a,1 if pow(a,3,P)==1 else -1) for a in sorted(Q)])
