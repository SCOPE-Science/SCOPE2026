"""Finite diagnostics for the power-weighted Rhaly singular-value Weyl law.

These calculations test only finite matrices and finite generalized strings;
they do not establish the infinite-dimensional asymptotic theorem.
"""
import math


def constant(exponent):
    g = exponent
    return 2**(-1/g) * math.gamma((g-1)/(2*g)) / (math.sqrt(math.pi)*math.gamma(1-1/(2*g)))


def count_string(exponent, radius, length):
    """Sturm count for q_N(w) minus radius^(2g) * weighted_mass(w)."""
    lam = float(radius)**(2*exponent)
    prev = None
    negative = 0
    for j in range(1, length+1):
        pivot = (1.0 if j == length else 2.0) - lam * j**(-2*exponent)
        if prev is not None:
            pivot -= 1.0 / prev
        if abs(pivot) < 1e-12:
            pivot = -1e-12
        negative += pivot < 0
        prev = pivot
    return negative


def check():
    for g in [1.5, 2.0, 3.0]:
        C = constant(g)
        assert C > 1
        # The remote free boundary causes a small positive missing-tail bias.
        for r in [80, 160]:
            m = int((300 if g < 2 else 90)*r)
            observed = count_string(g, r, m)/r
            assert 0 < C-observed < 0.07, (g, r, C, observed)
        assert math.isfinite(C**g)
    for g in [1.5, 2.0, 3.0]:
        n = 45
        mat = [[j**(-g) if k <= j else 0.0 for k in range(1,n+1)] for j in range(1,n+1)]
        direct = sum(abs(z)**2 for row in mat for z in row)
        expected = sum(j**(1-2*g) for j in range(1,n+1))
        assert abs(direct-expected) <= 1e-10
    print('PASS: finite Hilbert--Schmidt and string-phase diagnostics')
    print('Example exponent 2 coefficient:', constant(2.0)**2)


if __name__ == '__main__':
    check()
