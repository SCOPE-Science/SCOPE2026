#!/usr/bin/env python3
"""Exact finite corroboration of a four-point Fourier construction.

No third-party dependencies. Universal statements rely on the written proof.
"""
from itertools import product


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))


def dot(u, v, p):
    return (u[0] * v[0] + u[1] * v[1]) % p


def cyclotomic_zero(terms, p):
    """Test exact vanishing in Z[ζ_p] via Φ_p(x)=1+...+x^(p-1)."""
    c = [0] * p
    for exponent, integer_coeff in terms:
        c[exponent % p] += integer_coeff
    return len(set(c)) == 1


def test_witnesses(limit=800):
    tested = 0
    for p in range(3, limit):
        if not is_prime(p) or p % 8 != 3:
            continue
        roots = [a for a in range(p) if (a * a + 2) % p == 0]
        assert len(roots) == 2, (p, roots)
        a = roots[0]
        S = [(0, 0), (0, 1), (a, 0), (a, (-1) % p)]
        assert len(set(S)) == 4
        weights = [(1, 0), (-1, 0), (1, 1), (-1, 1)]
        for xi in S:
            terms = [(dot(xi, x, p) + exponent, integer_coeff)
                     for x, (integer_coeff, exponent) in zip(S, weights)]
            # Stronger than merely cyclotomic vanishing: formal cancellations.
            coefficients = [0] * p
            for exponent, sign in terms:
                coefficients[exponent % p] += sign
            assert all(value == 0 for value in coefficients), (p, xi)
            assert cyclotomic_zero(terms, p)
        tested += 1
    assert tested >= 30
    return tested


def test_lower_minors(primes=(3, 11, 19)):
    count2 = count3 = 0
    for p in primes:
        assert is_prime(p) and p % 4 == 3
        P = list(product(range(p), repeat=2))
        P.remove((0, 0))
        for u in P:
            A = dot(u, u, p)
            assert A != 0    # Exact 2x2 principal determinant ζ^A - 1.
            count2 += 1
            for v in P:
                if u == v:
                    continue
                B = dot(v, v, p)
                C = dot(u, v, p)
                # det([[1,1,1],[1,ζ^A,ζ^C],[1,ζ^C,ζ^B]])
                terms = [(A + B, 1), (A, -1), (B, -1),
                         (2*C, -1), (C, 2)]
                assert not cyclotomic_zero(terms, p), (p, u, v)
                count3 += 1
    return count2, count3


if __name__ == '__main__':
    n = test_witnesses()
    n2, n3 = test_lower_minors()
    print('PRIMES_WITH_EXACT_FOUR_POINT_WITNESS', n)
    print('NONZERO_TWO_POINT_DETERMINANTS', n2)
    print('NONZERO_THREE_POINT_DETERMINANTS', n3)
    print('VERIFY_OK')
