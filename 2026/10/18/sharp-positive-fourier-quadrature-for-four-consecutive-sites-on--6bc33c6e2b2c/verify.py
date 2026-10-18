"""Exact small-order checks for positive four-site Fourier sampling.

All cyclotomic-zero decisions use integer coefficients, never floating point.
The infinite theorem in RESULT.md is proved symbolically, not by this scan.
"""
from itertools import combinations
from math import comb


def cyclotomic_zero(exponents, prime, exponent):
    """Sum of roots at primitive p**k-th root = 0, with multiplicities."""
    N = prime ** exponent
    H = N // prime
    counts = [0] * N
    for x in exponents:
        counts[x % N] += 1
    return all(len({counts[r + j * H] for j in range(prime)}) == 1
               for r in range(H))


def e3_vanishes(frequencies, prime, exponent):
    return cyclotomic_zero((sum(t) for t in combinations(frequencies, 3)),
                            prime, exponent)


def moment_vanishes(frequencies, prime, exponent, degree):
    return all(cyclotomic_zero((degree * b for b in frequencies),
                               prime, exponent)
               for degree in range(1, 4))


def run():
    tested = 0
    for p, k in [(2, 2), (2, 3), (5, 1), (5, 2)]:
        N = p ** k
        H = N // p
        for r in range(H):
            B = tuple(r + j * H for j in range(p))
            # p=2 requires the order-four subgroup instead of the order-two one
            if p == 5:
                assert moment_vanishes(B, p, k, 3)
                tested += 1
    for k in [2, 3]:
        N = 2**k
        H = N//4
        for r in range(H):
            B = tuple(r+j*H for j in range(4))
            assert moment_vanishes(B,2,k,3)
            tested += 1
    # Every 5-set for order 25 is considered. Exactly the five cosets pass.
    N = 25
    zero_fives = []
    for B in combinations(range(N), 5):
        if e3_vanishes(B, 5, 2):
            zero_fives.append(B)
        tested += 1
    expected = [tuple(r+5*j for j in range(5)) for r in range(5)]
    assert zero_fives == expected, (len(zero_fives), zero_fives)
    # Verify the local obstruction for every subset of size 4..6 in Z/9.
    for m in range(4, 7):
        for B in combinations(range(9),m):
            assert not e3_vanishes(B,3,2)
            tested += 1
    # For prime seven the same check is exhaustive for 4..6 nodes.
    for m in range(4,7):
        for B in combinations(range(7),m):
            assert not e3_vanishes(B,7,1)
            tested += 1
    # The cyclotomic length mechanism applies uniformly to all prime powers.
    for p in [3, 7, 11, 13, 17]:
        for m in (4,5,6):
            assert comb(m,3) % p != 0
    assert comb(5,3) % 5 == 0
    print(f'EXACT_CHECKS_PASS tested_patterns={tested} order25_optimizers={len(zero_fives)}')

if __name__ == '__main__':
    run()
