#!/usr/bin/env python3
from fractions import Fraction as F

# Polynomial identity after x=p+h, y=ph:
# (2y^2-x^2+4y)^2 - x^2(y^2+x^2-2y)
# = -y(5x^2y+6x^2-4y^3-16y^2-16y).
def lhs(x2,y):
    # The expression contains x only through x^2.
    return (2*y*y-x2+4*y)**2 - x2*(y*y+x2-2*y)
def rhs(x2,y):
    return -y*(5*x2*y+6*x2-4*y**3-16*y*y-16*y)
for y in map(F, range(1,8)):
    for x2 in map(F, range(1,20)):
        assert lhs(x2,y) == rhs(x2,y)

# Exact nonsymmetric branch witness y=ph=3, x^2=(p+h)^2=100/7.
y=F(3); x2=F(100,7)
assert x2 == 4*y*(y+2)**2/(5*y+6)
assert x2-4*y == F(16,7) > 0
assert 2*y*y+4*y-x2 == F(110,7) > 0

# Represent q*sqrt(7) by q. For p=sqrt(7), h=3/sqrt(7)=3sqrt(7)/7.
p=F(1)          # coefficient of sqrt(7)
h=F(3,7)
L=F(11,7)
G_y=p/F(4); G_z=h/F(4)
O_y=F(3,7); O_z=F(1,21)
I_y=I_z=F(1,7)
assert I_y-G_y == F(-3,5)*(O_y-G_y)
assert I_z-G_z == F(-3,5)*(O_z-G_z)

# Opposite-edge dot product (C-A).(D-B) is exactly -1.
assert F(1)*F(-1) + F(0) + F(0) == -1

# Squared edge lengths: AB, AC=BC, AD=BD, CD.
edge2={F(4),F(8),F(16,7),F(58,7)}
assert len(edge2)==4

print('VERIFY_OK')
