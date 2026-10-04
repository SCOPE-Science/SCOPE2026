from fractions import Fraction as F

a1 = F(6242, 10000)
a2 = F(8157, 10000)
assert a1 + (1-a1) == 1
assert a2 + (1-a2) == 1
assert a1 + a2 == F(14399,10000)
assert a1 + a2 > 1

def shares(sigma):
    return (sigma*a1, sigma*(1-a1), (1-sigma)*a2, (1-sigma)*(1-a2))

for sigma in (F(4479,10000), F(5521,10000)):
    p = shares(sigma)
    assert all(x >= 0 for x in p)
    assert sum(p, F(0,1)) == 1

print("VERIFY_OK")
