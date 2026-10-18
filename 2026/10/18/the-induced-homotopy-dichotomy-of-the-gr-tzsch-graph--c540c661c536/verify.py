#!/usr/bin/env python3
"""Exact, self-contained verifier for induced sphere carriers in the Grötzsch independence complex.
Run: python3 verify.py (Python 3.9+, standard library only).
"""
import json
from collections import Counter, defaultdict
from pathlib import Path
from itertools import combinations

N = 11
ALL = (1 << N) - 1
EDGES = set()
def add(a, b):
    EDGES.add(tuple(sorted((a, b))))
for i in range(5):
    add(i, (i + 1) % 5)
    add(i, 5 + (i + 1) % 5)
    add((i + 1) % 5, 5 + i)
    add(10, 5 + i)
assert len(EDGES) == 20
EDGE_MASKS = {sum(1 << i for i in e) for e in EDGES}
FACES = {s for s in range(1, ALL + 1) if all(s & e != e for e in EDGE_MASKS)}
assert Counter(s.bit_count() for s in FACES) == {1:11, 2:35, 3:40, 4:15, 5:1}

def induced(mask):
    return {s for s in FACES if (s & mask) == s}

def collapse_check(start, pairs, desired, name):
    current = set(start)
    assert desired <= current, (name, 'bad target')
    for step, (lower, upper) in enumerate(pairs):
        assert lower in current and upper in current, (name, step, 'not present')
        assert lower > 0 and lower & upper == lower
        assert upper.bit_count() == lower.bit_count() + 1
        # A free face has precisely one strict containing simplex.
        strict_cofaces = [s for s in current if s != lower and (s & lower) == lower]
        assert strict_cofaces == [upper], (name, step, 'not a free face', strict_cofaces)
        current.remove(lower)
        current.remove(upper)
    assert current == desired, (name, len(current), len(desired))
    return current

def bits(mask):
    return [i for i in range(N) if (mask >> i) & 1]

def rotate_bit(i, j):
    return 10 if i == 10 else (5 if i >= 5 else 0) + ((i % 5 + j) % 5)

def rotated_mask(mask, j):
    return sum(1 << rotate_bit(i, j) for i in bits(mask))

cert = json.loads((Path(__file__).parent / 'certificate.json').read_text(encoding='utf8'))
C_MASK = ALL ^ (1 << 5) ^ (1 << 6)
CORE = induced(C_MASK)
case_specs = {
    'ambient_to_core': (ALL, CORE),
    'without_twin_0_to_core': (ALL ^ (1 << 5), CORE),
    'without_twin_1_to_core': (ALL ^ (1 << 6), CORE),
    'core_to_sphere': (C_MASK, None),
    'without_original_0_to_point': (ALL ^ 1, None),
    'without_root_to_point': (ALL ^ (1 << 10), None),
    'bad_triple_to_point': (sum(1 << i for i in (0,1,2,3,4,10,5,6,8)), None),
}
assert set(cert['cases']) == set(case_specs)
for name, (mask, required) in case_specs.items():
    case = cert['cases'][name]
    assert case['mask'] == mask
    rest = set(case['remaining'])
    if required is not None:
        assert rest == required
    elif name.endswith('to_point'):
        assert len(rest) == 1 and next(iter(rest)).bit_count() == 1
    collapse_check(induced(mask), case['pairs'], rest, name)

# The 44 remaining simplices are a genuine connected, closed, combinatorial surface.
SPHERE = set(cert['cases']['core_to_sphere']['remaining'])
assert Counter(s.bit_count() for s in SPHERE) == {1:9, 2:21, 3:14}
TRIANGLES = {s for s in SPHERE if s.bit_count() == 3}
EDGES2 = {s for s in SPHERE if s.bit_count() == 2}
VERTS2 = {s for s in SPHERE if s.bit_count() == 1}
for e in EDGES2:
    assert sum((t & e) == e for t in TRIANGLES) == 2
