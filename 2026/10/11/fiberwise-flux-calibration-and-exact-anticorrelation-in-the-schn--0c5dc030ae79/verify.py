from fractions import Fraction as F

a = F(2, 5)
b = F(3, 7)
u = F(11, 13)
v = F(5, 9)

udot = a-u+u*u*v
vdot = b-u*u*v
Sdot = udot+vdot
beta = a+b

assert Sdot == beta-u
assert u-beta == -Sdot

# Covariance algebra under Cov(S,u)=0.
varS = F(7, 5)
varU = F(11, 8)
covSU = F(0)

covUV = covSU-varU
varV = varS+varU-2*covSU
assert covUV == -varU
assert varV == varS+varU

# Unique positive equilibrium.
ue = beta
ve = b/(beta*beta)
assert a-ue+ue*ue*ve == 0
assert b-ue*ue*ve == 0

print("VERIFY_OK")
