#!/usr/bin/env python3
"""Independent radial-integral checks of the local intrinsic cone-distance formula.
Requires Python 3 and SciPy; does not attempt to certify all cone angles.
"""
from math import pi, sin, cos, acos, sqrt
from scipy.integrate import quad


def coefficient_closed(alpha):
    half = alpha / 2
    return -alpha / 8 * (cos(half) / sin(half) + (pi - half) / sin(half)**2)


def coefficient_radial_integral(alpha):
    def moment(phi):
        inner, _ = quad(lambda u: cos(u)/(1-cos(phi)*cos(u))**2,
                        0, pi/2, epsabs=2e-12, epsrel=2e-12)
        return inner/8
    val, _ = quad(moment, alpha/2, pi, epsabs=2e-12, epsrel=2e-12)
    return -2*alpha*val


# On the half-turn cone, the ball is the image of two antipodal disks.
# Their planar intersection divided by two yields the radial deficit.
def coefficient_antipodal_quotient():
    # Difference of ball areas for a center at radial distance t in a cone of angle pi:
    # -(r^2 arccos(t/r)-t sqrt(r^2-t^2)); integrate pi*t*dt, at r=1.
    val, _ = quad(lambda t: pi*t*(-acos(t)+t*sqrt(max(0,1-t*t))),
                  0, 1, epsabs=1e-12)
    return val


for p in (0.5, 1, 4/3, 1.5, 5/3, 1.8, 1.95):
    alpha = p*pi
    exact = coefficient_closed(alpha)
    numerical = coefficient_radial_integral(alpha)
    assert abs(exact-numerical) < 1e-9, (p, exact, numerical)
    print('CONE_RADIAL_ANGLE_QUADRATURE_OK', p, round(exact, 12))
assert abs(coefficient_antipodal_quotient() + pi*pi/16) < 1e-11
assert abs(coefficient_closed(pi)+pi*pi/16) < 1e-12
print('HALF_TURN_QUOTIENT_INDEPENDENT_CHECK_OK')
# Unit-edge tetrahedron: 4 cone angles pi, area sqrt(3).
assert abs(4*coefficient_closed(pi)/3 + pi*pi/12) < 1e-12
print('UNIT_EDGE_TETRAHEDRON_NORMALIZATION_OK')
print('ALL_CONE_DISTANCE_NUMERICAL_CHECKS_OK')
