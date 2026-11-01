#!/usr/bin/env python3
"""Exact finite verification of the Petersen graph's ordinary matching complex.

Only the Python standard library is needed. All graph edges, faces, Hasse incidences,
Morse gradient paths, and finite-group actions are regenerated from definitions.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, permutations
from math import comb

# Petersen graph = KG(5,2), vertices are pairs from {0,1,2,3,4}.
VERTICES = tuple(combinations(range(5), 2))
EDGES = tuple((i, j) for i in range(10) for j in range(i+1, 10)
              if not set(VERTICES[i]).intersection(VERTICES[j]))
assert len(EDGES) == 15
ENDPOINT_MASKS = tuple((1 << i) | (1 << j) for i, j in EDGES)

# An element of MATCHINGS is a bitmask of the 15 graph edges.
MATCHINGS = []
for face in range(1 << 15):
    seen = 0
    for i, endpoint_mask in enumerate(ENDPOINT_MASKS):
        if face & (1 << i):
            if seen & endpoint_mask:
                break
            seen |= endpoint_mask
    else:
        MATCHINGS.append(face)
MATCHINGS = tuple(MATCHINGS)
MATCH_SET = set(MATCHINGS)
EXPECTED = {0: 1, 1: 15, 2: 75, 3: 145, 4: 90, 5: 6}
assert dict(Counter(f.bit_count() for f in MATCHINGS)) == EXPECTED
assert len(MATCHINGS) == 332

# Independent matching polynomial from vertex-deletion recurrence.
ADJ = [set() for _ in range(10)]
for a, b in EDGES:
    ADJ[a].add(b)
    ADJ[b].add(a)

@lru_cache(maxsize=None)
def matching_poly(vertices):
    if not vertices:
        return (1,)
    v = (vertices & -vertices).bit_length() - 1
    rem = vertices ^ (1 << v)
    p0 = matching_poly(rem)
    out = list(p0)
    for u in ADJ[v]:
        if rem & (1 << u):
            q = matching_poly(rem ^ (1 << u))
            for k, value in enumerate(q):
                if len(out) <= k + 1:
                    out.extend([0] * (k + 2 - len(out)))
                out[k+1] += value
    return tuple(out)
assert matching_poly((1 << 10) - 1) == tuple(EXPECTED.values())
print('FACES_OK', EXPECTED, 'independent_deletion_recurrence=agrees')

# A fixed greedy sequence of toggling edges. The initial augmented pair
# (empty face, vertex) is removed to obtain a Morse vector field on the
# ordinary nonempty face poset, with exactly one critical vertex.
PRIORITY = (14, 12, 9, 13, 0, 4, 3, 1, 7, 11, 8, 6, 5, 2, 10)
unmatched = set(MATCHINGS)
pairs = []
for i in PRIORITY:
    for a in sorted(unmatched):
        b = a | (1 << i)
        if not (a & (1 << i)) and a in unmatched and b in unmatched:
            assert b.bit_count() == a.bit_count() + 1
            unmatched.remove(a)
            unmatched.remove(b)
            pairs.append((a, b))
assert len(pairs) == 161
empty_pair = next((a, b) for a, b in pairs if a == 0)
pairs.remove(empty_pair)
unmatched.add(empty_pair[1])
assert 0 not in unmatched
CRITICAL = set(unmatched)
assert Counter(f.bit_count()-1 for f in CRITICAL) == {0: 1, 2: 5, 3: 5}
assert len(pairs) == 160
LOWER_TO_UPPER = dict(pairs)
UPPER_TO_LOWER = {upper: lower for lower, upper in pairs}
assert len(LOWER_TO_UPPER) == len(UPPER_TO_LOWER) == 160

# Exhaustively check that reversing matched edges in the Hasse graph
# produces a directed acyclic graph (the acyclicity criterion for Morse).
adj = {f: [] for f in MATCHINGS if f}
indegree = {f: 0 for f in adj}
incidences = 0
for f in adj:
    for i in range(15):
        if f & (1 << i):
            lower = f ^ (1 << i)
            if not lower:
                continue
            a, b = ((lower, f) if LOWER_TO_UPPER.get(lower) == f
                    else (f, lower))
            adj[a].append(b)
            indegree[b] += 1
            incidences += 1
queue = deque(v for v in adj if indegree[v] == 0)
visited = 0
while queue:
    v = queue.popleft()
    visited += 1
    for w in adj[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            queue.append(w)
assert visited == 331 and incidences == 975
print('MORSE_OK', 'matched_pairs=160', 'critical={0:1,2:5,3:5}',
      'nonempty_faces=331', 'Hasse_incidences=975', 'DAG=True')

# Exact signed gradient-path computation of the Morse boundary d3: C3 -> C2.
CRIT2 = sorted(f for f in CRITICAL if f.bit_count() == 3)
CRIT3 = sorted(f for f in CRITICAL if f.bit_count() == 4)

def boundary(f):
    return [(f ^ (1 << i), (-1)**((f & ((1 << i)-1)).bit_count()))
            for i in range(15) if f & (1 << i)]

@lru_cache(None)
def project_to_critical_2(face):
    if face in CRITICAL:
        return {face: 1}
    if face in UPPER_TO_LOWER:
        return {}
    upper = LOWER_TO_UPPER[face]
    pivot = dict(boundary(upper))[face]
    result = {}
    for lower, incidence in boundary(upper):
        if lower == face:
            continue
        for crit, multiplicity in project_to_critical_2(lower).items():
            result[crit] = result.get(crit, 0) - (incidence//pivot)*multiplicity
    return {c: z for c, z in result.items() if z}

morse_boundary = []
for f in CRIT3:
    result = {}
    for lower, incidence in boundary(f):
        for crit, multiplicity in project_to_critical_2(lower).items():
            result[crit] = result.get(crit, 0) + incidence*multiplicity
    morse_boundary.append(tuple(result.get(g, 0) for g in CRIT2))
assert morse_boundary == [(0,)*5]*5
print('MORSE_BOUNDARY_OK', 'd3=zero_5_by_5_integer_matrix')

# Integral Morse CW model has cells only in degrees 0,2,3, and d3=0.
# Since the 1-skeleton is a point, every 3-cell attaching map is determined
# by its degree in pi_2(vee^5 S^2) = Z^5; zero boundary means null attaching.
# Hence the integral homotopy type is (vee^5 S^2) vee (vee^5 S^3).

# Full S5-representation: trace on im(d3) by modular Gaussian elimination.
# Its rational rank is exactly 79 by the verified Morse homology ranks:
# rank(d3) = 145 - rank(d2) - beta_2 = 145 - 61 - 5 = 79.
# We independently verify this rank in characteristic p. Since these
# representations are finite-order, integer traces are bounded in absolute
# value by their dimensions; p > 2*79 gives a unique integer lift.
prime = 1000003
faces2 = sorted(f for f in MATCHINGS if f.bit_count() == 3)
faces3 = sorted(f for f in MATCHINGS if f.bit_count() == 4)
index2 = {f: i for i, f in enumerate(faces2)}
basis = []
pivots = []

def eliminate(vec, extend=False):
    vec = {i: c % prime for i, c in vec.items() if c % prime}
    coeff = []
    for i, basis_vector in enumerate(basis):
        c = vec.get(pivots[i], 0)
        coeff.append(c)
        if c:
            for j, value in basis_vector.items():
                newval = (vec.get(j, 0) - c*value) % prime
                if newval:
                    vec[j] = newval
                else:
                    vec.pop(j, None)
    if extend and vec:
        pivot = min(vec)
        scale = pow(vec[pivot], -1, prime)
        basis.append({j: c*scale % prime for j, c in vec.items()})
        pivots.append(pivot)
    return coeff, vec

for f in faces3:
    eliminate({index2[g]: v for g, v in boundary(f)}, extend=True)
assert len(basis) == 79


def perm_sign(arr):
    return (-1)**sum(arr[i] > arr[j]
                     for i in range(len(arr)) for j in range(i+1, len(arr)))


def group_action(perm):
    vmap = {i: VERTICES.index(tuple(sorted(perm[t] for t in v)))
            for i, v in enumerate(VERTICES)}
    emap = [EDGES.index(tuple(sorted((vmap[i], vmap[j])))) for i, j in EDGES]
    assert sorted(emap) == list(range(15))
    def image(f):
        mapped_edges = [emap[i] for i in range(15) if f & (1 << i)]
        return sum(1 << i for i in mapped_edges), perm_sign(mapped_edges)
    return image


def fixed_chain_trace(faces, image):
    return sum(sign for face in faces
               for gface, sign in (image(face),) if gface == face)


def cycle_statistics(perm):
    f = sum(i == j for i, j in enumerate(perm))
    t = sum(perm[i] == j and perm[j] == i
            for i in range(5) for j in range(i+1, 5))
    sign = perm_sign(perm)
    return f, t, sign

characters = {}
class_counts = Counter()
for perm in permutations(range(5)):
    image = group_action(perm)
    chain_traces = {k: fixed_chain_trace(
        [face for face in MATCHINGS if face.bit_count() == k+1], image)
        for k in range(5)}
    moved_index = {}
    for i, face in enumerate(faces2):
        g, sign = image(face)
        moved_index[i] = (index2[g], sign)
    trace_b2 = 0
    for j, vec in enumerate(basis):
        transformed = {moved_index[i][0]: v*moved_index[i][1] % prime
                       for i, v in vec.items()}
        coordinates, remainder = eliminate(transformed)
        assert not remainder
        trace_b2 += coordinates[j]
    trace_b2 = trace_b2 % prime
    if trace_b2 > prime // 2:
        trace_b2 -= prime
    assert abs(trace_b2) <= 79
    # H_2 = C_2 - C_1 + C_0 - trivial - B_2 in R(S5).
    trace_h2 = chain_traces[2]-chain_traces[1]+chain_traces[0]-1-trace_b2
    # H_3 = C_3 - B_2 - C_4 since d4 is injective.
    trace_h3 = chain_traces[3]-trace_b2-chain_traces[4]
    fixed, transpositions, sign = cycle_statistics(perm)
    assert trace_h2 == sign*fixed, (perm, trace_h2, sign*fixed)
    assert trace_h3 == comb(fixed, 2) + transpositions - fixed
    assert abs(trace_h2) <= 5 and abs(trace_h3) <= 5
    cycle_type = []
    visited = set()
    for v in range(5):
        if v not in visited:
            w = v
            length = 0
            while w not in visited:
                visited.add(w)
                length += 1
                w = perm[w]
            cycle_type.append(length)
    cycle_type = tuple(sorted(cycle_type, reverse=True))
    class_counts[cycle_type] += 1
    characters.setdefault(cycle_type, (trace_h2, trace_h3))
    assert characters[cycle_type] == (trace_h2, trace_h3)
assert len(characters) == 7
EXPECTED_CHAR = {
    (1,1,1,1,1):(5,5),
    (2,1,1,1):(-3,1),
    (2,2,1):(1,1),
    (3,1,1):(2,-1),
    (3,2):(0,1),
    (4,1):(-1,-1),
    (5,):(0,0),
}
assert characters == EXPECTED_CHAR
assert sum(class_counts[t]*v[1]*v[1] for t,v in characters.items()) == 120
assert sum(class_counts.values()) == 120
print('SYMMETRY_OK', 'all_S5_elements=120', 'conjugacy_classes=7',
      'H2=sign_tensor_five_point_permutation',
      'H3=two_subset_permutation_minus_point_permutation')
for kind in sorted(characters, reverse=True):
    print('CHAR', kind, *characters[kind])
print('ALL_VERIFY_OK')
