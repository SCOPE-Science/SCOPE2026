"""Exact rational verification of the nine-prime Sylow-support threshold."""
from fractions import Fraction as F
from math import prod

P = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
T = F(4, 9)

def recip(primes):
    return sum((F(1, p + 1) for p in primes), F(0))

assert recip(P[:6]) == F(269, 630) < T
assert recip(P[:7]) == F(29, 63)
assert recip(P[:8]) == F(991, 2016)
assert F(29, 63) < F(12, 17) < F(10, 13) < F(3, 2)
assert F(991, 2016) < F(12, 17)

skip_expected = [F(739, 2016), F(823, 2016), F(121, 288), F(293, 672), F(4451, 10080)]
power_expected = [F(4477, 12600), F(5921, 15372), F(302, 765), F(1243, 3045), F(94207, 228060)]
for j in range(5):
    prefix = recip(P[:j])
    skipped = prefix + recip(P[j + 1:j + 1 + (7 - j)])
    squared = prefix + F(1, P[j]**2 + 1) + recip(P[j + 1:j + 1 + (6 - j)])
    assert skipped == skip_expected[j] < T, (j, skipped)
    assert squared == power_expected[j] < T, (j, squared)

assert recip(P[:5]) == F(971, 2520)
R = T - recip(P[:5])
assert R == F(149, 2520)
assert F(1, 32) + F(1, 38) == F(35, 608) < R
assert F(1, 23**2 + 1) + F(1, 30) == F(28, 795) < R
assert R - F(1, 24) == F(11, 630)
assert R - F(1, 30) == F(13, 504)
assert (F(1, R-F(1, 24))).denominator != 1
assert (F(1, R-F(1, 30))).denominator != 1

witness = [7, 11, 13, 17, 19, 29, 71, 83]
assert recip(witness) == T
assert F(5, 9) + F(10, 4) + F(6, 6) + recip(witness) == F(9, 2)
assert len(set([2] + witness)) == 9
print('seven-smallest-new-prime-sum=', recip(P[:7]))
print('six-smallest-new-prime-sum=', recip(P[:6]))
print('eight-smallest-new-prime-sum=', recip(P[:8]))
print('forced-first-five=', P[:5])
print('last-two-remainder=', R)
print('witness-primes=', [2] + witness)
print('VERIFY_OK')
