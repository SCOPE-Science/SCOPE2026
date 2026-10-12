"""Exact finite sanity checks for a divisor-function level-set counting theorem.

The infinite asymptotic theorem rests on its printed proof and a published
rough-number estimate, not on this finite computation.
"""
from fractions import Fraction

LIMIT = 100000
spf = list(range(LIMIT + 1))
for p in range(2, int(LIMIT**0.5) + 1):
    if spf[p] == p:
        for j in range(p*p, LIMIT + 1, p):
            if spf[j] == j:
                spf[j] = p


def factors(n):
    while n > 1:
        p = spf[n]
        a = 0
        while n % p == 0:
            a += 1
            n //= p
        yield p, a


def ratio(n):
    u, e = 1, 1
    for p, a in factors(n):
        u *= 1 + p**a
        e *= sum(p**d for d in range(1, a + 1) if a % d == 0)
    return Fraction(u, e)


values = {}
squarefree_seen = {}
coincidences = []
for n in range(1, LIMIT + 1):
    r = ratio(n)
    if r == 1:
        coincidences.append(n)
    ff = list(factors(n))
    if all(a == 1 for _, a in ff):
        assert r == Fraction(__import__('math').prod(p + 1 for p, _ in ff), n)
        assert r not in squarefree_seen, (n, squarefree_seen.get(r))
        squarefree_seen[r] = n
assert coincidences == [1, 20, 45, 320, 6615], coincidences
assert ratio(20) == ratio(45) == ratio(320) == ratio(6615) == 1
assert ratio(2) == Fraction(3, 2)
assert ratio(4) == Fraction(5, 6)
assert ratio(8) == Fraction(9, 10)
print('VERIFY_OK limit={} squarefree_unique={} equality_hits={}'.format(
    LIMIT, len(squarefree_seen), coincidences))
