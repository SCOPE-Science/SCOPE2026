#!/usr/bin/env python3
"""Exact chain-level and combinatorial verification for a Petersen 2-matching homology character."""
from collections import Counter, deque
from itertools import combinations, permutations

FIVE = tuple(range(5))
VERTICES = list(combinations(FIVE, 2))
VERTEX_INDEX = {x: i for i, x in enumerate(VERTICES)}
EDGES = [(a, b) for a in range(10) for b in range(a+1, 10)
         if set(VERTICES[a]).isdisjoint(VERTICES[b])]
assert len(EDGES) == 15 and len(set(EDGES)) == 15
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
FULL = 1 << 15


def valid(mask):
    degree = [0] * 10
    for i, (a, b) in enumerate(EDGES):
        if mask & (1 << i):
            degree[a] += 1
            degree[b] += 1
            if degree[a] > 2 or degree[b] > 2:
                return False
    return True


FACES = [m for m in range(FULL) if valid(m)]
FACE_INDEX = {m: i for i, m in enumerate(FACES)}
assert len(FACES) == 10870
actual_f = [sum(m.bit_count() == k for m in FACES) for k in range(11)]
expected_f = [1, 15, 105, 445, 1245, 2358, 2985, 2400, 1095, 215, 6]
assert actual_f == expected_f
print('FACES_OK', actual_f)

# Standard sequential element-matching on the augmented face poset;
# each toggle pairs a face with an immediately covering face.
unused = set(FACES)
pairs = []
for v in range(15):
    bit = 1 << v
    for face in FACES:
        if face in unused and not face & bit:
            extension = face | bit
            if extension in unused:
                unused.remove(face)
                unused.remove(extension)
                pairs.append((face, extension))
assert len(pairs) == 5433
assert len(unused) == 4
assert all(m.bit_count() == 8 for m in unused)
assert sorted(unused) == [3510, 30342, 31536, 32160]
empty_pairs = [(a, b) for a, b in pairs if a == 0]
assert len(empty_pairs) == 1
# Delete the augmented empty face and promote its partner to a critical
# vertex; this leaves an ordinary discrete Morse matching on nonempty faces.
ordinary_pairs = [(a, b) for a, b in pairs if a != 0]
critical = unused | {empty_pairs[0][1]}
assert len(ordinary_pairs) == 5432
assert Counter(m.bit_count()-1 for m in critical) == {0: 1, 7: 4}
print('MORSE_OK pairs=5432 critical=(one_0,four_7) critical_seven_masks=', sorted(unused))

# Independently check the entire directed ordinary Hasse graph.
paired = set(ordinary_pairs)
nonempty = [m for m in FACES if m]
indices = {m: i for i, m in enumerate(nonempty)}
indegree = [0] * len(nonempty)
outgoing = [[] for _ in nonempty]
incidences = 0
for higher in nonempty:
    for v in range(15):
        bit = 1 << v
        if not higher & bit:
            continue
        lower = higher ^ bit
        if lower == 0:
            continue
        assert lower in indices
        if (lower, higher) in paired:
            start, end = lower, higher
        else:
            start, end = higher, lower
        i, j = indices[start], indices[end]
        outgoing[i].append(j)
        indegree[j] += 1
        incidences += 1
queue = deque(i for i, d in enumerate(indegree) if d == 0)
visited = 0
while queue:
    i = queue.popleft()
    visited += 1
    for j in outgoing[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)
assert visited == len(nonempty) and incidences == 63780
print('ACYCLIC_OK nodes=', visited, 'incidences=', incidences)


def cycle_type(p):
    used = set()
    lengths = []
    for x in FIVE:
        if x in used:
            continue
        y = x
        length = 0
        while y not in used:
            used.add(y)
            length += 1
            y = p[y]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def edge_action(p):
    image_vertices = [VERTEX_INDEX[tuple(sorted(p[x] for x in v))] for v in VERTICES]
    return tuple(EDGE_INDEX[tuple(sorted((image_vertices[a], image_vertices[b])))]
                 for a, b in EDGES)


def orbit_masks(action):
    unseen = set(range(15))
    masks = []
    while unseen:
        j = min(unseen)
        mask = 0
        while j in unseen:
            unseen.remove(j)
            mask |= 1 << j
            j = action[j]
        masks.append(mask)
    return masks


def orbit_trace(action):
    orbits = orbit_masks(action)
    trace = 0
    count = 0
    for subset in range(1 << len(orbits)):
        mask = 0
        for j, orbit in enumerate(orbits):
            if subset & (1 << j):
                mask |= orbit
        if valid(mask):
            trace += -1 if subset.bit_count() & 1 else 1
            count += 1
    return trace, count, len(orbits)


def restricted_sign(members, action):
    image = [action[i] for i in members]
    inversions = sum(image[i] > image[j]
                     for i in range(len(image))
                     for j in range(i+1, len(image)))
    return -1 if inversions % 2 else 1


def direct_signed_trace(action):
    # Since reduced homology is concentrated in degree seven, its trace is
    # minus the reduced alternating chain trace. The augmented empty face
    # is included below, giving contribution +1 in this expression.
    ans = 0
    for mask in FACES:
        members = [i for i in range(15) if mask & (1 << i)]
        if any(not mask & (1 << action[i]) for i in members):
            continue
        sign = restricted_sign(members, action)
        ans += (-1 if len(members) % 2 else 1) * sign
    return ans

EXPECTED = {(1,1,1,1,1):4, (2,1,1,1):2, (2,2,1):0,
            (3,1,1):1, (3,2):-1, (4,1):0, (5,):-1}
COUNTS = Counter()
ORBIT_DETAILS = {}
for perm in permutations(FIVE):
    typ = cycle_type(perm)
    action = edge_action(perm)
    assert sorted(action) == list(range(15))
    count = orbit_trace(action)
    signed = direct_signed_trace(action)
    expected = sum(perm[i] == i for i in FIVE) - 1
    assert count[0] == signed == expected == EXPECTED[typ], (perm, count, signed, expected)
    COUNTS[typ] += 1
    if typ not in ORBIT_DETAILS:
        ORBIT_DETAILS[typ] = count
assert sum(COUNTS.values()) == 120
assert COUNTS == {(1,1,1,1,1):1, (2,1,1,1):10, (2,2,1):15,
                  (3,1,1):20, (3,2):20, (4,1):30, (5,):24}
for typ in sorted(EXPECTED, reverse=True):
    print('CHARACTER_OK', typ, 'class_size=', COUNTS[typ],
          'trace=', EXPECTED[typ], 'admissible_orbit_subsets=', ORBIT_DETAILS[typ][1])
print('ALL_VERIFY_OK')
