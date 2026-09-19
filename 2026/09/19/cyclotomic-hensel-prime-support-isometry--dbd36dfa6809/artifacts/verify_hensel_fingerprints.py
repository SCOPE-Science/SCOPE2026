#!/usr/bin/env python3
"""Exact checks for the cyclotomic Hensel fingerprint identities."""

import itertools
import math
import sympy as sp

X = sp.symbols("X")
K = 64


def cyclotomic_coeffs(n):
    poly = sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)
    return [int(poly.nth(i)) for i in range(poly.degree() + 1)]


def eval_mod(coeffs, a, modulus):
    value = 0
    for c in reversed(coeffs):
        value = (value * a + c) % modulus
    return value


def even_hensel_root(n, precision):
    coeffs = cyclotomic_coeffs(n)
    coeffs[0] += 1  # Phi_n(X)+1
    root = 0
    assert eval_mod(coeffs, root, 2) == 0
    for k in range(1, precision):
        modulus = 1 << (k + 1)
        candidates = (root, root + (1 << k))
        good = [c for c in candidates if eval_mod(coeffs, c, modulus) == 0]
        assert len(good) == 1
        root = good[0]
    return root


def v2_integer(z):
    if z == 0:
        return 10**9
    z = abs(z)
    return (z & -z).bit_length() - 1


def v2_mod_difference(a, b, precision):
    d = (a - b) % (1 << precision)
    if d == 0:
        return precision
    return (d & -d).bit_length() - 1


def prime_support(n):
    return set(sp.factorint(n))


squarefree = [n for n in range(2, 301) if sp.mobius(n) != 0]
roots = {n: even_hensel_root(n, K) for n in squarefree}

pair_checks = 0
for i, n in enumerate(squarefree):
    sn = prime_support(n)
    for m in squarefree[i + 1:]:
        sm = prime_support(m)
        q = min(sn ^ sm)
        if q < K:
            assert v2_mod_difference(roots[n], roots[m], K) == q
            pair_checks += 1

even_base_checks = 0
for n in range(2, 201):
    poly = sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)
    is_squarefree = sp.mobius(n) != 0
    for a in range(-40, 41, 2):
        value = int(poly.eval(a)) + 1
        actual = v2_integer(value)
        if is_squarefree:
            predicted = v2_mod_difference(a, roots[n], K)
            if actual < K:
                assert actual == predicted
        else:
            assert actual == 1
        even_base_checks += 1

residue_levels = 0
for B in range(3, 13):
    primes = list(sp.primerange(2, B))
    residues = set()
    for bits in itertools.product((0, 1), repeat=len(primes)):
        chosen = [p for p, bit in zip(primes, bits) if bit]
        if not chosen:
            alpha = 2 % (1 << B)
        else:
            alpha = even_hensel_root(math.prod(chosen), B)
        residues.add(alpha)
    assert len(residues) == 2 ** len(primes)
    residue_levels += 1

print(f"sympy_version={sp.__version__}")
print(f"squarefree_roots={len(squarefree)}")
print(f"pair_isometry_checks={pair_checks}")
print(f"even_base_checks={even_base_checks}")
print(f"residue_count_levels={residue_levels}")
print("status=PASS")
