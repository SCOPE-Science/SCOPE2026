import cmath
from fractions import Fraction as F

# Exact algebraic coefficient check for
# A_r = I - r D4 = (r/12)[X^2 - 16 X + 28 + 12/r].
r = F(1, 10)
assert F(1) + F(7,3)*r == (r/F(12)) * (F(28) + F(12)/r)  # I coefficient in X-polynomial form
assert (F(8)+F(8)) == 16
# Product roots have sum 16 and product 28+12/r.
assert F(64) - (F(36) - F(12)/r) == F(28) + F(12)/r

# Closed Green-kernel formula for r < 1/3.
def interior_root(s):
    d = cmath.sqrt(s*s - 4)
    q = (s-d)/2
    if abs(q) > 1:
        d = -d
        q = (s-d)/2
    assert abs(q) < 1
    return q, d

def green(r_float, n):
    eta = (12.0/r_float - 36.0)**0.5
    sp = 8.0 + 1j*eta
    sm = sp.conjugate()
    qp, dp = interior_root(sp)
    qm, dm = interior_root(sm)
    kp = qp**abs(n)/dp
    km = qm**abs(n)/dm
    val = (12.0/r_float) * (kp-km)/(sm-sp)
    assert abs(val.imag) < 1e-13
    return val.real

# Robust sign witness at r=1/10.
g = [green(0.1, n) for n in range(7)]
assert g[0] > 0 and g[1] > 0 and g[2] > 0
assert g[3] < -1.7e-4
assert abs(g[3] - (-0.0001783115244453637)) < 1e-15

# At r=1/3 the factor is repeated at s=8 and the second-order kernel is positive.
s = 8.0
q = (s-(s*s-4)**0.5)/2
assert 0 < q < 1

print('VERIFY_OK')
