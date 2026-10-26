from math import comb
from collections import Counter


def valuation(number, prime):
    assert number > 0
    count = 0
    while number % prime == 0:
        number //= prime
        count += 1
    return count


def polynomial_profile(prime, multiplier, exponent):
    assert exponent >= 1 and multiplier >= 1 and multiplier % prime
    h = [valuation(comb(multiplier - 1, b), prime) for b in range(multiplier)]
    g = [valuation(comb(multiplier, b), prime) for b in range(multiplier + 1)]
    histogram = Counter()
    for b in range(multiplier):
        histogram[g[b] + h[b]] += 1
        histogram[g[b + 1] + h[b]] += 1
        for j in range(1, exponent):
            histogram[2 * h[b] + j] += 2 * (prime - 1) * prime ** (j - 1)
        histogram[2 * h[b] + exponent] += (prime - 2) * prime ** (exponent - 1)
    assert sum(histogram.values()) == multiplier * prime ** exponent
    return +histogram


def independent_exact_narayana_profile(prime, multiplier, exponent):
    n = multiplier * prime ** exponent
    histogram = Counter()
    for k in range(n):
        numerator = comb(n, k) * comb(n, k + 1)
        assert numerator % n == 0
        histogram[valuation(numerator // n, prime)] += 1
    return +histogram


checks = 0
for p in (2, 3, 5, 7):
    for m in range(1, 28):
        if m % p == 0:
            continue
        for r in range(1, 5):
            if m * p ** r > 700:
                continue
            observed = independent_exact_narayana_profile(p, m, r)
            predicted = polynomial_profile(p, m, r)
            assert observed == predicted, (p, m, r, observed, predicted)
            checks += 1
assert checks == 202, checks

examples = {
    (2, 3, 3): {0: 4, 1: 6, 2: 8, 3: 2, 4: 4},
    (3, 4, 3): {0: 4, 1: 10, 2: 26, 3: 26, 4: 24, 5: 18},
    (5, 6, 2): {0: 4, 1: 18, 2: 36, 3: 32, 4: 60},
}
for key, expected in examples.items():
    assert dict(polynomial_profile(*key)) == expected
print('VERIFY_OK:', checks, 'independent exact Narayana-row histogram comparisons; normalization and shifted examples')
