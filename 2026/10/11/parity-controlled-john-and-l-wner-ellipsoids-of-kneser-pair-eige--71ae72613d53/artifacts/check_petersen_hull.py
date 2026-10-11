#!/usr/bin/env python3
"""Independent numerical hull check for the ten-vertex Petersen eigenpolytope.
Requires numpy and scipy. Numerics do not replace the all-n exact proof.
"""
from itertools import combinations
from collections import Counter
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull

n = 5
E = list(combinations(range(n), 2))
B = np.array([[int(a in e) for e in E] for a in range(n)], dtype=float)
U = null_space(B)
hull = ConvexHull(U)
facets = {}
for eq in hull.equations:
    normal, bound = eq[:-1], eq[-1]
    signed = U @ normal + bound
    support = tuple(i for i, val in enumerate(signed) if abs(val) <= 1e-8)
    facets[support] = abs(bound) / np.linalg.norm(normal)
assert len(facets) == 22
assert Counter(map(len, facets)) == Counter({6: 10, 5: 12})
touch = sum(abs(dis - (18**-0.5)) < 1e-8 for dis in facets.values())
assert touch == 10
print('HULL_OK Petersen eigenpolytope facets=22 support_spectrum={6:10,5:12} closest_facets=10 inradius_squared=1/18')
