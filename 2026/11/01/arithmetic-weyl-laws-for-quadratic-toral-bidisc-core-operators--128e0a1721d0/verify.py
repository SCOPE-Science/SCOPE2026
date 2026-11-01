"""Finite reproducibility checks for quadratic toral core spectral Weyl coefficients.

Not a substitute for proofs of infinite asymptotics or originality.
"""
from fractions import Fraction
from math import pi, sin, cos, gcd


def moments(c):
    a = [Fraction(1), -2 * c, Fraction(1)]
    return {k: sum((a[j + k] * a[j] for j in range(3-k)), Fraction(0)) for k in range(3)}


def monic_opuc_constant(c, n):
    """Constant term of degree-n monic polynomial orthogonal under |z^2-2cz+1|^2."""
    f = moments(c)
    def w(k): return f.get(abs(k), Fraction(0))
    A = [[w(j - k) for j in range(n)] + [-w(n - k)] for k in range(n)]
    for j in range(n):
        t = next((i for i in range(j, n) if A[i][j]), None)
        assert t is not None
        A[j], A[t] = A[t], A[j]
        u = A[j][j]
        A[j] = [v / u for v in A[j]]
        for i in range(n):
            if i != j:
                m = A[i][j]
                A[i] = [A[i][k] - m * A[j][k] for k in range(n + 1)]
    return A[0][-1]


def coefficient(q):
    if q % 2:
        return 4 / (q * sin(pi / (2 * q)))
    return 4 / (q * (sin(pi / (2 * q)) / cos(pi / (2 * q))))


def check():
    tests = 0
    for c, theta in [(Fraction(0), pi / 2), (Fraction(1,2), pi / 3), (Fraction(-1,2), 2*pi/3)]:
        for n in range(2, 20):
            alpha = -monic_opuc_constant(c,n)
            assert abs(float(alpha)) < 1
            # The leading Fisher-Hartwig term is 2 cos((n+2) theta)/(n-1)
            # for alpha_{n-1}, with O(n^-2) corrections.
            bound = 50 / (n * n)
            assert abs(float(alpha) - 2*cos((n+2)*theta)/(n-1)) < bound, (c,n,alpha)
            tests += 1
    assert abs(coefficient(2)-2.0) < 1e-12
    assert abs(coefficient(3)-8/3) < 1e-12
    tests += 2
    for q in range(2,101):
        mean = sum(abs(cos(pi*r/q)) for r in range(q)) / q
        assert abs(4*mean - coefficient(q)) < 1e-12, q
        if q % 2:
            assert 8/pi < coefficient(q) <= 8/3 + 1e-12
        else:
            assert 2 - 1e-12 <= coefficient(q) < 8/pi
        tests += 2
    for q in range(2,55):
        for p in range(1,q):
            if gcd(p,q) == 1:
                mean = sum(abs(cos(pi*p*r/q)) for r in range(q)) / q
                assert abs(4*mean - coefficient(q)) < 1e-12
                tests += 1
    print('PASS', tests, 'finite moment, phase sum, parity and coprime-residue checks')

if __name__ == '__main__': check()
