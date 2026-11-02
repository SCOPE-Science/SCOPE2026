"""Independent finite-residue checks for a quadratic-form root-count lemma.

This checks finite-field identities, not the asymptotic density theorem.
"""
from fractions import Fraction


def primes_below(n):
    return [p for p in range(2, n) if all(p % d for d in range(2, int(p**0.5) + 1))]


def legendre(a, p):
    v = pow(a % p, (p - 1) // 2, p)
    return 0 if v == 0 else 1 if v == 1 else -1


def test_root_counts():
    forms = [(1, 0, 1), (1, 1, 1), (1, 3, 2), (2, 5, 3), (3, -2, 3), (1, 5, 1)]
    tests = 0
    for A, B, C in forms:
        delta = B * B - 4 * A * C
        for ell in primes_below(150):
            if ell == 2 or (2 * A * C * delta) % ell == 0:
                continue
            chi = legendre(delta, ell)
            count = sum(
                (A*u*u + B*u*v + C*v*v) % ell == 0
                for u in range(1, ell) for v in range(1, ell)
            )
            assert count == (ell - 1) * (1 + chi), (A, B, C, ell, count)
            tests += 1
    return tests


def test_moments():
    forms = [(1, 0, 1), (1, 1, 1), (1, 3, 2), (2, 5, 3), (3, -2, 3)]
    tests = 0
    for A, B, C in forms:
        delta = B * B - 4*A*C
        for ell in (3, 5, 7, 11, 13):
            if (2*A*C*delta) % ell == 0:
                continue
            chi = legendre(delta, ell)
            values = [int((A*u*u + B*u*v + C*v*v) % ell == 0)
                      for u in range(1, ell) for v in range(1, ell)]
            prob = Fraction(sum(values), len(values))
            assert prob == Fraction(1 + chi, ell - 1)
            mean = Fraction(chi) * (prob - Fraction(1, ell))
            assert mean == Fraction(1, ell) + Fraction(1 + chi, ell * (ell - 1))
            assert prob*(1-prob) <= Fraction(3, ell)
            tests += 1
    return tests


if __name__ == '__main__':
    a = test_root_counts()
    b = test_moments()
    print(f'PASS: {a} local unit-root counts; {b} exact mean/variance checks')
