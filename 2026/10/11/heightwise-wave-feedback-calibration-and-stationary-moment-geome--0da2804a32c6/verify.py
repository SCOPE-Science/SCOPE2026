from fractions import Fraction as F

# Pointwise cancellation for the x,w subsystem.
sigma = F(3, 2)
b = F(7, 10)
r = F(26)
s = F(5, 4)
x = F(7, 5)
y = F(-4, 3)
z = F(9, 7)
w = F(2, 9)

xdot = sigma*(y-x) + s*w
wdot = -x - sigma*w
lhs = x*xdot + s*w*wdot
rhs = sigma*x*y - sigma*x*x - sigma*s*w*w
assert lhs == rhs

# Stationary y^2/z^2 elimination algebra.
m = F(11, 3)
Exy = b*m
Ez2 = F(19, 4)
Exyz = b*Ez2
Ey2 = r*Exy - Exyz
assert Ey2 + b*Ez2 == b*r*m
varz = Ez2 - m*m
assert Ey2 + b*varz == b*m*(r-m)

# Abstract regression algebra for xy = b z + R, E[R]=0, Cov(z,R)=0.
EZ = F(2, 5)
EZ2 = F(13, 11)
ER = F(0)
ER2 = F(5, 17)
EZR = F(0)
varZ = EZ2 - EZ*EZ
EQ = b*EZ + ER
EQ2 = b*b*EZ2 + 2*b*EZR + ER2
varQ = EQ2 - EQ*EQ
assert varQ == b*b*varZ + ER2
cov = (b*EZ2 + EZR) - EZ*EQ
assert cov == b*varZ

# Standard parameter coefficients.
sigma0 = F(1)
b0 = F(7,10)
r0 = F(26)
s0 = F(3,2)
assert b0*r0 == F(91,5)
assert s0 == F(3,2)
assert sigma0 == 1

print("VERIFY_OK")
