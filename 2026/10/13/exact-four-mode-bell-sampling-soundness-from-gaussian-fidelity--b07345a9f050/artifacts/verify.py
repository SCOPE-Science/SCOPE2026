#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

# Normalized Walsh characters on the four-cube have amplitude 1/4.
# The bridge zero sector is indexed by subsets T of size 2.
Ts = list(combinations(range(4), 2))
assert len(Ts) == 6

# e = |empty> + |full>.  For |T|=2, chi_T(empty)=chi_T(full)=1/4.
coeff = Fraction(1, 2)
kernel_norm_sq = sum(coeff * coeff for _ in Ts)
assert kernel_norm_sq == Fraction(3, 2)
e_norm_sq = Fraction(2, 1)
reject_norm_sq = e_norm_sq - kernel_norm_sq
assert reject_norm_sq == Fraction(1, 2)

# Cross-sector coefficient squared is f(1-f).
for f in [Fraction(1,2), Fraction(3,5), Fraction(3,4), Fraction(9,10), Fraction(1,1)]:
    r = f * (1-f) * reject_norm_sq
    assert r == f * (1-f) / 2

# Monotonicity of h(x)=x(1-x)/2 on [0,1/2].
vals = [Fraction(i, 20) for i in range(11)]
for x in vals:
    for y in vals:
        if x <= y <= Fraction(1,2):
            lhs = y*(1-y)/2 - x*(1-x)/2
            rhs = (y-x)*(1-x-y)/2
            assert lhs == rhs
            assert lhs >= 0

print('VERIFY_OK')
