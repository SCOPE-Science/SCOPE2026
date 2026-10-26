"""Exact, standalone finite certificate for complementary divisor-pair counts.

Every admissible n = 2**a * p, with p an odd prime, has complementary
pairs (2**i, p*2**(a-i)), i = 0,...,a. A positive number of omissions
cannot contain the i=0 or i=a pair. Exhaust all remaining index sets.
No dependencies beyond Python's standard library are used.
"""
from itertools import combinations
from math import isqrt, comb

BOUND = 630194176
FIRST = (BOUND, 20, 601, (9, 16, 18, 19))
EXPECTED_TRIPLES = [
    (16, 3531, (12, 13, 14)),
    (19, 4595, (12, 13, 17)),
    (26, 76083, (16, 17, 24)),
]
EXPECTED_QUADRUPLES = [
    (20, 601, (9, 16, 18, 19)),
    (20, 2311, (11, 12, 14, 17)),
    (21, 30363, (15, 16, 18, 19)),
    (23, 9615, (13, 14, 16, 19)),
    (23, 13815, (13, 18, 19, 20)),
    (24, 23631, (14, 16, 18, 20)),
    (24, 49123, (15, 19, 20, 22)),
    (27, 3369195, (22, 23, 24, 25)),
]

def is_prime(n):
    """Deterministic trial division, exhaustive up to floor(sqrt(n))."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True

def candidates(k, max_a=27):
    """Return (integer p, prime p, number of examined tuples)."""
    integer_p = []
    prime_p = []
    tuples = 0
    for a in range(k + 1, max_a + 1):
        for indices in combinations(range(1, a), k):
            tuples += 1
            numerator = (1 << (a+1)) - 1 - sum(1 << i for i in indices)
            denominator = 1 + sum(1 << (a-i) for i in indices)
            if numerator >= 3*denominator and numerator % denominator == 0:
                p = numerator // denominator
                if p % 2 == 1:
                    record = (a, p, indices)
                    integer_p.append(record)
                    if is_prime(p):
                        prime_p.append(record)
    return integer_p, prime_p, tuples

def validate_pair_sum(a, p, indices):
    n = (1 << a)*p
    assert len(indices) == len(set(indices))
    pairs = [(1 << i, (1 << (a-i))*p) for i in indices]
    assert all(x*y == n for x,y in pairs)
    assert all(x != y for x,y in pairs)
    assert len({d for pair in pairs for d in pair}) == 2*len(indices)
    sigma = ((1 << (a+1)) - 1)*(p+1)
    assert sum(x+y for x,y in pairs) == sigma-2*n
    # Independent direct divisor enumeration for n=2**a*p:
    divs = sorted(set([1 << i for i in range(a+1)] +
                      [(1 << i)*p for i in range(a+1)]))
    omissions = {d for pair in pairs for d in pair}
    assert sum(divs) == sigma
    assert sum(d for d in divs if d not in omissions) == 2*n
    assert all((d in omissions) == ((n//d) in omissions) for d in divs)

# If n <= BOUND and p >= 3, then 3*2**a <= BOUND implies a <= 27.
assert 3*(1 << 27) < BOUND < 3*(1 << 28)
triples, three_primes, ct3 = candidates(3)
quads, four_primes, ct4 = candidates(4)
assert ct3 == sum(comb(a-1, 3) for a in range(4, 28)) == 17550
assert ct4 == sum(comb(a-1, 4) for a in range(5, 28)) == 80730
assert triples == EXPECTED_TRIPLES
assert three_primes == []
assert quads == EXPECTED_QUADRUPLES
expected_prime_four = [quads[i] for i in (0,1,6)]
assert four_primes == expected_prime_four
ordered = sorted(((1 << a)*p,a,p,I) for a,p,I in four_primes)
assert ordered[0] == FIRST
assert sum(n<=BOUND for n,a,p,I in ordered) == 1
for a,p,I in four_primes:
    validate_pair_sum(a, p, I)
# Check that the first four-pair witness has no one-, two- or three-pair representation.
for k in (1,2,3):
    for indices in combinations(range(0,21), k):
        assert sum((1 << i)+(1 << (20-i))*601 for i in indices) != ((1 << 21)-1-601)
assert is_prime(601)
print('VERIFY_OK triple_tuples=17550 quadruple_tuples=80730 '
      'integer_triples=3 integer_quadruples=8 prime_quads=3 '
      'first_four_pair=630194176 no_smaller_three_pairs=PASS '
      'direct_divisor_sums=PASS')
