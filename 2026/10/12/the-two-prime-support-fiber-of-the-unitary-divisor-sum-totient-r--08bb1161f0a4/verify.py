#!/usr/bin/env python3
"""Finite independent check of a unitary-divisor/totient equality.

This is a finite corroboration only; the unrestricted proof is in RESULT.md.
"""

LIMIT = 1000000
spf = list(range(LIMIT + 1))
for p in range(2, int(LIMIT ** 0.5) + 1):
    if spf[p] == p:
        for multiple in range(p * p, LIMIT + 1, p):
            if spf[multiple] == multiple:
                spf[multiple] = p

hits = []
small_support_hits = []
small_support_tested = 0
for n in range(1, LIMIT + 1):
    x = n
    phi = 1
    unitary_sigma = 1
    omega = 0
    while x > 1:
        p = spf[x]
        power = 1
        while x % p == 0:
            x //= p
            power *= p
        omega += 1
        phi *= (power // p) * (p - 1)
        unitary_sigma *= power + 1
    if omega <= 2:
        small_support_tested += 1
    if unitary_sigma == 2 * phi:
        hits.append(n)
        if omega <= 2:
            small_support_hits.append(n)
assert small_support_hits == [3, 35, 99], small_support_hits
assert 1045 in hits
assert spf[1045] == 5
print('VERIFY_OK', 'limit=' + str(LIMIT),
      'omega_le2_checked=' + str(small_support_tested),
      'omega_le2_hits=' + str(small_support_hits),
      'all_hits_count=' + str(len(hits)),
      'first_support3=1045',
      'all_hits_first=' + str(hits[:15]))
