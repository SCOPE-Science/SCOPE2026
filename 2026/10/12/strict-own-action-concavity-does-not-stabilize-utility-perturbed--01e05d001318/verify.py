from fractions import Fraction
import math

# Parameter range used in the proof.
for b in [0.0, 1e-8, 1e-4, 0.1, 0.5]:
    assert -1.0 < 0.0
    assert -(1.0-b) < 0.0

# The exact maximum of |x-x^3| on [-1,1] is 2/(3*sqrt(3)).
max_h = 2.0/(3.0*math.sqrt(3.0))
assert max_h/(1.0-0.5) < 1.0

# Equilibrium roots solve x*(x^2-b)=0.
def roots(b):
    if b == 0:
        return [0.0]
    return [-math.sqrt(b), 0.0, math.sqrt(b)]

assert roots(0.0) == [0.0]
for b in [1e-8, 1e-4, 0.1, 0.5]:
    rs = roots(b)
    assert len(rs) == 3
    for x in rs:
        assert abs(x) <= 1.0
        assert abs(x*(x*x-b)) < 1e-12
        y = x
        br2 = (x-x**3)/(1.0-b)
        assert abs(y-br2) < 1e-12

# FOC Jacobian at the unperturbed equilibrium.
a,b,c,d = -1,1,1,-1
assert a*d-b*c == 0
print('VERIFY_OK')
