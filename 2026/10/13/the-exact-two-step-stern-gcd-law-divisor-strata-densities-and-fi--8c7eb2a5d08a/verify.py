"""Exact arithmetic regression and finite residue checks for two-step Stern gcds."""
from fractions import Fraction
from math import gcd

LIMIT = 250000
s = [0] * (LIMIT + 4)
s[1] = 1
for n in range(2, len(s)):
    s[n] = s[n // 2] if n % 2 == 0 else s[n // 2] + s[n // 2 + 1]


def split_valuation(n):
    r = 0
    m = n + 1
    while m % 2 == 0:
        r += 1
        m //= 2
    return r, (m - 1) // 2


def predict(n):
    if n % 2 == 0:
        return 1
    r, j = split_valuation(n)
    return gcd(2 * r + 1, s[j] - s[j + 1])


for n in range(1, LIMIT):
    assert gcd(s[n], s[n + 2]) == predict(n), n

for r in range(1, 16):
    m = 2 * r + 1
    seen = {predict((1 << r) * (2 * j + 1) - 1) for j in range(0, 2 ** min(11, r + 6))}
    assert seen == {d for d in range(1, m + 1) if m % d == 0}, (r, seen)

first = {}
for n in range(1, LIMIT):
    g = gcd(s[n], s[n + 2])
    first.setdefault(g, n)
for d in range(3, 33, 2):
    assert first[d] == 3 * (1 << ((d - 1) // 2)) - 1, (d, first[d])
assert first[1] == 1


def factor(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            factors.append((p, e))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def theoretical(m, d):
    if m % d != 0:
        return Fraction(0)
    prob = Fraction(1)
    for p, e in factor(m):
        t = 0
        z = d
        while z % p == 0:
            z //= p
            t += 1
        if t == 0:
            prob *= Fraction(p, p + 1)
        elif t == e:
            prob *= Fraction(1, (p + 1) * p ** (e - 1))
        else:
            prob *= Fraction(p - 1, (p + 1) * p ** t)
    return prob

for m in (3, 5, 7, 9, 15, 21, 25, 27, 45):
    counts = {}
    size = 0
    for a in range(m):
        for b in range(m):
            if gcd(gcd(a, b), m) == 1:
                size += 1
                counts[gcd(a - b, m)] = counts.get(gcd(a - b, m), 0) + 1
    for d in range(1, m + 1):
        if m % d == 0:
            assert Fraction(counts.get(d, 0), size) == theoretical(m, d), (m, d)
    assert sum(theoretical(m, d) for d in range(1, m + 1) if m % d == 0) == 1

print('EXACT_CERTIFICATE_OK', 'pointwise_n=' + str(LIMIT-1),
      'valuation_strata=15', 'first_occurrences_through=31',
      'finite_residue_moduli=9')
