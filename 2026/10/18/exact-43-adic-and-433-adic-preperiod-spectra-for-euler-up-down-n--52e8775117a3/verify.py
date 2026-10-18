#!/usr/bin/env python3
"""Exact small-index certificates for Euler zigzag preperiod spectra.

No preperiod at large exponents is simulated: the arithmetic progression
statement follows from the proved prime-square affine-difference lemma.
"""
from math import lcm

def boustrophedon(limit, modulus):
    prev = [1]
    E = [1]
    for n in range(1, limit + 1):
        now = [0] * (n + 1)
        for k in range(1, n + 1):
            now[k] = (now[k-1] + prev[n-k]) % modulus
        E.append(now[-1])
        prev = now
    return E

def euler_via_egf(limit, modulus):
    # (sec z + tan z)' = ((sec z + tan z)^2 + 1)/2.
    # Binomial convolution of the exponential generating coefficients.
    E = [1]
    row = [1]  # binomial row n = 0
    half = pow(2, -1, modulus)
    for n in range(limit):
        convolution = sum((row[k] * E[k] * E[n-k]) for k in range(n+1))
        E.append(((convolution + (1 if n == 0 else 0)) * half) % modulus)
        row = [1] + [(row[k-1] + row[k]) % modulus for k in range(1,n+1)] + [1]
    return E

def check(p, zeros, double_data):
    d = lcm(p-1, 4)
    modulus = p*p
    limit = 3*d + 9
    a = boustrophedon(limit, modulus)
    b = euler_via_egf(limit, modulus)
    assert a == b, ('independent recurrence disagreement', p)
    assert [n % d for n in range(2,d+2) if a[n] % p == 0] == zeros
    for n in range(2,limit-2*d+1):
        assert (a[n+2*d] - 2*a[n+d] + a[n]) % modulus == 0
    for n, an, next_an, root in double_data:
        assert a[n] == an and a[n+d] == next_an
        assert an % p == 0 and next_an % p == 0
        A, B = an // p, ((next_an-an) % modulus)//p
        assert B > 0
        roots = [k for k in range(p) if (A + k*B)%p == 0]
        assert roots == [root], (p,n,A,B,roots)
        r = n + 2 + d * root
        assert a[n+1] % p == 0
        assert a[n-1] % p != 0
        print(f'p={p} d={d} M={modulus} n={n} E_n={an} E_(n+d)={next_an} '
              f'linear=A({A})+k*B({B}) root={root} first_r={r}')
    print(f'VALIDATED_{p}: {limit+1} terms, {len(zeros)} zero residue classes, '
          f'independent recurrences and second differences')

check(43,[12,13,27,54,55,69],[(12,1376,774,33),(54,774,1376,11)])
check(433,[71,143,214,215,287,359,365,0],[(214,38104,175365,165)])
print('CERTIFICATE_OK')
