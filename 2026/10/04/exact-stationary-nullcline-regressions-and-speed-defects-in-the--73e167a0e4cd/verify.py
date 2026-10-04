from fractions import Fraction as F

# Abstract conditional-regression variance identity.
EA = F(7, 3)
EB = EA
EB2 = F(29, 5)
EAB = EB2
EA2 = F(41, 6)

residual_sq = EA2 - 2 * EAB + EB2
var_gap = (EA2 - EA * EA) - (EB2 - EB * EB)
assert residual_sq == var_gap

# Rate-tilt algebra at exact positive rational values.
q = F(7, 5)
delta = F(11, 9)
wdot = q * delta
assert q * delta * delta == wdot * wdot / q

# Standard conversion q = phi/tau.
phi = F(3, 7)
tau = F(5, 4)
q2 = phi / tau
wdot2 = F(13, 8)
left_numerator = wdot2 * wdot2 / q2
right_numerator = tau * wdot2 * wdot2 / phi
assert left_numerator == right_numerator

# Denominator conversion E[q] = phi E[1/tau] at one exact sample.
inv_tau = 1 / tau
assert q2 == phi * inv_tau

print("VERIFY_OK")
