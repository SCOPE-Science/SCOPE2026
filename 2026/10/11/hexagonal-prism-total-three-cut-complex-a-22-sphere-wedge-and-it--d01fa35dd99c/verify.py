"""Exact standalone verifier for the total three-cut complex of the hexagonal prism.
Only Python's standard library is required. All assertions are exact.
"""
from collections import Counter, deque
from itertools import combinations
from fractions import Fraction
from math import comb

N = 12
ORDER = tuple(range(N))
EDGE_SET = set()
for layer in (0, 1):
    for i in range(6):
        u = layer * 6 + i
        v = layer * 6 + (i + 1) % 6
        EDGE_SET.add(tuple(sorted((u, v))))
for i in range(6):
    EDGE_SET.add((i, i + 6))
assert len(EDGE_SET) == 18

# Independent triples and complements generate every face of the total cut complex.
independent = []
for tr in combinations(range(N), 3):
    if all(not (u in tr and v in tr) for u, v in EDGE_SET):
        independent.append(sum(1 << i for i in tr))
assert len(independent) == 76
faces = set()
for tr in independent:
    facet = ((1 << N) - 1) ^ tr
    s = facet
    while True:
        faces.add(s)
        if s == 0:
            break
        s = (s - 1) & facet
assert len(faces) == 3762
counts = Counter(s.bit_count() - 1 for s in faces)
assert [counts[d] for d in range(-1, 9)] == [1,12,66,220,495,792,924,792,384,76]

# Filtered element matchings. Excluding the empty face's pair from the
# ordinary matching leaves one critical vertex. The remaining pairs are unchanged.
remaining = set(faces)
matching = []
for vertex in ORDER:
    bit = 1 << vertex
    for lower in sorted(remaining):
        upper = lower | bit
        if not lower & bit and upper in remaining:
            assert lower in remaining
            remaining.remove(lower)
            remaining.remove(upper)
            matching.append((lower, upper))
assert len(matching) == 1870
assert len(remaining) == 22
assert Counter(x.bit_count() - 1 for x in remaining) == {6: 22}
assert (0, 1) in matching
ordinary_matching = {(lower, upper) for lower, upper in matching if lower}
ordinary_faces = faces - {0}
assert len(ordinary_matching) == 1869
critical = ordinary_faces - {s for pair in ordinary_matching for s in pair}
assert Counter(x.bit_count() - 1 for x in critical) == {0: 1, 6: 22}

# Complete directed Hasse graph with matched arcs reversed. Kahn sorting
# witnesses no directed cycle and therefore a valid Forman acyclic matching.
idx = {s: j for j, s in enumerate(sorted(ordinary_faces))}
adj = [[] for _ in idx]
indeg = [0] * len(idx)
incidences = 0
for upper in ordinary_faces:
    s = upper
    while s:
        lsb = s & -s
        s ^= lsb
        lower = upper ^ lsb
        if lower == 0:
            continue
        incidences += 1
        if (lower, upper) in ordinary_matching:
            a, b = idx[upper], idx[lower]
        else:
            a, b = idx[lower], idx[upper]
        adj[a].append(b)
        indeg[b] += 1
