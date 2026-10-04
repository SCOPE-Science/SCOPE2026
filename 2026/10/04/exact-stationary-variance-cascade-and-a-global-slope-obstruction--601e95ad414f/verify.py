from fractions import Fraction as F

# Residual-variance algebra with symbolic placeholders represented by exact samples
# satisfying E[A]=E[B] and E[AB]=E[B^2].
EA = F(7, 5)
EB = EA
EB2 = F(13, 4)
EAB = EB2
EA2 = F(19, 4)

lhs = EA2 - 2 * EAB + EB2
varA = EA2 - EA * EA
varB = EB2 - EB * EB
rhs = varA - varB
assert lhs == rhs

# Hill exponent h=2.
# R'(s) magnitude / alpha = 2s/(1+s^2)^2.
# Derivative has numerator proportional to 1-3s^2, so the positive critical point has s^2=1/3.
s2 = F(1, 3)
assert 1 - 3 * s2 == 0

# At s=1/sqrt(3):
# L/alpha = 2/sqrt(3) / (1+1/3)^2 = 9/(8 sqrt(3)).
# Verify the squared coefficient exactly.
coeff_sq = F(81, 64) / 3
assert coeff_sq == F(27, 64)

# Threshold alpha_c = 1/(L/alpha) = 8 sqrt(3)/9.
# Verify alpha_c^2 = 64/27.
alpha_c_sq = F(64, 27)
assert coeff_sq * alpha_c_sq == 1

print("VERIFY_OK")
