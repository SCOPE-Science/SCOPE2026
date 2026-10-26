#!/usr/bin/env python3
"""Finite numerical checks for the stated polynomial-root census; not a proof."""
import math
import numpy as np

def expected_count(m, q):
    return sum(q > 1 / (4 * math.sin((2*j+1)*math.pi/(2*(m+1)))**2)
               for j in range(m+1))

def actual_count(m, q):
    coeff = np.zeros(m + 3)
    coeff[0], coeff[m], coeff[m+1], coeff[m+2] = 1.0, -q, 2*q, -q
    if m == 1 or m == 2:
        # The coefficients at 0 and m are disjoint for m>=1.
        pass
    roots = np.polynomial.polynomial.polyroots(coeff)
    return sum(abs(t) < 1.0 - 1e-7 for t in roots), min(abs(abs(t)-1) for t in roots)

for m in range(1, 15):
    for q in (0.001, 0.22, 0.251, 0.29, 0.5, 0.51, 0.77,
              1, 1.23, 2, 2.7, 5, 8, 10, 15):
        if q >= m + 1:
            continue
        found, gap = actual_count(m, q)
        if gap < 1e-7:  # Boundary roots are outside the analytic disk.
            continue
        assert found == expected_count(m, q), (m, q, found, expected_count(m, q))
print('Finite sample root-count checks passed for orders 1..14.')
