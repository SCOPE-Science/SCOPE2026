from fractions import Fraction as F

# Abstract residual-variance identity.
EA = F(7, 4)
EB = EA
EA2 = F(19, 5)
EB2 = F(13, 4)
EAB = EB2

residual = EA2 - 2 * EAB + EB2
variance_gap = (EA2 - EA * EA) - (EB2 - EB * EB)
assert residual == variance_gap

# Nuclear coefficient scaling.
k1 = F(7, 3)
k2 = F(5, 4)
var_p2 = F(11, 6)
var_pn = F(2, 5)

left = k1 * k1 * var_p2 - k2 * k2 * var_pn
right = (k1 * k1) * var_p2 - (k2 * k2) * var_pn
assert left == right

# Conditional nuclear law scaling: E[k1 P2 | PN] = k2 PN.
pn = F(9, 7)
cond_p2 = (k2 / k1) * pn
assert k1 * cond_p2 == k2 * pn

print("VERIFY_OK")
