#!/usr/bin/env python3
"""Exact, standard-library verification of the Desargues 2-independence complex."""
from itertools import combinations, permutations
from collections import Counter, deque
from math import factorial

SYMBOLS = tuple(range(5))
VERTICES = [frozenset(s) for k in (2, 3) for s in combinations(SYMBOLS, k)]
VINDEX = {s: i for i, s in enumerate(VERTICES)}
N = len(VERTICES)
ADJ = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        if VERTICES[i] < VERTICES[j] or VERTICES[j] < VERTICES[i]:
            ADJ[i] |= 1 << j
            ADJ[j] |= 1 << i
assert N == 20
assert sum(x.bit_count() for x in ADJ) == 60
assert all(x.bit_count() == 3 for x in ADJ)

# An admissible face induces components of order <=2, equivalently degree <=1.
faces = []
def generate(remaining, mask, degree):
    if mask:
        faces.append(mask)
    while remaining:
        bit = remaining & -remaining
        remaining -= bit
        i = bit.bit_length() - 1
        adjacent = [j for j in range(N) if (mask & (1 << j)) and (ADJ[i] & (1 << j))]
        if len(adjacent) >= 2 or any(degree[j] != 0 for j in adjacent):
            continue
        new_degree = degree.copy()
        new_degree[i] = len(adjacent)
        for j in adjacent:
            new_degree[j] += 1
        generate(remaining, mask | bit, new_degree)
generate((1 << N) - 1, 0, [0] * N)
face_set = set(faces)
assert len(face_set) == len(faces)
assert len(face_set) == 62048
f_vector = Counter(s.bit_count() - 1 for s in faces)
assert tuple(f_vector[i] for i in range(12)) == (
    20, 190, 1080, 3985, 9784, 15910,
    16600, 10390, 3460, 564, 60, 5)

# Independent full-subset dynamic enumeration, rather than the recursive generator.
valid = bytearray(1 << N)
valid[0] = 1
for mask in range(1, 1 << N):
    bit = mask & -mask
    i = bit.bit_length() - 1
    prev = mask ^ bit
    neighbors = ADJ[i] & prev
    if not valid[prev] or neighbors.bit_count() > 1:
        continue
    if neighbors:
        j = neighbors.bit_length() - 1
        if ADJ[j] & prev:
            continue
    valid[mask] = 1
assert sum(valid) == len(face_set) + 1
assert all(valid[s] for s in face_set)
print('VERTICES', N, 'EDGES', 30, 'NONEMPTY_FACES', len(faces))
print('F_VECTOR', [f_vector[i] for i in range(12)])
print('INDEPENDENT_ENUMERATION_PASS')

# Successive vertex element matchings on the augmented face poset.
remaining = face_set | {0}
lower_to_upper = {}
upper_to_lower = {}
for i in range(N):
    pairs = [s for s in remaining if not(s & (1 << i)) and (s | (1 << i)) in remaining]
    for s in pairs:
        t = s | (1 << i)
        assert s in remaining and t in remaining
        lower_to_upper[s] = t
        upper_to_lower[t] = s
        remaining.remove(s)
        remaining.remove(t)
assert len(lower_to_upper) == 31004
assert len(remaining) == 41
assert all(s.bit_count() == 8 for s in remaining)
assert len(lower_to_upper) * 2 + len(remaining) == len(face_set) + 1
print('MORSE_PAIRS', len(lower_to_upper), 'CRITICAL_DEGREE_7', len(remaining))

# Direct acyclicity check of the full reversed Hasse graph; no homology assumption.
all_faces = face_set | {0}
out = {s: [] for s in all_faces}
indegree = dict.fromkeys(all_faces, 0)
for s in all_faces:
    bits = s
    while bits:
        bit = bits & -bits
        bits -= bit
        t = s ^ bit
        if upper_to_lower.get(s) == t:
            source, target = t, s
        else:
            source, target = s, t
        out[source].append(target)
        indegree[target] += 1
queue = deque(s for s, d in indegree.items() if not d)
count = 0
while queue:
    s = queue.popleft()
    count += 1
    for t in out[s]:
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
assert count == len(all_faces) == 62049
print('HASSE_DIRECTED_ACYCLIC', count)
del out, indegree, queue

# The full automorphism group consists of all symbol permutations, optionally
# followed by complementing every 2-subset to a 3-subset and conversely.
def permmap(p, exchange):
    return tuple(VINDEX[
        (frozenset(SYMBOLS) - frozenset(p[i] for i in v)) if exchange
        else frozenset(p[i] for i in v)] for v in VERTICES)
