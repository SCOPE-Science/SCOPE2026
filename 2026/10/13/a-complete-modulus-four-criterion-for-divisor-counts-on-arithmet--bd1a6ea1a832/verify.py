#!/usr/bin/env python3
"""Exact finite regression checks for a divisor-congruence classification.

Run with Python 3, using only the standard library. A finite regression is
not a substitute for the unrestricted proof in RESULT.md.
"""
from math import isqrt


def factor(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                e += 1
                n //= d
            out.append((d, e))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def divisor_count(n):
    assert n >= 1
    d = 1
    for _, e in factor(n):
        d *= e + 1
    return d


def force_data(A, B):
    assert A >= 1 and 0 <= B < A
    forced = []
    for p, a in factor(A):
        e = 0
        if B == 0:
            e = a
        else:
            x = B
            while x % p == 0:
                e += 1
                x //= p
        if e < a:
            forced.append((p, e, a))
    J = 1
    for _, e, _ in forced:
        J *= e+1
    return forced, J


def criterion(A, B):
    forced, J = force_data(A, B)
    if J % 4 == 0:
        return True
    if J % 2:
        return False
    odd_fixed = [(p, e) for p, e, _ in forced if e % 2]
    assert len(odd_fixed) == 1 and odd_fixed[0][1] % 4 == 1
    p = odd_fixed[0][0]
    return not any((p*t*t-B) % A == 0 for t in range(A))


def is_prime(n):
    return n >= 2 and len(factor(n)) == 1 and factor(n)[0][1] == 1


def beta_fiber(p):
    assert p % 2 and is_prime(p)
    beta = []
    for b in range(p*p):
        N = 8*b+1
        if N % p or N % (p*p) == 0:
            continue
        u = N//p
        # A square root of u modulo p exists iff u is a quadratic residue.
        squares = {x*x % p for x in range(p)}
        if p % 8 != 1 or u % p not in squares:
            beta.append(b)
    return beta


def main():
    total = 0
    for A in range(1, 61):
        for B in range(A):
            if criterion(A, B):
                total += 1
                for n in range(0 if B else 1, 100):
                    N = A*n+B
                    assert N > 0
                    assert divisor_count(N) % 4 == 0, (A, B, n, N)
    prime_checks = 0
    for p in range(3, 200, 2):
        if not is_prime(p):
            continue
        beta = beta_fiber(p)
        assert len(beta) == ((p-1)//2 if p % 8 == 1 else p-1), p
        if p <= 31:
            for b in range(p*p):
                assert criterion(8*p*p, 8*b+1) == (b in beta)
        prime_checks += 1
    assert beta_fiber(3) == [4, 7]
    assert beta_fiber(5) == [8, 13, 18, 23]
    b109 = beta_fiber(109)
    assert len(b109) == 108
    assert b109[:5] == [68, 177, 286, 395, 504]
    assert 109-1 == 108 and 108 % 27 == 0 and 109 % 8 == 5
    assert criterion(12, 10) and not criterion(12, 2)
    print('VERIFY_OK')
    print('all_progressions_A_at_most_60=1830')
    print('predicted_universal_progressions=', total)
    print('direct_terms_per_positive_progression=100')
    print('odd_primes_tested_up_to_199=', prime_checks)
    print('p109_fiber_size=', len(b109))
    print('p109_cubefree_prediction=54 actual=108')
    print('integer_arithmetic_and_quadratic_residue_checks=PASS')


if __name__ == '__main__':
    main()
