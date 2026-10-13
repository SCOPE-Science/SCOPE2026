"""Exact finite checks for uniform group-drawing vacancy distributions.

The analytic real-rootedness theorem is proved separately; finite checks
independently test the hypergeometric recurrence and factorial moments.
Requires Python 3 and SymPy.
"""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb
from sympy import Poly, QQ, oo, symbols

z = symbols('z')

def distribution(n, groups):
    probs = [Fraction(0) for _ in range(n + 1)]
    probs[n] = Fraction(1)
    for s in groups:
        remaining = n - s
        next_probs = [Fraction(0) for _ in range(n + 1)]
        for x, mass in enumerate(probs):
            if not mass:
                continue
            for y in range(max(0, remaining - (n - x)), min(x, remaining) + 1):
                next_probs[y] += mass * Fraction(
                    comb(x, y) * comb(n - x, remaining - y), comb(n, remaining)
                )
        probs = next_probs
    return probs

def factorial_moment(n, groups, j):
    out = Fraction(comb(n, j))
    for s in groups:
        out *= Fraction(comb(n - j, s), comb(n, s)) if s <= n-j else 0
    return out

def roots_all_real_nonpositive(probs):
    poly = Poly(sum(v * z**i for i, v in enumerate(probs)), z, domain=QQ)
    # A nonnegative coefficient polynomial has no strictly positive real zero.
    # Count every distinct real root of every squarefree factor by exact Sturm sequences.
    for factor, multiplicity in poly.sqf_list()[1]:
        if factor.count_roots(-oo, oo) != factor.degree():
            return False
    return True

def explicit_set_enumeration(n, groups):
    # Separate exhaustive enumeration (not the hypergeometric recurrence).
    law = [Fraction(0) for _ in range(n + 1)]
    choices = [list(combinations(range(n), s)) for s in groups]
    ways = 1
    for c in choices:
        ways *= len(c)
    for tup in product(*choices):
        seen = set()
        for group in tup:
            seen.update(group)
        law[n-len(seen)] += Fraction(1, ways)
    return law

def main():
    cases = moments = root_certificates = 0
    for n in range(1, 9):
        for depth in range(0, 4):
            for groups in combinations_with_replacement(range(n + 1), depth):
                probs = distribution(n, groups)
                assert sum(probs) == 1
                for j in range(n + 1):
                    lhs = sum(comb(k, j)*probs[k] for k in range(j, n + 1))
                    assert lhs == factorial_moment(n, groups, j), (n, groups, j)
                    moments += 1
                assert roots_all_real_nonpositive(probs), (n, groups, probs)
                root_certificates += 1
                cases += 1
    # Independent enumeration for selected heterogeneous schedules.
    enum_cases = [(5,(1,3,2)),(6,(2,3)),(6,(1,2,3)),(7,(2,4)),
                  (7,(1,4,2)),(7,(3,3,2)),(6,(0,3,6)),(5,(2,2))]
    for n, groups in enum_cases:
        assert distribution(n, groups) == explicit_set_enumeration(n, groups)
    assert distribution(5, (2,2)) == [Fraction(0),Fraction(3,10), Fraction(6,10),Fraction(1,10),Fraction(0),Fraction(0)]
    assert Poly(sum(v*z**i for i,v in enumerate(distribution(5,(2,2)))), z).factor_list()[1]
    print('PASS: %d exact distribution-and-real-root checks, %d factorial-moment identities, %d independent subset enumerations.' %(cases, moments, len(enum_cases)))
    print('Example n=5, groups=(2,2): F(z)=z(z^2+6z+3)/10; nonzero roots -3 +/- sqrt(6).')

if __name__ == '__main__':
    main()
