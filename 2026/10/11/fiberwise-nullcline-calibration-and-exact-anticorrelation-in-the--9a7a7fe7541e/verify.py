from fractions import Fraction as F

# Exact algebra for the vector field.
a = F(7, 5)
b = F(11, 6)
x = F(13, 7)
y = F(17, 9)

xdot = a - (b + 1) * x + x * x * y
ydot = b * x - x * x * y
assert xdot + ydot == a - x

Fnull = ((b + 1) * x - a) / (x * x)
assert x * x * (y - Fnull) == xdot

# Abstract covariance/variance algebra.
# Let S have variance VS, x have variance VX, and Cov(x,S)=0.
VS = F(19, 8)
VX = F(23, 10)
CXS = F(0)
# y = S - x.
CXY = CXS - VX
VY = VS + VX - 2 * CXS
assert CXY == -VX
assert VY == VS + VX

# Standard parameter support threshold.
a0 = F(1)
b0 = F(3)
assert a0 / (b0 + 1) == F(1, 4)

print("VERIFY_OK")
