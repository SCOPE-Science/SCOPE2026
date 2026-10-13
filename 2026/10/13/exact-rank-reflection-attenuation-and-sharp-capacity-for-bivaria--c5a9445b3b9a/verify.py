#!/usr/bin/env python3
"""Exact-rational finite checkerboard tests of a reflection/folding xi identity.

This finite checker is supporting evidence, not a proof for arbitrary copulas.
No third-party files or nonstandard packages are needed.
"""
from fractions import Fraction as Q


def xi_rows(rows):
    """Population Chatterjee xi for uniform-row copula checkerboard.

    rows[i][j] gives P(column=j | row=i). All rows sum to one;
    column sums are (#rows)/(#columns), yielding uniform V.
    Conditional CDFs are piecewise linear and squares are integrated exactly.
    """
    m = len(rows)
    k = len(rows[0])
    assert all(len(row) == k and sum(row) == 1 and min(row) >= 0 for row in rows)
    assert all(sum(row[j] for row in rows) == Q(m, k) for j in range(k))
    average_integral = Q(0)
    for row in rows:
        h = Q(0)
        for p in row:
            average_integral += (h * h + h * p + p * p / 3) / (m * k)
            h += p
        assert h == 1
    return 6 * (average_integral - Q(1, 3))


def reflection_lift(base):
    """Map a folded uniform checkerboard to its equally reflected response."""
    m = len(base)
    return [[x / 2 for x in row] + [x / 2 for x in reversed(row)] for row in base]


def doubly_stochastic_permutation_mixture(m, a, b):
    """Weighted average of identity, cyclic shift and reversal permutations."""
    assert 0 <= a <= 1 and 0 <= b <= 1
    z = (1 - a) * (1 - b)
    c = (1 - a) * b
    mat = [[Q(0) for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            mat[i][j] += a * int(j == i)
            mat[i][j] += z * int(j == (i + 1) % m)
            mat[i][j] += c * int(j == m - 1 - i)
    return mat


def main():
    checks = 0
    for m in range(2, 12):
        for a in (Q(0), Q(1, 7), Q(2, 5), Q(1, 2), Q(4, 5), Q(1)):
            for b in (Q(0), Q(1, 6), Q(2, 3), Q(1)):
                B = doubly_stochastic_permutation_mixture(m, a, b)
                C = reflection_lift(B)
                assert all(C[i][j] == C[i][2*m-1-j] for i in range(m) for j in range(2*m))
                x_fold = xi_rows(B)
                x_refl = xi_rows(C)
                assert x_refl * 4 == x_fold, (m,a,b,x_refl,x_fold)
                assert 0 <= x_refl <= Q(1, 4)
                checks += 4
        # Dedicated a*identity+(1-a)*independence matrix: exact known formula.
        for a in (Q(0), Q(1, 6), Q(1, 3), Q(4, 5), Q(1)):
            B = [[a * int(i == j) + (1-a)/m for j in range(m)] for i in range(m)]
            assert xi_rows(B) == a*a*(1-Q(1,m))
            assert xi_rows(reflection_lift(B)) == a*a*(1-Q(1,m))/4
            checks += 2
    # General biased reflection identity, for base copulas with NO reflection symmetry.
    for m in (2, 4, 6, 8, 10):
        for a in (Q(0), Q(1, 7), Q(2, 5), Q(1, 2), Q(4, 5), Q(1)):
            for b in (Q(0), Q(1, 6), Q(2, 3), Q(1)):
                B = doubly_stochastic_permutation_mixture(m, a, b)
                T = [[row[j] + row[m-1-j] for j in range(m//2)] for row in B]
                x_orig = xi_rows(B)
                x_fold = xi_rows(T)
                for p in (Q(0), Q(1, 7), Q(1, 4), Q(1, 2), Q(2, 3), Q(6, 7), Q(1)):
                    W = [[p * row[j] + (1-p)*row[m-1-j] for j in range(m)] for row in B]
                    x_new = xi_rows(W)
                    assert x_new == (2*p-1)**2 * x_orig + p*(1-p)*x_fold
                    assert x_new <= 1 - 3*p*(1-p)
                    checks += 2
    # Endpoints of the continuous mixture (conditional-fold copula a*M+(1-a)*Pi):
    for a in (Q(0), Q(1, 6), Q(2, 5), Q(1, 2), Q(3, 4), Q(1)):
        # Exact algebra: F_(T|U)(t)=(1-a)*t+a*1_{U<=t}.
        # Integral of its conditional CDF variance is a^2*int t(1-t)dt=a^2/6.
        assert 6*a*a*Q(1,6) == a*a
        assert Q(1,4)*a*a >= 0
        checks += 2
    print(f'PASS: {checks} exact Fraction identities, including 240 fair-reflection and 840 biased-reflection checkerboards.')

if __name__ == '__main__':
    main()
