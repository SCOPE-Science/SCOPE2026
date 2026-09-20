#!/usr/bin/env python3
"""Numerical checks for the seam-mass identities in RESULT.md.

Uses only Python's standard library.  It checks the closed formula against
the right-angled-hexagon cosine law on deterministic sample triples and
tests the fixed-total extremal inequalities on a small deterministic grid.
"""

import math

def seam_mass_from_hexagon(lengths):
    a = [x / 2.0 for x in lengths]
    d = []
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        c = (math.cosh(a[i]) + math.cosh(a[j]) * math.cosh(a[k])) / (
            math.sinh(a[j]) * math.sinh(a[k])
        )
        di = math.acosh(c)
        d.append(di)
    return 2.0 * sum(math.log(1.0 / math.tanh(di / 2.0)) for di in d)

def seam_mass_closed(lengths):
    L = sum(lengths)
    s = L / 4.0
    den = math.cosh(s) + sum(math.cosh(x - s) for x in lengths)
    return math.log(4.0 * math.cosh(s) ** 3 / den)

def seam_mass_max(L):
    return 3.0 * (math.log(math.cosh(L / 4.0)) - math.log(math.cosh(L / 12.0)))

samples = [
    (0.4, 0.7, 1.3),
    (1.0, 1.0, 1.0),
    (0.2, 3.0, 4.7),
    (5.0, 2.0, 0.8),
    (8.0, 8.0, 1.0),
]

for triple in samples:
    a = seam_mass_from_hexagon(triple)
    b = seam_mass_closed(triple)
    assert abs(a - b) < 5e-12, (triple, a, b)

for L in (0.6, 1.5, 3.0, 8.0, 20.0):
    mmax = seam_mass_max(L)
    assert 0.0 < mmax < L / 2.0
    for i in range(1, 20):
        for j in range(1, 20 - i):
            x = L * i / 20.0
            y = L * j / 20.0
            z = L - x - y
            if z <= 0:
                continue
            m = seam_mass_closed((x, y, z))
            assert m > 0.0
            assert m <= mmax + 2e-12, (L, x, y, z, m, mmax)

print("verified: direct/closed formulas agree on samples")
print("verified: 0 < seam mass <= equal-cuff maximum on deterministic grids")
print("verified: equal-cuff maximum < L/2 on tested totals")
