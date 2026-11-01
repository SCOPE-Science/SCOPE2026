"""Exact rational checks of two-circle residual-floor examples (stdlib only).

These computations verify finite identities and sharpness examples; the
universal inequality rests on the winding-number proof in RESULT.md.
"""
from fractions import Fraction as Q

r1, r2 = Q(1), Q(2)
w1, w2 = Q(2), Q(5)
omega = Q(4)
left1 = r1 * abs(w1 - omega)
left2 = r2 * abs(w2 - omega)
right = r1 * r2 / (r1 + r2) * abs(w1 - w2)
assert (left1, left2, right) == (Q(2), Q(2), Q(2))

# Weighted Chebyshev objective at the equalizing reference angular speed.
opt_omega = (r1*w1 + r2*w2)/(r1+r2)
assert opt_omega == omega
for integer in range(-30, 31):
    sample_omega = Q(integer, 4)
    assert max(r1*abs(w1-sample_omega),
               r2*abs(w2-sample_omega)) >= right

# Example with F(x1,x2)=(2x1,x2), global metric constants m=1,M=2.
# On a true radius-r circular orbit with speed w, the exact supremum of
# the residual over angle is r*max(|w-Omega/2|, |w-2*Omega|).
aniso_max1 = r1 * max(abs(w1 - omega/Q(2)), abs(w1 - Q(2)*omega))
aniso_max2 = r2 * max(abs(w2 - omega/Q(2)), abs(w2 - Q(2)*omega))
conditioned_floor = Q(1, 2) * right
assert (aniso_max1, aniso_max2, conditioned_floor) == (Q(6), Q(6), Q(1))

# Validate orientation reversal: F(x1,x2)=(x1,-x2) reverses winding;
# its pullback of a reference Omega J is -Omega J on the physical plane.
reflection_omega = Q(-4)
assert max(r1*abs(w1+reflection_omega),
           r2*abs(w2+reflection_omega)) == right
print('PASS: 65 exact rational equality and inequality checks')
