#!/usr/bin/env python3
"""Exact finite verification for the 2-independence complex of the Clebsch graph.

Only Python's standard library is used. All graph vertices, simplices, chain
coefficients, and incidence signs are reconstructed rather than loaded.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 16
STEPS = (1, 2, 4, 8, 15)
ORDER = (12, 11, 7, 13, 6, 0, 8, 3, 9, 4, 10, 2, 5, 14, 15, 1)


def vertices(mask):
    return [v for v in range(N) if mask & (1 << v)]


def boundary(mask):
    sign = 1
    for v in vertices(mask):
        yield mask ^ (1 << v), sign
        sign = -sign


edges = {(min(v, v ^ s), max(v, v ^ s)) for v in range(N) for s in STEPS}
adj = [0] * N
for u, v in edges:
    adj[u] |= 1 << v
    adj[v] |= 1 << u
assert len(edges) == 40 and all(a.bit_count() == 5 for a in adj)

bad_triples = set()
for v in range(N):
    for u, w in combinations(vertices(adj[v]), 2):
        bad_triples.add((1 << u) | (1 << v) | (1 << w))
assert len(bad_triples) == 160

# Two logically separate face tests: no length-two path, and induced maximum
# degree at most one. Their exact agreement checks the definition on all masks.
valid_by_triples = [True] * (1 << N)
for mask in range(1, 1 << N):
    valid_by_triples[mask] = not any((mask & t) == t for t in bad_triples)
valid_by_degrees = [True] * (1 << N)
for mask in range(1, 1 << N):
    valid_by_degrees[mask] = all((adj[v] & mask).bit_count() <= 1 for v in vertices(mask))
assert valid_by_triples == valid_by_degrees
faces = [mask for mask in range(1, 1 << N) if valid_by_triples[mask]]
face_set = set(faces)
face_counts = Counter(mask.bit_count() - 1 for mask in faces)
assert len(faces) == 2142

# Sequential available-face toggles: every face is in at most one pair.
remaining = set(faces)
lower_to_upper = {}
for v in ORDER:
    bit = 1 << v
    for lower in faces:
        upper = lower | bit
        if not lower & bit and lower in remaining and upper in remaining:
            remaining.remove(lower)
            remaining.remove(upper)
            lower_to_upper[lower] = upper
upper_to_lower = {upper: lower for lower, upper in lower_to_upper.items()}
assert len(lower_to_upper) == len(upper_to_lower) == 1069
critical = sorted(remaining)
assert critical == [4096, 33046, 33552, 34328]

# Directed Hasse graph: matched face coverings point upward, all others downward.
indegree = {mask: 0 for mask in faces}
outgoing = defaultdict(list)
cover_count = 0
for upper in faces:
    for lower, _ in boundary(upper):
        if not lower or lower not in face_set:
            continue
        cover_count += 1
        if lower_to_upper.get(lower) == upper:
            a, b = lower, upper
        else:
            a, b = upper, lower
        outgoing[a].append(b)
        indegree[b] += 1
queue = deque(mask for mask in faces if indegree[mask] == 0)
topologically_sorted = 0
while queue:
    cell = queue.popleft()
    topologically_sorted += 1
    for target in outgoing[cell]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
assert (cover_count, topologically_sorted) == (9280, len(faces))

# Exact integral algebraic-Morse path evaluation. For a matched lower d-cell
# a, its paired (d+1)-cell b obeys db = +/-a + sum other d-faces. Eliminating
# a substitutes the negative of the other terms divided by the unit incidence.
# An upper matched d-cell projects to zero. Acyclicity guarantees termination.
@lru_cache(maxsize=None)
def project(mask):
    if mask in remaining:
        return {mask: 1}
    if mask in upper_to_lower:
        return {}
    upper = lower_to_upper[mask]
    terms = dict(boundary(upper))
    unit = terms[mask]
    assert unit in (-1, 1)
    output = defaultdict(int)
    for subface, incidence in terms.items():
        if subface == mask:
            continue
        for critical_face, coeff in project(subface).items():
            output[critical_face] -= unit * incidence * coeff
    return {face: coefficient for face, coefficient in output.items() if coefficient}

critical_three_cells = [mask for mask in critical if mask.bit_count() == 4]
critical_four_cells = [mask for mask in critical if mask.bit_count() == 5]
assert len(critical_three_cells) == 1 and len(critical_four_cells) == 2
morse_rows = []
for upper in critical_four_cells:
    combination = defaultdict(int)
    for lower, incidence in boundary(upper):
        for other, coefficient in project(lower).items():
            combination[other] += incidence * coefficient
    morse_rows.append(tuple(combination[low] for low in critical_three_cells))
assert morse_rows == [(1,), (1,)]

# Independent calculation of homology over F_2 from ALL original boundaries.
by_dim = defaultdict(list)
for mask in faces:
    by_dim[mask.bit_count() - 1].append(mask)


def rank_mod_two(columns):
    pivots = {}
    for vector in columns:
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = vector
                break
            vector ^= pivots[pivot]
    return len(pivots)

ranks = {}
for d in range(1, max(by_dim) + 1):
    indexes = {mask: i for i, mask in enumerate(by_dim[d - 1])}
    columns = []
    for mask in by_dim[d]:
        vector = 0
        for subface, _ in boundary(mask):
            vector ^= 1 << indexes[subface]
        columns.append(vector)
    ranks[d] = rank_mod_two(columns)
betti = {d: len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0) - (d == 0)
         for d in sorted(by_dim)}
assert betti == {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0}


def reduced_lefschetz(mapping):
    assert set(mapping) == set(range(N))
    assert all(tuple(sorted((mapping[a], mapping[b]))) in edges for a, b in edges)
    signed_traces = Counter()
    fixed_by_dim = Counter()
    for face in faces:
        images = [mapping[v] for v in vertices(face)]
        if sum(1 << w for w in images) != face:
            continue
        d = face.bit_count() - 1
        inversions = sum(images[i] > images[j] for i in range(len(images))
                         for j in range(i + 1, len(images)))
        signed_traces[d] += -1 if inversions % 2 else 1
        fixed_by_dim[d] += 1
    trace = -1 + sum((-1) ** d * coeff for d, coeff in signed_traces.items())
    return trace, dict(sorted(fixed_by_dim.items())), dict(sorted(signed_traces.items()))

translation = [v ^ 1 for v in range(N)]
swap_steps = [((v & 1) << 1) | ((v & 2) >> 1) | (v & 12) for v in range(N)]
swap_last = [(v & 7) ^ (15 if v & 8 else 0) for v in range(N)]
tr, cnt_t, signs_t = reduced_lefschetz(translation)
sw, cnt_s, signs_s = reduced_lefschetz(swap_steps)
sw_last, cnt_l, signs_l = reduced_lefschetz(swap_last)
assert (tr, sw, sw_last) == (1, -1, -1)

print('graph_vertices=16 graph_edges=40 forbidden_induced_paths_on_three_vertices=160')
print('nonempty_faces=', len(faces))
print('face_counts_by_dimension=', dict(sorted(face_counts.items())))
print('matching_pairs=', len(lower_to_upper), 'face_cover_relations=', cover_count,
      'topological_sort_vertices=', topologically_sorted)
print('critical_mask_and_dimension=', [(mask, mask.bit_count() - 1) for mask in critical])
print('integral_morse_boundary_4_to_3_columns=', morse_rows)
print('reduced_homology_ranks_mod_2=', betti)
print('translation_generator_trace=', tr, 'fixed_counts=', cnt_t, 'signed_chain_traces=', signs_t)
print('S5_transposition_trace=', sw, 'fixed_counts=', cnt_s, 'signed_chain_traces=', signs_s)
print('second_transposition_trace=', sw_last, 'fixed_counts=', cnt_l, 'signed_chain_traces=', signs_l)
print('ALL_CHECKS_PASSED')
