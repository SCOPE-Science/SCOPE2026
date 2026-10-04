from fractions import Fraction as F

def q(r, sigma11):
    return F(-2) + F(2) * r / (sigma11 * sigma11)

def h(r, sigma11):
    return F(-2) - F(2) * r / (sigma11 * sigma11)

for r, s in [(F(1, 2), F(3, 5)), (F(7, 3), F(5, 4)), (F(11, 9), F(2, 7))]:
    assert q(r, s) + h(r, s) == F(-4)

s = F(2)
r_critical = s * s / 2
assert q(r_critical, s) == F(-1)
assert q(F(3, 2), F(2)) < F(-1)
assert q(F(5, 2), F(2)) > F(-1)

r_example = F(1, 2)
s_example = F(3, 5)
threshold = s_example * s_example / 2
assert threshold == F(9, 50)
assert r_example > threshold
assert q(r_example, s_example) > F(-1)
print("VERIFY_OK")
