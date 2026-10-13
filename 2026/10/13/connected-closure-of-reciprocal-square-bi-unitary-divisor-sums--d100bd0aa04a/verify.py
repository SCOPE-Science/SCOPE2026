"""Exact rational checks for reciprocal-square bi-unitary divisor sums.

The infinite-prime step uses the classical fifth Ramanujan-prime bound:
for real x >= 41, pi(x)-pi(x/2) >= 5.
That external theorem is an analytic input, not inferred from this code.
"""
from fractions import Fraction as Q
from math import gcd, isqrt


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def c(p):
    return Q(p * p, p * p - 1)


def biunitary_local(p, a):
    return sum((Q(1, p ** (2 * j)) for j in range(a + 1)
                if not (a % 2 == 0 and a > 0 and j == a // 2)), Q(0))

# Direct local-formula checks, including the subtle exponent-two deletion.
for p in (2, 3, 5, 7, 11):
    assert biunitary_local(p, 0) == 1
    assert biunitary_local(p, 1) == 1 + Q(1, p * p)
    assert biunitary_local(p, 2) == 1 + Q(1, p ** 4)
    for a in range(1, 17):
        assert 1 <= biunitary_local(p, a) < c(p)

# Independent divisor-definition regression, not based on the deleted-middle formula.
def divisors(n):
    small = [d for d in range(1, isqrt(n)+1) if n % d == 0]
    return sorted(set(small + [n // d for d in small]))


def unitary(e, n):
    return n % e == 0 and gcd(e, n // e) == 1


def biunitary(e, n):
    if n % e:
        return False
    return not any(unitary(c, e) and unitary(c, n//e)
                   for c in divisors(gcd(e, n//e)) if c > 1)


def factor_blocks(n):
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                a += 1
                n //= p
            yield p, a
        p += 1
    if n > 1:
        yield n, 1


for n in range(1, 257):
    by_definition = sum((Q(1,d*d) for d in divisors(n)
                         if biunitary(d,n)), Q(0))
    by_formula = Q(1)
    for p, a in factor_blocks(n):
        by_formula *= biunitary_local(p,a)
    assert by_definition == by_formula, (n,by_definition,by_formula)

# Each finite witness product proves the tail beyond the displayed prime
# is large enough for the binary multiplicative no-gap condition.
witnesses = {
    5:  [7, 11, 13, 17, 19],
    7:  [11, 13, 17, 19, 23],
    11: [13, 17],
    13: [17, 19],
    17: [19, 23],
    19: [23, 29],
    23: [29, 31],
    29: [31, 37],
    31: [37, 41],
    37: [41, 43],
}
for p, following in witnesses.items():
    assert is_prime(p)
    assert all(is_prime(q) and q > p for q in following)
    product = Q(1)
    for q in following:
        product *= c(q)
    assert product > c(p), (p, following)

# For every prime p>=41, Ramanujan's 1919 theorem supplies five
# primes q in (p,2p), so C_q>1+1/(4p^2). This exact inequality
# makes the product of those five C_q strictly larger than C_p.
assert 5 * (41 * 41 - 1) > 4 * 41 * 41
assert all(5 * (p * p - 1) > 4 * p * p for p in range(41, 300))

# For p>=5 the prime tail closure is [1, pi^2/9]. The following
# eight boundary multipliers use p=2 exponents 0,2,1,infinity
# and p=3 exponents 0,infinity.
local2 = [Q(1), biunitary_local(2, 2), biunitary_local(2, 1), c(2)]
local3 = [Q(1), c(3)]
multipliers = sorted({x * y for x in local2 for y in local3})
expected = [Q(1), Q(17,16), Q(9,8), Q(153,128), Q(5,4),
            Q(4,3), Q(45,32), Q(3,2)]
assert multipliers == expected, multipliers
max_ratio = max(b / a for a, b in zip(multipliers, multipliers[1:]))
assert max_ratio == Q(16,15)

# The Archimedean lower bound pi>223/71 gives pi^2/9>16/15.
assert Q(223,71) ** 2 / 9 > max_ratio
assert multipliers[0] == 1 and multipliers[-1] == Q(3,2)
assert multipliers[-1] * Q(1,9) == Q(1,6)
print('EXACT_CERTIFICATE_OK definition_checks=256 finite_tail_primes=10 witness_factors=26 '
      'boundary_intervals=8 max_ratio=16/15 endpoint=pi^2/6')
