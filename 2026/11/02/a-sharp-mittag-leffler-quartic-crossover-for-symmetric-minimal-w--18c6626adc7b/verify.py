"""Reproduce finite-sample identities and numerical checks for the Rademacher-clock theorem.

All tests use the Python standard library. This checks finite consequences only;
the uniform moderate-deviation limit is proved analytically in RESULT.md.
"""
import math
from fractions import Fraction

checks = 0

def check(test, description):
    global checks
    if not test:
        raise AssertionError(description)
    checks += 1


def increasing_factorial(k, r):
    v = 1
    for j in range(r):
        v *= k + j
    return v


def clock_law(n, p):
    masses = {1: Fraction(1)}
    for j in range(1, n):
        nxt = {}
        for k, weight in masses.items():
            a = p * k / j
            nxt[k] = nxt.get(k, Fraction(0)) + weight * (1 - a)
            nxt[k + 1] = nxt.get(k + 1, Fraction(0)) + weight * a
        masses = nxt
    return masses


def gaussian_tail(x):
    return math.erfc(x / math.sqrt(2)) / 2


def fair_binomial_tail(m, x):
    # P((2 B_m-m)/sqrt(m) >= x) for B_m~Bin(m,1/2), via a stable recurrence.
    threshold = math.ceil((m + x * math.sqrt(m)) / 2 - 1e-11)
    if threshold <= 0:
        return 1.0
    if threshold > m:
        return 0.0
    logpmf = (math.lgamma(m + 1) - math.lgamma(threshold + 1)
              - math.lgamma(m - threshold + 1) - m * math.log(2))
    mass = math.exp(logpmf)
    result = mass
    for j in range(threshold, m):
        mass *= (m - j) / (j + 1)
        result += mass
    return result


def rate(z):
    return ((1 + z) * math.log1p(z) + (1 - z) * math.log1p(-z)) / 2

# Exact clock recursion, normalization, first movement state and rising-factorial eigenfunctions.
for p in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
    for n in range(1, 19):
        masses = clock_law(n, p)
        check(sum(masses.values()) == 1, 'clock mass')
        check(all(v >= 0 for v in masses.values()), 'clock positivity')
        check(all(1 <= k <= n for k in masses), 'clock support')
        first = Fraction(1)
        for j in range(1, n):
            first *= 1 - p / j
        check(masses.get(1, 0) == first, 'single-movement mass')
        for r in range(1, 6):
            observed = sum(weight * increasing_factorial(k, r)
                           for k, weight in masses.items())
            expected = Fraction(math.factorial(r))
            for j in range(1, n):
                expected *= 1 + p * r / j
            check(observed == expected, 'rising-factorial moment')

# Exact small-sample binomial tails and parity, checked against direct enumeration.
for m in range(1, 22):
    for threshold in range(-m, m + 2):
        direct = sum(math.comb(m, j) for j in range(m + 1)
                     if 2*j - m >= threshold) / (2 ** m)
        via_tail = fair_binomial_tail(m, threshold / math.sqrt(m))
        check(abs(direct - via_tail) < 2e-13, 'finite binomial tail')

# Rate-function fourth-order coefficient and nonnegative remainder.
for z in [.003, .012, .03, .08, .16, .24]:
    fourth = z*z/2 + z**4/12
    check(rate(z) >= fourth - 1e-14, 'quartic lower bound')
    check(abs(rate(z)-fourth-z**6/30) <= z**8/50 + 2e-16,
          'sixth-order term plus controlled remainder')

# Fixed sample quartic crossover; lattice oscillations decay at large m.
for m, tol in [(10000, .14), (100000, .065), (1000000, .033)]:
    for c in [.5, 1.0]:
        x = c * m**.25
        observed = fair_binomial_tail(m, x) / gaussian_tail(x)
        expected = math.exp(-c**4 / 12)
        check(abs(observed - expected) < tol,
              'finite-size Rademacher quartic profile')

# Universal Gaussian envelope from the external martingale tail theorem:
# the finite checks do not prove the universal theorem.
constant = max(2, 2*math.exp(3)/9)
for m in range(1, 91):
    for x in [0, .1, .35, .8, 1, 1.5, 2, 2.5, 3, 4, 6, 9]:
        if gaussian_tail(x) > 0:
            check(fair_binomial_tail(m, x) <=
                  constant * gaussian_tail(x) * (1 + 1e-9),
                  'finite Gaussian domination')

print(f'VERIFY_OK {checks} finite exact/numerical assertions')
print('Fixed-sample quartic target: exp(-c^4/12); random-clock mixture is an analytical limit.')
