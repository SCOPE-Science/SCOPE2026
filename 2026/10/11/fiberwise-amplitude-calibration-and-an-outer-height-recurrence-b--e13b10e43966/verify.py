from fractions import Fraction as F

# Pointwise algebra at exact rational parameters and state values.
x = F(7, 5)
y = F(11, 6)
z = F(13, 7)
alpha = F(9, 4)
lam = F(5, 3)

xdot = y
ydot = x*(1-z) - lam*y
zdot = -alpha*z + x*x
assert zdot == x*x - alpha*z
assert xdot*y + x*ydot == y*y + x*x - lam*x*y - x*x*z

# Abstract stationary moment substitution.
Ez = F(5, 4)
Ez2 = F(19, 10)
Exy = F(0)
Ex2 = alpha*Ez
Ex2z = alpha*Ez2
Ey2 = -Ex2 + lam*Exy + Ex2z
assert Ey2 == alpha*(Ez2-Ez)

# Projection algebra for A=x^2, B=alpha*z, with E[A|z]=B.
EB = F(7, 5)
EB2 = F(23, 8)
EA = EB
EAB = EB2
EA2 = F(31, 7)
varA = EA2 - EA*EA
varB = EB2 - EB*EB
res2 = EA2 - 2*EAB + EB2
assert varA - varB == res2

# Cov(A,z)=alpha Var(z) follows from E[A z]=alpha E[z^2].
Ez = F(4, 5)
Ez2 = F(17, 20)
EA = alpha*Ez
EAz = alpha*Ez2
covAz = EAz - EA*Ez
varz = Ez2 - Ez*Ez
assert covAz == alpha*varz

print('VERIFY_OK')
