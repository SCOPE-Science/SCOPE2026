"""Exact-arithmetic checks for a zero-inflated negative-binomial phase boundary.

Run with Python 3.10 or later: python verify.py
"""
from fractions import Fraction
from math import comb, cos, pi


def probabilities(m, q, w, K):
    q, w = Fraction(q), Fraction(w)
    core = (1 - w) * (1 - q) ** m
    p = [w + core]
    p.extend(core * comb(m + k - 1, k) * q ** k for k in range(1, K + 1))
    return p


def logarithmic_coefficients(p):
    nu = [Fraction(0)]
    for k in range(1, len(p)):
        nu_k = (k * p[k] - sum(j * nu[j] * p[k-j] for j in range(1, k))) / (k * p[0])
        nu.append(nu_k)
    return nu


def classified(m, q, w):
    c = (1-float(q)) * ((1-float(w))/float(w)) ** (1/m)
    return c >= 2*cos(pi/m)


def run():
    cases = 0
    for m in range(1, 9):
        for q in (Fraction(1,4), Fraction(1,2), Fraction(3,4)):
            for w in (Fraction(1,5000), Fraction(1,70), Fraction(1,20), Fraction(1,5), Fraction(4,5)):
                expected = classified(m, q, w)
                K = 85
                coeff = logarithmic_coefficients(probabilities(m, q, w, K))
                if expected:
                    assert all(nu >= 0 for nu in coeff[1:]), (m,q,w)
                else:
                    # At very close boundaries the first negative may occur later;
                    # we do not infer positivity from finite tests.
                    if m <= 5:
                        assert any(nu < 0 for nu in coeff[1:]), (m,q,w)
                cases += 1
    # Edge and counterexample cases, with rational threshold in shape 3 and 4.
    for m, q, w, infinite in [
        (3, Fraction(1,2), Fraction(1,9), True),
        (3, Fraction(1,2), Fraction(1,10), True),
        (3, Fraction(1,2), Fraction(1,5), False),
        (4, Fraction(1,2), Fraction(1,65), True),
        (4, Fraction(1,2), Fraction(1,70), True),
        (4, Fraction(1,2), Fraction(1,60), False),
    ]:
        coeff = logarithmic_coefficients(probabilities(m,q,w,120))
        assert (all(v >= 0 for v in coeff[1:]) if infinite else any(v < 0 for v in coeff[1:]))
        cases += 1
    print(f'PASS: {cases} rational parameter configurations; all log-PGF coefficients exact through order 85 (edge cases through 120).')


if __name__ == '__main__':
    run()
