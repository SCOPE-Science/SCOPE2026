#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

primes = []
n = 2
while len(primes) < 59:
    if is_prime(n):
        primes.append(n)
    n += 1

assert primes[57] == 271
assert primes[58] == 277

h58 = sum((Fraction(1, p) for p in primes[:58]), Fraction(0, 1))
h59 = h58 + Fraction(1, primes[58])

expected_num = 632922102284802030608735614303171023883353726199065754232874723702048629323675218406677909479222722729203736409
expected_den = 316660540451402206051523961799780143689087330537799173695893334666158783075592938409825136155637880209438531070

assert h58.numerator == expected_num
assert h58.denominator == expected_den
assert h58 < 2
assert h59 > 2

gap = Fraction(2, 1) - h58
assert gap > 0

print(
    "VERIFY_OK",
    "P58=271",
    "P59=277",
    f"H58={h58.numerator}/{h58.denominator}",
    f"gap_num={gap.numerator}",
    f"gap_den={gap.denominator}",
)
