"""Exact finite checks for a Lucas-cobalancing consecutive-square GCD identity.

All integer calculations use Python's arbitrary precision integers.  Finite checks
support but cannot replace the unrestricted mathematical proof.
"""
from math import gcd

MAX_K = 320
MAX_N = 24
LENGTH = MAX_K + MAX_N + 9

P = [0, 1]
Q = [1, 1]
B = [0, 1]
c = [-1, 1]
for _ in range(2, 4 * LENGTH + 12):
    P.append(2 * P[-1] + P[-2])
    Q.append(2 * Q[-1] + Q[-2])
    B.append(6 * B[-1] - B[-2])
    c.append(6 * c[-1] - c[-2])

prefix = [0]
for x in c:
    prefix.append(prefix[-1] + x*x)

checks = 0
identity_checks = 0
for k in range(1, MAX_K + 1):
    observed = 0
    for n in range(MAX_N + 1):
        s = prefix[n+k+1] - prefix[n+1]
        observed = gcd(observed, s)
        if 2*s != B[k]*Q[4*n + 2*k] - k:
            raise AssertionError(('sum identity', k, n))
        identity_checks += 1
    target = gcd(B[k], k) * (3 if k % 6 == 3 else 1)
    if observed != target:
        raise AssertionError(('gcd', k, observed, target))
    checks += 1

# Exact Pell strong-divisibility identity over a finite testing region.
strong_div_checks = 0
for i in range(1, 111):
    for j in range(1, 111):
        if gcd(P[i], P[j]) != P[gcd(i, j)]:
            raise AssertionError(('Pell strong divisibility', i, j))
        strong_div_checks += 1

# Independent modular tests of the two exceptional prime analyses.
modular_checks = 0
for k in range(2, MAX_K + 1, 2):
    t = (k & -k).bit_length() - 1
    odd = k >> t
    b_unit = B[k] >> t
    if b_unit % 4 != (3 * odd) % 4:
        raise AssertionError(('2-adic unit', k))
    modular_checks += 1

print('VERIFY_OK')
print('windows_parameter_values=', checks)
print('exact_window_sum_identities=', identity_checks)
print('Pell_strong_divisibility_pairs=', strong_div_checks)
print('even_parameter_2adic_unit_checks=', modular_checks)
print('finite_checks_are_not_an_infinite_proof=True')
