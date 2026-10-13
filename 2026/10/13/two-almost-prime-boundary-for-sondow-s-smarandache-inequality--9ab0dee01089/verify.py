#!/usr/bin/env python3
from math import isqrt

NMAX = 200_000
CAP = NMAX * NMAX + 1

# Smallest-prime-factor sieve.
spf = list(range(NMAX + 1))
for i in range(2, isqrt(NMAX) + 1):
    if spf[i] == i:
        for j in range(i * i, NMAX + 1, i):
            if spf[j] == j:
                spf[j] = i

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p, e))
    return out

def vp_fact(m, p):
    total = 0
    while m:
        m //= p
        total += m
    return total

def least_m_for_prime_power(p, e):
    lo, hi = 1, p * e
    while lo < hi:
        mid = (lo + hi) // 2
        if vp_fact(mid, p) >= e:
            hi = mid
        else:
            lo = mid + 1
    return lo

def S(n):
    return max(least_m_for_prime_power(p, e) for p, e in factor(n))

# Capped exact factorials: the cap exceeds every n^2 in the scan,
# so comparisons against n^2 are exact even after saturation.
fact = [1] * (NMAX + 1)
for m in range(1, NMAX + 1):
    fact[m] = min(CAP, fact[m-1] * m)

failures = []
cases = 0
prime_cases = square_cases = semiprime_cases = 0
for n in range(2, NMAX + 1):
    fac = factor(n)
    Omega = sum(e for _, e in fac)
    if Omega > 2:
        continue
    cases += 1
    if len(fac) == 1 and fac[0][1] == 1:
        prime_cases += 1
    elif len(fac) == 1 and fac[0][1] == 2:
        square_cases += 1
    elif len(fac) == 2 and all(e == 1 for _, e in fac):
        semiprime_cases += 1
    else:
        raise AssertionError((n, fac))
    s = S(n)
    if not (n*n < fact[s]):
        failures.append(n)

assert failures == [2, 3, 6, 15], failures
assert S(4) == 4 and S(9) == 6 and S(6) == 3 and S(15) == 5
print('VERIFY_OK')
print(f'n_max={NMAX}')
print(f'two_almost_prime_cases={cases}')
print(f'prime_cases={prime_cases}')
print(f'prime_square_cases={square_cases}')
print(f'squarefree_semiprime_cases={semiprime_cases}')
print('exceptions=2,3,6,15')
