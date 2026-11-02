#!/usr/bin/env python3
"""Exact arithmetic checks for the six-support unitary-totient extremum.

Run with: python3 verify_unitary_phi_six.py
The universal inequalities and interval lemma are proved in RESULT.md.
"""
from itertools import combinations
from math import isqrt, prod


def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def prime_power_base(n):
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            if not prime(p):
                return None
            y = n
            while y % p == 0:
                y //= p
            return p if y == 1 else None
    return n if prime(n) else None


def unitary_weights(bases):
    ans = [1]
    for base in bases:
        ans += [w * (base - 1) for w in ans]
    return ans


def complete_by_bitset(bases):
    weights = unitary_weights(bases)
    reachable = 1
    for w in weights:
        reachable |= reachable << w
    total = prod(bases)
    return (reachable & ((1 << (total + 1)) - 1)) == ((1 << (total + 1)) - 1)


def criterion(bases):
    m = 1
    for base in bases:
        if base > m + 2:
            return False
        m *= base
    return True


def main():
    fermat = [2**(2**j) + 1 for j in range(6)]
    assert fermat[:5] == [3, 5, 17, 257, 65537]
    assert all(prime(f) for f in fermat[:5])
    assert fermat[5] == 641 * 6700417
    assert prime(641) and prime(6700417) and 641 != 6700417
    assert prime_power_base(fermat[5]) is None

    bases = [3, 5, 17, 257, 65537, 2**32]
    assert len(bases) == 6 and bases == sorted(bases)
    assert len(set(prime_power_base(b) for b in bases)) == 6
    assert all(prime_power_base(b) is not None for b in bases)
    assert criterion(bases)
    prefixes = [prod(bases[:i]) for i in range(1, 7)]
    assert prefixes[:5] == [2**(2**i) - 1 for i in range(1, 6)]
    g5 = 2**32 - 1
    max_n = prod(bases)
    assert max_n == 18446744069414584320
    assert max_n == g5 * (g5 + 1)
    assert max_n < g5 * (g5 + 2) == 2**64 - 1
    assert (g5 - 1) * (g5 + 1) < max_n

    # Independently test the theorem's exact criterion using all lists
    # of two or three distinct prime-power bases not exceeding 100.
    pp = [x for x in range(2, 101) if prime_power_base(x) is not None]
    tested = 0
    for k in (1, 2, 3):
        for bases_small in combinations(pp, k):
            if len(set(prime_power_base(b) for b in bases_small)) != k:
                continue
            if prod(bases_small) > 3000:
                continue
            assert complete_by_bitset(bases_small) == criterion(bases_small), bases_small
            tested += 1

    # Small OEIS A286906 members and nonmembers, verifying the convention.
    members = [1, 2, 3, 6, 12, 15, 30, 42, 60, 84, 105, 120, 132, 156, 165]
    # The identity 1 has the empty prime-power list.
    assert complete_by_bitset([])
    for n in members[1:]:
        y = n
        bs = []
        for p in range(2, n + 1):
            if not prime(p) or y % p:
                continue
            pk = 1
            while y % p == 0:
                y //= p
                pk *= p
            bs.append(pk)
            if y == 1:
                break
        assert prod(bs) == n and complete_by_bitset(sorted(bs)), (n, bs)
    print(f'VERIFY_OK six_bases={bases} maximum={max_n} greedy_deficit={(2**64-1)-max_n} finite_criterion_cases={tested} OEIS_examples={len(members)}')


if __name__ == '__main__':
    main()
