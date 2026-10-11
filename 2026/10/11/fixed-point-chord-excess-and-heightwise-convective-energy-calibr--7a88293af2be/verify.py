from fractions import Fraction as F

a = F(2)
b = F(67, 10)
x = F(3, 7)
y = F(-5, 4)
z = F(11, 6)

xdot = -a*x + b*y - y*z
ydot = x
zdot = -z + y*y

# Pointwise identities.
assert zdot == y*y - z
dxy = xdot*y + x*ydot
assert dxy == x*x - a*x*y + b*y*y - y*y*z

# Stationary chord algebra at exact rational test moments.
m = F(9, 5)
Ex2 = F(13, 11)
Ez2 = b*m + Ex2
varz = Ez2 - m*m
assert varz == m*(b-m) + Ex2

# Abstract orthogonal residual algebra:
# Y2 = Z + R, E[R]=0, Cov(Z,R)=0.
EZ = F(2, 3)
EZ2 = F(17, 10)
ER = F(0)
ER2 = F(7, 13)
EZR = F(0)

EY2 = EZ + ER
EY2sq = EZ2 + 2*EZR + ER2
varY2 = EY2sq - EY2*EY2
varZ = EZ2 - EZ*EZ
assert varY2 == varZ + ER2

covZY2 = (EZ2 + EZR) - EZ*EY2
assert covZY2 == varZ

# Nonzero equilibrium relations for b > 0 use y^2=b, z=b, x=0.
assert b > 0
ystar_sq = b
zstar = b
assert -zstar + ystar_sq == 0
assert b - zstar == 0

print("VERIFY_OK")
