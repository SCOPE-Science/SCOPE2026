"""Independent numerical checks of radial-annulus Fourier zero interlacing.
The mathematical argument is analytic; the finite checks are diagnostic only.
"""
from math import pi, sin, cos, sqrt
from scipy.special import jv, jvp
from scipy.optimize import brentq
from scipy.integrate import quad


def positive_zeros(order, count):
    roots = []
    h = 0.04
    x = h
    previous = jv(order, x)
    while len(roots) < count:
        y = x + h
        current = jv(order, y)
        if previous * current < 0:
            roots.append(brentq(lambda t: jv(order, t), x, y, xtol=1e-13))
        x, previous = y, current
        assert x < 1000
    return roots


def zero_function(nu, radius, t):
    return jv(nu, t) - radius ** nu * jv(nu, radius * t)


def zero_derivative(nu, radius, t):
    return jvp(nu, t) - radius ** (nu + 1) * jvp(nu, radius * t)


def energy(nu, t):
    return t ** (2 * nu) * (jv(nu, t) ** 2 + jv(nu - 1, t) ** 2)


cases = 0
max_residual = 0.0
for dimension in (2, 3, 4, 6):
    nu = dimension / 2
    knots = positive_zeros(nu - 1, 8)
    solid = positive_zeros(nu, 7)
    for radius in (0.1, 0.35, 0.7, 0.95):
        for k in range(7):
            left, right = knots[k:k + 2]
            t = brentq(lambda x: zero_function(nu, radius, x), left, right, xtol=1e-13)
            residual = abs(zero_function(nu, radius, t))
            max_residual = max(max_residual, residual)
            assert left < t < right
            assert zero_derivative(nu, radius, t) * jv(nu - 1, t) > 0
            assert energy(nu, t) > energy(nu, radius * t)
            cases += 1
        # The first root stays between contiguous-order Bessel zeros.
        assert knots[0] < solid[0] < knots[1]

# An exact one-dimensional double zero: r=1/5, t=5*pi/2.
r = 1 / 5
t = 5 * pi / 2
assert abs(sin(t) - sin(r * t)) < 1e-14
assert abs(cos(t) - r * cos(r * t)) < 1e-14
# Its second derivative in sin(t)-sin(r*t) is nonzero.
assert abs(-sin(t) + r * r * sin(r * t)) > 0.9
for radius in (0.2, 0.6):
    for t in (1.7, 4.5, 9.2):
        planar_integral = 2 * pi * quad(lambda s: s * jv(0, s * t), radius, 1,
                                      epsabs=1e-12)[0]
        planar_formula = 2 * pi / t * zero_function(1, radius, t)
        assert abs(planar_integral - planar_formula) < 5e-12
        spatial_integral = 4 * pi * quad(lambda s: s * sin(s * t) / t,
                                       radius, 1, epsabs=1e-12)[0]
        spatial_formula = (2*pi)**1.5 / t**1.5 * zero_function(1.5, radius, t)
        assert abs(spatial_integral - spatial_formula) < 5e-12
print(f"checked interlacing and derivative orientation: {cases} roots")
print("12 independent radial quadratures matched Fourier-Bessel formulas")
print(f"maximum Bessel-difference residual: {max_residual:.3e}")
print("dimension-one resonant double zero: verified at radius 1/5, frequency 5*pi/2")
print("all finite diagnostics passed; analytic proof is required for global claims")
