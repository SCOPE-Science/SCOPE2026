#!/usr/bin/env python3
"""Exact facet and symmetry-orbit checks for the Fano-incidence metric.

Standard Python 3 only. The graph is represented by the incidence parity
of seven nonzero vectors in F_2^3 and their seven orthogonal lines.
"""
from collections import Counter
from itertools import product

POINTS = tuple(range(1, 8))
PARITY = lambda n: n.bit_count() & 1
EDGES = tuple((p-1, 6+q) for p in POINTS for q in POINTS
              if PARITY(p & q) == 0)
assert len(EDGES) == 21
ADJ = [set() for _ in range(14)]
for u, v in EDGES:
    ADJ[u].add(v)
    ADJ[v].add(u)
assert all(len(a) == 3 for a in ADJ)

# Enumeration I: independence of the seven Fano-line choices after fixing
# all point heights. The two envelopes overlap only when all points are zero.
def classify_by_points():
    families = set()
    histogram = Counter()
    for sign in (1, -1):
        for mask in range(64):
            x = (0,) + tuple(2*sign*((mask >> j) & 1) for j in range(6))
            choices = []
            for q in POINTS:
                pts = [x[p-1] for p in POINTS if PARITY(p&q) == 0]
                possible = tuple(y for y in range(-3, 4)
                                 if all(abs(y-t) == 1 for t in pts))
                assert len(possible) in (1, 2)
                choices.append(possible)
            for ys in product(*choices):
                f = x+ys
                assert all(abs(f[u]-f[v]) == 1 for u,v in EDGES)
                families.add(f)
    for f in families:
        histogram[len(set(f))] += 1
    return families, histogram

# Enumeration II: build every integer function satisfying the (unoriented)
# graph-Lipschitz constraints via the three values on each tree edge, then
# independently test connectedness of the unit-slope edge graph.
def classify_by_spanning_tree():
    order = [0]
    parent = [-1]*14
    parent[0] = 0
    for v in order:
        for w in sorted(ADJ[v]):
            if parent[w] < 0:
                parent[w] = v
                order.append(w)
    assert len(order) == 14
    f = [0]*14
    seen = set()
    def visit(index):
        if index == 14:
            tight = [(a,b) for a,b in EDGES if abs(f[a]-f[b]) == 1]
            reached = {0}
            frontier = [0]
            for u in frontier:
                for v in ADJ[u]:
                    if abs(f[u]-f[v]) == 1 and v not in reached:
                        reached.add(v)
                        frontier.append(v)
            if len(reached) == 14:
                seen.add(tuple(f))
            return
        u = order[index]
        for d in (-1, 0, 1):
            f[u] = f[parent[u]] + d
            if all(abs(f[u]-f[v]) <= 1
                   for v in ADJ[u] if v in assigned[index]):
                visit(index+1)
    assigned = [set(order[:i]) for i in range(15)]
    visit(1)
    return seen

# All 168 invertible linear maps of F_2^3, followed by point-line duality,
# give 336 incidence automorphisms. The size is maximal: every color-
# preserving automorphism is determined by a projective basis.
def graph_automorphisms():
    perms = set()
    for cols in product(POINTS, repeat=3):
        def linear(x):
            return ((cols[0] if x&1 else 0) ^
                    (cols[1] if x&2 else 0) ^
                    (cols[2] if x&4 else 0))
        if len({linear(x) for x in POINTS}) != 7:
            continue
        points = tuple(linear(x)-1 for x in POINTS)
        normals = tuple(next(y-1 for y in POINTS
                             if all(PARITY(linear(x)&y) == PARITY(x&q)
                                    for x in POINTS)) for q in POINTS)
        perms.add(points+tuple(7+y for y in normals))
        perms.add(tuple(7+x for x in points)+normals)
    assert len(perms) == 336
    assert all({tuple(sorted((s[u],s[v]))) for u,v in EDGES} ==
               {tuple(sorted(e)) for e in EDGES} for s in perms)
    return sorted(perms)

def action(f, permutation, sign):
    result = [0]*14
    for i, j in enumerate(permutation):
        result[j] = sign*f[i]
    c = result[0]
    return tuple(x-c for x in result)

def symmetry_orbits(facets, group):
    unused = set(facets)
    orbits = []
    while unused:
        rep = min(unused)
        orbit = {action(rep, p, sign) for p in group for sign in (1,-1)}
        assert orbit <= unused
        unused.difference_update(orbit)
        orbits.append((len(orbit), rep))
    orbits.sort(key=lambda o: (-o[0], o[1]))
    return orbits

def main():
    facets, levels = classify_by_points()
    assert len(facets) == 660
    assert levels == {2: 2, 3: 252, 4: 406}
    # A completely different spanning-tree enumeration yields the same set.
    check_facets = classify_by_spanning_tree()
    assert check_facets == facets
    group = graph_automorphisms()
    orbits = symmetry_orbits(facets, group)
    sizes = [size for size,_ in orbits]
    assert sizes == [168,112,112,84,56,42,28,28,28,2]
    assert sum(sizes) == len(facets) and len(orbits) == 10
    # Count the monochromatic Fano lines directly and by the pair argument.
    for k in range(7):
        assert (k*(7-k)) % 2 == 0
    totals = sum(__import__('math').comb(6,k) *
                 2**(7-k*(7-k)//2) for k in range(7))
    assert totals == 394 and 2*totals - 128 == 660
    print('Heawood metric facets:', len(facets))
    print('Heights by level-count:', dict(sorted(levels.items())))
    print('Full automorphism group:', len(group))
    print('Orbit count including global negation:', len(orbits))
    print('Orbit sizes:', sizes)
    print('Representatives (points 1..7, lines 1..7):')
    for size, rep in orbits:
        print(size, ' '.join(str(x) for x in rep))
    print('ALL EXACT CHECKS PASSED')

if __name__ == '__main__':
    main()
