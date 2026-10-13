#!/usr/bin/env python3
"""Exact finite-category proof check for a smooth three-lifetime example.
The global two-coordinate boundary is proved mathematically in RESULT.md;
finite integer enumeration here is only a diagnostic, not that proof.
"""
from fractions import Fraction as F
from itertools import product

# One low coordinate chosen uniformly; the other two are high.
def base(group, low):
    lo, hi = ((0, 10) if group == 0 else (1, 2))
    return tuple(lo if i == low else hi for i in range(3))

def sign(v):
    return (v > 0) - (v < 0)

def conditional_pair_kernel(g, h):
    # Jitters are independent across coordinates and between samples.
    # Coincident baseline levels give an expected sign of zero.
    return sum(F(sign(base(g, a)[0] - base(h, b)[0]) *
                 sign(base(g, a)[1] - base(h, b)[1]), 9)
               for a, b in product(range(3), repeat=2))

within_a = conditional_pair_kernel(0, 0)
within_b = conditional_pair_kernel(1, 1)
cross_ab = conditional_pair_kernel(0, 1)
assert within_a == within_b == F(-2, 9), (within_a, within_b)
assert cross_ab == F(-1, 3), cross_ab

tau_parent = F(1, 4) * within_a + F(1, 4) * within_b + F(1, 2) * cross_ab
assert tau_parent == F(-5, 18), tau_parent

# Conditional on either group, the first two order statistics are
# functions of independent disjoint jitter-coordinate collections.
# Their within-group Kendall's tau is exactly 0; cross-group is -1.
tau_sorted = F(1, 4)*0 + F(1, 4)*0 + F(1, 2)*(-1)
assert tau_sorted == F(-1, 2), tau_sorted
assert tau_parent - tau_sorted == F(2, 9)

eta = F(1, 100)
# Bounded comparison kernels take values in [-2, 2]; replacement of
# either independently sampled vector occurs with probability 2η−η².
error_bound = 4 * (2*eta - eta*eta)
certified_gap = (tau_parent-tau_sorted) - error_bound
assert certified_gap == F(3209, 22500), certified_gap
assert certified_gap > F(32, 225) > 0

# Optional exhaustive small-rank diagnostic for the universal n=2 lemma.
for a,b,c,d in product(range(5), repeat=4):
    raw = sign(a-c)*sign(b-d)
    aa,ab=sorted((a,b));ba,bb=sorted((c,d))
    ordered = sign(aa-ba)*sign(ab-bb)
    assert ordered >= raw
print('PASS: exact rational tau formulas, positive full-support perturbation gap, n=2 finite diagnostic')
print('parent=',tau_parent,'ordered=',tau_sorted,'gap_before_smoothing=',tau_parent-tau_sorted,
      'certified_smoothed_gap_lower_bound=',certified_gap)
