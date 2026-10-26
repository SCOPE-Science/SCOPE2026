"""Reproduce exact degree-five identities and a bounded-integrand witness.

Only standard-library modules are required. The proof of the node minimum and
asymptotic claims is mathematical, not inferred from these finite tests.
"""
from fractions import Fraction
from math import exp, sqrt


def moments(L, eps):
    return (Fraction(1) + eps * (L * L - 1),
            3 * (Fraction(1) + eps * (L**4 - 1)))


def check_exact(L, eps):
    m2, m4 = moments(L, eps)
    radius_sq = m4 / m2
    wing = m2 * m2 / (2 * m4)
    center = 1 - 2 * wing
    assert wing > 0 and center > 0
    assert 2 * wing * radius_sq == m2
    assert 2 * wing * radius_sq * radius_sq == m4
    # The componentwise rule has weights 2/3 at zero, and (1-eps)/6,
    # eps/6 at each pair ±sqrt(3), ±L sqrt(3).
    assert (1-eps) + eps == 1
    assert (1-eps) + eps * L * L == m2
    assert 3*((1-eps) + eps * L**4) == m4
    # Odd moments 1,3,5 vanish in both rules by point reflection.
    return True


def gaussian_witness(L):
    eps = L**-3
    m2 = 1 + eps*(L*L-1)
    m4 = 3*(1 + eps*(L**4-1))
    a2 = m4/m2
    wing = m2*m2/(2*m4)
    q3 = 1 - 2*wing*(1 - exp(-a2))
    q5 = 2/3 + (1-eps)*exp(-3)/3 + eps*exp(-3*L*L)/3
    exact = (1-eps)/sqrt(3) + eps/sqrt(1+2*L*L)
    return q3, q5, exact


def main():
    cases = 0
    for L in [2, 3, 5, 7, 11, 17, 29, 53, 101, 401]:
        for den in [3, 5, 11, 17, 43, 97]:
            eps = Fraction(1, den)
            assert check_exact(Fraction(L), eps)
            cases += 1
    for L in [20, 100, 1000, 10000]:
        q3, q5, exact = gaussian_witness(L)
        assert q3 > q5 > exact
    q3, q5, exact = gaussian_witness(10000)
    assert abs(q3-1)<1e-4
    assert abs(q5-(2/3+exp(-3)/3))<1e-8
    assert abs(exact-1/sqrt(3))<1e-8
    print(f"PASS: {cases} exact parameter checks, four bounded-integrand comparisons, three asymptotic checks")
    print(f"L=10000: direct={q3:.12f}, componentwise={q5:.12f}, integral={exact:.12f}")

if __name__ == '__main__':
    main()
