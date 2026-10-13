"""Finite checks supporting a prime-support obstruction for a divisor-sum congruence.

The proof is independent of the finite checks. Run with Python 3 and no external packages.
"""
from fractions import Fraction


def sieve_sigma(N):
    values = [0] * (N + 1)
    for d in range(1, N + 1):
        for k in range(d, N + 1, d):
            values[k] += d
    return values


def omega_support_and_odd_square_part(n):
    remaining = n
    count = 0
    odd_part_square = True
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            exponent = 0
            while remaining % p == 0:
                exponent += 1
                remaining //= p
            count += 1
            if p != 2 and exponent % 2:
                odd_part_square = False
        p += 1 if p == 2 else 2
    if remaining > 1:
        count += 1
        if remaining % 2:
            odd_part_square = False
    return count, odd_part_square


def geometric_sum(p, e):
    return sum(p ** j for j in range(e + 1))


def main():
    N = 1000000
    sigmas = sieve_sigma(N)
    hits = []
    odd_small_support_hits = []
    even_small_support_hits = []
    even_nonsquare_oddpart_hits = []
    for n in range(6, N + 1):
        if sigmas[n] % n == 5:
            hits.append(n)
            count, square_oddpart = omega_support_and_odd_square_part(n)
            if n % 2 and count < 4:
                odd_small_support_hits.append(n)
            if n % 2 == 0 and count < 3:
                even_small_support_hits.append(n)
            if n % 2 == 0 and not square_oddpart:
                even_nonsquare_oddpart_hits.append(n)
    assert not odd_small_support_hits
    assert not even_small_support_hits
    assert not even_nonsquare_oddpart_hits
    assert Fraction(3, 2)*Fraction(5, 4)*Fraction(17, 16) < 2
    assert Fraction(3, 2)*Fraction(7, 6)*Fraction(11, 10) < 2
    assert Fraction(5, 4)*Fraction(7, 6)*Fraction(11, 10) < 2
    for p in (3, 5, 7, 11, 13):
        for e in range(2, 22, 2):
            if p in (7, 13):
                assert geometric_sum(p, e) % 5 != 0
            if p in (5, 11):
                assert geometric_sum(p, e) % 3 == 1
    for a in range(1, 20):
        t = 2 ** (a + 1)
        for p in (3, 5, 7, 11, 13, 17, 19, 23):
            for b in range(2, 16, 2):
                lhs = (t-p)*geometric_sum(p,b-1)
                n = 2 ** a * p ** b
                assert (lhs == 6) == ((2 ** (a+1)-1)*geometric_sum(p,b) == 2*n + 5)
                assert lhs != 6
    print(f'VERIFY_OK range=6..{N} residue_five_hits={len(hits)} support_violations=0 local_power_cases={19*8*7} low_boundaries_passed=3')
    if hits:
        print('residue_five_witnesses=', hits[:20])


if __name__ == '__main__':
    main()
