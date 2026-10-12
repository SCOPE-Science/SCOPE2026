"""Exact finite verification for the one-exceptional-weight Bernoulli theorem.

Requires Python 3 standard library only. Universal estimates are proved in
RESULT.md; this checker supplies the complete finite n<=19 part and
independent exact checks of the displayed binomial identities.
"""
from fractions import Fraction
from math import comb


def choose(n, j):
    return comb(n, j) if 0 <= j <= n else 0


def finite_case(n, k):
    assert 1 <= n <= 19 and 1 <= k <= n
    numerators = [choose(n, j) + choose(n, j-k)
                  for j in range(n+k+1)]
    assert len(numerators) == n+k+1
    assert all(v > 0 for v in numerators)
    assert sum(numerators) == 2**(n+1)
    q = Fraction((n+k+1)*max(numerators)**2, 4**(n+1))
    assert q < 1, (n, k, q)
    return q, len(numerators)


def main():
    cases = 0
    atoms = 0
    worst = (Fraction(0), (0, 0))
    for n in range(1, 20):
        for k in range(1, n+1):
            ratio, inspected = finite_case(n, k)
            cases += 1
            atoms += inspected
            if ratio > worst[0]:
                worst = (ratio, (n, k))
    assert cases == 190
    assert worst == (Fraction(3, 4), (1, 1)), worst

    # Separate independent structural checks, not surrogates for induction.
    central_tests = 0
    for n in range(1, 1001):
        c = Fraction(comb(n, n//2), 2**n)
        assert (n+1)*c*c <= Fraction(3, 4)
        if n % 2 == 0 and n >= 4:
            assert (n+n//2+1)*c*c < 1
        if n % 2 == 1:
            assert (n+n//2+1)*c*c < 1
        central_tests += 1
    for m in range(1, 1001):
        assert (3*m+1)*(2*m+2)**2 - (3*m+4)*(2*m+1)**2 == m
    print('PASS:', cases, 'complete small-case (n,k) pairs;', atoms,
          'positive mass positions;', central_tests, 'central-mass samples;'
          ' worst small-case ratio =', worst[0], 'at', worst[1])


if __name__ == '__main__':
    main()
