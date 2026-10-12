"""Exact finite regression checks for the odd-squarefree totient/divisor theorem.

The unrestricted exclusion is established by the written proof, not by this file.
"""
from fractions import Fraction
from itertools import combinations
from math import prod


def local_gap(primes):
    return prod(primes) - 2 * prod(p - 1 for p in primes)


def arithmetic_signatures(r, bound=48):
    result = []
    for k in range(r, bound):
        numerator = k + 3
        denominator = 1 << (k - r)
        if numerator % denominator == 0 and (numerator // denominator) % 2:
            result.append((k, numerator // denominator))
    return result


def upper_ratio(primes):
    return prod((Fraction(p, p - 1) for p in primes), start=Fraction(1))


def sieve_phi_tau(bound):
    phi = list(range(bound + 1))
    tau = [0] * (bound + 1)
    tau[1] = 1
    for p in range(2, bound + 1):
        if phi[p] == p:
            for n in range(p, bound + 1, p):
                phi[n] -= phi[n] // p
    for d in range(1, bound + 1):
        for n in range(d, bound + 1, d):
            tau[n] += 1
    return phi, tau


def odd_part_squarefree(n):
    while not n & 1:
        n //= 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            n //= d
            if n % d == 0:
                return False
        d += 2
    return True


def main():
    assert arithmetic_signatures(3) == []
    assert arithmetic_signatures(4) == [(4, 7)]
    assert arithmetic_signatures(5) == []
    assert arithmetic_signatures(6) == [(6, 9), (7, 5)]
    assert upper_ratio([5, 7, 11, 13]) == Fraction(1001, 576) < 2
    assert upper_ratio([3, 11, 13, 17]) == Fraction(2431, 1280) < 2
    assert upper_ratio([5, 7, 11, 13, 17, 19]) == Fraction(323323, 165888) < 2
    assert upper_ratio([3, 13, 17, 19, 23, 29]) == Fraction(2800733, 1419264) < 2
    assert upper_ratio([3, 11, 17, 23, 29, 41]) < 2
    assert all(local_gap([3, 5, p]) > 0 for p in (7, 11, 13))
    assert 233 > 1 and all(233 % d for d in range(2, 16))
    assert 249 == 3 * 83
    for r in range(0, 7):
        ps = [3, 5, 7, 11, 13, 17][:r]
        for k in range(0, 14):
            P = prod(ps)
            Q = prod(p - 1 for p in ps)
            n = (1 << (k + 2)) * P
            phi = (1 << (k + 1)) * Q
            tau = (k + 3) * (1 << r)
            assert (phi + tau == n // 4) == ((1 << k) * (P - 2 * Q) == (1 << r) * (k + 3))
    source_m = (1 << 4) * 3 * 5 * 17 * 251
    source_n = 4 * source_m
    source_phi = (1 << 5) * 2 * 4 * 16 * 250
    source_tau = 7 * 16
    assert source_m == 1024080 and source_phi == 1024000
    assert source_phi + source_tau - source_m == 32
    bound = 100000
    phi, tau = sieve_phi_tau(bound)
    examined = 0
    for n in range(4, bound + 1, 4):
        if odd_part_squarefree(n):
            examined += 1
            assert phi[n] + tau[n] != n // 4
    print('VERIFY_OK')
    print('valuation_signatures_r3_to_r6=' + repr({r: arithmetic_signatures(r) for r in range(3, 7)}))
    print('rational_prime_product_bounds=PASS')
    print('algebraic_factorization_checks=PASS')
    print('source_proposed_example_gap=32')
    print('direct_squarefree_odd_part_tested=%d_up_to=%d' % (examined, bound))
    print('unrestricted_claim_depends_on_symbolic_proof=TRUE')


if __name__ == '__main__':
    main()
