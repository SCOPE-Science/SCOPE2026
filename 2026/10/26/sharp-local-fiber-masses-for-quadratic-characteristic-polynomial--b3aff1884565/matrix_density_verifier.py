"""Exact checks of quadratic characteristic-polynomial matrix fibers.

Run with Python 3 (standard library only). The infinite assertions need the
separate mathematical argument; this finite program tests arithmetic identities.
"""
from fractions import Fraction
from itertools import product


def root_count(p, e, trace, determinant):
    modulus = p ** e
    return sum((x * x - trace * x + determinant) % modulus == 0
               for x in range(modulus))


def predicted_count(p, e, trace, determinant):
    modulus = p ** e
    phi = modulus - modulus // p
    weighted_roots = sum(p ** (e - j) * root_count(p, j, trace, determinant)
                         for j in range(1, e + 1))
    return phi * (modulus + weighted_roots) + modulus // p * root_count(p, e, trace, determinant)


def direct_count(p, e, trace, determinant):
    modulus = p ** e
    return sum((a * (trace - a) - b * c - determinant) % modulus == 0
               for a, b, c in product(range(modulus), repeat=3))


def p_valuation(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v, n


def exact_local_mass(p, trace, determinant):
    """Independent closed discriminant/2-adic classification."""
    upper = Fraction(p + 1, p)
    if p != 2:
        delta = trace * trace - 4 * determinant
        if delta == 0:
            return upper
        v, unit = p_valuation(delta, p)
        if not v % 2 and pow(unit % p, (p - 1) // 2, p) == 1:
            return upper
        s = v // 2
        if v % 2:
            return upper - Fraction(p + 1, p ** (s + 2))
        return upper - Fraction(2, p ** (s + 1))
    if trace % 2:
        return Fraction(3, 2) if determinant % 2 == 0 else Fraction(1, 2)
    half_trace = trace // 2
    c = half_trace * half_trace - determinant
    if c == 0:
        return Fraction(3, 2)
    v, unit = p_valuation(c, 2)
    s = v // 2
    if v % 2:
        return Fraction(3, 2) - Fraction(3, 2 ** (s + 2))
    u = unit % 8
    if u == 1:
        return Fraction(3, 2)
    if u == 5:
        return Fraction(3, 2) - Fraction(1, 2 ** (s + 1))
    return Fraction(3, 2) - Fraction(3, 2 ** (s + 2))


def finite_mass(p, e, trace, determinant):
    return Fraction(predicted_count(p, e, trace, determinant), p ** (2 * e))


def run():
    brute_cases = 0
    for p, exponents, bound in [(2, range(1, 6), 8), (3, range(1, 4), 6), (5, range(1, 3), 6)]:
        for e in exponents:
            for trace in range(bound):
                for determinant in range(bound):
                    assert direct_count(p, e, trace, determinant) == predicted_count(p, e, trace, determinant), (p, e, trace, determinant)
                    brute_cases += 1

    # In nonsplit cases the root counts eventually vanish, so the normalized
    # finite mass stabilizes. Split cases converge, rather than stabilize.
    samples = [
        (2,1,0),(2,1,1),(2,0,1),(2,0,3),(2,0,5),(2,0,7),
        (2,0,2),(2,0,4),(2,0,12),(2,0,8),
        (3,0,0),(3,0,1),(3,0,2),(3,0,3),(3,0,9),(3,0,-9),
        (5,0,0),(5,0,1),(5,0,2),(5,0,5),(5,0,25),(5,0,50),
    ]
    density_cases = 0
    for p,trace,determinant in samples:
        e = {2:12, 3:9, 5:7}[p]
        predicted = exact_local_mass(p,trace,determinant)
        actual = finite_mass(p,e,trace,determinant)
        # Uniform convergence crosscheck; finite levels are not infinite proofs.
        assert abs(predicted - actual) < Fraction(1, 100), (p,trace,determinant,predicted,actual)
        assert Fraction(p-1,p) <= predicted <= Fraction(p+1,p)
        density_cases += 1
    print('CERTIFICATE_OK exact_finite_fibers=',brute_cases,
          'local_classification_samples=',density_cases)

if __name__ == '__main__':
    run()
