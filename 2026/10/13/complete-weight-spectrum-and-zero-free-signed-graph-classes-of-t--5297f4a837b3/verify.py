#!/usr/bin/env python3
"""Exact standalone proof checker for the ternary five-variable quadratic toric code.

Uses integer arithmetic only.  No external files or packages are needed.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

NVAR = 5
EDGES = tuple(combinations(range(NVAR), 2))
EDGE_INDEX = {edge: i for i, edge in enumerate(EDGES)}
POWERS = tuple(3**i for i in range(len(EDGES)))
TOTAL = 3**len(EDGES)
SIGNS = tuple(product((-1, 1), repeat=NVAR))
ROWS = tuple(tuple(x[i]*x[j] for i, j in EDGES) for x in SIGNS)
EXPECTED = {0: 1, 8: 120, 12: 720, 14: 2240, 16: 4500, 18: 8000,
            20: 10992, 22: 12384, 24: 10320, 26: 6240, 28: 2880,
            30: 480, 32: 172}
EXPECTED_ORBITS = {0: 1, 8: 1, 12: 3, 14: 2, 16: 7, 18: 5, 20: 11,
                   22: 8, 24: 11, 26: 5, 28: 4, 30: 1, 32: 3}

def coeffs(index):
    return tuple((index//p) % 3 for p in POWERS)

def direct_weight(a):
    return sum(sum(t*v for t, v in zip(a, row)) % 3 != 0 for row in ROWS)

def split_weight(a):
    """Independently count zeros by the last-variable 2-point fiber formula."""
    z = 0
    for y in product((-1, 1), repeat=4):
        g = sum(a[EDGE_INDEX[(i, j)]]*y[i]*y[j]
                for i, j in combinations(range(4), 2)) % 3
        h = sum(a[EDGE_INDEX[(i, 4)]]*y[i] for i in range(4)) % 3
        z += 2 if g == 0 and h == 0 else (1 if g != 0 and h != 0 else 0)
    return 32-z

# Check that the evaluation map has full rank by column character orthogonality:
# independent degree-two sign characters on the Boolean cube.
for i, row_i in enumerate(zip(*ROWS)):
    for j, row_j in enumerate(zip(*ROWS)):
        assert sum(a*b for a, b in zip(row_i, row_j)) == (32 if i == j else 0)

coef = tuple(coeffs(i) for i in range(TOTAL))
weights = []
spectrum = Counter()
sparse_spectrum = Counter()
for a in coef:
    w = direct_weight(a)
    assert w == split_weight(a)
    weights.append(w)
    spectrum[w] += 1
    sparse_spectrum[(sum(t != 0 for t in a), w)] += 1
assert dict(spectrum) == EXPECTED
assert len(weights) == TOTAL
assert sum(spectrum.values()) == TOTAL
assert spectrum[32] == 172
assert {k for k,w in enumerate(weights) if w == 32 and sum(t != 0 for t in coef[k]) not in (1,4,10)} == set()
assert sum(v for (n,w),v in sparse_spectrum.items() if w == 32 and n == 1) == 20
assert sum(v for (n,w),v in sparse_spectrum.items() if w == 32 and n == 4) == 120
assert sum(v for (n,w),v in sparse_spectrum.items() if w == 32 and n == 10) == 32

# The intrinsic switching group is S_5 x (C_2)^4 x C_2 in size (not as an
# abstract direct product), acting through vertex permutations, sign switches,
# and coefficient scaling. Enumerate its orbits by elementary generators.
SWAPS = []
for v in range(4):
    perm = list(range(5))
    perm[v], perm[v+1] = perm[v+1], perm[v]
    SWAPS.append(tuple(EDGE_INDEX[tuple(sorted((perm[i], perm[j])))]
                       for i, j in EDGES))

def neighbors(a):
    for p in SWAPS:
        yield sum(a[j]*POWERS[p[j]] for j in range(10))
    for v in range(4):
        yield sum(((3-a[j]) % 3 if v in EDGES[j] else a[j])*POWERS[j]
                  for j in range(10))
    yield sum(((-a[j]) % 3)*POWERS[j] for j in range(10))

seen = bytearray(TOTAL)
orbit_summaries = []
for start in range(TOTAL):
    if seen[start]:
        continue
    orbit = [start]
    seen[start] = 1
    for v in orbit:
        for w in neighbors(coef[v]):
            assert weights[w] == weights[v]
            if not seen[w]:
                seen[w] = 1
                orbit.append(w)
    orbit_summaries.append((start, len(orbit), weights[start]))
assert all(seen)
assert len(orbit_summaries) == 62
assert sum(n for _,n,_ in orbit_summaries) == TOTAL
orbit_counts = Counter(w for _, _, w in orbit_summaries)
assert dict(orbit_counts) == EXPECTED_ORBITS
assert sorted(n for _,n,w in orbit_summaries if w == 32) == [20,32,120]
assert {sum(a!=0 for a in coef[k]): n
        for k,n,w in orbit_summaries if w==32} == {1:20,4:120,10:32}

# Independent Burnside count: the coefficient action is a signed permutation
# of ten edges.  Each edge cycle gives one free F3-coordinate exactly when
# the product of its signs along that cycle equals +1.
fixed_sum = 0
group_size = 0
for pi in permutations(range(5)):
    edge_perm = tuple(EDGE_INDEX[tuple(sorted((pi[i],pi[j])))]
                      for i,j in EDGES)
    for switch in product((0,1), repeat=4):
        switch = switch + (0,)
        for scalar in (-1,1):
            signs = tuple(scalar * ((-1)**(switch[i]+switch[j]))
                          for i,j in EDGES)
            visited = set()
            positive_cycles = 0
            for edge in range(10):
                if edge in visited: continue
                v = edge
                cycle_sign = 1
                while v not in visited:
                    visited.add(v)
                    cycle_sign *= signs[v]
                    v = edge_perm[v]
                assert v == edge
                if cycle_sign == 1: positive_cycles += 1
            fixed_sum += 3**positive_cycles
            group_size += 1
assert group_size == 3840
assert fixed_sum == 62*group_size
print('VERIFY_OK')
print('weight spectrum', sorted(spectrum.items()))
print('orbit counts by weight', sorted(orbit_counts.items()))
print('full support orbit sizes', sorted(n for _,n,w in orbit_summaries if w==32))
print('Burnside fixed sum', fixed_sum)
