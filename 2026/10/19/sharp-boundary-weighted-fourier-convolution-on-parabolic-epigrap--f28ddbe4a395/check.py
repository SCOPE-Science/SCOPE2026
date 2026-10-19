#!/usr/bin/env python3
"""Independent numerical checks for the weighted Fourier convolution paraboloid formulas.
These finite computations do not establish any continuum operator-norm assertion.
"""
import math


def simpson(f, a, b, intervals=200000):
    assert intervals % 2 == 0
    step = (b-a) / intervals
    total = f(a) + f(b)
    for i in range(1, intervals):
        total += (4 if i % 2 else 2) * f(a + i*step)
    return total * step / 3


def unit_ball_volume(d):
    return math.pi ** (d / 2) / math.gamma(d / 2 + 1)


def weight_coefficient(d):
    return 2**(d/2 + 2) * unit_ball_volume(d)/(d+2)


def kernel_coeff(d):
    return 1/weight_coefficient(d)


def horizontal_integral(d, h_plus_k, cutoff):
    sphere_area = d * unit_ball_volume(d)
    power = (d+2)/2
    return kernel_coeff(d)*sphere_area * simpson(
        lambda r: r**(d-1) / (h_plus_k + r*r/2)**power,
        0.0, cutoff, 120000)


# An independent direct spherical section integral for the Macbeath-region volume.
for d in range(1, 6):
    for H in (0.3, 1.0, 2.7):
        radius = math.sqrt(2*H)
        numerical = 2*d*unit_ball_volume(d) * simpson(
            lambda r: max(0, H-r*r/2) *r**(d-1), 0, radius, 2000)
        expected = weight_coefficient(d) * H**((d+2)/2)
        assert math.isclose(numerical, expected, rel_tol=5e-8), (d, H, numerical, expected)

# Independent horizontal integrals at two positive vertical heights.
for d in range(1, 6):
    for A in (0.3, 1.0, 2.7):
        numerical = horizontal_integral(d, A, cutoff=600*math.sqrt(A))
        expected = (d+2)/(4*A)
        assert math.isclose(numerical, expected, rel_tol=2e-5), (d, A, numerical, expected)

# Carleman kernel after logarithmic unitary: its L1 integral is pi.
j = lambda s: 1/(2*math.cosh(s/2))
integral = simpson(j, -38, 38, 80000)
assert abs(integral - math.pi) < 3e-8, (integral, math.pi)

# Rayleigh quotient of normalized log-box probes, convergence from below.
def box_carleman_quotient(L):
    return simpson(lambda s: (1-abs(s)/(2*L)) * j(s), -2*L, 2*L, 40000)
previous = 0
for L in (2, 8, 32, 128):
    quotient = box_carleman_quotient(L)
    assert previous < quotient < math.pi, (L, quotient)
    previous = quotient
assert math.pi - previous < 0.06

for d in range(1, 6):
    print(f'd={d}: weight factor={weight_coefficient(d):.12g}, sharp candidate={math.pi*(d+2)/4:.12g}')
print(f'Carleman integral={integral:.12f}, log-box L=128 quotient={previous:.12f}')
print('PASS: direct volume integrals, horizontal kernel masses, Carleman consistency')
