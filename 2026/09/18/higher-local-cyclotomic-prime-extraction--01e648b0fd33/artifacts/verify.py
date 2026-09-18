#!/usr/bin/env python3
"""Exact-integer checks for the higher local cyclotomic extractor.

No external packages are used.  The script verifies the theorem for all squarefree
n <= LIMIT with at least two prime factors, at several evaluation bases.  Cyclotomic
values are evaluated from the Mobius product using only integer arithmetic.
"""
from functools import lru_cache
from math import prod

LIMIT = 5000
BASES = (3, 5, 6, 9, 10, 12, 15)
ODD_LOCAL_PRIMES = (3, 5)


def squarefree_prime_factors(n):
    ps = []
    t = n
    p = 2
    while p * p <= t:
        if t % p == 0:
            t //= p
            ps.append(p)
            if t % p == 0:
                return None
        p = 3 if p == 2 else p + 2
    if t > 1:
        ps.append(t)
    return ps


@lru_cache(maxsize=None)
def phi_squarefree_at(primes, x):
    primes = tuple(primes)
    k = len(primes)
    num = 1
    den = 1
    for mask in range(1 << k):
        d = 1
        selected = 0
        for i, p in enumerate(primes):
            if (mask >> i) & 1:
                d *= p
                selected += 1
        factor = pow(x, d) - 1
        exponent = 1 if ((k - selected) % 2 == 0) else -1
        if exponent == 1:
            num *= factor
        else:
            den *= factor
    assert num % den == 0
    return num // den


def vp(z, p):
    if z == 0:
        return None
    z = abs(z)
    e = 0
    while z % p == 0:
        z //= p
        e += 1
    return e


def main():
    general_checks = 0
    odd_binary_checks = 0
    even_binary_checks = 0
    indices = 0

    for n in range(2, LIMIT + 1):
        ps = squarefree_prime_factors(n)
        if ps is None or len(ps) < 2 or prod(ps) != n:
            continue
        indices += 1

        # Binary corollary.
        C2 = phi_squarefree_at(tuple(ps), 2)
        assert vp(C2 + 1, 2) == ps[0]
        prefix = []
        for j in range(len(ps) - 1):
            prefix.append(ps[j])
            q = ps[j + 1]
            A2 = phi_squarefree_at(tuple(prefix), 2)
            pair = (vp(C2 - A2, 2), vp(C2 * A2 - 1, 2))
            if ps[0] & 1:
                assert sorted(pair) == sorted((q, ps[0] + 1)), (n, ps, j, pair)
                odd_binary_checks += 1
            elif q > 3:
                assert sorted(pair) == [3, q], (n, ps, j, pair)
                even_binary_checks += 1

        # General odd-local-prime theorem.
        for x in BASES:
            C = phi_squarefree_at(tuple(ps), x)
            for ell in ODD_LOCAL_PRIMES:
                if x % ell:
                    continue
                a = vp(x, ell)
                prefix = []
                for j in range(len(ps) - 1):
                    prefix.append(ps[j])
                    q = ps[j + 1]
                    A = phi_squarefree_at(tuple(prefix), x)
                    pair = (vp(C - A, ell), vp(C * A - 1, ell))
                    assert sorted(pair) == sorted((a, q * a)), (n, x, ell, ps, j, pair)
                    general_checks += 1

    # Explicit example from the statement.
    ps = (3, 5, 7)
    C = phi_squarefree_at(ps, 2)
    assert C == 473474689919911
    A1 = phi_squarefree_at((3,), 2)
    A2 = phi_squarefree_at((3, 5), 2)
    example = {
        "C": C,
        "p1": vp(C + 1, 2),
        "stage1": (vp(C - A1, 2), vp(C * A1 - 1, 2)),
        "stage2": (vp(C - A2, 2), vp(C * A2 - 1, 2)),
    }
    assert example == {"C": C, "p1": 3, "stage1": (5, 4), "stage2": (4, 7)}

    print(f"squarefree indices checked: {indices}")
    print(f"general odd-local-prime stage checks: {general_checks}")
    print(f"odd squarefree binary stage checks: {odd_binary_checks}")
    print(f"even squarefree nonexceptional binary stage checks: {even_binary_checks}")
    print("n=105 example:", example)
    print("all exact-integer checks passed")


if __name__ == "__main__":
    main()
