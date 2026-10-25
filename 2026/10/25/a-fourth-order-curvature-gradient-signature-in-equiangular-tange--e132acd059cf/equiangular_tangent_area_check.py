"""Reproducible checks for the equiangular-tangent area expansion.

Requires Python 3 and mpmath. Run: python equiangular_tangent_area_check.py
The analytic proof, not this finite test, establishes the theorem.
"""
import math
import mpmath as mp

mp.mp.dps = 65
PI = mp.pi


def h_fun(theta, modes):
    # Each mode is (frequency >= 2, cosine support coefficient, sine coefficient).
    return 1 + sum(a*mp.cos(k*theta) + b*mp.sin(k*theta)
                   for k,a,b in modes)


def direct_polygon_area(n, phase, modes):
    # Intersect adjacent supporting lines in R^2 and use a shoelace sum.
    step = 2*PI/n
    vertices = []
    for i in range(n):
        t = phase + i*step
        u = t+step
        h0, h1 = h_fun(t,modes), h_fun(u,modes)
        # x = h0*normal(t) + t_parameter*tangent(t).
        shift = (h1-h0*mp.cos(step))/mp.sin(step)
        vertices.append((h0*mp.cos(t)-shift*mp.sin(t),
                         h0*mp.sin(t)+shift*mp.cos(t)))
    twice_area = sum(vertices[i][0]*vertices[(i+1)%n][1]
                     - vertices[i][1]*vertices[(i+1)%n][0]
                     for i in range(n))
    return twice_area/2


def support_quadrature_area(n, phase, modes):
    step = 2*PI/n
    vals = [h_fun(phase+i*step,modes) for i in range(n)]
    return sum(vals[i]*vals[(i+1)%n]-mp.cos(step)*vals[i]**2
               for i in range(n))/mp.sin(step)


def averaged_area_closed(n, modes):
    step=2*PI/n
    return n*mp.tan(step/2) + n/(2*mp.sin(step))*sum(
        (a*a+b*b)*(mp.cos(k*step)-mp.cos(step))
        for k,a,b in modes)


def body_area(modes):
    return PI + PI/2*sum((1-k*k)*(a*a+b*b) for k,a,b in modes)


def invariant_coefficients(modes):
    # Coefficients of step^2 and step^4, where step=2*pi/n.
    r2 = 2*PI + PI*sum((1-k*k)**2*(a*a+b*b) for k,a,b in modes)
    rp2 = PI*sum(k*k*(1-k*k)**2*(a*a+b*b) for k,a,b in modes)
    return r2/24, (3*r2-rp2)/720


# The area identity uses direct coordinates, not its support-function derivation.
modes = [(2,mp.mpf('0.02'),mp.mpf('0.00')),
         (3,mp.mpf('0.00'),mp.mpf('0.006')),
         (5,mp.mpf('0.002'),mp.mpf('0.00'))]
for n in (8,11,19,64):
    for offset in (mp.mpf('0'),mp.mpf('0.1786329'),mp.mpf('0.325')):
        a=direct_polygon_area(n,offset,modes)
        b=support_quadrature_area(n,offset,modes)
        assert abs(a-b) < mp.mpf('1e-54'), (n, a, b)
print('ADJACENT_TANGENT_INTERSECTIONS_VS_EDGE_AREA_OK')

# When n=8, mixing frequencies 3+5 makes the area phase dependent.
# Averaging the phase nevertheless removes all cross-frequency terms.
n=8
rotation_averaged = sum(direct_polygon_area(n,2*PI*j/(n*160),modes)
                        for j in range(160))/160
exact_expected = averaged_area_closed(n,modes)
assert abs(rotation_averaged-exact_expected) < mp.mpf('1e-53')
assert abs(direct_polygon_area(n,0,modes)
           -direct_polygon_area(n,PI/(7*n),modes)) > mp.mpf('1e-8')
print('RANDOM_PHASE_FOURIER_DIAGONALIZATION_WITH_ALIASING_OK')

# The family has radius of curvature 1+a*cos(m*theta).
a = mp.mpf('0.5')
for m in (2,5,6,8):
    hs=[(m, a/(1-m*m), mp.mpf('0'))]
    b2,b4 = invariant_coefficients(hs)
    assert abs(b2-PI*(2+a*a)/24)<mp.mpf('1e-55')
    assert abs(b4-PI*(6+(3-m*m)*a*a)/720)<mp.mpf('1e-55')
    # For n>2m there is no cross-frequency alias, so orientation is immaterial.
    for n in (2*m+3, 64):
        err=direct_polygon_area(n,PI/(9*n),hs)-averaged_area_closed(n,hs)
        assert abs(err)<mp.mpf('1e-52')
    # Error after subtracting the second and fourth terms is sixth-order.
    errs=[]
    for n in (160,320,640):
        step=2*PI/n
        exact=averaged_area_closed(n,hs)-body_area(hs)
        rem=exact-b2*step**2-b4*step**4
        errs.append(abs(rem/step**6))
    assert max(errs)/min(errs) < 1.25, (m, errs)
    print('SHARP_FOURTH_ORDER_COEFFICIENT_OK',m,'sign',
          'negative' if b4<0 else 'positive',
          'value',mp.nstr(b4,13))
assert invariant_coefficients([(5,a/(1-25),0)])[1]>0
assert invariant_coefficients([(6,a/(1-36),0)])[1]<0
print('SAME_CURVATURE_HISTOGRAM_OPPOSITE_FOURTH_ORDER_SIGNS_OK')

# Circle baseline from the independent exact tangent-polygon formula.
for n in (7,24,80):
    area=direct_polygon_area(n,mp.mpf('0.13'),[])
    assert abs(area-n*mp.tan(PI/n))<mp.mpf('1e-52')
print('EXACT_CIRCLE_AREA_OK')
print('ALL_EQUANGULAR_TANGENT_AREA_CHECKS_OK')
