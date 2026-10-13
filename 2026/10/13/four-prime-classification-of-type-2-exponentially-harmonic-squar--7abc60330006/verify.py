"""Exact regressions and exhaustive bounded four-prime search for a theorem on
exponentially harmonic numbers of type 2. Only standard Python is required.
The all-input assertions rest on the proof, not on the finite regression.
"""
from math import prod, isqrt

Q = (5, 7, 11, 23)
EXPECTED = {
    5: (7, 19, 199),
    7: (13, 41, 97, 293),
    11: (43, 241),
    23: (),
}

def prime(n):
    if n < 2:
        return False
    for a in range(2, isqrt(n) + 1):
        if n % a == 0:
            return False
    return True

def squarefree_prime_factors(m):
    out = []
    d = 2
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return None
            out.append(d)
        d += 1
    if m > 1:
        out.append(m)
    return out

def first_principles_e_harmonic_type2_base(primes):
    # For n=prod(p^2), e-divisors are all products of p or p^2.
    e_divs = [1]
    n = 1
    for p in primes:
        n *= p * p
        e_divs = [x * p for x in e_divs] + [x * p * p for x in e_divs]
    # Evaluate the reciprocal sum exactly by clearing the common denominator n.
    return (n * len(e_divs)) % sum(n // d for d in e_divs) == 0

def reduced_condition(primes):
    m = prod(primes)
    return (m * m * (1 << len(primes))) % prod(p + 1 for p in primes) == 0

# Verify the original e-divisor definition agrees with the reduction.
for m in range(1, 12001):
    ps = squarefree_prime_factors(m)
    if ps is None:
        continue
    assert first_principles_e_harmonic_type2_base(ps) == reduced_condition(ps)
    if reduced_condition(ps):
        assert m in (1, 6) or (
            m % 6 == 0
            and len(ps) >= 3 and ps[2] in Q
        ), (m, ps)

# All feasible q are realized by the squarefree base 6*q.
for q in Q:
    assert prime(q)
    assert reduced_condition([2, 3, q])
for q in range(5, 600):
    if prime(q):
        assert reduced_condition([2, 3, q]) == (q in Q)

# Exact theorem-derived upper bound for the last prime of any four-support base.
found = {}
for q in Q:
    upper = 48 * q * q
    eligible = []
    for r in range(q + 1, upper):
        if (upper % (r + 1) == 0) and prime(r):
            if (48 * q * q * r * r) % ((q + 1) * (r + 1)) == 0:
                eligible.append(r)
                assert reduced_condition([2, 3, q, r])
    found[q] = tuple(eligible)
    assert found[q] == EXPECTED[q], (q, found[q])

bases4 = sorted(6 * q * r for q in Q for r in found[q])
assert bases4 == [210, 546, 570, 1722, 2838, 4074, 5970, 12306, 15906]
assert len(bases4) == 9
print('EXACT_CERTIFICATE_OK q_spectrum=5,7,11,23 four_support=9 largest_base=15906 finite_regression=12000')
