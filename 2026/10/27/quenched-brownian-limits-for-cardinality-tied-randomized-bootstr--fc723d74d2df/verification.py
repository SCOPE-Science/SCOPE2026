"""Finite reproducibility checks for a cardinality-driven bootstrap walk.

Run: python verify_quenched_cardinality.py
These checks corroborate combinatorial identities; the functional theorem is analytical.
"""
from fractions import Fraction
from math import comb, lgamma, exp, log
from itertools import product


def odd_count(m):
    return sum(comb(m, k) % 2 for k in range(m + 1))


def expected_sign_exact(m, ps):
    result = Fraction(0)
    for bits in product((0, 1), repeat=len(ps)):
        weight = Fraction(1)
        for b, p in zip(bits, ps):
            weight *= p if b else (1 - p)
        parity = sum(bits[k] * (comb(m, k) % 2) for k in range(m + 1)) % 2
        result += (-1 if parity else 1) * weight
    return result


def expected_sign_product(m, ps):
    ans = Fraction(1)
    for k in range(m + 1):
        if comb(m, k) % 2:
            ans *= 1 - 2 * ps[k]
    return ans


count = 0
for m in range(513):
    assert odd_count(m) == (1 << m.bit_count())
    for k in range(m + 1):
        assert (comb(m, k) & 1) == int((k & m) == k)
        count += 1
print('Lucas parity identities:', count)

small = 0
for n in range(9):
    ps = [Fraction(1,3), Fraction(2,5), Fraction(3,7), Fraction(3,5)]
    ps = [ps[k % len(ps)] for k in range(n + 1)]
    for m in range(n+1):
        assert expected_sign_exact(m,ps) == expected_sign_product(m,ps)
        small += 1
print('Exact finite-environment expectation identities:', small)

q = 1/3
for n in (16,64,256,1024,4096):
    masses = [exp(lgamma(n+1)-lgamma(m+1)-lgamma(n-m+1)-n*log(2)) for m in range(n+1)]
    exact = sum(float(masses[m]) * q**(2**(m.bit_count()+1)) for m in range(n+1))
    bounds = []
    for r in (1,2,3,4):
        length = max(1,n.bit_length())
        exceptional = sum(comb(length,j) for j in range(r))
        upper = min(1.0, exceptional*masses[n//2]) + q**(2**(r+1))
        assert exact <= upper+1e-12, (n,r, exact,upper)
        bounds.append(round(upper,8))
    print('n=',n,'mean-environment-sign L2 squared=',format(exact,'.10g'),'bounds=',bounds)
print('All verifier checks passed.')
