#!/usr/bin/env python3
"""Exact finite certificate for the two-independence complex of KG(6,2)."""
from collections import Counter, deque
from itertools import combinations, permutations

SYMBOLS = tuple(range(6))
VERTICES = tuple(combinations(SYMBOLS, 2))
N = len(VERTICES)
INDEX = {v: i for i, v in enumerate(VERTICES)}
NEIGHBORS = tuple(sum(1 << j for j, b in enumerate(VERTICES) if set(a).isdisjoint(b))
                  for a in VERTICES)


def allowed_by_degrees(mask):
    return all((mask & NEIGHBORS[i]).bit_count() <= 1
               for i in range(N) if mask & (1 << i))


# An independent test: every triple must span at most one graph edge.
FORBIDDEN_TRIPLES = tuple(sum(1 << i for i in triple)
                          for triple in combinations(range(N), 3)
                          if sum(bool(NEIGHBORS[i] & (1 << j))
                                 for i, j in combinations(triple, 2)) >= 2)


def allowed_by_triples(mask):
    return all(mask & t != t for t in FORBIDDEN_TRIPLES)


FACES = tuple(mask for mask in range(1 << N) if allowed_by_degrees(mask))
FACE_SET = set(FACES)
assert len(FACES) == 747
assert all(allowed_by_degrees(m) == allowed_by_triples(m)
           for m in range(1 << N))
COUNTS = Counter(m.bit_count() - 1 for m in FACES)
assert COUNTS == {-1: 1, 0: 15, 1: 105, 2: 260, 3: 255, 4: 96, 5: 15}

# Lexicographic toggle matching on the augmented face poset.
UNMATCHED = set(FACES)
PAIRS = []
for vertex in range(N):
    bit = 1 << vertex
    for lower in FACES:
        if lower in UNMATCHED and not lower & bit and lower | bit in UNMATCHED:
            UNMATCHED.remove(lower)
            UNMATCHED.remove(lower | bit)
            PAIRS.append((lower, lower | bit))
assert len(PAIRS) == 371
assert len(UNMATCHED) == 5
assert all(m.bit_count() == 4 for m in UNMATCHED)
EMPTY_PAIR = next(pair for pair in PAIRS if pair[0] == 0)
# Omit the empty face and its matching pair: exactly one critical vertex.
NONEMPTY_MATCHING = tuple(pair for pair in PAIRS if pair != EMPTY_PAIR)
CRITICAL = (set(FACES) - {0}) - {f for pair in NONEMPTY_MATCHING for f in pair}
assert len(NONEMPTY_MATCHING) == 370
assert Counter(s.bit_count() - 1 for s in CRITICAL) == {0: 1, 3: 5}

# Verify that each selected pair is a cover and that oriented Hasse is acyclic.
match_edges = set(NONEMPTY_MATCHING)
indegree = {f: 0 for f in FACES if f != 0}
successors = {f: [] for f in FACES if f != 0}
cover_count = 0
for upper in FACES:
    if not upper:
        continue
    for i in range(N):
        if not upper & (1 << i):
            continue
        lower = upper ^ (1 << i)
        if lower == 0:
            continue
        cover_count += 1
        if (lower, upper) in match_edges:
            src, dst = lower, upper
        else:
            src, dst = upper, lower
        successors[src].append(dst)
        indegree[dst] += 1
assert cover_count == 2580, cover_count
queue = deque(f for f, degree in indegree.items() if degree == 0)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for other in successors[f]:
        indegree[other] -= 1
        if indegree[other] == 0:
            queue.append(other)
assert visited == len(FACES) - 1, (visited, len(FACES)-1)

# Separate mod-two chain ranks, not used to deduce the integral homotopy type.
def rank_binary(columns):
    pivots = {}
    for column in columns:
        v = column
        while v:
            lead = v.bit_length() - 1
            if lead not in pivots:
                pivots[lead] = v
                break
            v ^= pivots[lead]
    return len(pivots)

levels = [[m for m in FACES if m.bit_count() == k] for k in range(1, 7)]
ranks = [0]
for dimension in range(1, 6):
    idx = {s: i for i, s in enumerate(levels[dimension-1])}
    cols = []
    for upper in levels[dimension]:
        column = 0
        for j in range(N):
            if upper & (1 << j):
                column ^= 1 << idx[upper ^ (1 << j)]
        cols.append(column)
    ranks.append(rank_binary(cols))
ranks.append(0)
betti = [len(levels[d]) - ranks[d] - ranks[d+1] for d in range(6)]
assert betti == [1, 0, 0, 5, 0, 0], (ranks, betti)


def parity(values):
    return -1 if sum(values[i] > values[j]
                     for i in range(len(values)) for j in range(i+1, len(values))) % 2 else 1


def cycle_type(perm):
    unseen = set(range(6))
    lengths = []
    while unseen:
        x = min(unseen)
        k = 0
        while x in unseen:
            unseen.remove(x)
            x = perm[x]
            k += 1
        lengths.append(k)
    return tuple(sorted(lengths, reverse=True))


# Compute each rational homology trace from its signed simplicial Lefschetz number.
CHARACTER = {}
TYPE_SIZES = Counter()
for symbol_perm in permutations(SYMBOLS):
    induced = [INDEX[tuple(sorted((symbol_perm[a], symbol_perm[b])))]
               for a, b in VERTICES]
    assert all(sum(1 << induced[i] for i in range(N) if f & (1 << i))
               in FACE_SET for f in FACES)
    lefschetz = 0
    for face in FACES[1:]:
        inds = [i for i in range(N) if face & (1 << i)]
        images = [induced[i] for i in inds]
        if set(images) != set(inds):
            continue
        lefschetz += (-1 if len(inds) % 2 == 0 else 1) * parity(images)
    homology_trace = 1 - lefschetz
    expected = parity(symbol_perm) * (sum(symbol_perm[i] == i for i in range(6)) - 1)
    assert homology_trace == expected, (symbol_perm, homology_trace, expected)
    typ = cycle_type(symbol_perm)
    if typ in CHARACTER:
        assert CHARACTER[typ] == homology_trace
    else:
        CHARACTER[typ] = homology_trace
    TYPE_SIZES[typ] += 1
assert len(CHARACTER) == 11 and sum(TYPE_SIZES.values()) == 720
assert sum(TYPE_SIZES[t] * CHARACTER[t] for t in CHARACTER) == 0
assert sum(TYPE_SIZES[t] * CHARACTER[t]**2 for t in CHARACTER) == 720

print('vertices=15 ambient_subsets=32768 forbidden_triples=', len(FORBIDDEN_TRIPLES))
print('face_counts', sorted(COUNTS.items()))
print('augmented_matching_pairs=', len(PAIRS), 'nonempty_matching_pairs=', len(NONEMPTY_MATCHING))
print('critical_vertex=', [tuple(VERTICES[i] for i in range(N) if s & (1 << i))
                           for s in CRITICAL if s.bit_count() == 1])
print('critical_three_cells=', sorted(tuple(VERTICES[i] for i in range(N) if s & (1 << i))
                                      for s in CRITICAL if s.bit_count() == 4))
print('Hasse_cover_count=', cover_count, 'directed_acyclic_vertices=', visited)
print('mod2_boundary_ranks=', ranks, 'mod2_betti=', betti)
print('cycle_type,number_of_permutations,H3_character')
for typ in sorted(CHARACTER, reverse=True):
    print(typ, TYPE_SIZES[typ], CHARACTER[typ])
print('ALL_CHECKS_PASS')
