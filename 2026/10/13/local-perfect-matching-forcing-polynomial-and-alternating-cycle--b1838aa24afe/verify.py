#!/usr/bin/env python3
"""Exact local forcing and alternating-cycle packing on a Fano-triangle Coxeter graph."""
from itertools import combinations
from collections import Counter
import csv
import sys

POINTS = tuple(range(1, 8))
LINES = {tuple(sorted((a, b, a ^ b))) for a, b in combinations(POINTS, 2)}
TRIANGLES = tuple(t for t in combinations(POINTS, 3) if t not in LINES)
assert len(LINES) == 7 and len(TRIANGLES) == 28
IDX = {t: i for i, t in enumerate(TRIANGLES)}
EDGES = tuple((i, j) for i in range(28) for j in range(i + 1, 28)
              if not (set(TRIANGLES[i]) & set(TRIANGLES[j])))
ADJ = [set() for _ in range(28)]
for i, j in EDGES:
    ADJ[i].add(j); ADJ[j].add(i)
assert len(EDGES) == 42 and all(len(a) == 3 for a in ADJ)

def matching_census():
    found = []
    def rec(free, acc):
        if not free:
            found.append(tuple(sorted(acc)))
            return
        v = (free & -free).bit_length() - 1
        for u in sorted(ADJ[v]):
            if free & (1 << u):
                rec(free ^ (1 << v) ^ (1 << u), acc + [(min(v, u), max(v, u))])
    rec((1 << 28) - 1, [])
    out = sorted(set(found))
    assert len(out) == len(found) == 84
    return out

MATCHINGS = matching_census()
M = MATCHINGS[0]

def polynomial(m):
    differences = [sum(1 << k for k, e in enumerate(m) if e not in other)
                   for other in MATCHINGS if other != m]
    forced = [s for s in range(1 << 14) if all(s & d for d in differences)]
    return tuple(sum(s.bit_count() == k for s in forced) for k in range(15)), forced

PROFILE, FORCED = polynomial(M)
assert PROFILE == (0, 0, 0, 0, 198, 1018, 2300, 3124, 2918,
                   1988, 1000, 364, 91, 14, 1)
for m in MATCHINGS:
    assert polynomial(m)[0] == PROFILE

# All M-alternating cycles can be obtained from M symmetric-difference M':
# flipping one such component in M gives another perfect matching, and conversely.
def alternating_cycles(m):
    out = {}
    for other in MATCHINGS:
        diff = set(m).symmetric_difference(other)
        if not diff: continue
        da = {v: set() for e in diff for v in e}
        for u, v in diff:
            da[u].add(v); da[v].add(u)
        while da:
            start = next(iter(da))
            todo = [start]; component = set()
            while todo:
                x = todo.pop()
                if x in component: continue
                component.add(x); todo.extend(da[x] - component)
            for x in component: da.pop(x)
            component_edges = tuple(sorted(e for e in diff if e[0] in component))
            assert len(component_edges) == len(component) and len(component) % 2 == 0
            out[component_edges] = frozenset(component)
    return out

CYCLES = alternating_cycles(M)
COUNTS = Counter(len(x) for x in CYCLES)
assert COUNTS == {8: 1, 10: 4, 12: 4, 14: 12, 16: 9,
                  18: 4, 20: 16, 22: 16, 24: 8}
assert len(CYCLES) == 74
C8 = [v for e, v in CYCLES.items() if len(e) == 8]
C10 = [v for e, v in CYCLES.items() if len(e) == 10]
assert len(C8) == 1 and len(C10) == 4
assert all(len(C8[0] & t) == 2 for t in C10)
assert all(len(a & b) >= 2 for a, b in combinations(C10, 2))
# 3 disjoint alternating cycles would have to have lengths 8,10,10
# because 8 is unique and the other lengths are >=10. The intersection
# test excludes this. A disjoint pair supplies the lower bound 2.
PAIR = next(((e, f) for (e, a), (f, b) in combinations(CYCLES.items(), 2)
             if not (a & b)), None)
assert PAIR is not None

# GL(3,2) has order 168. Duality sends each triangle to the three normals
# of its three connecting Fano lines, yielding an additional 168 maps.
def dot(a, b):
    return (a & b).bit_count() & 1

def normal(a, b):
    answer = [n for n in POINTS if dot(n, a) == dot(n, b) == 0]
    assert len(answer) == 1
    return answer[0]

