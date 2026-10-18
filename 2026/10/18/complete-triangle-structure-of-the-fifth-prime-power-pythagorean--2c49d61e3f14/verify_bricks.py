"""Exact finite certificate for the fifth prime-power Pythagorean graph.

Run: python3 verify_bricks.py
Only Python's standard library is required. All squared integers use exact arithmetic.
"""
from collections import Counter, defaultdict
from itertools import product
from math import gcd, isqrt, prod

PRIMES = (2, 3, 5, 7, 11)
vertices = sorted(prod(p ** exponent for p, exponent in zip(PRIMES, exponents))
                  for exponents in product(range(5), repeat=5))
assert len(vertices) == 3125 and len(set(vertices)) == len(vertices)
n = len(vertices)
adj = [set() for _ in range(n)]
for i, u in enumerate(vertices):
    for j in range(i + 1, n):
        s = u * u + vertices[j] * vertices[j]
        r = isqrt(s)
        if r * r == s:
            adj[i].add(j)
            adj[j].add(i)
edges = sum(len(a) for a in adj) // 2
assert edges == 14856, edges

triangles = []
for i in range(n):
    for j in adj[i]:
        if j <= i:
            continue
        for k in adj[i] & adj[j]:
            if k > j:
                triangles.append((vertices[i], vertices[j], vertices[k]))
triangles.sort()
assert len(triangles) == len(set(triangles)) == 288
primitive_counts = Counter()
for triple in triangles:
    g = gcd(gcd(triple[0], triple[1]), triple[2])
    primitive_counts[tuple(v // g for v in triple)] += 1
expected = {(240, 252, 275): 144, (1008, 1100, 1155): 144}
assert primitive_counts == expected, primitive_counts

by_vertex = defaultdict(list)
for i, triple in enumerate(triangles):
    for v in triple:
        by_vertex[v].append(i)
assert max(map(len, by_vertex.values())) == 2
conflicts = [set() for _ in triangles]
for members in by_vertex.values():
    for i in members:
        conflicts[i].update(j for j in members if j != i)
assert Counter(map(len, conflicts)) == {0: 174, 1: 114}
pairs = [(i, j) for i, neighbors in enumerate(conflicts) for j in neighbors if i < j]
assert len(pairs) == 57
assert Counter(len(set(triangles[i]) & set(triangles[j])) for i, j in pairs) == {1: 9, 2: 48}

packing_indices = [i for i, neighbors in enumerate(conflicts) if not neighbors] + [i for i, j in pairs]
assert len(packing_indices) == 231
all_packing_vertices = [v for i in packing_indices for v in triangles[i]]
assert len(all_packing_vertices) == len(set(all_packing_vertices)) == 693
hitting = [min(triangles[i]) for i, neighbors in enumerate(conflicts) if not neighbors]
hitting += [min(set(triangles[i]) & set(triangles[j])) for i, j in pairs]
assert len(hitting) == len(set(hitting)) == 231
assert all(not set(t).isdisjoint(hitting) for t in triangles)
print('VERIFIED vertices=3125 edges=14856 triangles=288 '
      'primitive_types=2 isolated_triangles=174 overlapping_pairs=57 '
      'shared_one_vertex=9 shared_two_vertices=48 packing=231 transversal=231')
