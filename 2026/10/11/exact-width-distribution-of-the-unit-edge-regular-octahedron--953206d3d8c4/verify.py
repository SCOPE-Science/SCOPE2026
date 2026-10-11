#!/usr/bin/env python3
import math
import numpy as np
from scipy.integrate import quad

SQ2 = math.sqrt(2.0)
PI = math.pi

def fm(m):
    if m < 1/math.sqrt(3):
        return 0.0
    if m < 1/math.sqrt(2) - 1e-14:
        beta = math.acos(m*m/(1-m*m))
        alpha = math.acos(m/math.sqrt(1-m*m))
        return 3*m - 2 + 6*beta/PI - 12*m*alpha/PI
    if m <= 1:
        return 3*m - 2
    return 1.0

def fw(w):
    return fm(w/SQ2)

# Unit-edge octahedron normalization.
verts = []
for i in range(3):
    for s in (-1,1):
        v = np.zeros(3)
        v[i] = s/SQ2
        verts.append(v)
edges = 0
for i in range(6):
    for j in range(i+1,6):
        d = np.linalg.norm(verts[i]-verts[j])
        if abs(d-1.0) < 1e-12:
            edges += 1
assert edges == 12

# Direct support-width identity on deterministic test directions.
tests = [
    np.array([1.,0.,0.]),
    np.array([1.,1.,1.])/math.sqrt(3),
    np.array([2.,-1.,3.])/math.sqrt(14),
    np.array([-5.,4.,2.])/math.sqrt(45),
]
for u in tests:
    hplus = max(float(np.dot(v,u)) for v in verts)
    hminus = max(float(np.dot(v,-u)) for v in verts)
    direct = hplus+hminus
    formula = SQ2*max(abs(float(x)) for x in u)
    assert abs(direct-formula) < 1e-12

# Exact endpoint identities, evaluated at high floating precision.
w0 = math.sqrt(2/3)
assert abs(fw(w0)) < 5e-15
join = 3/SQ2 - 2
assert abs(fw(1.0)-join) < 5e-15
assert abs(fw(SQ2)-1.0) < 5e-15

# Independent direct spherical-area quadrature.
# z is uniform on [-1,1]; at fixed z, longitude is uniform.
def direct_cdf_m(m):
    if m < 1/math.sqrt(3): return 0.0
    if m >= 1: return 1.0
    def lon_fraction(z):
        if abs(z) > m:
            return 0.0
        r2 = max(0.0,1-z*z)
        if r2 == 0.0:
            return 1.0
        a = m/math.sqrt(r2)
        if a >= 1:
            return 1.0
        # Need |cos phi|<=a and |sin phi|<=a.
        # In each quadrant the allowed angular length is
        # max(0, 2 asin(a)-pi/2).
        q = max(0.0, 2*math.asin(a)-math.pi/2)
        return 4*q/(2*math.pi)
    val, err = quad(lon_fraction, -m, m, epsabs=2e-11, epsrel=2e-11,
                    points=[-math.sqrt(max(0,1-2*m*m)),
                            math.sqrt(max(0,1-2*m*m))], limit=200)
    return 0.5*val

for m in (1/math.sqrt(3), 0.60, 0.65, 1/math.sqrt(2), 0.8, 0.95):
    a = fm(m)
    b = direct_cdf_m(m)
    assert abs(a-b) < 2e-9, (m,a,b)

# Independent one-dimensional lens-area integral:
# area{x>m,y>m} = integral over x, with y-longitude interval.
# Use z as polar axis x; conditional circle at x has y=sqrt(1-x^2) cos(phi).
def lens_quad(m):
    if m >= 1/math.sqrt(2):
        return 0.0
    xmax = math.sqrt(1-m*m)
    def circumference_fraction(x):
        a = m/math.sqrt(max(1e-300,1-x*x))
        if a >= 1:
            return 0.0
        # fraction of azimuth with cos(phi)>a
        return math.acos(a)/math.pi
    # surface area band x..x+dx is 2*pi dx
    val, err = quad(lambda x: 2*math.pi*circumference_fraction(x),
                    m, xmax, epsabs=2e-11, epsrel=2e-11)
    return val

def lens_formula(m):
    beta = math.acos(m*m/(1-m*m))
    alpha = math.acos(m/math.sqrt(1-m*m))
    return 2*beta - 4*m*alpha

for m in (1/math.sqrt(3),0.60,0.65,0.70):
    assert abs(lens_quad(m)-lens_formula(m)) < 2e-9

# Monotonicity sanity check over dense grid.
grid = np.linspace(math.sqrt(2/3), math.sqrt(2), 10001)
vals = np.array([fw(float(x)) for x in grid])
assert vals.min() >= -1e-12 and vals.max() <= 1+1e-12
assert np.min(np.diff(vals)) >= -2e-10

print("VERIFY_OK")
print("unit_edge_vertices = exact construction")
print("width_identity = checked")
print("endpoint_and_join_checks = passed")
print("direct_spherical_area_quadrature = passed")
print("independent_lens_quadrature = passed")
