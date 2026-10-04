from fractions import Fraction as F

a = F(1, 4)
c = F(1, 2)
d = F(1, 20)
b1 = F(0)
b2 = F(-20, 119)
b3 = F(-3, 10)
b4 = F(157, 11900)

# Equilibrium reduction:
# z=-y, w=(c/d)z=-10y, x=-a*y-w=39y/4.
assert c / d == 10
xcoef = c / d - a
assert xcoef == F(39, 4)

linear = b1 * xcoef + b2 - b3 - b4 * (c / d)
assert linear == 0
quad = -xcoef
assert quad == F(-39, 4)

# General characteristic coefficients for det(lambda I - J0).
p3 = -(a + b3 + d)
p2 = a*b3 + a*d + b1 + b3*d + b4*c + 1
p1 = -a*b1 - a*b3*d - a*b4*c - b1*d + b2*c + b2 - b3 - d
p0 = a*b1*d - b1*c - b2*d + b3*d + b4*c

assert p3 == 0
assert p2 == F(1769, 1904)
assert p1 == 0
assert p0 == 0
assert p2 > 0

# Equilibria solve mu - (39/4)y^2 = 0:
# mu<0: none; mu=0: y=0 only; mu>0: two real roots.
for mu in [F(-1), F(-1, 7)]:
    assert mu < 0
for mu in [F(1), F(2, 5)]:
    assert mu > 0

print("VERIFY_OK")
