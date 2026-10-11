#!/usr/bin/env python3
"""Exact integer/cyclotomic checks of Fourier orthogonality on prime-power parabolae.

No external packages required. Finite tests do not establish the universal theorem.
"""
from itertools import product
from math import gcd
from random import Random


def valuation(x, p, k):
    x %= p**k
    if x == 0:
        return k
    r = 0
    while x % p == 0:
        x //= p
        r += 1
    return r


def gauss_zero_exact(a, b, p, k):
    """Cyclotomic coefficient test modulo Phi_(p^k)(X)."""
    n = p**k
    root_block = p**(k - 1)
    counts = [0] * n
    for x in range(n):
        counts[(a*x+b*x*x) % n] += 1
    # Phi_(p^k)(X) = sum_{j=0}^{p-1} X^(j*p^(k-1)).
    return all(len({counts[r + j*root_block] for j in range(p)}) == 1
               for r in range(root_block))


def strict_contraction(bvals, p, k):
    n = p**k
    return all(valuation(bvals[x]-bvals[y], p, k) > valuation(x-y, p, k)
               for x in range(n) for y in range(x+1, n))


def digit_maps(p, k):
    """Enumerate all canonical digit tables; suitable for small parameters."""
    slots = [(j, a) for j in range(k) for a in range(p**j)]
    for digits in product(range(p), repeat=len(slots)):
        tables = [digits[sum(p**i for i in range(j)):sum(p**i for i in range(j+1))]
                  for j in range(k)]
        bvals = [sum(p**j*tables[j][x % (p**j)] for j in range(k))
                 for x in range(p**k)]
        yield tuple(bvals)


def brute_spectrum_count(p, k):
    """Independent exact backtrack among all q frequency-fibre assignments."""
    n = p**k
    allowed = {(x,y): {(bx,by) for bx in range(n) for by in range(n)
                       if gauss_zero_exact(x-y,bx-by,p,k)}
               for x in range(n) for y in range(x+1,n)}
    total = 0
    def walk(partial):
        nonlocal total
        a = len(partial)
        if a == n:
            total += 1
            return
        for b in range(n):
            if all((partial[x],b) in allowed[x,a] for x in range(a)):
                walk(partial + [b])
    walk([])
    return total


def verify():
    comparisons = 0
    for p, k in [(3,1), (3,2), (3,3), (5,1), (5,2), (7,1)]:
        n = p**k
        for a, b in product(range(n), repeat=2):
            observed = gauss_zero_exact(a, b, p, k)
            expected = valuation(a,p,k) < valuation(b,p,k)
            assert observed == expected, (p,k,a,b,observed,expected)
            comparisons += 1
    constructed = 0
    for p,k in [(3,1),(3,2),(5,1)]:
        patterns = set(digit_maps(p,k))
        assert len(patterns)==p**sum(p**j for j in range(k))
        for bvals in patterns:
            assert strict_contraction(bvals,p,k)
            assert all(gauss_zero_exact(x-y,bvals[x]-bvals[y],p,k)
                       for x in range(p**k) for y in range(x+1,p**k))
            constructed += 1
    rng = Random(1729)
    sampled = 0
    for p,k in [(3,3),(5,2)]:
        for rep in range(32):
            tables = [[rng.randrange(p) for _ in range(p**j)] for j in range(k)]
            bvals = [sum(p**j * tables[j][x%(p**j)] for j in range(k))
                     for x in range(p**k)]
            assert strict_contraction(bvals,p,k)
            assert all(gauss_zero_exact(x-y,bvals[x]-bvals[y],p,k)
                       for x in range(p**k) for y in range(x+1,p**k))
            sampled += 1
    independent = [(p,k,brute_spectrum_count(p,k)) for p,k in [(3,2),(5,1)]]
    assert independent == [(3,2,81),(5,1,5)]
    # First nontrivial modulus k=2: arbitrary maps violate the condition unless
    # the first output digit is constant and second depends only on first input digit.
    assert len(set(digit_maps(3,2))) == 3**4
    print(f'VERIFY_OK exact_cyclotomic_zero_pairs={comparisons} all_constructed_spectra={constructed} sampled_deeper_spectra={sampled} digit_count=PASS independent_exhaustive_spectrum_census=PASS all_orthogonality=PASS')


if __name__ == '__main__':
    verify()
