"""Exact rational checks of the maximal-circle boundary identities for Cassini lemniscates.

Run with Python 3 standard library: python verify.py
This checks exact polynomial coefficients at representative rational squared-separations;
the universal mathematical proof is given in RESULT.md.
"""
from fractions import Fraction as Q
from math import cos, pi, sqrt

squared_parameters = [Q(0), Q(1, 100), Q(1, 4), Q(9, 25), Q(1, 2), Q(9, 16), Q(1), Q(4), Q(9)]


def coefficients(u):
    """Coefficients of |(c+r exp(it))^2-u|^2 as polynomial in cos(t).

    Returns constant, linear, quadratic; c^2=C, r^2=R, and A=c^2-u.
    The linear term contains c*r but vanishes by construction.
    """
    if u <= Q(1, 2):
        C = Q(0)
        R = 1-u
        A = -u
        linear = Q(0)
        expected_t2 = -4*u*R
    else:
        R = Q(1)/(4*u)
        C = u-R
        A = C-u
        assert A+R == 0
        linear = Q(0)  # 2(2cr)(A+R)
        expected_t2 = -4*R*R
    constant = (A-R)**2 + 4*C*R
    t2 = 4*A*R
    return C,R,constant,linear,t2,expected_t2

for u in squared_parameters:
    C,R,k0,k1,k2,exp2 = coefficients(u)
    assert C >= 0 and R > 0
    assert k0 == 1 and k1 == 0 and k2 == exp2 and k2 <= 0
    if u > Q(1,2):
        assert 4*u*R == 1 and C+R == u
    else:
        assert u+R == 1

# Check the exact quartic identity at rational planar points, not floating approximations.
plane_points = [(Q(a,4),Q(b,5)) for a in range(-7,8) for b in range(-7,8)]
identity_count=0
for u in squared_parameters:
    for x,y in plane_points:
        lhs = (x*x-y*y-u)**2 + 4*x*x*y*y
        rhs = (x*x+y*y-u)**2 + 4*u*y*y
        assert lhs == rhs
        identity_count += 1

# Supplemental non-certifying boundary sampling at representative parameter values.
samples=0
for u in squared_parameters:
    C,R,*_ = coefficients(u)
    c,r=sqrt(float(C)),sqrt(float(R))
    s=sqrt(float(u))
    for center in set((c,-c)):
        for k in range(720):
            t=2*pi*k/720
            z=complex(center + r*cos(t),r*__import__('math').sin(t))
            assert abs(z*z-s*s) <= 1 + 5e-12
            samples += 1
print(f'VERIFY_OK squared_parameter_cases={len(squared_parameters)} exact_quartic_evaluations={identity_count} supplemental_circle_samples={samples}')
