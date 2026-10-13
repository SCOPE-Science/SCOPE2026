#!/usr/bin/env python3
from fractions import Fraction
import math

LIMIT = 396800
ENUM_LIMIT = 200000

def sieve(n):
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p*p:n+1:p] = b"\x00" * (((n - p*p)//p)+1)
    return is_prime

IP = sieve(LIMIT)
primes = [i for i in range(2, LIMIT + 1) if IP[i]]

violations = []
checked_pairs = 0
for idx, (p, q) in enumerate(zip(primes, primes[1:]), start=1):
    if p >= 396738:
        break
    checked_pairs += 1
    if not (q*q < 2*p*p):
        violations.append((idx, p, q))
assert violations == [(1,2,3),(2,3,5),(4,7,11)], violations

lhs = Fraction(50,49)
tail4_certificate = (
    Fraction(122,121) *
    Fraction(170,169) *
    Fraction(290,289) *
    Fraction(362,361)
)
assert tail4_certificate == Fraction(128075600,125495513)
assert lhs < tail4_certificate
assert tail4_certificate - lhs == Fraction(928750,6149280137)

zeta2_lower = sum(Fraction(1,n*n) for n in range(1,6)) + Fraction(1,6)
assert zeta2_lower == Fraction(5869,3600)
pi2_lower = 6 * zeta2_lower
assert pi2_lower == Fraction(5869,600)
assert pi2_lower > Fraction(243,25)
assert Fraction(54,5) * Fraction(25,243) == Fraction(10,9)

R = 54.0/(5.0*math.pi*math.pi)
intervals = [
    (1.0, R),
    (10.0/9.0, (10.0/9.0)*R),
    (5.0/4.0, (5.0/4.0)*R),
    (25.0/18.0, (25.0/18.0)*R),
]
assert abs(intervals[1][1] - 12.0/(math.pi*math.pi)) < 1e-15
assert abs(intervals[2][1] - 27.0/(2.0*math.pi*math.pi)) < 1e-15
assert abs(intervals[3][1] - 15.0/(math.pi*math.pi)) < 1e-15
for i in range(3):
    assert intervals[i][1] < intervals[i+1][0]

# Finite direct stress test on squarefree integers.
spf = list(range(ENUM_LIMIT + 1))
for p in range(2, int(ENUM_LIMIT**0.5)+1):
    if spf[p] == p:
        for m in range(p*p, ENUM_LIMIT+1, p):
            if spf[m] == m:
                spf[m] = p

tested = 0
for n in range(1, ENUM_LIMIT+1):
    x = n
    value = 1.0
    squarefree = True
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e > 1:
            squarefree = False
            break
        value *= 1.0 + 1.0/(p*p)
    if not squarefree:
        continue
    tested += 1
    assert any(lo - 1e-13 <= value <= hi + 1e-13 for lo, hi in intervals), (n, value)

print(
    "VERIFY_OK",
    f"prime_pairs={checked_pairs}",
    f"ratio_violations={violations}",
    f"tail4_diff={tail4_certificate-lhs}",
    f"pi2_lower={pi2_lower}",
    f"squarefree_tested={tested}",
    f"enum_limit={ENUM_LIMIT}",
)
