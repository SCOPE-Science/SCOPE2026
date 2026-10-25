"""Numerical cross-checks for the spherical fourteen-site coverage law.

Requires scipy and numpy. Evaluates the closed one-dimensional quadrature and
compares it with directly sampled points of the sphere, without constructing
Voronoi cells. No random seed or external data is required.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc

RT3 = math.sqrt(3.0)
r = RT3 - 1.0
q = 1.0 / math.sqrt(1.0 + r * r)
rho = math.acos(q)
K = 6.0 / (math.pi * q**5 * r**2 * (1.0 - r))
c0 = math.sqrt((1.0 + 1.0 / RT3) / 2.0)


def angular_bound(x, c):
    root = math.sqrt(max(0.0, 1.0 - x*x))
    if x < 1.0/math.sqrt(2.0):
        lower = math.acos(min(1.0, x/root))
    else:
        lower = 0.0
    if root < 1e-12:
        return 0.0
    b = (RT3*c - x)/root
    if b <= 1.0:
        upper = 0.0
    elif b >= math.sqrt(2.0):
        upper = math.pi/4.0
    else:
        upper = math.pi/4.0 - math.acos(b/math.sqrt(2.0))
    return max(0.0, upper - lower)


def cdf(c):
    if c <= q:
        return 0.0
    if c >= 1.0:
        return 1.0
    lo = 1.0/RT3
    joins = sorted(set(v for v in (1.0/math.sqrt(2.0), (q+c)/2.0)
                       if lo < v < c))
    return (12.0/math.pi) * quad(angular_bound, lo, c,
                                args=(c,), epsabs=2e-11, limit=300,
                                points=joins)[0]


def empirical_cdf():
    uv = qmc.Sobol(d=2, scramble=False).random_base2(m=18)
    z = 2.0*uv[:, 0] - 1.0
    phi = 2.0*math.pi*uv[:, 1]
    s = np.sqrt(1.0-z*z)
    coords = np.column_stack((s*np.cos(phi),s*np.sin(phi),z))
    dot_max = np.maximum(np.max(np.abs(coords),axis=1),
                         np.sum(np.abs(coords),axis=1)/RT3)
    assert np.min(dot_max) >= q-2e-15
    for c in (.83, .85, .88, .90, .94, .97):
        integral = cdf(c)
        estimated = float(np.mean(dot_max <= c))
        assert abs(estimated-integral) < 0.0015, (c, estimated, integral)
    print('DIRECT_SPHERICAL_SOBOL_VERSUS_CHAMBER_QUADRATURE_OK',len(dot_max))


def identity_and_endpoints():
    assert abs(math.degrees(rho)-36.2060231130)<1e-8
    assert abs(cdf(math.cos(math.radians(35.9839)))-0.000209636)<1e-6
    for c in (c0+.0001, .90, .92, .96, .99):
        assert abs(cdf(c)-(7*c-6)) < 4e-9, (c,cdf(c))
    for eps in (1e-4,2e-4,4e-4,8e-4):
        ratio = cdf(q+eps)/eps**2
        assert abs(ratio/K-1.0) < 0.025, (eps,ratio/K)
    print('PUBLISHED_COVERING_BENCHMARK_AND_EXACT_DISJOINT_CAP_BRANCH_OK')
    print('QUADRATIC_ONSET_CONSTANT_AND_24_GAP_VERTICES_OK',round(K,11))


def verify_local_tangent_geometry():
    A = r*q
    B = (1.0-r)*q/RT3
    E = 1.0/RT3
    local_area = (1.0+B/A)**2/(B*E)
    assert abs(24*local_area/(4*math.pi)-K)<1e-10
    u = np.array([q, q*r, 0.0])
    assert abs(np.linalg.norm(u)-1)<1e-13
    site_vals = [u[0], sum(u)/RT3]
    assert abs(max(site_vals)-q)<1e-13
    print('INDEPENDENT_TANGENT_POLYGON_CONSTANT_IDENTITY_OK')

if __name__ == '__main__':
    verify_local_tangent_geometry()
    identity_and_endpoints()
    empirical_cdf()
    print('ALL_FOURTEEN_SITE_COVERAGE_CHECKS_OK')
