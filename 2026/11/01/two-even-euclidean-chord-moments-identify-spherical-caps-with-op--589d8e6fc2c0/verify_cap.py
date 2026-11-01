"""Independent finite checks for the spherical-cap two-chord-moment theorem.

Only Python's standard library is required. The analytical proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import cos, sin, sqrt, pi


def moments(R, z):
    return (R * R * (1-z) * (3+z) / 2,
            F(2, 3) * R**4 * (1-z)**2 * (z*z + 4*z + 5))


def ratio(z):
    return F(8, 3) * (z*z + 4*z + 5) / (z+3)**2


def t_to_z(t):
    return (3*t - 1) / (1-t)


def inverse(mu, rho):
    t = sqrt(0.75 * float(rho) - 1)
    return (sqrt(float(mu) * (1-t)**2 / (2*(1-2*t))),
            (3*t-1)/(1-t))

checks = 0
for zi in [F(-1), F(-3, 4), F(-1, 2), F(0), F(1, 3), F(3, 4), F(99, 100)]:
    for R in [F(1, 2), F(1), F(7, 3)]:
        mu, nu = moments(R, zi)
        assert mu > 0
        assert nu / mu**2 == ratio(zi)
        tau = (zi+1)/(zi+3)
        assert ratio(zi) == F(4, 3)*(1+tau**2)
        assert t_to_z(tau) == zi
        assert mu == 2*R**2*(1-2*tau)/(1-tau)**2
        r2, z2 = inverse(mu, nu/mu**2)
        assert abs(r2-float(R)) < 1e-9
        assert abs(z2-float(zi)) < 1e-9
        checks += 6

# Exact rational stability tests, including the full-sphere endpoint.
for i in range(0, 64):
    a = F(i, 128)
    for j in range(i+1, 65):
        b = F(j, 128)
        za, zb = t_to_z(a), t_to_z(b)
        ra = F(4, 3)*(1+a*a)
        rb = F(4, 3)*(1+b*b)
        assert (zb-za)**2 <= 12*(rb-ra)
        checks += 1

# Direct four-dimensional midpoint quadrature: no use of a closed moment
# formula to compute the numerical integrals.
def direct_quad(R, z, n_z=48, n_phi=12):
    pts = []
    for j in range(n_z):
        u = z+(j+0.5)*(1-z)/n_z
        h = sqrt(max(0., 1-u*u))
        for i in range(n_phi):
            phi = 2*pi*(i+0.5)/n_phi
            pts.append((h*cos(phi), h*sin(phi), u))
    s2 = s4 = 0.
    for x in pts:
        for y in pts:
            dot = x[0]*y[0]+x[1]*y[1]+x[2]*y[2]
            d2 = 2*R*R*(1-dot)
            s2 += d2
            s4 += d2*d2
    n = len(pts)
    return s2/(n*n), s4/(n*n)

for R,z in [(1.0,-1.), (1.7,-0.6), (2.0,0.), (0.9,0.53), (3.0,0.87)]:
    quad2, quad4 = direct_quad(R,z)
    target2, target4 = moments(R,z)
    assert abs(quad2-target2) / target2 < 0.0002
    assert abs(quad4-target4) / target4 < 0.0004
    checks += 2

for eps in [0.1,0.03,0.01,0.003]:
    h = sin(eps/2)**2
    t = h/(1+h)  # avoids subtracting two nearly equal cosines
    delta = F(4,3)*t*t
    # (rho-4/3) / (pi-alpha)^4 tends to 1/12.
    assert abs(delta/eps**4 - 1/12) < 0.004
    checks += 1

print('VERIFY_OK', checks, 'checks: 2206 rational, 10 quadrature, 4 asymptotic')
