#!/usr/bin/env python3
"""Exact symbolic checks for the support-function identities in RESULT.md."""
import sympy as s

sqrt = s.sqrt
c = s.Rational(6, 1) / sqrt(61)
t = s.Rational(5, 1) / sqrt(61)
lam = s.Rational(9, 1) / sqrt(61)

# Candidate-angle identities: h(x)=3 cos(beta), h(beta)=2 cos(beta)+3 sin(beta).
assert s.simplify(3*c/2 - lam) == 0
assert s.simplify((2*c + 3*t)/3 - lam) == 0
assert s.simplify(s.tan(s.atan(s.Rational(5, 6)) - s.pi/4) + s.Rational(1, 11)) == 0

# With y=beta-pi/4, cos(y)=11/sqrt(122), sin(y)=-1/sqrt(122).
cy = s.Rational(11, 1) / sqrt(122)
sy = -s.Rational(1, 1) / sqrt(122)
hy = s.simplify(2*cy - sy)
assert s.simplify(hy - 23/sqrt(122)) == 0

# Three breakpoint ratios: the first two have reciprocal lambda; the third is strictly smaller.
r0 = s.simplify(2 / (18/sqrt(61)))
r1 = s.simplify(3 / (27/sqrt(61)))
r2 = s.simplify((3*sqrt(2)/2) / (23/sqrt(122)))
assert s.simplify(r0 - 1/lam) == 0
assert s.simplify(r1 - 1/lam) == 0
assert s.simplify(r2 - 3*sqrt(61)/23) == 0
assert 3*61 < 9*23

# Strict interval-separation constants exceed the claimed minimum.
assert 2 > s.Rational(81, 61)                    # sqrt(2) > 9/sqrt(61)
assert s.Rational(9, 4) > s.Rational(81, 61)    # 3/2 > 9/sqrt(61)
assert s.Rational(25, 18) > s.Rational(81, 61)  # 5/(3sqrt(2)) > 9/sqrt(61)
assert s.Rational(13, 9) > s.Rational(81, 61)   # sqrt(13)/3 > 9/sqrt(61)

print("HEXAGON_CHIRALITY_CHECK_OK")
print("candidate_angle_identities=passed")
print("three_breakpoint_ratios=passed")
print("strict_interval_comparisons=passed")
