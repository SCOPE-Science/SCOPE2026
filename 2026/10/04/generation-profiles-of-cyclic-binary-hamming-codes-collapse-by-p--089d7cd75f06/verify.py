#!/usr/bin/env python3
"""Exact finite checks for the cyclic-Hamming pair-generation formula."""
from collections import Counter


def pdeg(a):
    return a.bit_length() - 1


def pmod(a, b):
    db = pdeg(b)
    while a and pdeg(a) >= db:
        a ^= b << (pdeg(a) - db)
    return a


def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a


def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
    return r


def pmulmod(a, b, f):
    return pmod(pmul(a, b), f)


def ppowmod(a, e, f):
    r = 1
    while e:
        if e & 1:
            r = pmulmod(r, a, f)
        a = pmulmod(a, a, f)
        e >>= 1
    return r


def prime_factors(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def irreducible(f, m):
    x = 2
    y = x
    for _ in range(m):
        y = pmulmod(y, y, f)
    if y != x:
        return False
    for q in prime_factors(m):
        y = x
        for _ in range(m // q):
            y = pmulmod(y, y, f)
        if pgcd(y ^ x, f) != 1:
            return False
    return True


def primitive(f, m):
    if pdeg(f) != m or not irreducible(f, m):
        return False
    n = (1 << m) - 1
    for q in prime_factors(n):
        if ppowmod(2, n // q, f) == 1:
            return False
    return ppowmod(2, n, f) == 1


def discrete_log_one_plus_x(f, m):
    n = (1 << m) - 1
    target = 0b11
    z = 1
    for ell in range(n):
        if z == target:
            return ell
        z = pmulmod(z, 2, f)
    raise AssertionError("discrete log missing")


def pair_weight(v, n):
    return sum(1 for i in range(n) if ((v >> i) & 1) or ((v >> ((i + 1) % n)) & 1))


def rank_binary(vectors):
    piv = {}
    for x in vectors:
        y = x
        while y:
            b = y.bit_length() - 1
            if b in piv:
                y ^= piv[b]
            else:
                piv[b] = y
                break
    return len(piv)


def cyclic_codewords(g, m):
    n = (1 << m) - 1
    k = n - m
    return [pmul(q, g) for q in range(1 << k)]


def expected_middle_dimension(g, m):
    n = (1 << m) - 1
    ell = discrete_log_one_plus_x(g, m)
    c = 0b11 ^ (1 << ell)
    d = pgcd(c, (1 << n) | 1)
    return n - pdeg(d), ell, d


def exhaustive_small(g, m):
    n = (1 << m) - 1
    k = n - m
    words = cyclic_codewords(g, m)
    pw = {w: pair_weight(w, n) for w in words}
    dims = {}
    for a in range(0, 7):
        dims[a] = rank_binary([w for w in words if w and pw[w] <= a])
    mid, ell, d = expected_middle_dimension(g, m)
    assert all(dims[a] == 0 for a in range(0, 5))
    assert dims[5] == mid
    assert dims[6] == k
    assert min(pw[w] for w in words if w) == 5
    return Counter(pw.values()), dims, ell, d


def bits(*exponents):
    z = 0
    for e in exponents:
        z |= 1 << e
    return z


def main():
    # Small exhaustive checks.
    for m, g in [(3, bits(3, 1, 0)), (4, bits(4, 1, 0))]:
        assert primitive(g, m)
        exhaustive_small(g, m)

    # Degree-six examples showing both threshold regimes.
    g_a = bits(6, 1, 0)
    assert primitive(g_a, 6)
    dim_a, ell_a, d_a = expected_middle_dimension(g_a, 6)
    assert ell_a == 6
    assert d_a == g_a
    assert dim_a == 57

    g_b = bits(6, 4, 3, 1, 0)
    assert primitive(g_b, 6)
    dim_b, ell_b, d_b = expected_middle_dimension(g_b, 6)
    assert ell_b == 56
    assert d_b == bits(8, 7, 0)
    assert dim_b == 55
    assert (57 - dim_b) == 2
    assert (1 << (57 - dim_b)) == 4

    print("VERIFY_OK")


if __name__ == "__main__":
    main()
