"""Reproduce the exact diameter law for planar projections of the unit octahedron.

Uses only the Python standard library. The analytic argument is independent of
these finite numerical and exact-arithmetic consistency checks.
"""
import math
import random
from fractions import Fraction

PI = math.pi
T0 = 1 / math.sqrt(3)
D0 = 2 * math.sqrt(2 / 3)


def beta(t):
    return PI / 2 - 2 * math.asin(t / math.sqrt(1 - t * t))


def q(t):
    """P(min_i |U_i| >= t), U uniform on the two-sphere."""
    if t <= 0:
        return 1.0
    if t >= T0:
        return 0.0
    alpha = math.acos(t * t / (1 - t * t))
    return (2 / PI) * (3 * alpha - PI - 3 * t * beta(t))


def cdf(d):
    if d <= D0:
        return 0.0
    if d >= 2:
        return 1.0
    return q(math.sqrt(max(0, 1 - (d / 2) ** 2)))


def density(d):
    t = math.sqrt(1 - (d / 2) ** 2)
    return 3 * d * beta(t) / (2 * PI * t)


def simpson(f, a, b, n=2800):
    if a >= b:
        return 0.0
    assert n % 2 == 0
    h = (b - a) / n
    s = f(a) + f(b)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * f(a + k * h)
    return s * h / 3


def q_direct(t):
    """Independent spherical-area integral, NOT the spherical-curvature law."""
    if t <= 0:
        return 1.0
    if t >= T0:
        return 0.0
    a = math.asin(t / math.sqrt(1 - t*t))
    b = PI/2 - a
    def integrand(phi):
        bound = max(t / math.cos(phi), t / math.sin(phi))
        return max(0.0, math.sqrt(max(0.0, 1 - bound*bound)) - t)
    def smoothed_integral(left, right):
        width = right - left
        def transformed(u):
            phi = left + width * (1 - math.cos(PI*u)) / 2
            return integrand(phi) * width * (PI/2) * math.sin(PI*u)
        return simpson(transformed, 0, 1)
    return (2 / PI) * (smoothed_integral(a, PI/4) + smoothed_integral(PI/4, b))


def pairwise_projected_diameter(x, y, z):
    norm = math.sqrt(x*x + y*y + z*z)
    u = (x/norm, y/norm, z/norm)
    vertices = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    farthest = 0.0
    for v in vertices:
        for w in vertices:
            dif = [v[k]-w[k] for k in range(3)]
            d2 = sum(zz*zz for zz in dif) - sum(dif[k]*u[k] for k in range(3))**2
            farthest = max(farthest, math.sqrt(max(0.0, d2)))
    return farthest


def main():
    for a in range(1, 11):
        for b in range(1, 9):
            for c in range(1, 6):
                got = pairwise_projected_diameter(a,b,c)
                expected = 2 * math.sqrt(1 - min(a*a,b*b,c*c)/Fraction(a*a+b*b+c*c))
                assert abs(got-expected) < 2e-13
    print('INDEPENDENT_SIX_PROJECTED_VERTICES_DIAMETER_OK')

    for t in (0.003,0.04,0.1,0.2,0.31,0.43,0.51,0.55,0.57):
        actual = q_direct(t)
        predicted = q(t)
        assert abs(actual-predicted) < 2.5e-7, (t,actual,predicted)
    print('EXACT_SPHERICAL_CURVATURE_AND_INDEPENDENT_AREA_INTEGRALS_OK')

    for i in range(1, 50):
        d = D0 + (2-D0)*i/50
        h = 1e-5
        numerical = (cdf(d+h)-cdf(d-h))/(2*h)
        assert abs(numerical-density(d)) < 5e-5, (d,numerical,density(d))
    print('NORMALIZED_PDF_CDF_DERIVATIVE_IDENTITY_OK')

    c_low = 9*math.sqrt(3)/(2*PI)
    for eps in (1e-3,4e-4,1e-4):
        r = cdf(D0+eps)/(c_low*eps*eps)
        assert abs(r-1) < 0.004, (eps,r)
    for eps in (1e-3,1e-4):
        error = (1-cdf(2-eps)) - (3*math.sqrt(eps)-6*eps/PI)
        assert abs(error) < 2*eps**1.5
    print('SHARP_TWO_ENDPOINT_ASYMPTOTIC_CONSTANTS_OK')

    # Vertices of the scaled tangent-plane lower-tail triangle.
    verts = ((2.,-1.,-1.),(-1.,2.,-1.),(-1.,-1.,2.))
    for v in verts:
        assert abs(sum(v)) < 1e-12 and min(v) >= -1
    edge = math.sqrt(sum((verts[0][i]-verts[1][i])**2 for i in range(3)))
    assert abs(edge - 3*math.sqrt(2)) < 1e-12
    triangle_area = math.sqrt(3)*edge*edge/4
    assert abs(triangle_area - 9*math.sqrt(3)/2) < 1e-12
    assert abs((2/PI) * triangle_area / 2 - c_low) < 1e-12
    print('LOWER_ENDPOINT_TANGENT_TRIANGLE_AND_COEFFICIENT_OK')

    rng = random.Random(220261020)
    thresholds=(0.05,0.14,0.26,0.38,0.49)
    success=[0]*len(thresholds)
    N=260000
    for _ in range(N):
        a,b,c=(rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1))
        normal=math.sqrt(a*a+b*b+c*c)
        t=min(abs(a),abs(b),abs(c))/normal
        for j,s in enumerate(thresholds):
            success[j]+=(t >= s)
    for t,n in zip(thresholds,success):
        estimate=n/N
        assert abs(estimate-q(t)) < 0.0055, (t,estimate,q(t))
    print('SEEDED_INDEPENDENT_HAAR_ORIENTATION_CDF_OK',N)
    print('ALL_PROJECTED_OCTAHEDRON_DIAMETER_CHECKS_OK')

if __name__ == '__main__':
    main()
