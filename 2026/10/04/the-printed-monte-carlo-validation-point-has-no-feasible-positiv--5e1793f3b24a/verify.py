from fractions import Fraction as F

r = F(113, 100)
v = F(8, 625)
a = 1 - 1 / r
assert a == F(13, 113)

upper = 2 * r**3 * a**4 + 3 * r * (r*r - 1) * a**2
rv = r * v
assert upper == F(292201, 22600000)
assert rv == F(226, 15625)
assert rv - upper == F(173427, 113000000)
assert rv > upper

mu = F(33, 100)
s = F(3, 5000)
next_mu = r * (mu - mu*mu - s)
assert next_mu == F(49833, 200000)
assert next_mu - mu == F(-16167, 200000)
assert mu > a

print("VERIFY_OK")
