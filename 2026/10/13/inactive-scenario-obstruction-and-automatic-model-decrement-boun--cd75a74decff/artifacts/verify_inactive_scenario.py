import sympy as sp
from fractions import Fraction as F

M = sp.symbols("M", positive=True)
a = -(M + 2) / (M + 1)

assert sp.simplify(a + 1 + 1/(M + 1)) == 0

v = sp.Integer(-1)
branch1 = v
branch2 = -(M + 2) - M*v
assert branch1 == -1
assert sp.simplify(branch2 + 2) == 0

theta = branch1 + sp.Rational(1, 2)*v**2
assert theta == -sp.Rational(1, 2)

Fa = a + sp.Rational(1, 2)*a**2
gap = sp.simplify(Fa - theta)
assert sp.simplify(gap - sp.Rational(1, 2)/(M + 1)**2) == 0

# The second-branch derivative at the right endpoint is negative:
# a-M = -(M^2+2M+2)/(M+1).
assert sp.simplify((a - M) + (M**2 + 2*M + 2)/(M + 1)) == 0

g1v = sp.Integer(1)*v
g2v = (-M)*v
assert g1v == -1
assert sp.simplify(g2v - M) == 0

for m in [F(1,10), F(1), F(2), F(7,3), F(25)]:
    inter = -(m + 2)/(m + 1)
    assert inter < -1
    assert F(-1) >= -(m + 2) + m
    assert F(-1) + F(1,2) == F(-1,2)
    assert (inter + F(1,2)*inter*inter) - F(-1,2) == F(1,2)/(m + 1)**2
    assert max(F(-1), m) == m > 0

print("VERIFY_OK")
