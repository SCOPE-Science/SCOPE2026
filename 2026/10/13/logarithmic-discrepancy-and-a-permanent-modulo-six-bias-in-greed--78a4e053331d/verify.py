"""Exact replay of the residue-density certificate for greedy gcd records.

Runs with Python 3 standard library only. Finite checks support the symbolic
primorial-copy proof; they are not a substitute for its unrestricted induction.
"""
from fractions import Fraction
from math import gcd
from bisect import bisect_left, bisect_right


def primes_below(bound):
    z = bytearray(b'\x01') * bound
    z[:2] = b'\x00\x00'
    for d in range(2, int(bound ** .5) + 1):
        if z[d]:
            z[d*d:bound:d] = b'\x00' * (((bound-1-d*d)//d)+1)
    return [i for i, v in enumerate(z) if v]

primes = primes_below(300)
assert primes[:9] == [2, 3, 5, 7, 11, 13, 17, 19, 23]
primorial = [1]
for p in primes:
    primorial.append(primorial[-1]*p)

def next_record(record):
    for p in primes:
        if (record - 1) % p:
            return record + p - 1
    raise AssertionError('insufficient primes')

records = []
r = 5
while r <= primorial[7] + 1:
    records.append(r)
    r = next_record(r)
record_set = set(records)
assert records[:10] == [5, 7, 11, 13, 17, 19, 23, 25, 29, 31]

# An independent implementation of the original greedily chosen permutation.
# The turning-point values agree with the direct prime-nondivisor record map.
seen = {1, 3}
fprev = 3
minimum_free = 2
direct_turning = []
for i in range(3, 10001):
    while minimum_free in seen:
        minimum_free += 1
    k = minimum_free
    while k in seen or gcd(k, fprev) != 1:
        k += 1
    if i >= 4 and k - fprev > 1:
        direct_turning.append(k)
    seen.add(k)
    fprev = k
assert direct_turning == records[:len(direct_turning)]

# Verify the exact disjoint-copy identity at several complete primorial scales.
for n in range(3, 7):
    P = primorial[n]
    q = primes[n]
    block = [t for t in records if q <= t <= P+1]
    copies = [t + j*P for j in range(q) for t in block]
    actual = [t for t in records if q <= t <= primorial[n+1]+1]
    assert copies == actual, (n, len(copies), len(actual))

# Direct counts on five consecutive primorial levels.
base = {1: 5, 5: 4}
P = 30
w = dict(base)
assert sum(1 for t in records if 7 <= t <= 31) == 9
for n in range(4, 8):
    q, nextprime = primes[n-1], primes[n]
    removed = {a: sum(1 for t in records if q <= t < nextprime and t % 6 == a)
               for a in (1, 5)}
    w = {a: q*w[a] - removed[a] for a in (1, 5)}
    P *= q
    direct = {a: sum(1 for t in records if nextprime <= t <= P+1 and t % 6 == a)
              for a in (1, 5)}
    assert w == direct
assert P == 510510 and w == {1: 82637, 5: 67846}

# Beyond P7, only short prime-gap intervals are needed, never a huge census.
# The first record list already covers all gaps through p15.
for n in range(8, 15):
    q, nextprime = primes[n-1], primes[n]
    removed = {a: sum(1 for t in records if q <= t < nextprime and t % 6 == a)
               for a in (1, 5)}
    w = {a: q*w[a] - removed[a] for a in (1, 5)}
    P *= q
assert P == 13082761331670030
assert w == {1: 2117724294581810, 5: 1738678957000765}
assert w[1] - w[5] == 379045337581045
lo = Fraction(w[1]-w[5]-1, P)
hi = Fraction(w[1]-w[5]+1, P)
assert lo > Fraction(1, 35)
assert lo > Fraction(2897288484988, 10**14)  # 0.02897288484988
assert hi < Fraction(2897288484990, 10**14)  # 0.02897288484990

# Finite regression of the provable 2*p_(n+2) discrepancy majorant.
# Use the rational midpoint of each certified limiting-density interval.
centre = {a: Fraction(w[a], P) - Fraction(1, 2*P) for a in (1, 5)}
for n in range(3, 8):
    H = primorial[n]
    for a in (1, 5):
        selected = [t for t in records if t <= H and t%6 == a]
        c = 0
        k = 0
        maxerr = Fraction(0)
        for x in range(0,H+1):
            if k < len(selected) and selected[k] == x:
                c += 1
                k += 1
            d = abs(c - centre[a]*x)
            if d > maxerr:
                maxerr = d
        assert maxerr < 2*primes[n+1], (n,a,maxerr)

print('VERIFY_OK')
print('direct_greedy_turning_records=%d' % len(direct_turning))
print('primorial_block_copies=3..6')
print('direct_primorial_count_levels=3..7')
print('certified_density_primorial_level=14')
print('P14=%d' % P)
print('w14_mod1=%d w14_mod5=%d' % (w[1], w[5]))
print('beta_rational_lower=(%d)/%d' % (w[1]-w[5]-1, P))
print('beta_rational_upper=(%d)/%d' % (w[1]-w[5]+1, P))
print('beta_strictly_greater_than_1_over_35=PASS')
print('logarithmic_discrepancy_regressions=PASS')
