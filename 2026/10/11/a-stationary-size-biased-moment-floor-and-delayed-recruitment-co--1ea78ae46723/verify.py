from fractions import Fraction as F

p = F(8)
delta = F(2)

EX = F(5, 3)
VarX = F(7, 11)
EX2 = VarX + EX*EX

EB = delta*EX/p
EXB = delta*EX2/p
CovXB = EXB - EX*EB
assert CovXB == delta*VarX/p

# A compatible variance test for the Cauchy consequence.
VarB = F(5, 17)
lower = (delta/p)**2 * VarX
assert VarB >= lower
assert CovXB*CovXB <= VarX*VarB

# Equilibrium exponential relation is encoded exactly by q = p/delta.
q = p/delta
assert q == 4
# If K = log(q)/a, then exp(-aK) = 1/q = delta/p.
assert F(1, 1) / q == delta/p

print("VERIFY_OK")
