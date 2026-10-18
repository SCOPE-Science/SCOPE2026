"""Construct all 336 Fano-incidence symmetries and check optimum-placement orbits.
Run alongside verify_bfs.py: python3 verify_symmetry.py
"""
from collections import Counter
from itertools import permutations, product
from verify_bfs import ADJ, LINES, all_distributions, reach_mask

def parity(x):
    return x.bit_count() & 1

def action(columns, x):
    result = 0
    for i in range(3):
        if x & (1 << i):
            result ^= columns[i]
    return result

# A line consists of the three nonzero vectors killed by one linear covector.
line_index = {}
for j, line in enumerate(LINES, 7):
    lambdas = [q for q in range(1, 8) if all(parity(q & x) == 0 for x in line)]
    assert len(lambdas) == 1
    line_index[lambdas[0]] = j
assert len(line_index) == 7
symmetries = set()
for a, b, c in product(range(1, 8), repeat=3):
    if len({action((a, b, c), x) for x in range(1, 8)}) != 7:
        continue
    cols = (a, b, c)
    pm = [0] * 14
    for x in range(1, 8):
        pm[x - 1] = action(cols, x) - 1
    for q in range(1, 8):
        transformed = [r for r in range(1, 8)
                       if all(parity(r & action(cols, x)) == parity(q & x) for x in (1, 2, 4))]
        assert len(transformed) == 1
        pm[line_index[q]] = line_index[transformed[0]]
    assert len(set(pm)) == 14
    symmetries.add(tuple(pm))
    # Incidence-preserving duality: point vector x <-> line covector x.
    dual = [0] * 14
    for x in range(1, 8):
        dual[x - 1] = line_index[x]
        dual[line_index[x]] = x - 1
    symmetries.add(tuple(dual[pm[i]] for i in range(14)))
assert len(symmetries) == 336
for perm in symmetries:
    for u in range(14):
        assert {perm[v] for v in ADJ[u]} == {v for v in ADJ[perm[u]]}

opt = {d for d in all_distributions(6) if reach_mask(d) == (1 << 14) - 1}
assert len(opt) == 161
unseen = set(opt)
orbits = []
while unseen:
    d = min(unseen)
    orbit = set()
    for perm in symmetries:
        transformed = [0] * 14
        for i in range(14):
            transformed[perm[i]] = d[i]
        orbit.add(tuple(transformed))
    assert orbit <= opt
    unseen -= orbit
    orbits.append(len(orbit))
assert sorted(orbits) == [21, 42, 42, 56]
print(f'graph_automorphisms={len(symmetries)} optimum_orbit_sizes={sorted(orbits)}')
