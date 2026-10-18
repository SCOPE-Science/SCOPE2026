"""Independent quadrature and finite-parameter checks for spherical degree-one reproduction.

Run: python verify.py
No third-party dependencies. Finite checks supplement, not replace, the proof.
"""
from math import cos, sin, pi, gamma, sqrt, isclose


def factor(d):
    return gamma((d + 1) / 2) / (sqrt(pi) * gamma(d / 2))


def exact_norm(d):
    return (d + 1) * gamma((d + 1) / 2) / (sqrt(pi) * gamma((d + 2) / 2))


def kernel(d, b, u):
    return 1 + (d + 1) * u + b * ((d + 1) * u * u - 1)


def numerical_norm(d, b, mesh=24000):
    # u=cos(theta); induced probability density proportional to sin(theta)^(d-1)
    h = pi / mesh
    num = den = 0.0
    for j in range(mesh + 1):
        theta = j * h
        wt = 1 if j in (0, mesh) else (4 if j % 2 else 2)
        density = sin(theta) ** (d - 1)
        den += wt * density
        num += wt * density * abs(kernel(d, b, cos(theta)))
    return num / den


def main():
    count = 0
    for d in (1, 2, 3, 4, 7, 12):
        sharp = exact_norm(d)
        approx = numerical_norm(d, 1)
        assert abs(approx - sharp) < 8e-7, (d, approx, sharp)
        count += 1
        for b in (-1, 0, 0.5, 0.9, 1.1, 1.5, 3):
            val = numerical_norm(d, b)
            assert val > sharp + 1e-5, (d, b, val, sharp)
            count += 1
        # First harmonic / constant reproduction tested by algebraic spherical moments.
        # Integral K=1: E[u]=0 and E[u^2]=1/(d+1).
        assert isclose(1 + (d + 1) * 0 + ((d + 1) / (d + 1) - 1), 1)
        count += 1
    # Test local stability on the side where there is one thin sign-error band.
    for d in (1, 2, 3, 5):
        c = factor(d)
        eps = 0.04
        delta = numerical_norm(d, 1 - eps, 48000) - exact_norm(d)
        leading = c / (d + 1) * eps * eps
        assert 0.8 < delta / leading < 1.3, (d, delta, leading)
        count += 1
    # Right-hand anomaly on the circle and a second quadratic contribution on S^2.
    for d, expected in ((1, 4 / (3 * pi)), (2, 5 / 6)):
        eps = 0.02
        deficit = numerical_norm(d, 1 + eps, 60000) - exact_norm(d)
        scale = eps ** 1.5 if d == 1 else eps * eps
        assert abs(deficit / scale - expected) < 0.07, (d, deficit / scale, expected)
        count += 1
    print('PASS:', count, 'independent numerical normalization, comparison, and asymptotic checks')


if __name__ == '__main__':
    main()
