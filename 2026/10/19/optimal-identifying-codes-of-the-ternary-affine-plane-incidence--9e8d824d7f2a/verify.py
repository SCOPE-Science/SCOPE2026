#!/usr/bin/env python3
"""Exact finite verification of identifying-code exchange in AG(2,3)'s Levi graph.

Standalone: Python 3.10+ standard library only. Run with `python3 verify.py`.
"""
from itertools import combinations, product
from collections import Counter, deque

F = range(3)
points = tuple(product(F, repeat=2))
pid = {p: i for i, p in enumerate(points)}
lines = []
for m in F:
    for b in F:
        lines.append(frozenset(pid[(x, (m*x + b) % 3)] for x in F))
for x in F:
    lines.append(frozenset(pid[(x, y)] for y in F))
assert len(lines) == 12 and len(set(lines)) == 12
assert all(len(line) == 3 for line in lines)
assert all(sum(i in line for line in lines) == 4 for i in range(9))
assert all(sum(i in line and j in line for line in lines) == 1
           for i, j in combinations(range(9), 2))

# The 21 vertices are points 0..8 and lines 9..20.
N = [1 << i for i in range(21)]
for j, line in enumerate(lines):
    for p in line:
        N[p] |= 1 << (9 + j)
        N[9 + j] |= 1 << p

# Two different exhaustive predicates: trace comparison versus hitting all
# domination and symmetric-difference constraints. Neither relies on the other.
def signature_identifying(mask):
    seen = set()
    for closed in N:
        trace = closed & mask
        if not trace or trace in seen:
            return False
        seen.add(trace)
    return True

constraints = tuple(sorted(
    set(N) | {N[i] ^ N[j] for i, j in combinations(range(21), 2)},
    key=lambda s: (s.bit_count(), s)))
assert all(c != 0 for c in constraints)

def hitting_identifying(mask):
    return all(mask & restriction for restriction in constraints)

def masks_of_size(k):
    for choose in combinations(range(21), k):
        yield sum(1 << i for i in choose)

# An identifying code is upward closed. Absence of size-eight codes rules
# out all smaller sizes, since any smaller code can be extended to eight.
small_a = sum(signature_identifying(s) for s in masks_of_size(8))
small_b = sum(hitting_identifying(s) for s in masks_of_size(8))
assert small_a == small_b == 0
opt_a = {s for s in masks_of_size(9) if signature_identifying(s)}
opt_b = {s for s in masks_of_size(9) if hitting_identifying(s)}
assert opt_a == opt_b

# Independent geometrical classification of all optimum sets.
all_points = (1 << 9) - 1
flags = {}
for p in range(9):
    for j, line in enumerate(lines):
        if p in line:
            flags[(p, j)] = (all_points ^ (1 << p)) | (1 << (9 + j))
assert len(flags) == 36
parallel_classes = [tuple(range(3*i, 3*i + 3)) for i in range(4)]
triangles = {}
for T in combinations(range(9), 3):
    if any(set(T) <= line for line in lines):
        continue
    # A noncollinear three-set uses three different joining directions.
    used_classes = {next(j // 3 for j, line in enumerate(lines)
                         if pair[0] in line and pair[1] in line)
                    for pair in combinations(T, 2)}
    assert len(used_classes) == 3
    unique_class = (set(range(4)) - used_classes).pop()
    mask = all_points ^ sum(1 << p for p in T)
    mask |= sum(1 << (9 + j) for j in parallel_classes[unique_class])
    triangles[T] = (mask, unique_class)
assert len(triangles) == 72
expected = {all_points} | set(flags.values()) | {s for s, _ in triangles.values()}
assert len(expected) == 109 and opt_a == expected
assert Counter(((s & all_points).bit_count(), (s >> 9).bit_count())
               for s in opt_a) == {(9, 0): 1, (8, 1): 36, (6, 3): 72}

# All single-exchange edges are tested; the graph has 109 vertices.
adj = {s: set() for s in expected}
for s in expected:
    for deleted in range(21):
        if not (s >> deleted) & 1:
            continue
        for added in range(21):
            if (s >> added) & 1:
                continue
            t = s ^ (1 << deleted) ^ (1 << added)
            if t in expected:
                adj[s].add(t)
assert all(s in adj[t] for s, ns in adj.items() for t in ns)
assert sum(map(len, adj.values())) // 2 == 234
assert Counter(map(len, adj.values())) == {3: 72, 6: 36, 36: 1}

remaining = set(expected)
components = []
while remaining:
    start = min(remaining)
    reached = {start}
    q = deque([start])
    while q:
        for t in adj[q.popleft()]:
            if t not in reached:
                reached.add(t)
                q.append(t)
    components.append(reached)
    remaining -= reached
