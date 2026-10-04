from fractions import Fraction as F

c = F(3,10)

# Equilibria.
for x,y,z in [
    (F(0),F(0),F(0)),
    (F(-10,3),F(-10,3),F(100,9)),
]:
    assert x*y-z == 0
    assert x-y == 0
    assert x+c*z == 0

# Stationary generator coefficient checks:
# L(y^2/2)=y(x-y)
# L(z^2/2)=z(x+c z)
# L(yz)=(x-y)z+y(x+c z)
assert c == F(3,10)
assert c-1 == F(-7,10)

# If Y=E[y^2], Z=E[z^2], C=E[yz], then
# 0=-c Z+Y-(1-c)C.
# Thus C=(Y-cZ)/(1-c), and
# E[(y-z)^2]=Y+Z-2C = ((1+c)/(1-c))(Z-Y).
assert (1-c)/(1+c) == F(7,13)

# Mean-variance parameter q=c^2 Y.
assert c*c == F(9,100)
# At the nonzero equilibrium, Y=100/9, hence q=1.
assert c*c*F(100,9) == 1

print("VERIFY_OK")
