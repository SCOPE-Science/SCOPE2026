#!/usr/bin/env python3
"""Exact verification for the p^2 local-triviality criterion."""

from math import comb

TARGET = [
    19, 37, 41, 47, 61, 67, 89, 113, 229, 239, 331, 373, 379, 383,
    397, 401, 431, 479, 503, 593, 613, 617, 643, 691, 719, 787, 811,
    877, 881, 907, 911,
]


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return n == d
        d += 1 if d == 2 else 2
    return True


def mul_quad(z, w, m):
    """Multiply in (Z/mZ)[sqrt(2)], represented by pairs."""
    a, b = z
    c, d = w
    return ((a * c + 2 * b * d) % m, (a * d + b * c) % m)


def pow_quad(z, n, m):
    r = (1, 0)
    while n:
        if n & 1:
            r = mul_quad(r, z, m)
        z = mul_quad(z, z, m)
        n >>= 1
    return r


def f_ring(p, a, b):
    """F_p(a,b) mod p^2 via the quadratic-ring identity."""
    m = p * p
    u, v = pow_quad((a, b), p, m)
    # coefficient of sqrt(2) in (1+sqrt(2))(a+b sqrt(2))^p
    return (u + v) % m


def coefficients(p):
    """Coefficients C(p,k) 2^floor(k/2) modulo p^2."""
    m = p * p
    out = []
    for k in range(p + 1):
        out.append((comb(p, k) * pow(2, k // 2, m)) % m)
    return out


def f_poly(p, a, b, coeff):
    """Independent direct polynomial evaluation of F_p(a,b) mod p^2."""
    m = p * p
    total = 0
    apow = [1] * (p + 1)
    bpow = [1] * (p + 1)
    for j in range(1, p + 1):
        apow[j] = (apow[j - 1] * a) % m
        bpow[j] = (bpow[j - 1] * b) % m
    for k, c in enumerate(coeff):
        total = (total + c * apow[p - k] * bpow[k]) % m
    return total


def branches(p):
    """Residue pairs mod p compatible with F_p(a,b)=1 mod p^2."""
    eps = 1 if pow(2, (p - 1) // 2, p) == 1 else -1
    coeff = coefficients(p)
    out = []
    for a in range(p):
        # F_p(a,b)=1 mod p implies a + eps*b = 1 mod p.
        b = (eps * (1 - a)) % p
        r1 = f_ring(p, a, b)
        r2 = f_poly(p, a, b, coeff)
        assert r1 == r2
        if r1 == 1:
            out.append((a, b))
    return out


def main():
    residual = [
        p for p in range(17, 912)
        if is_prime(p) and p % 24 in (13, 17, 19, 23)
    ]
    assert len(residual) == 84

    data = {p: branches(p) for p in residual}
    locally_trivial = [p for p in residual if data[p] == [(1, 0)]]
    assert locally_trivial == TARGET

    print("residual_prime_count =", len(residual))
    print("unique_mod_p_branch_count =", len(locally_trivial))
    print("unique_mod_p_branch_primes =", locally_trivial)
    print("branch_counts =")
    print(" ".join(f"{p}:{len(data[p])}" for p in residual))
    print("all_checks_passed = True")


if __name__ == "__main__":
    main()
