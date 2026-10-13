#!/usr/bin/env python3
"""Exact modular checks for the radical-discriminant Dold multiplier theorem.

Only finite tests; the proof of the unrestricted assertion is in RESULT.md.
Requires Python 3 standard library only.
"""
from math import gcd, lcm, isqrt


def radical(n):
    n = abs(n)
    if n == 0:
        raise ValueError('radical of zero is undefined')
    out = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            out *= d
            while n % d == 0:
                n //= d
        d += 1
    return out * n if n > 1 else out


def lucas_mod(n, P, Q, modulus):
    if modulus == 1:
        return 0
    assert n >= 1
    def mul(a, b):
        return ((a[0]*b[0]+a[1]*b[2])%modulus,
                (a[0]*b[1]+a[1]*b[3])%modulus,
                (a[2]*b[0]+a[3]*b[2])%modulus,
                (a[2]*b[1]+a[3]*b[3])%modulus)
    A = (P % modulus, (-Q) % modulus, 1, 0)
    R = (1, 0, 0, 1)
    while n:
        if n & 1:
            R = mul(R, A)
        A = mul(A, A)
        n //= 2
    return R[2]  # U_n = (C^n)_(2,1)


def mobius(n):
    if n == 1:
        return 1
    k = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            k += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        k += 1
    return (-1)**k


def divisors(n):
    ans = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            ans.append(d)
            if d * d != n:
                ans.append(n // d)
    return ans


def check():
    nchecks = 0
    cases = 0
    stronger = 0
    # Full Möbius sums for many signed parameters (not just local checks).
    for P in range(-7, 8):
        for Q in range(-7, 8):
            delta = P*P - 4*Q
            if delta == 0:
                continue
            M = radical(delta)
            cases += 1
            if M < abs(delta):
                stronger += 1
            for n in range(1, 86):
                s = sum(mobius(n // d)*lucas_mod(d*d, P, Q, n)
                        for d in divisors(n))
                assert (M*s) % n == 0, (P,Q,n,delta,M,s)
                nchecks += 1
            # Sharpness witnessed already by n=p for each discriminant prime factor.
            for p in range(2, abs(delta)+1):
                if abs(delta) % p == 0 and all(p % d for d in range(2,isqrt(p)+1)):
                    assert (lucas_mod(p*p,P,Q,p)-1) % p == p-1, (P,Q,p)
    assert cases > 200
    even_power_checks = 0
    # The optimal multiplier is unchanged along any even-power index map.
    for P in range(-5,6):
        for Q in range(-5,6):
            delta = P*P - 4*Q
            if delta == 0: continue
            M = radical(delta)
            for s in [2,3,4]:
                for n in range(1,42):
                    total = sum(mobius(n//d)*lucas_mod(d**(2*s),P,Q,n)
                                for d in divisors(n))
                    assert (M*total)%n == 0, (P,Q,s,n)
                    even_power_checks += 1
    # Degenerate discriminant: arbitrarily many distinct prime obstructions.
    zero_cases = 0
    for P in range(-12,13,2):
        Q = P*P//4
        for p in [2,3,5,7,11,13,17,19]:
            assert (lucas_mod(p*p,P,Q,p)-1)%p == p-1
            zero_cases += 1
    # Explicit improvement over the previously published |Delta| scalar.
    for P,Q,expected in [(2,-8,6),(12,0,6),(2,-2,6),(1,-1,5),(0,-9,6)]:
        assert radical(P*P-4*Q) == expected
    print('VERIFY_OK')
    print(f'nonzero_discriminant_parameter_pairs={cases}')
    print(f'full_mobius_dold_congruences={nchecks}')
    print(f'parameter_pairs_strictly_improving_discriminant_multiplier={stronger}')
    print(f'higher_even_index_power_mobius_checks={even_power_checks}')
    print(f'zero_discriminant_prime_obstructions={zero_cases}')
    print('examples_(P,Q,minimal_M)=(2,-8,6);(12,0,6);(2,-2,6);(1,-1,5);(0,-9,6)')
    print('finite_tests_supplement_the_unrestricted_matrix_proof')


if __name__ == '__main__':
    check()
