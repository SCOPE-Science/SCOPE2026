#!/usr/bin/env python3
"""Exact finite verification for the icosahedral odd-cycle-independent complex.

Requires only the Python 3 standard library. Vertices are numbered 0,...,11.
A simplex is a nonempty subset of vertices inducing a bipartite graph.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

NBR = (
 (1, 5, 7, 8, 11),
 (0, 2, 5, 6, 8),
 (1, 3, 6, 8, 9),
 (2, 4, 6, 9, 10),
 (3, 5, 6, 10, 11),
 (0, 1, 4, 6, 11),
 (1, 2, 3, 4, 5),
 (0, 8, 9, 10, 11),
 (0, 1, 2, 7, 9),
 (2, 3, 7, 8, 10),
 (3, 4, 7, 9, 11),
 (0, 4, 5, 7, 10),
)
N = len(NBR)
assert N == 12 and all(len(a) == 5 for a in NBR)
assert all(i in NBR[j] for i in range(N) for j in NBR[i])
assert sum(len(a) for a in NBR) // 2 == 30


def vertices(mask):
    return tuple(i for i in range(N) if mask & (1 << i))


def bipartite(mask):
    """Independent two-color propagation, not using forbidden-cycle lists."""
    colors = {}
    for root in vertices(mask):
        if root in colors:
            continue
        colors[root] = 0
        todo = [root]
        for a in todo:
            for b in NBR[a]:
                if not (mask & (1 << b)):
                    continue
                if b not in colors:
                    colors[b] = 1 - colors[a]
                    todo.append(b)
                elif colors[b] == colors[a]:
                    return False
    return True


def odd_cycle_vertex_sets():
    """Independent exhaustive simple-cycle enumeration by DFS."""
    odd = set()
    for first in range(N):
        def visit(path, used):
            x = path[-1]
            for y in NBR[x]:
                if y == first:
                    if len(path) >= 3 and len(path) % 2 and path[1] < path[-1]:
                        odd.add(used)
                elif y > first and not used & (1 << y):
                    visit(path + (y,), used | (1 << y))
        for second in NBR[first]:
            if second > first:
                visit((first, second), (1 << first) | (1 << second))
    return odd


odd = odd_cycle_vertex_sets()
faces = {m for m in range(1, 1 << N) if bipartite(m)}
assert all(((not any(m & o == o for o in odd)) == (m in faces))
           for m in range(1, 1 << N))
assert len(faces) == 1023
fvector = tuple(sum(m.bit_count() == k for m in faces) for k in range(1, 7))
assert fvector == (12, 66, 200, 345, 300, 100)
assert max(m.bit_count() for m in faces) == 6
minimum_odd = set()
for m in range(1, 1 << N):
    if m not in faces and all((m ^ (1 << i)) in faces or
                              (m ^ (1 << i)) == 0 for i in vertices(m)):
        minimum_odd.add(m)
assert Counter(m.bit_count() for m in minimum_odd) == {3: 20, 5: 12}
assert minimum_odd <= odd
triangles = {m for m in minimum_odd if m.bit_count() == 3}
tri_free = {m for m in range(1, 1 << N)
            if not any((m & t) == t for t in triangles)}
difference = tri_free - faces
assert len(tri_free) == 1047 and len(difference) == 24
assert Counter(m.bit_count() for m in difference) == {5: 12, 6: 12}

# The larger triangle-free complex elementary-collapses onto the
# odd-cycle-independent complex, through exactly 12 free-face pairs.
remaining = set(tri_free)
removed = []
for m in sorted(x for x in difference if x.bit_count() == 5):
    cofaces = [t for t in remaining if t != m and (m & t) == m]
    assert len(cofaces) == 1 and cofaces[0].bit_count() == 6
    big = cofaces[0]
    assert big in difference
    remaining.remove(m)
    remaining.remove(big)
    removed.append((m, big))
assert remaining == faces and len(removed) == 12

# Pure connected pseudomanifold, every codimension-one face in two facets.
facets = sorted(m for m in faces if m.bit_count() == 6)
assert all(not any(m | (1 << i) in faces for i in range(N) if not m & (1 << i))
           for m in facets)


def boundary(mask):
    return tuple((mask ^ (1 << i), (-1) ** j)
                 for j, i in enumerate(vertices(mask)))

ridges = defaultdict(list)
for f in facets:
    for a, coefficient in boundary(f):
        ridges[a].append((f, coefficient))
assert len(ridges) == 300 and all(len(p) == 2 for p in ridges.values())
dual = defaultdict(list)
for pair in ridges.values():
    (f, s), (g, t) = pair
    transition = -s * t
    dual[f].append((g, transition))
    dual[g].append((f, transition))
assert sum(len(v) for v in dual.values()) == 600
seen = {facets[0]}
queue = deque([facets[0]])
while queue:
    for target, s in dual[queue.popleft()]:
        if target not in seen:
            seen.add(target)
            queue.append(target)
assert len(seen) == len(facets)
# A closed signed walk with product of transition signs -1
obstruction = (0x09f, 0x89e, 0xa96, 0x2b6, 0x2b5, 0x0bd, 0x09f)
product = 1
for a, b in zip(obstruction, obstruction[1:]):
    shifts = [s for other, s in dual[a] if other == b]
    assert len(shifts) == 1
    product *= shifts[0]
assert product == -1

# Construct a perfect algebraic discrete-Morse pairing. At step v,
# pair every remaining simplex A not containing v with A union {v}
# whenever both are remaining. This includes no empty simplex.
rest = set(faces)
matched = {}
pair_counts = []
for v in range(N):
    vbit = 1 << v
    choices = [(a, a | vbit) for a in rest
               if not a & vbit and a | vbit in rest]
    pair_counts.append(len(choices))
    for lower, upper in choices:
        assert lower in rest and upper in rest
        matched[lower] = upper
        matched[upper] = lower
        rest.remove(lower)
        rest.remove(upper)
assert pair_counts == [351, 77, 30, 28, 15, 1, 0, 4, 1, 0, 3, 0]
assert rest == {0x001, 0xa52, 0xf60}
assert len(matched) == 1020

# Check acyclicity of the FULL reversed Hasse diagram, not just
# absence of closed gradient paths in selected dimensions.
out = defaultdict(list)
indeg = {a: 0 for a in faces}
incidences = 0
for upper in faces:
    for lower, _ in boundary(upper):
        if lower == 0:
            continue
        source, target = ((lower, upper) if matched.get(lower) == upper
                          else (upper, lower))
        out[source].append(target)
        indeg[target] += 1
        incidences += 1
assert incidences == 4212
queue = deque(m for m, k in indeg.items() if k == 0)
count = 0
while queue:
    x = queue.popleft()
    count += 1
    for y in out[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            queue.append(y)
assert count == len(faces) == 1023

# Determine the exact signed algebraic Morse differential.
# For 4-face A matched upward to 5-face B, eliminate A with the
# integer relation boundary(B) = 0. Lower-dimensional pairs are
# projected away; an acyclic matching makes this recursion finite.
critical4 = 0xa52
critical5 = 0xf60


@lru_cache(None)
def reduce_four_cell(a):
    partner = matched.get(a)
    if partner is None:
        return int(a == critical4)
    if partner.bit_count() < a.bit_count():
        return 0
    pivot = dict(boundary(partner))[a]
    return sum((-pivot) * sign * reduce_four_cell(other)
               for other, sign in boundary(partner) if other != a)

morse_degree = sum(sign * reduce_four_cell(a) for a, sign in boundary(critical5))
assert morse_degree == 2
assert reduce_four_cell.cache_info().currsize == 300

# Independent modular homology sanity check for the two top dimensions.
def boundary_rank_modp(k, p):
    upper = sorted(m for m in faces if m.bit_count() == k + 1)
    lower = sorted(m for m in faces if m.bit_count() == k)
    index = {m: j for j, m in enumerate(lower)}
    pivot_basis = {}
    for x in upper:
        col = {index[y]: s % p for y, s in boundary(x)}
        while col:
            r = max(col)
            if r not in pivot_basis:
                inv = pow(col[r], -1, p)
                pivot_basis[r] = {j: v * inv % p for j, v in col.items()
                                  if v * inv % p}
                break
            factor = col[r]
            for j, v in pivot_basis[r].items():
                w = (col.get(j, 0) - factor * v) % p
                if w:
                    col[j] = w
                else:
                    col.pop(j, None)
    return len(pivot_basis)

mod2 = (boundary_rank_modp(4, 2), boundary_rank_modp(5, 2))
mod3 = (boundary_rank_modp(4, 3), boundary_rank_modp(5, 3))
assert mod2 == (200, 99)
assert mod3 == (200, 100)

print('GRAPH vertices=12 edges=30 degree=5')
print('MINIMAL_ODD_CYCLES lengths:', dict(sorted(Counter(m.bit_count() for m in minimum_odd).items())))
print('BIPARTITE_F_VECTOR', fvector)
print('TRIANGLE_FREE_FACES', len(tri_free), 'COLLAPSE_PAIRS', len(removed))
print('RIDGES', len(ridges), 'DUAL_CONNECTED', len(seen) == 100)
print('NONORIENTABLE_HOLONOMY', product, 'WALK', [hex(m) for m in obstruction])
print('MORSE_PAIR_COUNTS', pair_counts, 'TOTAL', len(matched) // 2)
print('MORSE_CRITICAL', [hex(m) for m in sorted(rest)])
print('HASSE_INCIDENCES', incidences, 'ACYCLETOPOSORT', count)
print('INTEGRAL_MORSE_DEGREE', morse_degree)
print('BOUNDARY_RANKS_MOD2', mod2, 'MOD3', mod3)
print('HOMOTOPY Moore(Z/2,4)')
print('VERIFY_OK')
