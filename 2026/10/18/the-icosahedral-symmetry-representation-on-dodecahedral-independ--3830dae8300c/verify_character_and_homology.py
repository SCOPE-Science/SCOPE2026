#!/usr/bin/env python3
"""Exact combinatorial verification for the dodecahedral independence complex.

Requires Python >= 3.9; standard library only. The graph vertex labels are
0,...,9 (outer ring) and 10,...,19 (inner pentagram rings).
"""
from collections import Counter

N = 20
EDGES = set()
for j in range(10):
    for a, b in ((j, (j + 1) % 10), (j, j + 10),
                 (j + 10, 10 + (j + 2) % 10)):
        EDGES.add(tuple(sorted((a, b))))
assert len(EDGES) == 30
NEIGHBORS = [0] * N
for a, b in EDGES:
    NEIGHBORS[a] |= 1 << b
    NEIGHBORS[b] |= 1 << a

# Recursive enumeration: choose/exclude successive labels; each independent set once.
FACES = []
def enumerate_independent(free, chosen):
    if not free:
        FACES.append(chosen)
        return
    bit = free & -free
    i = bit.bit_length() - 1
    enumerate_independent(free ^ bit, chosen)
    enumerate_independent((free ^ bit) & ~NEIGHBORS[i], chosen | bit)
enumerate_independent((1 << N) - 1, 0)
FACE_SET = set(FACES)
assert len(FACE_SET) == len(FACES) == 5828
BY_DEGREE = [[] for _ in range(8)]
for face in FACES:
    if face:
        BY_DEGREE[face.bit_count() - 1].append(face)
assert tuple(map(len, BY_DEGREE)) == (20, 160, 660, 1510, 1912, 1240, 320, 5)

# Exhaustive binary boundary-matrix elimination: bit vectors are rows indexed by faces.
RANKS = []
for k in range(1, 8):
    lower = {mask: idx for idx, mask in enumerate(BY_DEGREE[k-1])}
    pivots = {}
    for mask in BY_DEGREE[k]:
        c = 0
        y = mask
        while y:
            bit = y & -y
            c ^= 1 << lower[mask ^ bit]
            y ^= bit
        while c:
            pivot = c.bit_length() - 1
            if pivot in pivots:
                c ^= pivots[pivot]
            else:
                pivots[pivot] = c
                break
    RANKS.append(len(pivots))
assert RANKS == [19, 141, 519, 991, 921, 315, 5]
full_ranks = [1] + RANKS + [0]
BETTI = [len(group) - full_ranks[k] - full_ranks[k+1]
         for k, group in enumerate(BY_DEGREE)]
assert BETTI == [0, 0, 0, 0, 0, 4, 0, 0]
assert sum((-1)**k * len(F) for k, F in enumerate(BY_DEGREE)) - 1 == -4

IDENTITY = tuple(range(N))
ROTATION = tuple((i+1)%10 if i < 10 else 10 + (i-9)%10 for i in range(N))
REFLECTION = tuple((-i)%10 if i < 10 else 10 + (-(i-10))%10 for i in range(N))
THIRD = (0,9,19,17,15,5,4,14,12,10,1,8,11,7,13,6,3,16,2,18)
GENERATORS = (ROTATION, REFLECTION, THIRD)

def compose(a,b):
    return tuple(a[b[i]] for i in range(N))

for g in GENERATORS:
    assert set(g) == set(range(N))
    assert {tuple(sorted((g[a], g[b]))) for a, b in EDGES} == EDGES

GROUP = {IDENTITY}
queue = [IDENTITY]
while queue:
    g = queue.pop()
    for h in GENERATORS:
        gh = compose(g, h)
        if gh not in GROUP:
            GROUP.add(gh)
            queue.append(gh)
assert len(GROUP) == 120

def cycle_decomposition(g):
    seen = set()
    cycles = []
    for i in range(N):
        if i in seen:
            continue
        c = []
        j = i
        while j not in seen:
            seen.add(j)
            c.append(j)
            j = g[j]
        cycles.append(c)
    return cycles

def order(g):
    z = IDENTITY
    for k in range(1, 121):
        z = compose(g, z)
        if z == IDENTITY:
            return k
    raise AssertionError('not of finite order <=120')

# Each invariant face is a union of vertex orbits. Its signed Lefschetz
# contribution to trace on fifth reduced homology is (-1) per selected orbit.
def character(g):
    cycle_masks = []
    for c in cycle_decomposition(g):
        mask = sum(1 << i for i in c)
        if mask in FACE_SET:
            cycle_masks.append(mask)
    value = 0
    for subset in range(1 << len(cycle_masks)):
        mask = 0
        for k, c in enumerate(cycle_masks):
            if subset & (1 << k):
                mask |= c
        if mask in FACE_SET:
            value += -1 if subset.bit_count() & 1 else 1
    return value

CENTER = [g for g in GROUP if g != IDENTITY and
          all(compose(g,h) == compose(h,g) for h in GROUP)]
assert len(CENTER) == 1 and order(CENTER[0]) == 2
assert character(CENTER[0]) == -4
CLASS_COUNTS = Counter((order(g), character(g)) for g in GROUP)
EXPECTED = {(1,4):1, (2,-4):1, (2,0):30, (3,1):20,
            (5,-1):24, (6,-1):20, (10,1):24}
assert CLASS_COUNTS == EXPECTED, CLASS_COUNTS
assert sum(character(g)**2 for g in GROUP) == len(GROUP)
print('VERIFY_OK')
print('faces_including_empty:',len(FACES))
print('f_vector:',list(map(len,BY_DEGREE)))
print('boundary_ranks_mod_2:',RANKS)
print('reduced_betti_mod_2:',BETTI)
print('automorphisms_generated:',len(GROUP))
print('order_and_character_classes:',sorted(CLASS_COUNTS.items()))
print('complex_character_inner_product:', '120/120 = 1')
