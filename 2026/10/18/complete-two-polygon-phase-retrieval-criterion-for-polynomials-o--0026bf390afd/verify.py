"""Deterministic checks for two regular-polygon intensity sampling of polynomials.

Numerical tests supplement, and do not substitute for, the all-degree proof.
Run: python3 verify.py
"""
import math
import numpy as np


def intensity(coeff, points):
    return np.abs(np.polynomial.polynomial.polyval(points, coeff)) ** 2


def circle_samples(coeff, degree, radius, origin):
    j = np.arange(2 * degree)
    theta = origin + np.pi * j / degree
    z = radius * np.exp(1j * theta)
    return theta, intensity(coeff, z)


def positive_fourier_coefficient(coeff, radius, k):
    degree = len(coeff) - 1
    return radius ** k * sum(
        coeff[j + k] * np.conj(coeff[j]) * radius ** (2 * j)
        for j in range(degree + 1 - k)
    )


def map_rank(degree, radius1, radius2, phi, psi):
    z = np.concatenate([
        rr * np.exp(1j * (origin + np.arange(2 * degree) * np.pi / degree))
        for rr, origin in ((radius1, phi), (radius2, psi))
    ])
    rows = []
    for zz in z:
        v = zz ** np.arange(degree + 1)
        row = [abs(v[j]) ** 2 for j in range(degree + 1)]
        for j in range(degree + 1):
            for k in range(j + 1, degree + 1):
                cross = v[j] * np.conj(v[k])
                row.extend((2 * cross.real, 2 * cross.imag))
        rows.append(row)
    return int(np.linalg.matrix_rank(np.asarray(rows, dtype=float), tol=1e-8))


def main():
    rng = np.random.default_rng(20260923)
    tests = 0
    for d in range(1, 9):
        r, s, phi = 0.7, 1.3, 0.17
        psi = phi + np.pi / (4 * d)
        assert map_rank(d, r, s, phi, psi) == 4 * d
        tests += 1
        for _ in range(60):
            coeff = rng.normal(size=d + 1) + 1j * rng.normal(size=d + 1)
            circle_data = []
            for radius, angle in ((r, phi), (s, psi)):
                theta, y = circle_samples(coeff, d, radius, angle)
                circle_data.append((radius, angle, theta, y))
                for k in range(d):
                    got = np.mean(y * np.exp(-1j * k * theta))
                    expected = positive_fourier_coefficient(coeff, radius, k)
                    assert abs(got - expected) < 1e-8 * (1 + abs(expected))
                    tests += 1
                expected_top = positive_fourier_coefficient(coeff, radius, d)
                alias = np.mean(y * np.asarray([(-1) ** j for j in range(2 * d)]))
                assert abs(alias - 2 * np.real(expected_top * np.exp(1j * d * angle))) < 1e-8 * (1 + abs(alias))
                tests += 1
            measured = []
            matrix = []
            for radius, angle, theta, y in circle_data:
                alias = np.mean(y * (-1.0) ** np.arange(2 * d))
                measured.append(alias / (2 * radius ** d))
                matrix.append([np.cos(d * angle), -np.sin(d * angle)])
            top = np.linalg.solve(np.asarray(matrix), np.asarray(measured))
            target = coeff[d] * np.conj(coeff[0])
            assert abs(complex(*top) - target) < 1e-7 * (1 + abs(target))
            tests += 1
        # Explicit nonuniqueness if both radii coincide, regardless of offset.
        z = r * np.exp(1j * (phi + np.arange(2 * d) * np.pi / d))
        z_other = r * np.exp(1j * (psi + np.arange(2 * d) * np.pi / d))
        a = np.zeros(d + 1, dtype=complex)
        b = np.zeros(d + 1, dtype=complex)
        a[1], b[0] = 1, r
        assert np.max(abs(intensity(a, np.r_[z, z_other]) - intensity(b, np.r_[z, z_other]))) < 1e-10
        tests += 1
        # Explicit nonuniqueness if the polygons have d-fold aligned origins.
        a, b = np.zeros(d + 1, complex), np.zeros(d + 1, complex)
        a[0] = b[0] = 1
        a[d] = 1j * np.exp(-1j * d * phi)
        b[d] = -1j * np.exp(-1j * d * phi)
        samples = np.concatenate([
            rr * np.exp(1j * (origin + np.arange(2 * d) * np.pi / d))
            for rr, origin in ((r, phi), (s, phi + np.pi / d))
        ])
        assert np.max(abs(intensity(a, samples) - intensity(b, samples))) < 1e-10
        tests += 1
    print(f'VERIFY_OK {tests} deterministic finite comparisons; tested degrees 1 through 8')


if __name__ == '__main__':
    main()