queue = deque(i for i, degree in enumerate(indeg) if degree == 0)
visited = 0
while queue:
    x = queue.popleft()
    visited += 1
    for y in adj[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            queue.append(y)
assert visited == len(idx)

# An independent chain-complex check over F_2, using all simplices and boundary
# reductions (not the matching). Rank counts include augmented d_0.
bydim = {d: sorted(s for s in faces if s.bit_count() - 1 == d) for d in range(-1, 9)}
ranks = {}
for d in range(9):
    prior = {s: j for j, s in enumerate(bydim[d - 1])}
    pivots = {}
    for upper in bydim[d]:
        column = 0
        z = upper
        while z:
            b = z & -z
            z -= b
            column ^= 1 << prior[upper ^ b]
        while column:
            pivot = column.bit_length()
            if pivot in pivots:
                column ^= pivots[pivot]
            else:
                pivots[pivot] = column
                break
    ranks[d] = len(pivots)
assert ranks == {0: 1, 1: 11, 2: 55, 3: 165, 4: 330,
                 5: 462, 6: 462, 7: 308, 8: 76}
betti = {d: counts[d] - ranks[d] - ranks.get(d + 1, 0) for d in range(9)}
assert {d: x for d, x in betti.items() if x} == {6: 22}

# All 24 graph automorphisms preserving the two hexagonal rims.
def transform(v, sign, shift, swap):
    layer, i = divmod(v, 6)
    return 6 * (layer ^ swap) + (sign * i + shift) % 6

def permutation_sign(entries):
    return -1 if sum(entries[i] > entries[j]
                     for i in range(len(entries)) for j in range(i + 1, len(entries))) % 2 else 1

def trace_on_reduced_homology(sign, shift, swap):
    permutation = [transform(i, sign, shift, swap) for i in range(N)]
    assert {tuple(sorted((permutation[u], permutation[v]))) for u, v in EDGE_SET} == EDGE_SET
    # Reduced Lefschetz: -1 from the augmented chain of the empty face.
    answer = -1
    for face in ordinary_faces:
        verts = [i for i in range(N) if face >> i & 1]
        image = [permutation[i] for i in verts]
        if sum(1 << i for i in image) == face:
            answer += (-1) ** (len(verts) - 1) * permutation_sign(image)
    return answer

characters = {(sgn, shift, swap): trace_on_reduced_homology(sgn, shift, swap)
              for sgn in (1, -1) for shift in range(6) for swap in (0, 1)}
assert len(characters) == 24
for swap in (0, 1):
    assert characters[(1, 0, swap)] == (22 if swap == 0 else 10)
    for shift in range(1, 6):
        assert characters[(1, shift, swap)] == (4 if shift == 3 else 1)
    for shift in range(6):
        expected = 4 if shift % 2 == 0 else (6 if swap == 0 else 2)
        assert characters[(-1, shift, swap)] == expected

# Character orthogonality for D_6 x C_2, with r -> alpha, s -> beta.
actual_decomposition = {}
for alpha in (1, -1):
    for beta in (1, -1):
        for gamma in (1, -1):
            dot = sum(char * alpha ** shift * (beta if sgn == -1 else 1) * gamma ** swap
                      for (sgn, shift, swap), char in characters.items())
            multiplicity = Fraction(dot, 24)
            assert multiplicity.denominator == 1 and multiplicity >= 0
            actual_decomposition[('linear', alpha, beta, gamma)] = int(multiplicity)
for j in (1, 2):
    cosine_trace = {1: (2, 1, -1, -2, -1, 1),
                    2: (2, -1, -1, 2, -1, -1)}[j]
    for gamma in (1, -1):
        dot = sum(char * (cosine_trace[shift] if sgn == 1 else 0) * gamma ** swap
                  for (sgn, shift, swap), char in characters.items())
        multiplicity = Fraction(dot, 24)
        assert multiplicity.denominator == 1 and multiplicity >= 0
        actual_decomposition[('doublet', j, gamma)] = int(multiplicity)
expected_decomposition = {
    ('linear', 1, 1, 1): 4, ('linear', 1, 1, -1): 1,
    ('linear', 1, -1, 1): 0, ('linear', 1, -1, -1): 0,
    ('linear', -1, 1, 1): 1, ('linear', -1, 1, -1): 0,
    ('linear', -1, -1, 1): 1, ('linear', -1, -1, -1): 1,
    ('doublet', 1, 1): 2, ('doublet', 1, -1): 1,
    ('doublet', 2, 1): 3, ('doublet', 2, -1): 1,
}
assert actual_decomposition == expected_decomposition
assert sum((1 if key[0] == 'linear' else 2) * m
           for key, m in actual_decomposition.items()) == 22

print('VERIFY_OK', 'facets', len(independent), 'simplices', len(faces),
      'matching_pairs', len(matching), 'Hasse_incidences', incidences,
      'critical_0', 1, 'critical_6', 22, 'homology_rank_6', betti[6],
      'automorphisms', len(characters))
