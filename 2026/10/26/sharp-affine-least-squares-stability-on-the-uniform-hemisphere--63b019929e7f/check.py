#!/usr/bin/env python3
"""Reproducible arithmetic and quadrature for hemispherical affine projection.

All infinite-domain assertions are proved in RESULT.md; this checker supplies
exact rational identities and non-exhaustive numerical cross-checks only.
"""
from fractions import Fraction as Q
from math import sqrt, pi, asin, cos, sin

checks = 0

def test(ok, description):
    global checks
    if not ok:
        raise AssertionError(description)
    checks += 1

# Exact low-order moments of uniform arclength on the upper hemisphere.
mz = Q(1, 2)
mxx = Q(1, 3)
mzz = Q(1, 3)
var_z = mzz - mz*mz
test(var_z == Q(1, 12), 'vertical centered variance')
test(3*mxx == 1, 'horizontal reciprocal Gram coefficient')
test(12*var_z == 1, 'vertical reciprocal Gram coefficient')

# Exact Cauchy-Schwarz gap: norm at equator is above sqrt(13/3).
test(Q(447, 200)**2 < 5, 'rational lower bound on sqrt(5)')
test(Q(2089, 1000) > Q(25, 12), 'rational comparison')
test(Q(25, 12)**2 > Q(13, 3), 'upper rational bound on sqrt(13/3)')

def exact_norm():
    return 61*sqrt(5)/15 - 7

L = exact_norm()
test(L > sqrt(13/3) > 2, 'key strict norm gap')
test(abs(L - (1 + (3*sqrt(5)-4)**2/(3*sqrt(5)))) < 1e-14,
     'two forms of spherical-cap result')
test(abs((L-1)/2 - (3*sqrt(5)-4)**2/(6*sqrt(5))) < 1e-14,
     'negative cap mass')

# Azimuthal average of |a + b cos(phi)|, b >= 0.
def avg_abs(a, b):
    if b <= abs(a):
        return abs(a)
    return 2/pi*(sqrt(max(0, b*b-a*a)) + a*asin(a/b))

def simpson(g, n):
    assert n % 2 == 0
    h = 1/n
    s = g(0) + g(1)
    for j in range(1, n):
        s += (4 if j % 2 else 2)*g(j*h)
    return s*h/3

def row(z, radial=None, n=6000):
    if radial is None:
        radial = sqrt(1-z*z)
    return simpson(lambda t: avg_abs(4-6*z+(12*z-6)*t,
                                   3*radial*sqrt(max(0, 1-t*t))), n)

norm0 = row(0)
test(abs(norm0 - L) < 1e-6, 'azimuth-reduced quadrature, equator')
test(abs(row(1) - Q(5, 3)) < 2e-7, 'pole value 5/3')
# Upper bound from Hilbert-space Cauchy-Schwarz for all z in [1/3,1].
for k in range(0, 41):
    z = k/40
    computed = row(z, n=1800)
    test(computed <= L + 1e-6, 'numerical row maximum, sample %s' % z)
    if z >= 1/3:
        test(computed <= sqrt(7-12*z+9*z*z)+1e-6,
             'Cauchy-Schwarz row bound, sample %s' % z)
    if z <= 1/3:
        test(computed <= (1-3*z)*L + 3*z*sqrt(13/3) + 1e-6,
             'convex interpolation bound, sample %s' % z)

# Direct 2D integration independent of the analytic azimuth formula.
def raw_2d_equator(nt=650, nphi=720):
    # Midpoint sampling in height and azimuth; discontinuous derivative across a sign circle.
    acc = 0.0
    for i in range(nt):
        t = (i+0.5)/nt
        r = sqrt(1-t*t)
        base = 4-6*t
        for j in range(nphi):
            theta = 2*pi*(j+0.5)/nphi
            acc += abs(base+3*r*cos(theta))
    return acc/(nt*nphi)
raw = raw_2d_equator()
test(abs(raw-L) < 3e-5, 'direct spherical midpoint quadrature')

# Full-sphere orthogonal projection comparator and strict undershoot.
test(Q(5, 3) < L, 'hemisphere increases first-degree full-sphere stability')
test((L-1)/2 > Q(1, 2), 'hemisphere projector exceeds half-unit positivity defect')
print('CHECKS_PASSED=%d' % checks)
print('HEMISPHERE_NORM=%.15f' % L)
print('AZIMUTH_QUADRATURE=%.15f' % norm0)
print('DIRECT_SURFACE_QUADRATURE=%.15f' % raw)
print('SHARP_NEGATIVE_OVERSHOOT=%.15f' % ((L-1)/2))
