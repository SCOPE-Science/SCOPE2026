from fractions import Fraction as F

g = F(1, 2)
zeta = F(1, 3)
h = F(1, 1)

lam1 = 1 + h * (1 - g)
lam2 = 1 + h * (1 - zeta)
t1 = F(2, 1) / (g - 1)
t2 = F(2, 1) / (zeta - 1)

assert lam1 == F(3, 2)
assert lam2 == F(5, 3)
assert abs(lam1) > 1 and abs(lam2) > 1
assert t1 == -4 and t2 == -3
assert h > max(t1, t2)
print("VERIFY_OK")
