"""Exact algebraic checks for the balanced joint radius of two rank-one projections.

This checks the finite identities used in the proof; uniqueness and all-dimensional
quantifiers are established analytically in the accompanying proof.
"""
from fractions import Fraction as Q
from math import cos, pi, sqrt

def f(c, y):
    return (2-c*c)/4 + c*y/2 + (2*c*c-1)*y*y/4

def vertex(c):
    return c/(1-2*c*c)

def low_square(c):
    return (1-c*c)**2/(2*(1-2*c*c))

def bisector_square(c):
    return (1+c)**2/4

for c in [Q(0), Q(1,10), Q(1,4), Q(2,5), Q(1,2), Q(3,4), Q(1)]:
    assert f(c,Q(1)) == bisector_square(c)
    assert f(c,c) == (1+c**4)/2
    if 0<c<Q(1,2):
        v=vertex(c)
        assert c<v<1
        assert f(c,v)==low_square(c)
        assert (f(c,v)-f(c,Q(1))) == (1-c-2*c*c)**2/(4*(1-2*c*c))
    if c>=Q(1,2):
        # For all y in [c,1], derivative nonnegative at y=1 or convex.
        assert (c+(2*c*c-1))>=0
# Direct sampled maximizations for many real overlaps, not an infinite certificate.
for c in [0.0, .1,.25,.4,.49,.5,.51,.75,.9,1.0]:
    phase=__import__('math').acos(c)
    grid=max((cos(t)**4+cos(t-phase)**4)/2 for t in [i*pi/200000 for i in range(100001)])
    exact=float(low_square(Q(str(c))) if c<.5 else bisector_square(Q(str(c))))
    assert abs(grid-exact)<2e-7,(c,grid,exact)
# Coefficient in the singular gain, exact via polynomial expansion:
# f(y*)-f(1) = (1-c-2c^2)^2 / (4(1-2c^2)).
# At c = 1/2 - delta, numerator ~ (3 delta)^2; denominator ~ 2.
# Thus squared gain ~ (9/2) delta^2 and R gain ~ 3 delta^2.
assert (1-Q(1,2)-2*Q(1,2)**2)==0
assert (Q(1,2)+2*Q(1,2)**2)==1
print('RANK_ONE_PROJECTION_JOINT_RADIUS_BIFURCATION_EXACT_OK')
