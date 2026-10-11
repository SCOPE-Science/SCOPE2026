"""Exact integer certificate for the Heawood independence-homology character.
Execute: python3 verify.py (standard library only).
"""
from collections import Counter
from itertools import combinations

BIT_VECTORS = range(1, 8)
VERTEX_COUNT = 14

def dot(x, y):
    return (x & y).bit_count() % 2

# Points and dual points (lines) are respectively vertices 0..6 and 7..13.
edges = {(p - 1, 7 + a - 1) for p in BIT_VECTORS
         for a in BIT_VECTORS if dot(p, a) == 0}
assert len(edges) == 21
edge_masks = [(1 << u) | (1 << v) for u, v in sorted(edges)]
faces = [mask for mask in range(1 << VERTEX_COUNT)
         if all((mask & e) != e for e in edge_masks)]
counts = Counter(mask.bit_count() for mask in faces)
assert [counts[k] for k in range(8)] == [1, 14, 70, 154, 147, 56, 14, 2]

# Exact F_2 chain boundary ranks; this is exhaustive, not sampling.
by_size = {k: [m for m in faces if m.bit_count() == k] for k in range(8)}
ranks = {}
for k in range(2, 8):
    row_index = {mask: j for j, mask in enumerate(by_size[k-1])}
    pivots = {}
    for mask in by_size[k]:
        col = 0
        for i in range(VERTEX_COUNT):
            if mask & (1 << i):
                col ^= 1 << row_index[mask ^ (1 << i)]
        while col:
            pivot = col.bit_length()-1
            if pivot in pivots:
                col ^= pivots[pivot]
            else:
                pivots[pivot] = col
                break
    ranks[k-1] = len(pivots)
assert tuple(ranks[k] for k in range(1, 7)) == (13, 57, 97, 44, 12, 2)
# Reduced boundary d_0 has rank one on nonempty vertices.
assert tuple(counts[k+1] - ranks.get(k, 0) - ranks.get(k+1, 0)
             for k in range(1, 7)) == (0, 0, 6, 0, 0, 0)

# Matrices with ordered images of standard basis e0,e1,e2.
actions = []
for x in BIT_VECTORS:
    for y in BIT_VECTORS:
        for z in BIT_VECTORS:
            if len({0, x, y, z, x^y, y^z, x^z, x^y^z}) < 8:
                continue
            def act(v):
                return ((x if v&1 else 0) ^
                        (y if v&2 else 0) ^
                        (z if v&4 else 0))
            im = [act(v) for v in BIT_VECTORS]
            dual = [next(b for b in BIT_VECTORS
                        if all(dot(a, v) == dot(b, act(v))
                               for v in BIT_VECTORS))
                    for a in BIT_VECTORS]
            permutation = tuple([v-1 for v in im] + [7+a-1 for a in dual])
            assert {tuple(sorted((permutation[u], permutation[v]))) for u, v in edges} == edges
            actions.append(permutation)
assert len(actions) == 168 and len(set(actions)) == 168

def order(perm):
    x = list(range(VERTEX_COUNT))
    for k in range(1, 9):
        x = [perm[i] for i in x]
        if x == list(range(VERTEX_COUNT)):
            return k
    raise AssertionError('order exceeds eight')

def fixed_cycle_count(perm, face):
    visited = set()
    cycles = 0
    for v in range(VERTEX_COUNT):
        if (face & (1 << v)) and v not in visited:
            cycles += 1
            u = v
            while u not in visited:
                assert face & (1 << u)
                visited.add(u)
                u = perm[u]
    return cycles

character = Counter()
cycle_polynomials = {}
for perm in actions:
    g_order = order(perm)
    trace = 0
    polynomial = Counter()
    for mask in faces:
        moved = sum(1 << perm[i] for i in range(VERTEX_COUNT) if mask & (1 << i))
        if moved == mask:
            c = fixed_cycle_count(perm, mask)
            polynomial[c] += 1
            trace += (-1) ** c
    character[g_order, trace] += 1
    coeffs = tuple(polynomial[k] for k in range(max(polynomial)+1))
    if g_order in cycle_polynomials:
        assert cycle_polynomials[g_order] == coeffs
    else:
        cycle_polynomials[g_order] = coeffs
assert character == Counter({(1, 6): 1, (2, -2): 21, (3, 0): 56,
                            (4, 2): 42, (7, -1): 48}), character
assert cycle_polynomials == {
    1:(1,14,70,154,147,56,14,2),
    2:(1,10,32,38,15,2),
    3:(1,6,9,4),
    4:(1,6,9,2),
    7:(1,2),
}, cycle_polynomials
class_values = {1: 6, 2: -2, 3: 0, 4: 2, 7: -1}
order_sizes = {1: 1, 2: 21, 3: 56, 4: 42, 7: 48}
assert sum(order_sizes[o]*class_values[o] for o in order_sizes) == 0  # no trivial summand
assert sum(order_sizes[o]*class_values[o]**2 for o in order_sizes) == 336  # norm=2
# Contrast 6-dimensional nonexceptional character, obtained as reduced 7-point action.
for perm in actions:
    fixed_points = sum(perm[i] == i for i in range(7))
    if order(perm) == 2:
        assert fixed_points-1 == 2 and class_values[2] == -2
print('VERIFY_OK')
print('independent set cardinalities:', tuple(counts[i] for i in range(8)))
print('orbit polynomial coefficients:', cycle_polynomials)
print('mod2 boundary ranks:', tuple(ranks[i] for i in range(1, 7)))
print('group character by order,trace:', dict(sorted(character.items())))
print('character norm squared: 2; invariant subspace dimension: 0')