assert Counter(map(len, components)) == {18: 4, 37: 1}

def ecc_in_component(vertex, component):
    d = {vertex: 0}
    q = deque([vertex])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if w in component and w not in d:
                d[w] = d[v] + 1
                q.append(w)
    assert len(d) == len(component)
    return max(d.values())

big = next(c for c in components if len(c) == 37)
assert big == {all_points} | set(flags.values())
assert adj[all_points] == set(flags.values())
flag_inverse = {s: key for key, s in flags.items()}
for s, t in combinations(flags.values(), 2):
    p, ell = flag_inverse[s]
    q, m = flag_inverse[t]
    assert (t in adj[s]) == (p == q or ell == m)
assert sum(len(adj[s] & big) for s in big) // 2 == 126
assert {ecc_in_component(s, big) for s in big} == {1, 2}

# For each parallel class, normalize it to the horizontal lines of F_3^2.
# The missing noncollinear triangle has one point on each such line,
# giving three x-coordinates with sum 1 or 2 in F_3.
forms = ((0, 1), (2, 1), (1, 1), (1, 0))
triangle_by_code = {s: (T, k) for T, (s, k) in triangles.items()}
for component in components:
    if len(component) != 18:
        continue
    class_ids = {triangle_by_code[s][1] for s in component}
    assert len(class_ids) == 1
    k = class_ids.pop()
    a, b = forms[k]
    labels = {}
    for s in component:
        T, _ = triangle_by_code[s]
        coords = {}
        for p in T:
            px, py = points[p]
            y = (a * px + b * py) % 3
            x = px if b else py
            assert y not in coords
            coords[y] = x
        assert len(coords) == 3
        label = tuple(coords[i] for i in F)
        assert sum(label) % 3 in (1, 2)
        labels[s] = label
    assert len(set(labels.values())) == 18
    assert sum(len(adj[s] & component) for s in component) // 2 == 27
    for s, t in combinations(component, 2):
        xs, xt = labels[s], labels[t]
        # The standard Pappus bi-Cayley model: from coordinate-sum 1,
        # add 1 to one of the three coordinates to obtain sum 2.
        standard_edge = (
            sum(x != y for x, y in zip(xs, xt)) == 1
            and {sum(xs) % 3, sum(xt) % 3} == {1, 2})
        assert (t in adj[s]) == standard_edge
    assert {ecc_in_component(s, component) for s in component} == {4}

# Independent explicit isomorphism between the standard bi-Cayley model
# and the Pappus incidence graph (points (x,y), lines y=m*x+b).
def pappus_point(u, v):
    return (v - u) % 3, (-u*u - u - v*v - v - u*v) % 3

def pappus_line(u, v):
    x, y = pappus_point(u, v)
    return x, (y - x*x) % 3

uv = list(product(F, repeat=2))
assert len({pappus_point(*t) for t in uv}) == 9
assert len({pappus_line(*t) for t in uv}) == 9
for u, v in uv:
    p = pappus_point(u, v)
    for s, t in uv:
        ell = pappus_line(s, t)
        standard_edge = ((s,t) in (((u,v), ((u+1)%3,v), (u,(v+1)%3))))
        incidence = (p[1] == (ell[0]*p[0] + ell[1])%3)
        assert standard_edge == incidence

# Verify that the 432 affine automorphisms generate three precise orbits.
linear = [(a,b,c,d) for a,b,c,d in product(F,repeat=4) if (a*d-b*c)%3]
line_lookup = {line: j for j,line in enumerate(lines)}
perms = []
for a,b,c,d in linear:
    for dx,dy in uv:
        pp = [pid[((a*x+b*y+dx)%3,(c*x+d*y+dy)%3)] for x,y in points]
        perm = pp + [9 + line_lookup[frozenset(pp[p] for p in ell)]
                     for ell in lines]
        perms.append(perm)
assert len(perms) == 432

def transform(mask, perm):
    return sum((1<<perm[i]) for i in range(21) if mask>>i & 1)

left = set(expected)
orbits = []
while left:
    s = min(left)
    orbit = {transform(s,perm) for perm in perms}
    assert orbit <= expected
    orbits.append(len(orbit))
    left -= orbit
assert sorted(orbits) == [1, 36, 72]
print('OK: all 203490 size-8 sets rejected by two independent predicates')
print('OK: both size-9 enumerations give exactly 109 minimal codes (1+36+72)')
print('OK: affine symmetry orbit sizes 1,36,72; 432 affine maps')
print('OK: exchange graph 109 vertices, 234 edges: cone over line graph (37,126) plus 4 Pappus components (18,27 each)')
print('OK: radii/diameters 1/2 for cone, 4/4 for Pappus; explicit incidence isomorphism validated')
