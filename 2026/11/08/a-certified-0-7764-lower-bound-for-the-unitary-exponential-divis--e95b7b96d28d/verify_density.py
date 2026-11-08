"""Exact integer certificate for a unitary/exponential divisor-sum density bound.

Run with Python 3.10 or newer: python verify_density.py
No third-party packages are required.
"""
from fractions import Fraction
from math import isqrt

PRIME_CUTOFF = 503
GRID = 100000
SCALE = 10**18
EXPECTED_GOOD_WEIGHT = 771520086457799875

def primes_up_to(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            for j in range(p * p, n + 1, p):
                is_prime[j] = False
    return [p for p in range(2, n + 1) if is_prime[p]]

def certified_lower_log_bin(numerator, denominator):
    """Prove GRID*log(numerator/denominator) >= returned integer.

    Write u=(a-b)/(a+b), log(a/b)=2*atanh(u). After twenty
    terms, absolute remainder is at most 2*|u|^41/[41*(1-u^2)].
    All calculations below use exact rational arithmetic.
    """
    if numerator == denominator:
        return 0
    u = Fraction(numerator - denominator, numerator + denominator)
    term = u
    series = Fraction(0)
    for j in range(20):
        series += term / (2 * j + 1)
        term *= u * u
    lower = 2 * series - 2 * abs(term) / (41 * (1 - u * u))
    return (GRID * lower.numerator) // lower.denominator

def local_terms(p):
    """The discarded exponent tail is omitted, never renormalized."""
    result = []
    a = 0
    while p ** (a + 1) < 10**12:
        if a == 0:
            numerator, denominator = 1, 1
        elif a == 1:
            numerator, denominator = p + 1, p
        else:
            numerator = p**a + 1
            denominator = sum(p**d for d in range(1, a + 1) if a % d == 0)
        bin_shift = certified_lower_log_bin(numerator, denominator)
        result.append((a, bin_shift, p - 1, p ** (a + 1)))
        a += 1
    return result

def certify():
    primes = primes_up_to(PRIME_CUTOFF)
    assert len(primes) == 96 and primes[-1] == PRIME_CUTOFF
    lo = hi = 0
    state = [SCALE]
    p2 = p3 = p5 = None
    for p in primes:
        terms = local_terms(p)
        if p == 2: p2 = dict((a, shift) for a, shift, _, _ in terms)
        if p == 3: p3 = dict((a, shift) for a, shift, _, _ in terms)
        if p == 5: p5 = dict((a, shift) for a, shift, _, _ in terms)
        newlo = lo + min(t[1] for t in terms)
        newhi = hi + max(t[1] for t in terms)
        successor = [0] * (newhi - newlo + 1)
        for exponent, shift, weight_num, weight_den in terms:
            offset = lo + shift - newlo
            for j, mass in enumerate(state):
                if mass:
                    successor[j + offset] += mass * weight_num // weight_den
        state, lo, hi = successor, newlo, newhi
    # Every cell stores a LOWER bound, scaled by SCALE, on the
    # exact rational probability of its corresponding integer score.
    good_weight = sum(state[max(0, -lo):])
    assert good_weight == EXPECTED_GOOD_WEIGHT
    # These two exact-equality cylinders are disjoint from scored >= 0.
    assert p2[2] + p5[1] == -1
    assert p3[2] + p5[1] == -1
    assert Fraction(1 + 2**2, 2 + 2**2) * Fraction(5 + 1, 5) == 1
    assert Fraction(1 + 3**2, 3 + 3**2) * Fraction(5 + 1, 5) == 1
    mertens = Fraction(1)
    for p in primes:
        mertens *= Fraction(p - 1, p)
    # w(2^2,5^1) and w(3^2,5^1) relative to all-zero exponents:
    bonus = mertens * (Fraction(1, 20) + Fraction(1, 45))
    # Tail squarefreeness has density >= 1-1/503.
    exact_lower_bound = Fraction(502, 503) * (Fraction(good_weight, SCALE) + bonus)
    assert exact_lower_bound > Fraction(1941, 2500)  # 0.7764
    print('VERIFY_OK')
    print('primes=' + str(len(primes)) + ', largest=' + str(primes[-1]))
    print('lower_score_mass=' + str(good_weight) + '/' + str(SCALE))
    print('additional_equal_cylinders=2; disjoint_shift=-1')
    print('certified_density_lower_bound_gt=0.7764')
    print('rational_lower_bound_decimal_approx=' + format(float(exact_lower_bound), '.12f'))

if __name__ == '__main__':
    certify()
