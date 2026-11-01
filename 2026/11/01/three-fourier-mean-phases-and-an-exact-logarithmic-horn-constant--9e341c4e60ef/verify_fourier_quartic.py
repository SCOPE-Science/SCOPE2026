"""Reproducibility checks for the quartic-disk Fourier calculation.

Requires Python 3, scipy and numpy. These finite diagnostics are not a proof
of the asymptotic or compactness assertions.
"""
import math
from scipy.integrate import quad
from scipy.special import gamma


def axial(t):
    # Unnormalised Fourier transform of 1_{x^4+y^4<=1} at (t,0).
    return 4.0 * quad(lambda x: (1.0-x**4)**0.25,
                      0.0, 1.0, weight="cos", wvar=t,
                      epsabs=2e-11, epsrel=2e-11, limit=500)[0]


def angled(t, angle):
    c, s = math.cos(angle), math.sin(angle)
    if abs(s) < 1.e-13:
        return axial(t)
    return 4.0 * quad(
        lambda x: math.cos(t*c*x) * math.sin(t*s*(1.-x**4)**0.25)/(t*s),
        0.0, 1.0, epsabs=1.e-9, epsrel=1.e-9, limit=700)[0]


def main():
    area = 4.0 * gamma(1.25)**2 / gamma(1.5)
    C = 4.0 * math.sqrt(2.0) * gamma(1.25)
    residue = 2.5*C**2/(2.0*area)
    assert abs(residue - 5.0*math.sqrt(math.pi)) < 2.e-13
    angular = residue*4.0/3.0
    assert abs(angular - 20.0*math.sqrt(math.pi)/3.0) < 2.e-13
    assert abs(area - 3.7081493546027438) < 1.e-13
    # At large frequency the leading endpoint expansion becomes precise.
    for t in (50.0, 100.0, 200.0, 500.0, 1000.0):
        asym = C*t**(-1.25)*math.cos(t-5*math.pi/8)
        deviation = abs(axial(t)-asym) * t**1.25
        assert deviation < 0.065, (t, deviation)
    # Numerical comparison of the 1D projection-integral identity with
    # the zero-angle limit for each frequency.
    for t in (7.0, 23.0, 71.0):
        assert abs(angled(t, 1.e-5)-axial(t)) < 2.e-6
        assert abs(angled(t, -.1)-angled(t, .1)) < 1.e-9
        assert abs(angled(t, .3)-angled(t, -.3)) < 1.e-9
    print("PASS: 17 exact-constant and Fourier-quadrature diagnostics")
    print(f"area={area:.12f}; axial residue={residue:.12f}; angular coefficient={angular:.12f}")

if __name__ == '__main__':
    main()
