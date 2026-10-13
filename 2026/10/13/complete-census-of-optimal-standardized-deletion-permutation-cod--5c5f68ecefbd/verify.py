#!/usr/bin/env python3
"""Exact finite classification of standardized single-deletion permutation codes.

Requires only Python's standard library. Run next to representatives.csv.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
import csv

N = 5
P = list(permutations(range(N)))
assert len(P) == 120
index = {p: j for j, p in enumerate(P)}
Q = list(permutations(range(N - 1)))
qindex = {p: j for j, p in enumerate(Q)}


def standardize(values):
    rank = {value: i for i, value in enumerate(sorted(values))}
    return tuple(rank[value] for value in values)


def deletion_shadow(p):
    return frozenset(standardize(p[:j] + p[j + 1:]) for j in range(N))


shadows = [deletion_shadow(p) for p in P]
assert len(set(shadows)) == len(shadows)
shadow_masks = [sum(1 << qindex[q] for q in s) for s in shadows]
assert set().union(*shadows) == set(Q)
assert sum(len(s) for s in shadows) == 408

# A separate representation of admissibility: two codewords are compatible
# precisely if their descendant SETS have empty intersection.
compatible = [[not bool(shadows[i] & shadows[j])
               for j in range(len(P))] for i in range(len(P))]


def enumerate_k(k):
    solutions = []
    visited = Counter()

    def search(candidates, code):
        level = len(code)
        visited[level] += 1
        if level == k:
            solutions.append(tuple(code))
            return
        needed = k - level
        if len(candidates) < needed:
            return
        for offset, vertex in enumerate(candidates):
            if len(candidates) - offset < needed:
                break
            survivors = [v for v in candidates[offset + 1:]
                         if compatible[vertex][v]]
            if len(survivors) + 1 >= needed:
                search(survivors, code + [vertex])

    search(list(range(len(P))), [])
    return solutions, visited


optimal, counts8 = enumerate_k(8)
assert len(optimal) == 1568
nine, counts9 = enumerate_k(9)
assert not nine
assert tuple(sorted(counts9.items())) == (
    (0, 1), (1, 98), (2, 2732), (3, 24318), (4, 62064),
    (5, 37398), (6, 4843), (7, 62)
)


def transform(p, bits):
    if bits & 1:  # Reverse coordinate order.
        p = p[::-1]
    if bits & 2:  # Reverse value order.
        p = tuple(N - 1 - x for x in p)
    if bits & 4:  # Invert the permutation.
        p = tuple(p.index(x) for x in range(N))
    return p


def images(code):
    return {tuple(sorted(index[transform(P[i], t)] for i in code))
            for t in range(8)}

# Independently verify that all claimed operations respect the error model.
for t in range(8):
    permutation = [index[transform(p, t)] for p in P]
    assert len(set(permutation)) == len(P)
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            assert compatible[i][j] == compatible[permutation[i]][permutation[j]]

optimal_set = set(optimal)
seen = set()
classes = []
class_sizes = Counter()
for code in optimal:
    if code in seen:
        continue
    orbit = images(code)
    assert orbit <= optimal_set
    seen.update(orbit)
    representative = min(orbit)
    classes.append((representative, len(orbit)))
    class_sizes[len(orbit)] += 1
assert seen == optimal_set
classes.sort()
assert class_sizes == Counter({8: 174, 4: 43, 2: 1, 1: 2})
assert len(classes) == 220

rows = []
with (Path(__file__).resolve().parent / 'representatives.csv').open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == ['orbit_size', 'codeword_indices_0_based']
    for row in reader:
        rows.append((tuple(map(int, row['codeword_indices_0_based'].split(' '))),
                     int(row['orbit_size'])))
assert rows == classes

# Compare with the double-signature construction of Gabrys et al.
def vt_pair(p):
    inverse = tuple(p.index(x) for x in range(N))
    signature = lambda v: sum(i for i in range(1, N) if v[i] > v[i - 1]) % N
    return (signature(p), signature(inverse))

syndrome_classes = {}
for i, p in enumerate(P):
    syndrome_classes.setdefault(vt_pair(p), []).append(i)
max_vt = max(len(v) for v in syndrome_classes.values())
assert max_vt == 8
max_vt_classes = [tuple(v) for v in syndrome_classes.values() if len(v) == 8]
assert len(max_vt_classes) == 1
assert max_vt_classes[0] in optimal_set

monotone_types = Counter((0 in code, 119 in code) for code in optimal)
assert monotone_types == Counter({(True, True): 1100,
                                 (True, False): 216,
                                 (False, True): 216,
                                 (False, False): 36})
print('VERIFY_OK rank_del_S5=8 labeled_optima=1568 classes=220 '
      'orbits=1:2,2:1,4:43,8:174 double_signature_optima=1 '
      'without_both_monotones=36 exhaustive_nine=0')
