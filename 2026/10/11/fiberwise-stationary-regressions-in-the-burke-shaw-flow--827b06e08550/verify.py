from fractions import Fraction as F

# Exact residual identities at a rational test point.
a = F(7, 3)
k = F(5, 2)
g = F(11, 4)
d = F(13, 6)
x = F(17, 9)
y = F(-8, 7)
z = F(19, 10)

xdot = -a*(x+y)
ydot = -y-k*x*z
zdot = g*x*y+d

assert y+x == -xdot/a
assert x*z + y/k == -ydot/k
assert x*y + d/g == zdot/g

# Abstract orthogonal regression variance/covariance algebra.
EB = F(2, 5)
EB2 = F(17, 13)
ER = F(0)
ER2 = F(7, 11)
EBR = F(0)

varB = EB2-EB*EB
varBR = (EB2+2*EBR+ER2) - (EB+ER)**2
assert varBR == varB + ER2

cov_B_BR = (EB2+EBR) - EB*(EB+ER)
assert cov_B_BR == varB

# Classical bounded-chaos parameter ratio.
a0 = k0 = g0 = F(10)
d0 = F(4272, 1000)
assert d0/g0 == F(267, 625)  # 0.4272

# Equilibria p_±=(±sqrt(d/g),∓sqrt(d/g),1/k) are checked
# algebraically through q^2=d/g, avoiding irrational arithmetic.
q2 = d0/g0
z0 = F(1, 1)/k0

# For x=q, y=-q:
# xdot=-a(q-q)=0
# ydot=q-k*q*(1/k)=0
# zdot=-g*q^2+d=0
assert F(0) == F(0)
assert F(1)-k0*z0 == 0
assert -g0*q2+d0 == 0

print("VERIFY_OK")
