from fractions import Fraction as F

r = F(17, 100)
d1 = F(1, 100)
b = F(1, 2)
beta = F(3, 5)
c = F(89, 100)
alpha = F(3, 5)
q1 = F(4, 5)
xi = F(7, 50)
delta = F(3, 2)
q = F(29, 50)
d3 = F(1, 5)
d2 = F(9, 10)

assert d2 / beta == F(3, 2)
G1 = c * alpha * q1 / (1 + q1)
assert G1 == F(89, 375)
assert G1 - d3 == F(14, 375)
den = xi * delta * q
assert den == F(609, 5000)
lower_XI = (G1 - d3) / den
assert lower_XI == F(80, 261)
margin = (r - d1) - (b + beta) * lower_XI
assert margin == -F(1156, 6525)
assert margin < 0

XS = F(3001, 5000)
XI = F(71, 2000)
Y = F(971, 10000)
residual = beta * XS - delta * q * Y - d2
assert residual == -F(624357, 1000000)
dot_XI = XI * residual
assert dot_XI == -F(44329347, 2000000000)
assert dot_XI != 0

print('VERIFY_OK')
