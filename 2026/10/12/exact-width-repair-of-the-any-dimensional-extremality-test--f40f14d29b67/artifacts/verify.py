from fractions import Fraction
from math import comb

primes = [2, 3, 5, 7, 11, 101, 1009]
checks = 0
for g in range(2, 13):
    for p in primes:
        W = (p + 1) ** (2 * g) - (p - 1) ** (2 * g)
        expanded = 2 * sum(comb(2 * g, j) * p ** (2 * g - j) for j in range(1, 2 * g + 1, 2))
        assert W == expanded
        lead = 4 * g * p ** (2 * g - 1)
        assert W > lead
        # The coarser inequality stated in the source's width lemma remains safe.
        assert W <= (4 ** g) * p ** (2 * g - 1)
        checks += 1

for p in primes:
    W2 = (p + 1) ** 4 - (p - 1) ** 4
    assert W2 == 8 * p ** 3 + 8 * p

# Fixed-g asymptotic sanity: p*B_g(p) approaches 4g from above.
limits = []
for g in (2, 3, 5, 10):
    p = 1000003
    W = (p + 1) ** (2 * g) - (p - 1) ** (2 * g)
    B = Fraction(W, (p - 1) ** (2 * g))
    scaled = B * p
    assert scaled > 4 * g
    assert scaled < 4 * g + Fraction(1, 1000)
    limits.append((g, scaled))

print('VERIFY_OK width_checks={} g2_identity={} asymptotic_cases={}'.format(checks, len(primes), len(limits)))
print('sample_g2_p101_exact_bound={}/{}'.format((102**4-100**4),100**4))
