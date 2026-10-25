#!/usr/bin/env python3
"""Exact complete census of ordinary secure vertex domination on the Fano Levi graph."""
from collections import Counter, deque
from itertools import combinations, product

VEC = range(1, 8)

def dot(a, b):
    return (a & b).bit_count() % 2

# Points p_1,...,p_7 have indices 0,...,6; lines ell_1,...,ell_7 have 7,...,13.
adj = [0] * 14
for p in VEC:
    for ell in VEC:
        if dot(p, ell) == 0:
            a, b = p - 1, 7 + ell - 1
            adj[a] |= 1 << b
            adj[b] |= 1 << a
closed = [adj[v] | (1 << v) for v in range(14)]

def dominates(s):
    return all(s & closed[v] for v in range(14))

def secure(s):
    if not dominates(s):
        return False
    for attacked in range(14):
        if s & (1 << attacked):
            continue
        if not any(dominates((s ^ (1 << defender)) | (1 << attacked))
                   for defender in range(14)
                   if (s & adj[attacked] & (1 << defender))):
            return False
    return True

def geometric(s):
    pp = [p for p in VEC if s & (1 << (p-1))]
    ll = [ell for ell in VEC if s & (1 << (7+ell-1))]
    return len(pp) == len(ll) == 3 and sum(dot(p, ell) == 0 for p in pp for ell in ll) == 2

ordinary_optima = [s for s in range(1 << 14) if s.bit_count() == 4 and dominates(s)]
assert len(ordinary_optima) == 21 and not any(dominates(s) for s in range(1<<14) if s.bit_count() < 4)
solutions = [s for s in range(1 << 14) if secure(s)]
minimum = min(s.bit_count() for s in solutions)
optimal = sorted(s for s in solutions if s.bit_count() == minimum)
assert minimum == 6 and len(optimal) == 84
assert all(secure(s) == geometric(s) for s in range(1 << 14) if s.bit_count() <= 6)
assert all(sum(dot(p, ell) == 0 for p in VEC for ell in VEC if
               s & (1 << (p-1)) and s & (1 << (7+ell-1))) == 2 for s in optimal)

# The optimal-set exchange graph uses unrestricted one-vertex substitutions.
links = [set() for _ in optimal]
for i in range(len(optimal)):
    for j in range(i):
        if (optimal[i] ^ optimal[j]).bit_count() == 2:
            links[i].add(j)
            links[j].add(i)

def distances(start):
    d = [-1] * len(optimal)
    d[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for w in links[v]:
            if d[w] < 0:
                d[w] = d[v] + 1
                q.append(w)
    return d

one_bfs = distances(0)
assert -1 not in one_bfs
assert Counter(one_bfs) == {0: 1, 1: 4, 2: 8, 3: 16, 4: 28, 5: 22, 6: 4, 7: 1}
assert Counter(map(len, links)) == {4: 84}
assert Counter(max(distances(i)) for i in range(84)) == {7: 84}

# The invertible linear maps of F_2^3 act simultaneously on points and dual lines.
def transform(rows, x):
    return sum(((row & x).bit_count() % 2) << i for i, row in enumerate(rows))

orbit = set()
full_rank_maps = 0
for rows in product(VEC, repeat=3):
    point_map = {x: transform(rows, x) for x in VEC}
    if len(set(point_map.values())) != 7 or 0 in point_map.values():
        continue
    full_rank_maps += 1
    line_map = {}
    for ell in VEC:
        targets = [z for z in VEC if all(dot(z, point_map[x]) == dot(ell, x) for x in VEC)]
        assert len(targets) == 1
        line_map[ell] = targets[0]
    s = optimal[0]
    changed = 0
    for p in VEC:
        if s & (1 << (p-1)):
            changed |= 1 << (point_map[p]-1)
    for ell in VEC:
        if s & (1 << (7+ell-1)):
            changed |= 1 << (7+line_map[ell]-1)
    assert changed in optimal
    orbit.add(changed)
assert full_rank_maps == 168 and len(orbit) == 84

# A representative that makes the geometric construction immediately visible.
witness = ((1 << 0) | (1 << 1) | (1 << 3) |
           (1 << (7+3-1)) | (1 << (7+5-1)) | (1 << (7+7-1)))
assert witness in optimal
assert sum(1 for s in optimal if (s & 127) == (witness & 127)) == 3
print('graph_vertices=14 graph_edges=21')
print('examined_subsets=16384')
print('secure_sets_by_size=' + repr(sorted(Counter(s.bit_count() for s in solutions).items())))
print('ordinary_domination_minimum=4 ordinary_domination_minimum_count=21')
print('minimum_size=6 minimum_count=84 split_3_plus_3=84 incidences_two=84')
print('geometric_criterion_tested_for_all_subsets_of_size_at_most_6=true')
print('exchange_vertices=84 exchange_edges=168 exchange_degree=4 connected=true')
print('distance_layers=' + repr([Counter(one_bfs)[j] for j in range(8)]))
print('radius=7 diameter=7 eccentricity_distribution=' + repr(dict(Counter(max(distances(i)) for i in range(84)))))
print('linear_automorphisms=168 representative_orbit=84')
print('witness_points=[1,2,4] witness_lines=[3,5,7]')
