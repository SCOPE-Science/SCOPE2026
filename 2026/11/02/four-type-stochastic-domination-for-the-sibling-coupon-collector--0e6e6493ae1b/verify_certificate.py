#!/usr/bin/env python3
"""Exact finite certificate for four-type sibling coupon-collector stochastic order.

Only Python standard-library arithmetic is used. All polynomial coefficient
checks are exhaustive identities, not numerical samples.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path

ZERO = (0, 0, 0, 0)

def c(n):
    return {ZERO: int(n)} if n else {}

def v(j):
    e = tuple(int(i == j) for i in range(4))
    return {e: 1}

def add(*polys):
    d = {}
    for poly in polys:
        for e, q in poly.items():
            d[e] = d.get(e, 0) + q
    return {e: q for e, q in d.items() if q}

def scale(poly, a):
    return {e: a*q for e, q in poly.items() if a*q}

def mul(a, b):
    d = {}
    for e, x in a.items():
        for f, y in b.items():
            g = tuple(e[i] + f[i] for i in range(4))
            d[g] = d.get(g, 0) + x*y
    return {e: q for e, q in d.items() if q}

def prod(polys):
    out = c(1)
    for poly in polys:
        out = mul(out, poly)
    return out

def power(poly, n):
    result = c(1)
    for _ in range(n):
        result = mul(result, poly)
    return result

def gap_polynomial():
    u, w1, w2, w3 = [v(j) for j in range(4)]
    x = [u, add(u, w1), add(u, w1, w2), add(u, w1, w2, w3)]
    total = add(*x)
    B = [add(total, scale(x[i], -1)) for i in range(4)]
    A = [prod(x[j] for j in range(4) if j != i) for i in range(4)]
    Q = prod(power(b, 3) for b in B)
    e3, e4 = add(*A), prod(x)
    # This is precisely 144 times the denominator-cleared rational gap
    # 47/144 - [6 sum(A_i/B_i^3) - 6 e3/S^3 - 48 e4/S^4].
    S4 = power(total, 4)
    removed = add(*(mul(A[i], prod(power(B[j], 3)
                             for j in range(4) if j != i))
                    for i in range(4)))
    P = add(scale(mul(S4, Q), 47),
            scale(mul(S4, removed), -864),
            scale(prod([e3, total, Q]), 864),
            scale(mul(e4, Q), 6912))
    return P

def pmf_from_arrival_integral(p):
    """Independent exponential last-arrival expansion, with exact integration."""
    p = tuple(Fraction(x) for x in p)
    assert len(p) == 4 and sum(p) == 1 and min(p) > 0
    C = [Fraction(0) for _ in range(4)]
    for k in range(4):
        other = [i for i in range(4) if i != k]
        for size in range(4):
            for S in combinations(other, size):
                rate = p[k] + sum(p[i] for i in S)
                for m in range(size + 1):
                    for A in combinations(S, m):
                        C[m] += (-1)**(size-m)*p[k]*factorial(m) * (
                            prod_fraction(p[i] for i in A)) / rate**(m+1)
    # G(z)=z*sum C_m*(z-1)^m.
    out = [Fraction(0) for _ in range(5)]
    for ell in range(1, 5):
        out[ell] = sum(((-1)**(m-(ell-1)) * comb(m, ell-1) * C[m]
                        for m in range(ell-1, 4)), Fraction(0))
    assert sum(out) == 1 and min(out) >= 0
    return out

def prod_fraction(xs):
    out = Fraction(1)
    for x in xs:
        out *= x
    return out

def closed_middle_tail(p):
    p = tuple(Fraction(x) for x in p)
    A = [prod_fraction(p[j] for j in range(4) if j != i)
         for i in range(4)]
    return (6*sum(A[i]/(1-p[i])**3 for i in range(4))
            - 6*sum(A) - 48*prod_fraction(p))

def verify():
    assertions = 0
    P = gap_polynomial()
    assert len(P) == 955; assertions += 1
    assert all(sum(e) == 16 for e in P); assertions += len(P)
    assert all(isinstance(q, int) and q > 0 for q in P.values())
    assertions += len(P)
    assert min(P.values()) == 47; assertions += 1
    # Explicit strictness witnesses: when any ordered gap is nonzero and
    # the smallest probability is positive, the polynomial is positive.
    for j in (1, 2, 3):
        mon = tuple(14 if i == 0 else 2 if i == j else 0
                    for i in range(4))
        assert P[mon] > 0
        assertions += 1
    table = Path(__file__).with_name('certificate.tsv').read_text('utf-8')
    expected = 'u\tv\tw\tz\tcoefficient\n' + ''.join(
        '\t'.join(map(str, (*e, q))) + '\n' for e, q in sorted(P.items()))
    assert table == expected; assertions += 1
    # The closed middle-tail identity is independently checked against
    # the exact last-arrival Poissonized integral expansion.
    test_vectors = [
        (1, 1, 1, 1), (1, 2, 3, 4), (1, 1, 1, 7),
        (1, 5, 7, 11), (2, 3, 5, 13), (3, 3, 4, 10),
        (1, 1, 8, 90), (7, 9, 10, 11)
    ]
    for raw in test_vectors:
        p = tuple(Fraction(a, sum(raw)) for a in raw)
        pmf = pmf_from_arrival_integral(p)
        assert pmf[3] + pmf[4] == closed_middle_tail(p)
        assert pmf[4] == 24*prod_fraction(p)
        assertions += 3
    p = (Fraction(1, 4),)*4
    pmf = pmf_from_arrival_integral(p)
    assert pmf == [0, Fraction(97,288), Fraction(97,288),
                   Fraction(67,288), Fraction(3,32)]
    assert sum(pmf[3:]) == Fraction(47,144)
    assertions += 2
    print('CERTIFICATE_OK; positive_terms=955; min_coeff=47; '
          'uniform_middle_tail=47/144; assertions=' + str(assertions))

if __name__ == '__main__':
    verify()