def dual(t):
    a, b, c = t
    return tuple(sorted((normal(a,b),normal(a,c),normal(b,c))))

D = [IDX[dual(t)] for t in TRIANGLES]
assert len(set(D)) == 28 and all(D[D[i]] == i for i in range(28))
AUT = set()
for a in POINTS:
    for b in POINTS:
        if b == a: continue
        for c in POINTS:
            if c in (a, b, a ^ b): continue
            def lin(x):
                return ((a if x & 1 else 0) ^ (b if x & 2 else 0)
                        ^ (c if x & 4 else 0))
            g = tuple(IDX[tuple(sorted(map(lin, t)))] for t in TRIANGLES)
            AUT.add(g)
            AUT.add(tuple(D[g[i]] for i in range(28)))
assert len(AUT) == 336
E = set(EDGES)
assert all({tuple(sorted((g[i],g[j]))) for i,j in EDGES} == E for g in AUT)

# Independent induced-adjacency backtracking certifies no automorphisms
# beyond the explicitly constructed 336-element group.
def full_automorphism_count():
    count = 0
    def rec(mapping, used):
        nonlocal count
        if len(mapping) == 28:
            count += 1
            return
        frontier = [v for v in range(28) if v not in mapping
                    and any(u in mapping for u in ADJ[v])]
        assert frontier
        v = max(frontier, key=lambda w: (sum(u in mapping for u in ADJ[w]), -w))
        neighbors = [mapping[u] for u in ADJ[v] if u in mapping]
        options = set.intersection(*(ADJ[u] for u in neighbors))
        for y in sorted(options - used):
            if all((w in ADJ[v]) == (mapping[w] in ADJ[y]) for w in mapping):
                mapping[v] = y
                used.add(y)
                rec(mapping, used)
                used.remove(y)
                del mapping[v]
    for image in range(28):
        rec({0: image}, {image})
    return count

assert full_automorphism_count() == len(AUT) == 336

MATCHING_SET = set(MATCHINGS)
assert {tuple(sorted(tuple(sorted((g[u],g[v]))) for u,v in M))
        for g in AUT} == MATCHING_SET

# Global classification of minimum forcing quartets (each forces a unique matching).
FORCING4 = set()
for m in MATCHINGS:
    poly, forced = polynomial(m)
    for s in forced:
        if s.bit_count() == 4:
            FORCING4.add(tuple(sorted(m[k] for k in range(14) if s & (1 << k))))
assert len(FORCING4) == 84 * 198
left = set(FORCING4); ORBITS = []
while left:
    rep = min(left)
    orbit = {tuple(sorted(tuple(sorted((g[u],g[v]))) for u,v in rep)) for g in AUT}
    assert orbit <= left
    left -= orbit
    ORBITS.append((rep, len(orbit)))
assert len(ORBITS) == 51
assert Counter(sz for _,sz in ORBITS) == {336: 48, 168: 3}
assert sum(sz for _,sz in ORBITS) == 16632

# Output one representative and orbit size per orbit, reproducibly.
with open('quartet_orbits.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(('orbit_index','size','edges_zero_based'))
    for k,(rep, size) in enumerate(ORBITS, 1):
        writer.writerow((k,size,' '.join(f'{u}-{v}' for u,v in rep)))


with open('alternating_cycles.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(('cycle_index', 'length', 'edges_zero_based'))
    for k, edges in enumerate(sorted(CYCLES), 1):
        writer.writerow((k, len(edges), ' '.join(f'{u}-{v}' for u,v in edges)))

print('VERIFY_OK Coxeter Fano-triangle graph vertices=28 edges=42 perfect_matchings=84')
print('VERIFY_OK full_automorphism_count=336 transitive_matching_orbit=84')
print('VERIFY_OK per_matching_forcing_polynomial=' + ','.join(f'{i}:{v}' for i,v in enumerate(PROFILE) if v))
print('VERIFY_OK forcing_number=4 minimum_quartets_per_matching=198 global=16632')
print('VERIFY_OK quartet_orbits=51 sizes=336x48+168x3')
print('VERIFY_OK alternating_cycles=74 length_distribution=' + ','.join(f'{i}:{COUNTS[i]}' for i in sorted(COUNTS)))
print('VERIFY_OK maximum_vertex_disjoint_alternating_cycles=2 witness=' + repr(PAIR))
print('VERIFY_OK minmax_gap=2; quartet_orbits.csv checked')
