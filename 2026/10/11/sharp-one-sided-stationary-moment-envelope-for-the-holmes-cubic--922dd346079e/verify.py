from fractions import Fraction as F

# General invariant mean algebra at exact rational placeholders.
a = F(271, 100)
b = F(18, 100)
m = F(7, 20)
rho2 = a - b - 1
Ex3 = rho2 * m
assert a*m - Ex3 - b*m == m
assert rho2 == F(153, 100)

# Rational sharpness test with rho=1: choose a-b-1=1.
a0 = F(3)
b0 = F(1)
rho0 = F(1)
assert a0 - b0 - 1 == rho0*rho0

t = F(3, 7)
mean = t*rho0
Ex2 = t*rho0*rho0
Ex3_mix = t*rho0*rho0*rho0
var = Ex2 - mean*mean
assert Ex3_mix == rho0*rho0*mean
assert var == mean*(rho0-mean)

# Fixed points satisfy the Holmes map exactly whenever rho^2=a-b-1.
def T(x, y, a, b):
    return y, a*x - x*x*x - b*y
assert T(F(0), F(0), a0, b0) == (F(0), F(0))
assert T(rho0, rho0, a0, b0) == (rho0, rho0)
assert T(-rho0, -rho0, a0, b0) == (-rho0, -rho0)

# Off-diagonal equality candidates cannot remain in the equality carrier.
assert T(F(0), rho0, a0, b0) == (rho0, -b0*rho0)
assert T(rho0, F(0), a0, b0) == (F(0), (b0+1)*rho0)

print('VERIFY_OK')
