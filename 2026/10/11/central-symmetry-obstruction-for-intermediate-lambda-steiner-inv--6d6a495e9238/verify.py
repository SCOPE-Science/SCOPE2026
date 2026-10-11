from fractions import Fraction
import math

# Exact interval-reflection identity for several rational parameters.
for lam in (Fraction(0,1), Fraction(1,7), Fraction(2,9), Fraction(3,8)):
    assert lam < Fraction(1,2)
    for L in (Fraction(1,1), Fraction(5,3), Fraction(17,4)):
        t = (Fraction(1,1)-2*lam)*L/Fraction(2,1)
        lower = -lam*L
        upper = (Fraction(1,1)-lam)*L
        reflected_lower = 2*t-upper
        reflected_upper = 2*t-lower
        assert reflected_lower == lower
        assert reflected_upper == upper

# If two different positive chord lengths were both compatible with one center,
# the identity forces them equal.
for lam in (Fraction(1,10), Fraction(1,3), Fraction(2,5)):
    factor = Fraction(1,1)-2*lam
    assert factor != 0
    L1, L2 = Fraction(3,2), Fraction(7,4)
    assert factor*L1 != factor*L2

# Representative ellipsoid: z-parallel chord length varies with the base point.
a,b,c = 2.0, 3.0, 5.0
def ellipsoid_chord(x,y):
    q = 1.0-(x*x)/(a*a)-(y*y)/(b*b)
    return 2.0*c*math.sqrt(max(0.0,q))
assert abs(ellipsoid_chord(0.0,0.0)-10.0) < 1e-12
assert ellipsoid_chord(1.0,0.0) < ellipsoid_chord(0.0,0.0)
assert ellipsoid_chord(0.0,1.0) < ellipsoid_chord(0.0,0.0)

print("VERIFY_OK")
print("exact_interval_checks=12")
print("ellipsoid_nonconstant_chord_check=passed")
