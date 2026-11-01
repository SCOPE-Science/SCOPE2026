#!/usr/bin/env python3
"""Exact finite verification of the Clebsch independence-complex G-character.
Uses only Python's standard library and exhaustive bounded loops.
"""
from itertools import combinations, permutations
from collections import Counter, deque

N = 16
D = (1, 2, 4, 8, 15)
ADJ = [frozenset(v ^ d for d in D) for v in range(N)]

# Face enumeration uses independent-subset masks and explicit pairwise tests.
FACES = []
for size in range(1, N + 1):
    for vertices in combinations(range(N), size):
        if all(b not in ADJ[a] for a, b in combinations(vertices, 2)):
            FACES.append(sum(1 << v for v in vertices))
FACES.sort()
FACE_SET = set(FACES)
assert len(FACE_SET) == 392
assert [sum(f.bit_count() == k for f in FACES) for k in range(1, 6)] == [16, 80, 160, 120, 16]
assert all(len(neighbors) == 5 for neighbors in ADJ)
assert all(len(ADJ[a] & ADJ[b]) == (0 if b in ADJ[a] else 2)
           for a in range(N) for b in range(a + 1, N))

# A complete independently reconstructed Morse certificate: 191 pairs,
# one critical 0-cell, nine critical 3-cells and a globally acyclic Hasse graph.
ORDER = (3, 14, 7, 9, 13, 11, 4, 5, 12, 8, 1, 0, 15, 6, 2, 10)
unmatched = FACE_SET.copy()
paired = set()
for v in ORDER:
    bit = 1 << v
    for face in FACES:
        if face in unmatched and not face & bit and (face | bit) in unmatched:
            big = face | bit
            unmatched.remove(face)
            unmatched.remove(big)
            paired.add((face, big))
assert len(paired) == 191
assert Counter(s.bit_count() - 1 for s in unmatched) == {0: 1, 3: 9}
incidences = 0
indegree = {face: 0 for face in FACES}
arrows = {face: [] for face in FACES}
for large in FACES:
    for vertex in range(N):
        if not (large & (1 << vertex)):
            continue
        small = large ^ (1 << vertex)
        if small == 0:
            continue
        incidences += 1
        low, high = ((small, large) if (small, large) in paired
                     else (large, small))
        arrows[low].append(high)
        indegree[high] += 1
assert incidences == 1200
queue = deque(face for face in FACES if indegree[face] == 0)
visited = 0
while queue:
    current = queue.popleft()
    visited += 1
    for next_face in arrows[current]:
        indegree[next_face] -= 1
        if indegree[next_face] == 0:
            queue.append(next_face)
assert visited == len(FACES)
print('MORSE_OK faces=392 cover_relations=1200 pairs=191 critical=(one_0,nine_3)')


def lin_columns(p):
    return tuple(D[p[i]] for i in range(4))

def apply_lin(x, cols):
    result = 0
    for k in range(4):
        if x & (1 << k):
            result ^= cols[k]
    return result

def perm_sign(items):
    return -1 if (sum(items[i] > items[j] for i in range(len(items))
                       for j in range(i + 1, len(items))) % 2) else 1

def signed_simplex_character(mapping):
    """Reduced Lefschetz = -H3-character. Includes empty face with +1."""
    total = 1
    for face in FACES:
        vertices = [v for v in range(N) if face & (1 << v)]
        transformed = [mapping[v] for v in vertices]
        if sorted(transformed) == vertices:
            total += (-1 if len(vertices) & 1 else 1) * perm_sign(transformed)
    return total

def orbit_character(mapping):
    """A separate sign-free computation from allowable vertex orbits."""
    seen = set()
    orbits = []
    for v in range(N):
        if v in seen:
            continue
        orbit = []
        w = v
        while w not in seen:
            seen.add(w)
            orbit.append(w)
            w = mapping[w]
        assert w == v
        # The orbit may be chosen as a block only if its vertices are independent.
        if all(b not in ADJ[a] for a, b in combinations(orbit, 2)):
            orbits.append(orbit)
    orb_masks = [sum(1 << v for v in orbit) for orbit in orbits]
    nbr_masks = [sum(1 << n for n in set().union(*(ADJ[v] for v in orbit))) for orbit in orbits]
    def count(start, occupied, parity):
        ans = parity
        for i in range(start, len(orbits)):
            if occupied & orb_masks[i]:
                continue
            ans += count(i + 1, occupied | orb_masks[i] | nbr_masks[i], -parity)
        return ans
    return count(0, 0, 1)

def prediction(t, p):
    par = perm_sign(p)
    fixed = [i for i in range(5) if p[i] == i]
    a = (14, 13, 11, 7, 15)
    return par * (len(fixed) - 1 + sum(
        (-1) ** ((a[i] & t).bit_count() % 2) for i in fixed))

all_chars = Counter()
pure_trans = {}
full_checked = 0
for p in permutations(range(5)):
    cols = lin_columns(p)
    images = [apply_lin(x, cols) for x in range(N)]
    assert len(set(images)) == 16
    assert {apply_lin(d, cols) for d in D} == set(D)
    for t in range(N):
        mapping = tuple(images[x] ^ t for x in range(N))
        got = signed_simplex_character(mapping)
        independently_got = orbit_character(mapping)
        want = prediction(t, p)
        assert got == independently_got == want, (p, t, got, independently_got, want)
        all_chars[got] += 1
        if p == (0, 1, 2, 3, 4):
            pure_trans[t] = got
        full_checked += 1
assert full_checked == 1920
assert pure_trans[0] == 9
assert Counter(pure_trans.values()) == {9: 1, 5: 10, 1: 5}
# Orthogonality projector onto translations invariants: (9 + 5*1 + 10*5)/16=4.
assert sum(pure_trans.values()) == 64
# The five remaining 1D translation weights can be independently recovered.
weights = {}
for a in range(16):
    total = sum(((-1) ** ((a & t).bit_count() % 2)) * pure_trans[t]
                for t in range(16))
    assert total % 16 == 0
    weights[a] = total // 16
assert weights == {a: (4 if a == 0 else (1 if a in (7, 11, 13, 14, 15) else 0)) for a in range(16)}
print('CHARACTER_OK affine_automorphisms=1920 signed_face_trace=orbit_trace=module_formula')
print('TRANSLATION_OK traces={9:1,5:10,1:5} Fourier={trivial:4,five_weights:1_each}')
print('TRACE_DISTRIBUTION', sorted(all_chars.items()))
print('VERIFY_OK')
