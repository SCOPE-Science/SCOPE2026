#!/usr/bin/env python3
"""Exact finite verification of the Fano-incidence dominance-complex theorem.

Only Python's standard library is needed.  Vertices 0..6 are points and
7..13 are lines; line j contains points j, j+1, j+3 modulo seven.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

NVERT = 14
LINES = [frozenset((j+d) % 7 for d in (0, 1, 3)) for j in range(7)]
CLOSED = [1 << u for u in range(NVERT)]
for j, line in enumerate(LINES):
    for i in line:
        CLOSED[i] |= 1 << (7+j)
        CLOSED[7+j] |= 1 << i

assert sum((CLOSED[i] >> j) & 1 for i in range(7) for j in range(7,14)) == 21
assert all(x.bit_count() == 4 for x in CLOSED)
assert all(len(LINES[i] & LINES[j]) == 1 for i in range(7) for j in range(i+1, 7))

# The complement of a face must dominate each vertex, equivalently no face
# is allowed to contain an entire closed neighborhood.
faces = {s for s in range(1 << NVERT)
         if all((s & neighborhood) != neighborhood for neighborhood in CLOSED)}
fvector = Counter(s.bit_count()-1 for s in faces if s)
expected = [14, 91, 364, 987, 1862, 2394, 1962, 931, 224, 21]
assert [fvector[d] for d in range(10)] == expected
assert len(faces) == 8851

# Seven-pass toggle matching.  The empty face is used only to construct
# the matching; the pair with the empty face is omitted in ordinary Morse
# theory, so one vertex remains critical alongside the seven-line face.
remaining = set(faces)
augmented_pairs = []
stage_counts = []
for pivot in range(7):
    b = 1 << pivot
    candidates = sorted(s for s in remaining if not (s & b) and (s | b) in remaining)
    count = 0
    for lower in candidates:
        upper = lower | b
        if lower in remaining and upper in remaining:
            remaining.remove(lower)
            remaining.remove(upper)
            augmented_pairs.append((lower, upper))
            count += 1
    stage_counts.append(count)
assert stage_counts == [3737, 471, 145, 35, 21, 9, 7]
assert remaining == {sum(1 << i for i in range(7, 14))}
assert (0, 1) in augmented_pairs
pairs = {(lo, hi) for lo, hi in augmented_pairs if lo}
paired_faces = {x for lo, hi in pairs for x in (lo, hi)}
critical = sorted(set(faces) - {0} - paired_faces)
assert critical == [1, 16256]
assert len(pairs) == 4424

# Orient each covering relation in the nonempty face poset from higher
# to lower, except reverse the matched ones.  A topological ordering
# of all nonempty faces proves there is no directed cycle.
indeg = {f: 0 for f in faces if f}
arrows = defaultdict(list)
num_edges = 0
for upper in indeg:
    for i in range(NVERT):
        if not ((upper >> i) & 1):
            continue
        lower = upper ^ (1 << i)
        if lower == 0:
            continue
        if (lower, upper) in pairs:
            arrows[lower].append(upper)
            indeg[upper] += 1
        else:
            arrows[upper].append(lower)
            indeg[lower] += 1
        num_edges += 1
queue = deque(u for u in indeg if indeg[u] == 0)
visited = 0
while queue:
    u = queue.popleft()
    visited += 1
    for v in arrows[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            queue.append(v)
assert visited == len(faces) - 1

# Independently verify the four generators and their actions on the unique
# rational degree-six homology class by the simplicial Lefschetz formula.
line_index = {line: j for j, line in enumerate(LINES)}
def lift(pp):
    return tuple(pp) + tuple(7 + line_index[frozenset(pp[i] for i in LINES[j])]
                              for j in range(7))

r7 = lift(tuple((i+1) % 7 for i in range(7)))
m3 = lift(tuple(2*i % 7 for i in range(7)))
t2 = lift((0, 1, 4, 3, 2, 6, 5))
polarity = tuple([7 + (-i) % 7 for i in range(7)] + [(-j) % 7 for j in range(7)])
generators = {'rotation': r7, 'multiplier': m3,
              'extra_involution': t2, 'duality': polarity}
for name, g in generators.items():
    assert sorted(g) == list(range(NVERT)), name
    assert all(bool(CLOSED[v] & (1 << u)) == bool(CLOSED[g[v]] & (1 << g[u]))
               for u in range(NVERT) for v in range(NVERT)), name

# Every colour-preserving graph automorphism corresponds to a permutation
# of the seven points preserving the line triples.
all_point_aut = {
    p for p in permutations(range(7))
    if all(frozenset(p[i] for i in line) in line_index for line in LINES)
}
assert len(all_point_aut) == 168
p_gens = [tuple(g[:7]) for g in (r7, m3, t2)]
def compose(x, y):
    return tuple(x[y[i]] for i in range(7))
seen = {tuple(range(7))}
stack = list(seen)
while stack:
    a = stack.pop()
    for b in p_gens:
        c = compose(a, b)
        if c not in seen:
            seen.add(c)
            stack.append(c)
assert seen == all_point_aut
# The duality swaps bipartition classes, so these generate all 336 graph
# automorphisms (connected bipartite graphs have unique bipartitions).

def orbit_euler(g):
    unseen = set(range(NVERT))
    orbit_masks = []
    while unseen:
        x = min(unseen)
        cycle = []
        while x not in cycle:
            cycle.append(x)
            unseen.remove(x)
            x = g[x]
        orbit_masks.append(sum(1 << j for j in cycle))
    counts = Counter()
    for choices in range(1, 1 << len(orbit_masks)):
        face = 0
        for i, mask in enumerate(orbit_masks):
            if choices & (1 << i):
                face |= mask
        if face in faces:
            counts[choices.bit_count()] += 1
    # For an invariant simplex consisting of k permutation orbits,
    # (-1)^dimension times the orientation sign equals (-1)^(k-1).
    lefschetz = sum((-1)**(k-1) * count for k, count in counts.items())
    return len(orbit_masks), [counts[k] for k in range(1, len(orbit_masks)+1)], lefschetz

expected_l = {'rotation': (2, [2, 0], 2),
              'multiplier': (6, [6, 13, 10, 1, 0, 0], 2),
              'extra_involution': (10, [10, 45, 116, 176, 142, 51, 6, 0, 0, 0], 2),
              'duality': (7, [7, 21, 32, 19, 3, 0, 0], 2)}
for name, g in generators.items():
    assert orbit_euler(g) == expected_l[name], (name, orbit_euler(g))

print('graph: Fano incidence/Heawood; vertices=14; edges=21; aut_order=336')
print('face_count_with_empty:', len(faces), 'f_vector:', [fvector[d] for d in range(10)])
print('match_counts_by_pivot:', stage_counts)
print('matched_nonempty_pairs:', len(pairs), 'critical_faces:', critical)
print('oriented_Hasse_edges:', num_edges, 'acyclic_visits:', visited)
for name, g in generators.items():
    n_orbits, counts, L = orbit_euler(g)
    print('generator:', name, 'orbits:', n_orbits, 'invariant_orbit_face_counts:',
          counts, 'ordinary_Lefschetz:', L, 'H6_trace:', L-1)
print('PASS: homotopy S^6 and full automorphism group fixes rational H6')
