"""Exact finite-matrix checks for the Schatten-fourth weighted-shift identity.

The exact checks corroborate, but do not replace, the arbitrary-size proof.
Uses only Python's standard library.
"""
from fractions import Fraction as Q
from math import cos, pi, sin, sqrt


def conjugate_transpose(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a))]


def multiply(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def exact_quartic(weights, t):
    n = len(weights) + 1
    s = 1-t
    a = [[Q(0) for _ in range(n)] for _ in range(n)]
    for j, w in enumerate(weights):
        a[j + 1][j] = t * w
        a[j][j + 1] = s * w
    ata = multiply(conjugate_transpose(a), a)
    square = multiply(ata, ata)
    actual = sum((square[j][j] for j in range(n)), Q(0))
    predicted = (t**4 + s**4)*sum((w**4 for w in weights), Q(0))
    predicted += 4*t*t*s*s * sum((weights[j]**2 * weights[j + 1]**2
                                   for j in range(n-2)), Q(0))
    assert actual == predicted, (n, t, weights, actual, predicted)
    return actual


def check_path_extremizers():
    for n in range(3, 34):
        v = [sin((j+1)*pi/n) for j in range(n-1)]
        spectral_quotient = sum(v[j]*v[j+1] for j in range(n-2))/sum(z*z for z in v)
        assert abs(spectral_quotient - cos(pi/n)) < 1e-13
        u = [sin(2*(j+1)*pi/n) for j in range(n-1)]
        assert abs(sum(v[j]*u[j] for j in range(n-1))) < 1e-12
        lam2 = sum(u[j]*u[j+1] for j in range(n-2))/sum(z*z for z in u)
        assert abs(lam2-cos(2*pi/n)) < 1e-12
        eps = 0.001
        x = [v[j]+eps*u[j] for j in range(n-1)]
        assert min(x) >= 0
        norm2 = sum(z*z for z in x)
        projection = sum(x[j]*v[j] for j in range(n-1))**2 / sum(z*z for z in v)
        deficit = cos(pi/n)*norm2-sum(x[j]*x[j+1] for j in range(n-2))
        gap = (cos(pi/n)-cos(2*pi/n))*(norm2-projection)
        assert abs(deficit-gap) < 1e-11


if __name__ == "__main__":
    for n in range(2, 11):
        for t in (Q(0), Q(1,5), Q(1,2), Q(2,3), Q(1)):
            for offset in range(3):
                weights = [Q(((j+2)*(offset+3)) % 7 - 3, (j % 3)+1)
                           for j in range(n-1)]
                exact_quartic(weights, t)
    check_path_extremizers()
    print("SCHATTEN_FOURTH_SHIFT_EXACT_MATRIX_AND_PATH_CHECK_OK")
