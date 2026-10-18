#!/usr/bin/env python3
"""Finite integer-chain and rational-character verification for Ind(H(5,2)).

Run: python3 verification/verify_desargues_character.py
Standard library only. All vertex and simplex data are rebuilt here.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations
import sys

sys.setrecursionlimit(20000)
V = list(combinations(range(5), 2)) + list(combinations(range(5), 3))
assert len(V) == 20
index = {a: i for i, a in enumerate(V)}
neighbor_masks = [0] * 20
edges = []
for i in range(10):
    for j in range(10, 20):
        if set(V[i]) < set(V[j]):
            neighbor_masks[i] |= 1 << j
            neighbor_masks[j] |= 1 << i
            edges.append((i, j))
assert len(edges) == 30

# Exhaustive DFS: every independent vertex set is built in increasing order.
faces = [[] for _ in range(21)]
def enumerate_faces(remaining, face, size):
    faces[size].append(face)
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        i = bit.bit_length() - 1
        enumerate_faces(remaining & ~neighbor_masks[i], face | bit, size + 1)
enumerate_faces((1 << 20) - 1, 0, 0)
while not faces[-1]:
    faces.pop()
assert [len(a) for a in faces] == [1, 20, 160, 660, 1510, 1924,
                                     1320, 480, 115, 20, 2]
all_faces = {m for level in faces for m in level}
positive_faces = all_faces - {0}
assert len(all_faces) == 6212

def signed_boundary(simplex):
    """(codimension-one face, oriented coefficient), sorted vertices."""
    out = []
    bits = simplex
    position = 0
    while bits:
        b = bits & -bits
        bits ^= b
        out.append((simplex ^ b, -1 if position & 1 else 1))
        position += 1
    return out

# A prescribed algebraic discrete-Morse matching, with no arbitrary choices.
unmatched = set(positive_faces)
lower_to_upper = {}
for vertex in range(20):
    bit = 1 << vertex
    for face in sorted(unmatched, key=lambda m: (m.bit_count(), m)):
        if face not in unmatched or (face & bit) or (neighbor_masks[vertex] & face):
            continue
        upper = face | bit
        if upper in unmatched:
            lower_to_upper[face] = upper
            unmatched.remove(face)
            unmatched.remove(upper)
critical = unmatched
assert len(lower_to_upper) == 3102
assert len(critical) == 7
assert [sum(1 for lo in lower_to_upper if lo.bit_count() == k) for k in range(1,10)] == [19, 141, 519, 991, 932, 383, 97, 18, 2]
assert Counter(m.bit_count() - 1 for m in critical) == {0: 1, 4: 1, 5: 5}
upper_to_lower = {up: lo for lo, up in lower_to_upper.items()}

# Check the matching is acyclic on the full nonempty face Hasse diagram.
degree = {m: 0 for m in positive_faces}
outgoing = defaultdict(list)
arrows = 0
for upper in positive_faces:
    for lower, coefficient in signed_boundary(upper):
        if not lower:
            continue
        if lower_to_upper.get(lower) == upper:
            outgoing[lower].append(upper)
            degree[upper] += 1
        else:
            outgoing[upper].append(lower)
            degree[lower] += 1
        arrows += 1
assert arrows == 30360
queue = deque(m for m in degree if degree[m] == 0)
seen = 0
while queue:
    m = queue.popleft()
    seen += 1
    for to in outgoing[m]:
        degree[to] -= 1
        if degree[to] == 0:
            queue.append(to)
assert seen == len(positive_faces)

# Signed *integer* Morse differentials, not ranks over a finite field.
@lru_cache(None)
def reduced_face(face):
    if face in critical:
        return {face: 1}
    if face in upper_to_lower:
        return {}  # upper cell was eliminated using a lower-dimensional pivot
    assert face in lower_to_upper
    upper = lower_to_upper[face]
    boundary = signed_boundary(upper)
    pivot = next(coeff for f, coeff in boundary if f == face)
    assert abs(pivot) == 1
    result = defaultdict(int)
    for other, coeff in boundary:
        if other == face:
            continue
        for critical_face, value in reduced_face(other).items():
            result[critical_face] -= coeff * pivot * value
    return {f: coeff for f, coeff in result.items() if coeff}

crit_5 = sorted(m for m in critical if m.bit_count() == 6)
crit_4 = sorted(m for m in critical if m.bit_count() == 5)
assert len(crit_4) == 1 and len(crit_5) == 5
for simplex in crit_5:
    image = defaultdict(int)
    for face, coeff in signed_boundary(simplex):
        for target, value in reduced_face(face).items():
            image[target] += coeff * value
    assert all(v == 0 for v in image.values()), (simplex, dict(image))
# By integral acyclic matching, reduced homology is Z in degree 4,
# Z^5 in degree 5, and zero otherwise.

def permutation_sign(a):
    parity = 1
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                parity = -parity
    return parity

def perm_cycle_type(a):
    used = set()
    lengths = []
    for i in range(5):
        if i in used:
            continue
        j = i
        n = 0
        while j not in used:
            used.add(j)
            n += 1
            j = a[j]
        lengths.append(n)
    return tuple(sorted(lengths, reverse=True))

def vertex_permutation(p, swap):
    image = []
    for v in V:
        t = tuple(sorted(p[i] for i in v))
        if swap:
            t = tuple(i for i in range(5) if i not in t)
        image.append(index[t])
    return tuple(image)


def orbit_independence_trace(image):
    """Independently compute the trace via a vertex-orbit conflict graph."""
    used = set()
    orbits = []
    for start in range(20):
        if start in used:
            continue
        orbit = []
        v = start
        while v not in used:
            used.add(v)
            orbit.append(v)
            v = image[v]
        assert v == start
        orbits.append(set(orbit))
    # An orbit with an internal edge can never appear in an invariant face.
    good = [o for o in orbits if not any(i in o and j in o for i,j in edges)]
    clashes = [0] * len(good)
    for i, a in enumerate(good):
        for j in range(i+1, len(good)):
            b = good[j]
            if any((u in a and v in b) or (v in a and u in b) for u,v in edges):
                clashes[i] |= 1 << j
                clashes[j] |= 1 << i
    @lru_cache(None)
    def signed_independence_sum(mask):
        if not mask:
            return 1
        b = mask & -mask
        i = b.bit_length() - 1
        remainder = mask ^ b
        return (signed_independence_sum(remainder)
                - signed_independence_sum(remainder & ~clashes[i]))
    # Each chosen orbit contributes (-1) under signed Lefschetz; the empty
    # simplex contributes -1, so the reduced trace is -I_G(-1).
    return -signed_independence_sum((1 << len(good)) - 1)


def oriented_fixed_face_sum(image):
    # Reduced Lefschetz trace, including the empty simplex in degree -1.
    answer = -1
    for size in range(1, len(faces)):
        for face in faces[size]:
            indices = [i for i in range(20) if face & (1 << i)]
            images = [image[i] for i in indices]
            if set(indices) == set(images):
                answer += ((-1) ** (size - 1)) * permutation_sign(images)
    return answer

class_trace = {}
class_count = Counter()
all_images = set()
for p in permutations(range(5)):
    for swap in (0, 1):
        image = vertex_permutation(p, swap)
        assert image not in all_images
        all_images.add(image)
        # Independently verify every automorphism preserves all edges.
        assert all((image[i], image[j]) in edges or
                   (image[j], image[i]) in edges for i, j in edges)
        cycle_type = perm_cycle_type(p)
        key = (cycle_type, swap)
        trace = oriented_fixed_face_sum(image)
        assert trace == orbit_independence_trace(image)
        expected = ((-1) ** swap) * (permutation_sign(p) -
                                     sum(p[i] == i for i in range(5)))
        assert trace == expected, (key, trace, expected)
        if key in class_trace:
            assert class_trace[key] == trace
        class_trace[key] = trace
        class_count[key] += 1
assert len(all_images) == 240 and len(class_trace) == 14

# The paper's character determination is an exact deduction: the 1-dimensional
# integral H_4 action can be only sgn^a tensor epsilon^b. The order-two
# involution arguments in RESULT.md force a=b=1, so the H_5 character is
# the epsilon twist of the natural five-point permutation character.
expected_unflipped = {
    (1, 1, 1, 1, 1): -4, (2, 1, 1, 1): -4,
    (2, 2, 1): 0, (3, 1, 1): -1,
    (3, 2): -1, (4, 1): -2, (5,): 1,
}
for ct, v in expected_unflipped.items():
    assert class_trace[ct, 0] == v
    assert class_trace[ct, 1] == -v
    assert class_count[ct, 0] == class_count[ct, 1]
assert sum(class_count.values()) == 240
print('DESARGUES_EQUIVARIANT_HOMOLOGY_OK')
print('faces=6212 pairs=3102 critical=(1 in 0, 1 in 4, 5 in 5)')
print('Morse_boundary_5=(0,0,0,0,0); acyclic_cover_arrows=30360')
print('cycle-type | class-size (each swap value) | L(no swap), L(swap)')
for ct in expected_unflipped:
    print(ct, class_count[ct, 0], class_trace[ct, 0], class_trace[ct, 1])