all_actions = set()
for p in permutations(SYMBOLS):
    for exchange in (0, 1):
        pm = permmap(p, exchange)
        all_actions.add(pm)
        for i in range(N):
            for j in range(i + 1, N):
                assert bool(ADJ[i] & (1 << j)) == bool(ADJ[pm[i]] & (1 << pm[j]))
assert len(all_actions) == 240
print('GRAPH_AUTOMORPHISM_ACTIONS', len(all_actions))

# Signed Lefschetz: trace on reduced C_{-1} contributes -1.
def signed_lefschetz(pm):
    answer = -1
    image_bits = tuple(1 << i for i in pm)
    for simplex in faces:
        current = simplex
        images = []
        transformed = 0
        while current:
            bit = current & -current
            current -= bit
            i = bit.bit_length() - 1
            images.append(pm[i])
            transformed |= image_bits[i]
        if transformed != simplex:
            continue
        inversions = sum(images[i] > images[j]
                         for i in range(len(images))
                         for j in range(i + 1, len(images)))
        answer += (-1) ** (len(images) - 1 + inversions)
    return answer

def cycle_rep(partition):
    p = list(SYMBOLS)
    offset = 0
    for length in partition:
        for j in range(length):
            p[offset + j] = offset + (j + 1) % length
        offset += length
    return tuple(p)

def s5_irreducibles(p):
    fixed = sum(i == p[i] for i in SYMBOLS)
    transpositions = sum(i < p[i] and p[p[i]] == i for i in SYMBOLS)
    parity = (-1) ** sum(p[i] > p[j] for i in SYMBOLS for j in range(i + 1, N // 4))
    standard = fixed - 1
    two_subsets = fixed * (fixed - 1) // 2 + transpositions
    five = two_subsets - 1 - standard
    square = tuple(p[p[i]] for i in SYMBOLS)
    wedge2 = (standard ** 2 - (sum(i == square[i] for i in SYMBOLS) - 1)) // 2
    # (5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)
    return (1, standard, five, wedge2, parity * five,
            parity * standard, parity)

partitions = ((5,), (4,1), (3,2), (3,1,1),
              (2,2,1), (2,1,1,1), (1,1,1,1,1))
classes = []
for part in partitions:
    p = cycle_rep(part)
    size = factorial(5)
    for length, multiplicity in Counter(part).items():
        size //= length ** multiplicity * factorial(multiplicity)
    irreps = s5_irreducibles(p)
    for exchange in (0, 1):
        trace7 = -signed_lefschetz(permmap(p, exchange))
        classes.append((part, exchange, size, trace7, irreps))
assert len(classes) == 14
assert sum(size for _, _, size, _, _ in classes) == 240
assert classes[-2][3] == 41
print('CLASS_TABLE (S5_CYCLE_TYPE, EXCHANGE, CLASS_SIZE, H7_TRACE)')
for part, exchange, size, trace7, _ in classes:
    print(part, exchange, size, trace7)

# Prove the seven S5 character formulas are irreducible and orthogonal.
for j in range(7):
    for k in range(7):
        inner = sum(size * irreps[j] * irreps[k]
                    for part, exchange, size, tr, irreps in classes
                    if exchange == 0) // 120
        assert inner == int(j == k), (j, k, inner)

# Pair each S5 irreducible with the two C2 characters.
multiplicity = {}
for j in range(7):
    for eta in (0, 1):
        numerator = sum(size * tr * irreps[j] * ((-1) ** (eta * exchange))
                        for part, exchange, size, tr, irreps in classes)
        assert numerator % 240 == 0
        multiplicity[j, eta] = numerator // 240
        assert multiplicity[j, eta] >= 0
assert [multiplicity[j,eta] for j in range(7) for eta in (0,1)] == [
    1,0,1,0,1,1,1,1,1,1,0,1,0,0]
assert sum(multiplicity[j,eta] * s5_irreducibles(tuple(SYMBOLS))[j]
           for j in range(7) for eta in (0,1)) == 41
assert sum(multiplicity[j,0] * s5_irreducibles(tuple(SYMBOLS))[j]
           for j in range(7)) == 21
assert sum(multiplicity[j,1] * s5_irreducibles(tuple(SYMBOLS))[j]
           for j in range(7)) == 20
assert multiplicity[0,0] == 1
print('S5_SPECHT_WITH_EXCHANGE_MULTIPLICITIES', multiplicity)
print('CENTRAL_EVEN_ODD_DIMENSIONS', 21, 20)
print('FULL_GROUP_INVARIANTS', 1)
print('ALL_CHECKS_PASS')
