"""Numerical geometry checks for the six-normal planar 2-design area law.

Run: python verify.py
Uses only the Python standard library.  These tests are finite corroboration,
not a substitute for the algebraic classification and area proof.
"""
import cmath
import math
import random

TAU = 2.0 * math.pi
SQ3 = math.sqrt(3.0)
RNG = random.Random(428621)
CHECKS = 0


def close(a, b, eps=3e-11):
    global CHECKS
    assert abs(a-b) < eps * (1.0 + abs(a) + abs(b)), (a, b)
    CHECKS += 1


def exact_design(beta, rotation):
    return [cmath.exp(1j * (rotation + 2.0 * k * math.pi / 3.0 + shift))
            for k in range(3) for shift in (0.0, beta)]


def area_of_edges(nodes, side_length):
    # Rotate normals counterclockwise to get ordered CCW edge vectors.
    vertices = [0j]
    for u in nodes:
        vertices.append(vertices[-1] + 1j * side_length * u)
    close(abs(vertices[-1]), 0.0)
    return 0.5 * sum((vertices[j].conjugate() * vertices[j+1]).imag
                     for j in range(len(nodes)))


def theoretical_area(beta, ell):
    return SQ3 * ell**2 / 2 * (1 + 2 * math.cos(beta - math.pi/3))


def harmonic_area(nodes, ell):
    s3 = sum(z**3 for z in nodes)/len(nodes)
    mu = abs(s3)
    assert mu < 1 + 1e-12
    mu = min(1.0, mu)
    return SQ3 * ell**2 / 2 * (1 + 2 * math.cos(2 * math.asin(mu)/3)), mu


for _ in range(1200):
    beta = (0.00001 + 0.99998 * RNG.random()) * (2 * math.pi/3)
    rotation = TAU * RNG.random()
    ell = 0.05 + 6 * RNG.random()
    z = exact_design(beta, rotation)
    close(abs(sum(z)), 0.0)
    close(abs(sum(w*w for w in z)), 0.0)
    area = area_of_edges(z, ell)
    a2 = theoretical_area(beta, ell)
    a3, mu = harmonic_area(z, ell)
    close(area, a2)
    close(area, a3)
    close(mu, abs(math.cos(3*beta/2)))
    deficit = 3*SQ3/2 * ell*ell - area
    close(deficit, SQ3*ell*ell*(1-math.cos(2*math.asin(mu)/3)))
    close(deficit >= -1e-11, True, 1e-11)
    if mu > 1e-6:
        ratio = deficit/(ell*ell*mu*mu)
        assert 2*SQ3/9-1e-8 <= ratio <= SQ3/2+1e-8
        CHECKS += 1

# Regular endpoint and degeneration endpoints.
for ell in (0.25, 1.0, 2.5):
    regular = exact_design(math.pi/3, 0.1)
    close(area_of_edges(regular, ell), 3*SQ3/2*ell**2)
    for b in (1e-7, 2*math.pi/3-1e-7):
        near = exact_design(b, 0.1)
        close(area_of_edges(near, ell), SQ3*ell**2, 1e-6)

# The analytic quadratic ratio increases because 3 - 4 sin^2(t) decreases.
values = [2*SQ3/(3-4*math.sin(j*math.pi/600)**2)**2 for j in range(101)]
for i in range(len(values)-1):
    assert values[i+1] > values[i]
    CHECKS += 1
close(values[0], 2*SQ3/9)

if __name__ == '__main__':
    print(f'PASS: {CHECKS} numerical consistency and boundary checks')
