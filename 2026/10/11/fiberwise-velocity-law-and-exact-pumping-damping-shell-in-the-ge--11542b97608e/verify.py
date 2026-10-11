from fractions import Fraction as F

a = F(7, 5)
n = 2
x = F(11, 9)
y = F(3, 4)

xdot = y
ydot = -x + a*(1-y**(2*n))*y

Hdot = x*xdot + y*ydot
assert Hdot == a*y*y*(1-y**(2*n))
assert x - a*(1-y**(2*n))*y == -ydot

# Abstract consequences of E[y|x]=0.
Ey = F(0)
Exy = F(0)
Ex = F(5, 8)
cov = Exy - Ex*Ey
assert cov == 0

# Moment shell at exact test moment m2.
m2 = F(3, 5)
mhigh = m2
assert mhigh == m2
assert F(0) < m2 < F(1)

# Abstract orthogonal regression:
# x = G + R, E[R]=0, Cov(G,R)=0.
EG = F(2, 7)
EG2 = F(13, 11)
ER = F(0)
ER2 = F(5, 17)
EGR = F(0)
EX = EG + ER
EX2 = EG2 + 2*EGR + ER2
varX = EX2 - EX*EX
varG = EG2 - EG*EG
assert varX == varG + ER2

print("VERIFY_OK")
