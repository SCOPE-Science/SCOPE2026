from fractions import Fraction as F

# Source-model parameters and an exact coexistence point.
gamma = F(11)
alpha = F(1)
delta = F(1)
beta = F(39, 10)
xi = F(3, 10)
x = F(1, 3)

den = 1 + alpha*xi + x
p = x / den
y = (1 - x/gamma) * den
h = beta*(x + xi)/den - delta
c = h/(xi*y)

Fprime = -den/gamma + (1 - x/gamma)
hprime = beta*(1 + xi*(alpha - 1))/den**2

a1 = Fprime*p
a2 = -p
b1 = hprime*y
b2 = -xi*y

R1 = a1 + c*b2
R2 = c*a1*b2 - a2*b1

assert x == F(1, 3)
assert y == F(784, 495)
assert h == F(251, 490)
assert c == F(41415, 38416)
assert a1 == F(271, 1617)
assert a2 == -F(10, 49)
assert b1 == F(1248, 539)
assert b2 == -F(392, 825)
assert c*b2 == -F(251, 490)
assert R1 == -F(5573, 16170) < 0
assert R2 == F(306379, 792330) > 0
assert h == c*xi*y

d1 = F(13, 1000)
d2 = F(1)
A = d1*d2
B = a1*d2 + c*b2*d1
S = B*B - 4*A*R2

assert B == F(2602321, 16170000) > 0
assert S == F(1514610947041, 261468900000000) > 0

def D(z):
    z = F(z)
    return A*z*z - B*z + R2

vertex = B/(2*A)
assert vertex == F(2602321, 420420)
assert vertex < 100
assert D(100) == F(301859687, 2641100) > 0
assert D(4) == -F(3239273, 66027500) < 0
assert D(9) == -F(6921071, 792330000) < 0

# On l=1/10, z_k = 100*k^2. Since D is increasing for z >= 100,
# D(z_k) >= D(100) > 0 for every k >= 1.
assert 2*A*F(100) - B > 0

# Modal traces are strictly negative whenever R1<0.
# T_k = R1 - (d1+d2) z_k < 0 for every z_k >= 0.
assert R1 < 0

print('VERIFY_OK')
print('c =', c)
print('R1 =', R1)
print('R2 =', R2)
print('B =', B)
print('S =', S)
print('vertex =', vertex)
print('D(4) =', D(4))
print('D(9) =', D(9))
print('D(100) =', D(100))
