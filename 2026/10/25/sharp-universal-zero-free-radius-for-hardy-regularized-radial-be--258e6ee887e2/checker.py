"""Exact rational sanity checks for the radial Hardy–Bergman kernel theorem.

No numerical experiment is used as a replacement for the infinite proof.
"""
from fractions import Fraction


def moment_alpha3(n):
    return Fraction(24, (n + 1) * (n + 2) * (n + 3) * (n + 4))


def certified_value_at_negative_r(r, kappa, degree):
    """Return exact truncated value and rigorous absolute geometric remainder bound."""
    total = Fraction(0)
    power = Fraction(1)
    for n in range(degree + 1):
        coefficient = 1 / (kappa + moment_alpha3(n))
        total += ((-1) ** n) * coefficient * power
        power *= r
    # All coefficients are between zero and 1/kappa.
    bound = power / (kappa * (1-r))
    return total, bound


def main():
    kappa = Fraction(1, 6)
    for r, n, wanted in [(Fraction(9, 10), 240, 'positive'),
                          (Fraction(24, 25), 480, 'negative')]:
        s, b = certified_value_at_negative_r(r, kappa, n)
        if wanted == 'positive':
            assert s-b > 0
        else:
            assert s+b < 0
        print('smooth beta weight alpha=3; kappa=1/6; t=-{}; N={};'.format(r,n),
              'central={:.12f}; error<={:.12g}; sign={}'.format(float(s),float(b),wanted))
    for kappa in [Fraction(1,3),Fraction(1),Fraction(2)]:
        # Center-mass limit: (1-t)K(t)=(kappa+t)/(kappa*(1+kappa)).
        a0 = 1/(1+kappa)
        a1 = 1/kappa
        assert a0 + (a1-a0)*(-kappa) == 0
        for r in [Fraction(0), Fraction(1,4), Fraction(3,4)]:
            # The exact triangle bound is attained by the center mass if r<kappa.
            if r < kappa and r < 1:
                exact = a0 - (a1-a0)*r
                bound = (kappa-r)/(kappa*(1+kappa))
                assert exact == bound
        print('sharp center-mass identity confirmed for kappa={}'.format(kappa))
    print('all exact-rational checks passed; general theorem follows from the written proof')

if __name__ == '__main__':
    main()
