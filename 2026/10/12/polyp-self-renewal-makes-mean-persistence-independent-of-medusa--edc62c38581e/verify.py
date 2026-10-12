#!/usr/bin/env python3
from fractions import Fraction as F

a = F(3,20)
d = F(1,5000)
b = F(17,10)
c = F(61,625)
dstar = F(41,10000)
b1 = F(1,100000)
b2 = F(1,10000)
sigma1 = F(1,10)
sigma2 = F(1)

q = dstar / b
assert q*b == dstar

rP = a-d-sigma1*sigma1/2
polyp_mean = rP/b1
medusa_margin = c-dstar-sigma2*sigma2/2
weighted_lower = q*polyp_mean

assert rP == F(181,1250)
assert polyp_mean == F(14480)
assert medusa_margin == F(-813,2000)
assert weighted_lower == F(14842,425)

# Weighted drift after x=qP, y=M:
# A*x - kx*x^2 - ky*y^2
A = a-d+b*c/dstar
kx = b*b1/dstar
ky = b2
k = F(1,2)*min(kx,ky)
upper = A/k

assert A > 0
assert k > 0
assert upper > weighted_lower

# Source theorem is silent in this witness, while the new polyp condition holds.
assert rP > 0
assert medusa_margin < 0

print("VERIFY_OK")
print("q", q)
print("rP", rP, float(rP))
print("polyp_mean_lower", polyp_mean)
print("medusa_margin", medusa_margin, float(medusa_margin))
print("weighted_mean_lower", weighted_lower, float(weighted_lower))
print("weighted_mean_upper", upper, float(upper))
