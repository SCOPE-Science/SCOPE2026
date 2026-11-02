"""Finite independent checks for a two-prime bi-unitary harmonic obstruction.
Requires only the Python standard library. Finite checks are not the proof.
"""
from math import isqrt


def primes_below(limit):
    out = []
    for p in range(2, limit):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            out.append(p)
    return out


def sigma_biunitary(prime, exponent):
    total = 0
    for j in range(exponent + 1):
        if exponent % 2 == 0 and 2*j == exponent:
            continue
        total += prime ** j
    return total


def tau_biunitary(exponent):
    return exponent + 1 - (exponent % 2 == 0)


def run():
    assert sigma_biunitary(2, 2) == 5
    assert sigma_biunitary(3, 2) == 10
    assert tau_biunitary(2) == 2
    assert tau_biunitary(3) == 4
    for q in primes_below(60):
        for t in range(1, 8):
            e = 2 ** t
            b = e // 2
            s = sigma_biunitary(q, e)
            assert s == (q ** b - 1) * (q ** (b + 1) + 1) // (q - 1)
            assert tau_biunitary(e) == e
            if t >= 2:
                assert s % (q+1)**2 == 0
    cases = 0
    for p in primes_below(160):
        for q in primes_below(160):
            if p == q:
                continue
            for t in range(1, 8):
                e = 1 << t
                n = p*p * q**e
                s = sigma_biunitary(p, 2) * sigma_biunitary(q, e)
                d = tau_biunitary(2) * tau_biunitary(e)
                assert n*d % s != 0, (p,q,t)
                cases += 1
    print('VERIFY_OK distinct_prime_pairs_times_levels=', cases,
          'formula_and_square_factor_checked_levels=1..7')

if __name__ == '__main__':
    run()
