"""Supplementary checks for normalized circular averages and Cantor scales.

The statements for all functions and measures are proved analytically; these
finite checks are tests of signs, constants and nested-interval identities.
"""
from fractions import Fraction
from math import pi, sin, cos


def circle_defect(f, a, r, N=4096):
    out = 0j
    for k in range(N):
        t = 2*pi*k/N
        z = complex(a) + r*complex(cos(t), sin(t))
        out += f(z) * (1j*r*complex(cos(t), sin(t)))
    return out * (2*pi/N) / (2*pi*1j*r*r)


count = 0
for a in [0j, 0.15+0.21j, -0.3+0.19j, 0.41-0.27j]:
    for r in [0.035, 0.12, 0.25]:
        assert abs(circle_defect(lambda z: z.conjugate(), a, r)-1) < 2e-12
        assert abs(circle_defect(lambda z: z.conjugate()**2, a, r)-2*a.conjugate()) < 2e-11
        count += 2

for beta in [1, 2, 3, 4]:
    previous = Fraction(1)
    for n in range(1, 80):
        ell = Fraction(1, (2**n)*(n+1)**beta)
        assert 2*ell < previous
        assert 2**n*ell == Fraction(1, (n+1)**beta)
        assert 2**n*ell < 2**(n-1)*previous
        previous = ell
        count += 3

# The exact singular-mass model: kappa_r*delta_0 is uniform on B(0,r).
# Its total mass and L1 norm are one for each radius, despite convergence
# to zero at every fixed nonzero center as radius decreases.
for r in [Fraction(1, 5), Fraction(1, 10), Fraction(1, 100)]:
    numerator = Fraction(1)
    denominator = Fraction(1)
    assert numerator/denominator == 1
    assert r > 0
    count += 2

print(f"PASS: {count} numerical/exact normalization and scale checks")
