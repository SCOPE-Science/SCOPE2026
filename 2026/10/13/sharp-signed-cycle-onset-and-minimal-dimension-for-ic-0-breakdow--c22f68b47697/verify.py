from fractions import Fraction as F
from decimal import Decimal, getcontext

def pivots_from_u(u):
    q1 = F(1)
    q2 = F(1) - u
    q3 = (F(1) - 2*u) / (F(1) - u)
    q4 = (F(1) - u) * (F(1) - 3*u) / (F(1) - 2*u)
    return q1, q2, q3, q4

safe = pivots_from_u(F(1,4))
assert safe == (F(1), F(3,4), F(2,3), F(3,8))

kershaw_unit = pivots_from_u(F(4,9))
assert kershaw_unit == (F(1), F(5,9), F(1,5), F(-5,3))

kershaw_scaled = tuple(F(3)*q for q in kershaw_unit)
assert kershaw_scaled == (F(3), F(5,3), F(3,5), F(-5))

u0 = F(1,3)
assert (F(1)-u0)*(F(1)-3*u0) == 0
assert (F(1)-2*u0)/(F(1)-u0) == F(1,2)

getcontext().prec = 70
D = Decimal
r = (D(2)/D(3)).sqrt()
assert D(1)-r > 0
k1 = (D(1)+r)/(D(1)-r)
k2 = D(5) + D(2)*D(6).sqrt()
assert abs(k1-k2) < D("1e-60")

assert 2*F(4,9) < 1

print("VERIFY_OK")
print("safe_pivots", safe)
print("kershaw_scaled_pivots", kershaw_scaled)
print("kappa_boundary", k1)
