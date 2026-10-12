from fractions import Fraction as F

p1, p2 = F(0), F(1)
# Source bisector functions in one dimension.
def g2(x):
    return (p2-p1)*x - F(1,2)*(p2-p1)*(p2+p1)
def g1(x):
    return (p1-p2)*x - F(1,2)*(p1-p2)*(p1+p2)

assert g2(F(0)) == F(-1,2)
assert g2(F(1,2)) == 0
assert g1(F(1)) == F(-1,2)
assert g1(F(1,2)) == 0

# Because g2 is strictly increasing on [0,1], its unique minimizer is 0.
assert g2(F(0)) < g2(F(1,4)) < g2(F(1))
# Because g1 is strictly decreasing on [0,1], its unique minimizer is 1.
assert g1(F(1)) < g1(F(3,4)) < g1(F(0))

x1, tau1 = F(0), g2(F(0))
x2, tau2 = F(1), g1(F(1))
assert tau1 == tau2 == F(-1,2)
assert not (F(0) < x1 < F(1,2))
assert not (F(1,2) < x2 < F(1))
print("VERIFY_OK")
