"""Exact checks for ordinary additive infinite divisibility of geometric sample maxima.

Run with: python3 geometric_verify.py
Uses only the Python standard library. All arithmetic is rational.
The infinite-parameter proof is in RESULT.md, not inferred from this grid.
"""
from fractions import Fraction
from math import comb


def mass(m, q, k):
    # Maximum of m iid variables with mass (1-q)q^j, j>=0.
    return (1-q**(k+1))**m - (1-q**k)**m


def log_coefficient_2(m, q):
    a, b, c = (mass(m,q,j) for j in range(3))
    assert a > 0
    return c/a - Fraction(1,2)*(b/a)**2


def direct_log_coefficient_2(m, q):
    u, v = 1+q, 1+q+q*q
    return v**m - (u**(2*m)+1)/2


def verify():
    checked = 0
    for denominator in range(2,35):
        for numerator in range(1,denominator):
            q = Fraction(numerator,denominator)
            for m in range(1,31):
                actual = log_coefficient_2(m,q)
                predicted = direct_log_coefficient_2(m,q)
                assert actual == predicted, (m,q)
                assert (actual > 0 if m <= 2 else actual < 0), (m,q,actual)
                checked += 1
    # A second independent exact check of the closed generating-function
    # identities for two and three draws, coefficient by coefficient.
    rational_coefficient_checks = 0
    for q in (Fraction(1,9), Fraction(2,5), Fraction(3,4), Fraction(9,10)):
        p = 1-q
        for m in (2,3):
            if m==2:
                # p^2(1+q*z) / ((1-q*z)(1-q^2*z)).
                numerator = [p*p,p*p*q]
            else:
                # p^3(1+2q(1+q)*z+q^3*z^2) / product_{j=1}^3(1-q^j*z).
                numerator = [p**3,2*p**3*q*(1+q),p**3*q**3]
            den = [Fraction(1)]
            for j in range(1,m+1):
                new = [Fraction(0)]*(len(den)+1)
                for k,d in enumerate(den):
                    new[k]+=d
                    new[k+1]-=d*q**j
                den=new
            coefficients = []
            for k in range(0,18):
                coeff=(numerator[k] if k<len(numerator) else 0)
                for j in range(1,min(k,len(den)-1)+1):
                    coeff-=den[j]*coefficients[k-j]
                coefficients.append(coeff)
                assert coeff == mass(m,q,k),(m,q,k)
                rational_coefficient_checks+=1
    # The all-parameter certificate, to be checked algebraically in the proof:
    # (1+q)^6 + 1 - 2(1+q+q^2)^3 = q^2(3+6q+3q^2-q^4).
    for d in range(2,51):
        for n in range(1,d):
            q=Fraction(n,d)
            left=(1+q)**6 + 1 - 2*(1+q+q*q)**3
            right=q*q*(3+6*q+3*q*q-q**4)
            assert left == right and right > 0
    print(f'VERIFY_OK log_coeff_exact={checked} generating_coeff_exact={rational_coefficient_checks} positive_cubic_certificate=True')

if __name__=='__main__':
    verify()