for v in VERTS2:
    neighbors = {e ^ v for e in EDGES2 if e & v}
    link_edges = {t ^ v for t in TRIANGLES if t & v}
    assert len(neighbors) == len(link_edges) >= 3
    assert all(sum((le & u) == u for le in link_edges) == 2 for u in neighbors)
    seen = {next(iter(neighbors))}
    for _ in range(len(neighbors)):
        seen |= {u for e in link_edges if e & sum(seen) for u in (e & -e, e ^ (e & -e))}
    assert seen == neighbors
seen = {next(iter(VERTS2))}
for _ in range(len(VERTS2)):
    seen |= {e for edge in EDGES2 for e in (edge & -edge, edge ^ (edge & -edge)) if edge & sum(seen)}
assert seen == VERTS2
assert len(VERTS2) - len(EDGES2) + len(TRIANGLES) == 2

# Exact order complex of all vertex sets: five minimal good sets and eleven maximal bad sets.
CORE_MASKS = {rotated_mask(C_MASK, j) for j in range(5)}
BAD_MASKS = {ALL ^ (1 << i) for i in range(5)}
BAD_MASKS.add(ALL ^ (1 << 10))
BAD_BASE = case_specs['bad_triple_to_point'][0]
BAD_MASKS |= {rotated_mask(BAD_BASE, j) for j in range(5)}
assert len(CORE_MASKS) == 5 and len(BAD_MASKS) == 11
accepted_by_size = Counter()
for W in range(1 << N):
    containing = [c for c in CORE_MASKS if W & c == c]
    covered = [b for b in BAD_MASKS if W & b == W]
    assert bool(containing) != bool(covered), (W, containing, covered)
    if containing:
        accepted_by_size[W.bit_count()] += 1
        # Once the chosen core is rotated to C_MASK, only four intermediate
        # vertex sets can occur, all explicitly certified above.
        c = containing[0]
        j = next(j for j in range(5) if rotated_mask(C_MASK, j) == c)
        rotated = rotated_mask(W, -j)
        assert rotated in (C_MASK, ALL, ALL ^ (1 << 5), ALL ^ (1 << 6))
assert dict(accepted_by_size) == {9:5, 10:5, 11:1}

# All permutations of the Grötzsch graph: D_5, acting by simultaneous
# permutations of original and twin C_5 vertices and fixing the root.
def phi(a, reflection, i):
    if i == 10:
        return 10
    return (5 if i >= 5 else 0) + ((a + (-1 if reflection else 1) * (i % 5)) % 5)

def parity(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq))) % 2 else 1

characters = {}
for b in (0, 1):
    for a in range(5):
        perm = [phi(a, b, i) for i in range(N)]
        assert {tuple(sorted((perm[i], perm[j]))) for i, j in EDGES} == EDGES
        assert len(set(perm)) == N
        reduced_lefschetz = -1
        for simplex in FACES:
            members = bits(simplex)
            images = [perm[i] for i in members]
            if set(members) != set(images):
                continue
            ordering = sorted(images)
            signed_simplex_action = parity([ordering.index(x) for x in images])
            reduced_lefschetz += (-1) ** (len(members) - 1) * signed_simplex_action
        assert reduced_lefschetz == (-1 if b else 1)
        characters[(a, b)] = reduced_lefschetz
assert len(characters) == 10
print('VERIFY_OK GROTzSCH_INDEPENDENCE F_VECTOR_11_35_40_15_1')
print('SEVEN_EXPLICIT_COLLAPSE_CERTIFICATES VERIFIED CLOSED_SPHERE_9_21_14')
print('FIVE_MINIMAL_9_VERTEX_S2_CARRIERS BAD_MAXIMAL_CONTRACTIBLE_11')
print('ALL_2048_INDUCED_SETS CLASSIFIED GOOD_SIZES_9_5_10_5_11_1')
print('FULL_D5_CHARACTER ROTATIONS_POSITIVE REFLECTIONS_NEGATIVE')
