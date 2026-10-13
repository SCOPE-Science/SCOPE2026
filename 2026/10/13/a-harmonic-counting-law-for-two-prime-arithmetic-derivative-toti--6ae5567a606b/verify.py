"""Exact finite regression for arithmetic-derivative/totient prime-pair counting."""
from fractions import Fraction

LIMIT = 500_000
spf = list(range(LIMIT + 1))
spf[0] = 0
spf[1] = 1
for d in range(2, int(LIMIT ** .5) + 1):
    if spf[d] == d:
        for m in range(d * d, LIMIT + 1, d):
            if spf[m] == m:
                spf[m] = d
primes = [p for p in range(2, LIMIT + 1) if spf[p] == p]

def factor(n):
    result = {}
    while n > 1:
        p = spf[n]
        result[p] = result.get(p, 0) + 1
        n //= p
    return result

observed = set()
for n in range(2, LIMIT + 1):
    f = factor(n)
    if len(f) != 2:
        continue
    deriv = sum((n // p) * e for p, e in f.items())
    phi = n
    for p in f:
        phi = (phi // p) * (p - 1)
    if deriv == phi and min(f) % 2 == 1:
        observed.add(n)

predicted = set()
for p in primes:
    if p == 2 or p ** 2 > LIMIT:
        continue
    for a in range(1, p - 1):
        if p ** a > LIMIT:
            break
        c = p - a - 1
        r = pow(a + 1, -1, p)
        for q in primes:
            if q <= p:
                continue
            if p ** a * q > LIMIT:
                break
            if q % p != r:
                continue
            numerator = c * q + 1
            assert numerator % p == 0
            b = numerator // p - 1
            if b < 1:
                continue
            if b * (q.bit_length() - 1) > 19:
                continue
            n = p ** a * q ** b
            if n <= LIMIT:
                predicted.add(n)
assert observed == predicted, (sorted(observed - predicted)[:10], sorted(predicted - observed)[:10])
for p in primes[:20]:
    if p == 2:
        continue
    harmonic = sum((Fraction(1, c) for c in range(1, p-1)), Fraction(0))
    sum_by_a = sum((Fraction(p, (p-1)*(p-a-1)) for a in range(1,p-1)),Fraction(0))
    assert sum_by_a == Fraction(p,p-1)*harmonic
print(f'EXACT_REGRESSION_OK range=2..{LIMIT} observed={len(observed)} predicted={len(predicted)} first={sorted(observed)[:8]} constants=19')
