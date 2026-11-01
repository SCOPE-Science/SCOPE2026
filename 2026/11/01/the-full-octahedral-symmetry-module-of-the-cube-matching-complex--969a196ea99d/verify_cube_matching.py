#!/usr/bin/env python3
"""Exact finite verification for the symmetry representation of the cube matching complex.

Python 3.9+ standard library only. The graph, matching simplices, all 48
coordinate symmetries, Morse pairs, orientation signs, and character values
are reconstructed from definitions.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product

cube_vertices = list(product((0, 1), repeat=3))
vertex_index = {v: i for i, v in enumerate(cube_vertices)}
cube_edges = sorted((i, j) for i, v in enumerate(cube_vertices)
                    for j, w in enumerate(cube_vertices)
                    if i < j and sum(v[a] != w[a] for a in range(3)) == 1)
assert len(cube_edges) == 12
assert cube_edges == [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3),
                     (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]

faces = {d: [] for d in range(4)}
for size in range(1, 5):
    for cell in combinations(range(12), size):
        if len({v for i in cell for v in cube_edges[i]}) == 2 * size:
            faces[size - 1].append(cell)
assert [len(faces[d]) for d in range(4)] == [12, 42, 44, 9]
assert all(len({v for i in c for v in cube_edges[i]}) == 2 * len(c)
           for d in faces for c in faces[d])

# Explicit complete acyclic discrete-Morse matching on the nonempty faces.
all_cells = {frozenset(c) for d in faces for c in faces[d]}
unmatched = set(all_cells)
pairs = []
for pivot in range(12):
    for lower in sorted(unmatched, key=lambda s: (len(s), tuple(sorted(s)))):
        upper = lower | {pivot}
        if pivot not in lower and upper in unmatched:
            pairs.append((lower, upper))
            unmatched.remove(lower)
            unmatched.remove(upper)
critical = sorted((tuple(sorted(c)) for c in unmatched),
                  key=lambda s: (len(s), s))
assert len(pairs) == 51
assert critical == [(0,), (2, 5, 11), (2, 6, 10), (3, 6, 8), (4, 5, 9)]
paired = set(pairs)
directed = defaultdict(list)
indegree = {s: 0 for s in all_cells}
cover_count = 0
for upper in all_cells:
    if len(upper) == 1:
        continue
    for v in upper:
        lower = upper - {v}
        if (lower, upper) in paired:
            a, b = lower, upper
        else:
            a, b = upper, lower
        directed[a].append(b)
        indegree[b] += 1
        cover_count += 1
assert cover_count == 252
queue = deque(s for s in all_cells if indegree[s] == 0)
visited = 0
while queue:
    current = queue.popleft()
    visited += 1
    for nxt in directed[current]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
assert visited == len(all_cells) == 107
# Forman's theorem: the five critical cells yield one 0-cell and four
# 2-cells, hence a wedge of four 2-spheres with integral homology Z^4.

# Exhaust every signed coordinate permutation (48 graph automorphisms).
axes = sorted({tuple(sorted((vertex_index[v],
                             vertex_index[tuple(1 - b for b in v)])))
               for v in cube_vertices})
assert len(axes) == 4
axis_number = {axis: i for i, axis in enumerate(axes)}

def inversion_parity(seq):
    return (-1) ** sum(seq[i] > seq[j]
                       for i in range(len(seq))
                       for j in range(i + 1, len(seq)))

def cycle_type(mapping):
    seen = set()
    lengths = []
    for i in range(len(mapping)):
        if i in seen:
            continue
        n = 0
        j = i
        while j not in seen:
            seen.add(j)
            n += 1
            j = mapping[j]
        assert j == i
        lengths.append(n)
    return tuple(sorted(lengths, reverse=True))

def chain_trace(edge_permutation, dimension):
    trace = 0
    for simplex in faces[dimension]:
        image = [edge_permutation[e] for e in simplex]
        if tuple(sorted(image)) == simplex:
            trace += inversion_parity(image)
    return trace

class_values = defaultdict(list)
graph_permutations = set()
for coordinate_perm in permutations(range(3)):
    for flips in product((0, 1), repeat=3):
        image_vertices = tuple(vertex_index[tuple(v[coordinate_perm[i]] ^ flips[i]
                                                  for i in range(3))]
                               for v in cube_vertices)
        image_edges = tuple(cube_edges.index(tuple(sorted((image_vertices[a],
                                                            image_vertices[b]))))
                            for a, b in cube_edges)
        assert image_vertices not in graph_permutations
        graph_permutations.add(image_vertices)
        det = inversion_parity(coordinate_perm) * (-1) ** sum(flips)
        # Multiplication by central inversion (x -> 1-x) removes the
        # orientation-reversing factor, giving a rotation in S4.
        if det == 1:
            rotation_vertices = image_vertices
        else:
            rotation_vertices = tuple(
                vertex_index[tuple(1 - x for x in cube_vertices[image_vertices[i]])]
                for i in range(8))
        image_axes = [axis_number[tuple(sorted((rotation_vertices[a],
                                                 rotation_vertices[b])))]
                      for a, b in axes]
        class_label = (cycle_type(image_axes), det)
        # Hopf trace: H_0 = Q, H_2 = Q^4, and no other homology.
        lefschetz = sum((-1)**d * chain_trace(image_edges, d)
                        for d in range(4))
        trace_h2 = lefschetz - 1
        class_values[class_label].append(trace_h2)
assert len(graph_permutations) == 48

# Every class is constant, and the S4 x C2 character table is explicit.
expected = {
    ((1, 1, 1, 1), +1): (1, 4),
    ((2, 1, 1), +1): (6, -2),
    ((2, 2), +1): (3, 0),
    ((3, 1), +1): (8, 1),
    ((4,), +1): (6, 0),
    ((1, 1, 1, 1), -1): (1, 2),
    ((2, 1, 1), -1): (6, 0),
    ((2, 2), -1): (3, -2),
    ((3, 1), -1): (8, -1),
    ((4,), -1): (6, 2),
}
assert set(class_values) == set(expected)
for label, (size, value) in expected.items():
    assert len(class_values[label]) == size
    assert set(class_values[label]) == {value}

# The two rational irreducible summands are sign(S4) tensored with
# the inversion sign and sign-standard(S4) tensored with inversion-trivial.
# Character values ordered by S4 cycle shape are as follows.
order = [(1,1,1,1), (2,1,1), (2,2), (3,1), (4,)]
sign_character = [1, -1, 1, 1, -1]
sign_standard_character = [3, -1, -1, 0, 1]
for j, shape in enumerate(order):
    plus = expected[(shape, 1)][1]
    minus = expected[(shape, -1)][1]
    assert plus == sign_standard_character[j] + sign_character[j]
    assert minus == sign_standard_character[j] - sign_character[j]

# Invariants and quotient rational homology (finite-group transfer).
assert sum(expected[(shape,+1)][0]*expected[(shape,+1)][1]
           for shape in order) == 0
assert sum(expected[(shape,det)][0]*expected[(shape,det)][1]
           for shape in order for det in (-1,+1)) == 0
assert (expected[((1,1,1,1),+1)][1] +
        expected[((1,1,1,1),-1)][1]) // 2 == 3

print('CUBE_MATCHING_SYMMETRY_VERIFIED')
print('face_vector', [len(faces[d]) for d in range(4)])
print('Morse_pairs', len(pairs), 'Hasse_covers', cover_count,
      'critical_cells', critical)
print('homotopy', 'wedge_of_four_2_spheres')
print('group_order', len(graph_permutations), 'group', 'S4_x_C2')
for shape in order:
    print('class', shape, 'size', expected[(shape,+1)][0],
          'trace_plus', expected[(shape,+1)][1],
          'trace_minus', expected[(shape,-1)][1])
print('decomposition', 'S4_sign_standard_x_C2_trivial + S4_sign_x_C2_sign')
print('rational_H2_full_quotient', 0, 'rotational_quotient', 0,
      'central_inversion_quotient', 3)
