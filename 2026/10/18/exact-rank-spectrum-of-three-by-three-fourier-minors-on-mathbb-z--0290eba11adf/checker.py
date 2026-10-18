"""Finite modular cross-check of an analytic three-by-three Fourier-minor classification.

Uses primes congruent to 1 modulo the Fourier order. Modular agreement
corroborates examples; it does not imply the theorem over the complex numbers.
"""
from itertools import combinations
from math import comb


def prime(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


def primitive_root(n, modulus):
    for g in range(2, modulus):
        z = pow(g, (modulus - 1) // n, modulus)
        if pow(z, n, modulus) == 1 and pow(z, n // 3, modulus) != 1 and pow(z, n // (n // 3), modulus) != 1:
            return z
    raise AssertionError('No primitive root')


def run(p):
    assert p >= 5 and prime(p)
    n = 3 * p
    modulus = n * 1000 + 1
    while not prime(modulus) or modulus % n != 1:
        modulus += n
    root = primitive_root(n, modulus)
    powers = [pow(root, j, modulus) for j in range(n)]
    tris = list(combinations(range(n), 3))
    rcount = [0, 0, 0, 0]
    for R in tris:
        a = (R[1] - R[0]) % n
        b = (R[2] - R[0]) % n
        r3pure = R[0] % 3 == R[1] % 3 == R[2] % 3
        rppure = R[0] % p == R[1] % p == R[2] % p
        r3collision = len({x % 3 for x in R}) < 3
        rpcollision = len({x % p for x in R}) < 3
        for C in tris:
            c = (C[1] - C[0]) % n
            d = (C[2] - C[0]) % n
            c3pure = C[0] % 3 == C[1] % 3 == C[2] % 3
            cppure = C[0] % p == C[1] % p == C[2] % p
            c3collision = len({x % 3 for x in C}) < 3
            cpcollision = len({x % p for x in C}) < 3
            singular = ((r3pure and cpcollision) or (c3pure and rpcollision)
                        or (rppure and c3collision) or (cppure and r3collision))
            rank_one = (r3pure and cppure) or (rppure and c3pure)
            x = powers[(a * c) % n]
            y = powers[(a * d) % n]
            z = powers[(b * c) % n]
            t = powers[(b * d) % n]
            determinant_zero = ((x - 1) * (t - 1) - (y - 1) * (z - 1)) % modulus == 0
            rank1_mod = x == y == z == t == 1
            assert determinant_zero == singular, (p, R, C, singular, determinant_zero)
            assert rank1_mod == rank_one, (p, R, C, rank_one, rank1_mod)
            rank = 1 if rank1_mod else 2 if determinant_zero else 3
            rcount[rank] += 1
    T = comb(n, 3)
    r1 = p*p*(p-1)*(p-2)
    rs = p*p*(p-1)*(9*p*p-20*p+16)
    expected = [0, r1, rs-r1, T*T-rs]
    assert rcount == expected, (p, rcount, expected)
    print(f'CHECK_PASS p={p} n={n} triples={T} modulus={modulus} root={root} rank1={rcount[1]} rank2={rcount[2]} rank3={rcount[3]} full_exhaustive_modular=true')

if __name__ == '__main__':
    for p in (5, 7):
        run(p)
