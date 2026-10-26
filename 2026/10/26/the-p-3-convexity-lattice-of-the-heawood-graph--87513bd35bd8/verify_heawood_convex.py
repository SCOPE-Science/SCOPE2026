#!/usr/bin/env python3
"""Independent finite check of the Fano-plane incidence-graph P3-convexity classification.

Python 3.9+, standard library only. No input files or packages required.
"""
from collections import Counter
from itertools import combinations

points = range(1, 8)
lines = sorted({tuple(sorted((a, b, a ^ b))) for a, b in combinations(points, 2)})
assert len(lines) == 7 and all(len(line) == 3 for line in lines)
assert all(sum(p in line for line in lines) == 3 for p in points)
assert all(sum(p in line and q in line for line in lines) == 1
           for p, q in combinations(points, 2))
assert all(len(set(line) & set(other)) == 1
           for line, other in combinations(lines, 2))

neighbors = [0] * 14
for line_id, line in enumerate(lines):
    for p in line:
        neighbors[p - 1] |= 1 << (7 + line_id)
        neighbors[7 + line_id] |= 1 << (p - 1)

# Direct graph-neighborhood definition; does not use the geometric proof's
# case analysis or its formula.
convex = set()
counts = Counter()
for selected in range(1 << 14):
    good = True
    for v in range(14):
        if not ((selected >> v) & 1) and (selected & neighbors[v]).bit_count() >= 2:
            good = False
            break
    if good:
        convex.add(selected)
        x, y = selected & 127, (selected >> 7) & 127
        counts[x.bit_count(), y.bit_count()] += 1

expected = {
    (0, 0): 1, (0, 1): 7,
    (1, 0): 7, (1, 1): 49, (1, 2): 21, (1, 3): 7,
    (2, 1): 21, (2, 2): 84, (2, 3): 42,
    (3, 1): 7, (3, 2): 42, (3, 3): 49,
    (4, 4): 28, (7, 7): 1,
}
assert counts == expected, (counts, expected)
assert len(convex) == 366

# Independent direct geometric closure criterion: a selected pair of
# points forces its joining line, and a selected pair of lines forces its
# meeting point. Independently check that this agrees with graph convexity.
join = {}
for a, b in combinations(points, 2):
    join[a, b] = next(j for j, line in enumerate(lines) if a in line and b in line)
meet = {}
for j, k in combinations(range(7), 2):
    meet[j, k] = next(p for p in points if p in lines[j] and p in lines[k])
for s in range(1 << 14):
    x, y = s & 127, (s >> 7) & 127
    geo = all((y >> join[a, b]) & 1 for a, b in join
              if ((x >> (a - 1)) & 1) and ((x >> (b - 1)) & 1))
    geo &= all((x >> (meet[j, k] - 1)) & 1 for j, k in meet
               if ((y >> j) & 1) and ((y >> k) & 1))
    assert geo == (s in convex), ('closure mismatch', s)

proper = convex - {(1 << 14) - 1}
maximal = [s for s in proper if not any(s != t and (s & t) == s for t in proper)]
max_counts = Counter(((s & 127).bit_count(), ((s >> 7) & 127).bit_count())
                     for s in maximal)
assert max_counts == {(3, 3): 21, (4, 4): 28}, max_counts
assert len(maximal) == 49

# Every six-vertex maximal proper set has three collinear selected points;
# every eight-vertex one has a selected line plus an outside point.
for s in maximal:
    x, y = s & 127, (s >> 7) & 127
    P = {p for p in points if (x >> (p - 1)) & 1}
    if len(P) == 3:
        assert sum(set(line) == P for line in lines) == 1
        assert len(P) == len([j for j in range(7) if y >> j & 1])
    else:
        assert len(P) == 4
        assert sum(set(line).issubset(P) for line in lines) == 1

univar = Counter()
for (p, q), val in counts.items():
    univar[p + q] += val
assert dict(sorted(univar.items())) == {
    0: 1, 1: 14, 2: 49, 3: 42, 4: 98,
    5: 84, 6: 49, 8: 28, 14: 1,
}
print('VERIFY_OK')
print('Fano lines:', ' '.join(''.join(map(str, line)) for line in lines))
print('Total convex sets:', len(convex))
print('Bivariate coefficients:', sorted(expected.items()))
print('Univariate coefficients:', sorted(univar.items()))
print('Maximal proper types:', sorted(max_counts.items()))
print('Geometric closure equivalence checked on all 16384 subsets.')
