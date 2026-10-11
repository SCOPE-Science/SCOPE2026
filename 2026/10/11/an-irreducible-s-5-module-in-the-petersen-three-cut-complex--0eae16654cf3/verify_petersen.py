#!/usr/bin/env python3
"""Exact finite certificate for the Petersen graph three-cut complex.

No third-party dependencies.  Simplices use bit masks indexed by the
lexicographic two-element subsets of {0,1,2,3,4}.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict

V = tuple(combinations(range(5), 2))
N = len(V)
FULL = (1 << N) - 1
ADJ = set()
for i, a in enumerate(V):
    for j, b in enumerate(V):
        if i < j and set(a).isdisjoint(b):
            ADJ.add((i, j))
assert N == 10 and len(ADJ) == 15

# A three-vertex induced subgraph is connected precisely when it
# has at least two edges: the Petersen graph is triangle-free.
def num_edges(triple):
    return sum((min(i, j), max(i, j)) in ADJ
               for i, j in combinations(triple, 2))

FACETS = set()
for t in combinations(range(N), 3):
    if num_edges(t) < 2:
        t_mask = sum(1 << i for i in t)
        FACETS.add(FULL ^ t_mask)
assert len(FACETS) == 90

FACES = {mask for mask in range(1, FULL + 1)
         if any(mask & facet == mask for facet in FACETS)}
assert len(FACES) == 937
face_vector = tuple(sum(m.bit_count() == k for m in FACES) for k in range(1, 8))
assert face_vector == (10, 45, 120, 210, 252, 210, 90)
assert set(m for m in FACES if m.bit_count() == 7) == FACETS

# Staged element-toggle matching. At each stage i, the pairs (s,s+{i})
# are disjoint, so the order of iteration within a stage cannot matter.
remaining = set(FACES)
matched = []
for i in range(N):
    bit = 1 << i
    for s in sorted(remaining):
        if s & bit:
            continue
        t = s | bit
        if t in remaining:
            remaining.remove(s)
            remaining.remove(t)
            matched.append((s, t))
assert len(matched) == 465
assert Counter(m.bit_count() - 1 for m in remaining) == {0: 1, 6: 6}
assert len(set(x for p in matched for x in p)) == 2 * len(matched)

# Full Hasse diagram, oriented downward on unmatched covers and upward
# on matched covers. A topological sort is an exact acyclicity witness.
match_up = {lo: hi for lo, hi in matched}
out = {m: [] for m in FACES}
indegree = {m: 0 for m in FACES}
hasse_count = 0
for hi in FACES:
    if hi.bit_count() < 2:
        continue
    bits = [1 << i for i in range(N) if hi & (1 << i)]
    for bit in bits:
        lo = hi ^ bit
        assert lo in FACES
        hasse_count += 1
        u, v = (lo, hi) if match_up.get(lo) == hi else (hi, lo)
        out[u].append(v)
        indegree[v] += 1
assert hasse_count == sum((k + 1) * face_vector[k] for k in range(1, 7))
queue = [m for m in FACES if indegree[m] == 0]
reached = 0
while queue:
    u = queue.pop()
    reached += 1
    for v in out[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert reached == len(FACES), (reached, len(FACES))

# The natural S5 action on the ten 2-subsets preserves the complex.
index = {v: i for i, v in enumerate(V)}
def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(5):
        if i not in seen:
            j = i
            n = 0
            while j not in seen:
                seen.add(j)
                n += 1
                j = p[j]
            lengths.append(n)
    return tuple(sorted(lengths, reverse=True))

def induced_sign(s, perm10):
    seq = [perm10[i] for i in range(N) if (s >> i) & 1]
    inversions = sum(a > b for j, a in enumerate(seq) for b in seq[j + 1:])
    return -1 if inversions & 1 else 1

chi_classes = defaultdict(set)
counts = Counter()
for p in permutations(range(5)):
    perm10 = [index[tuple(sorted((p[a], p[b])))] for a, b in V]
    assert len(set(perm10)) == 10
    assert all((min(perm10[i], perm10[j]), max(perm10[i], perm10[j])) in ADJ
               for i, j in ADJ)
    # Signed fixed-face trace on simplicial chains gives Lefschetz number.
    lefschetz = 0
    for s in FACES:
        image = sum(1 << perm10[i] for i in range(N) if (s >> i) & 1)
        if image == s:
            lefschetz += (-1 if (s.bit_count() & 1) == 0 else 1) * induced_sign(s, perm10)
    top_trace = lefschetz - 1  # only H_0 and H_6; both even-dimensional
    fix = sum(i == p[i] for i in range(5))
    fix_sq = sum(i == p[p[i]] for i in range(5))
    ext_square_trace = ((fix - 1)**2 - (fix_sq - 1)) // 2
    assert top_trace == ext_square_trace, (p, top_trace, ext_square_trace)
    c = cycle_type(p)
    chi_classes[c].add(top_trace)
    counts[c] += 1
assert all(len(v) == 1 for v in chi_classes.values())
expected = {(1, 1, 1, 1, 1): 6, (2, 1, 1, 1): 0,
            (2, 2, 1): -2, (3, 1, 1): 0,
            (3, 2): 0, (4, 1): 0, (5,): 1}
assert {k: next(iter(v)) for k, v in chi_classes.items()} == expected
assert sum(counts[t] * expected[t]**2 for t in expected) == 120
assert sum(counts[t] for t in expected) == 120

print('vertices=10 edges=15 facets=90 faces=937')
print('face_vector=', face_vector)
print('hasse_covers=', hasse_count)
print('matched_pairs=465 critical_cells={0:1,6:6} acyclic=YES')
for typ in sorted(expected):
    print('class', typ, 'size', counts[typ], 'trace', expected[typ])
print('S5_characters_checked=120 irreducibility_inner_product=1')
print('VERIFY_OK')
