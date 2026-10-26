#!/usr/bin/env python3
"""Exact finite-field certificate for degree-six points on genus-four hyperelliptic curves.

Only standard-library Python required.  A separable hyperelliptic genus-four
curve over F2 has a model y^2+h(x)y=f(x), deg(h)<=5, deg(f)<=10, h != 0.
For each of the nine degree-six x-orbits, splitting is governed by the
absolute F64 trace of f(x)/h(x)^2.
"""
from collections import Counter

# Polynomial u^6+u+1 defining F64/F2.
def multiply(a, b, modulus=0x43, size=64):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & size:
            a ^= modulus
    return r


def power(a, n, modulus=0x43, size=64):
    r = 1
    while n:
        if n & 1:
            r = multiply(r, a, modulus, size)
        a = multiply(a, a, modulus, size)
        n >>= 1
    return r


def evaluate(mask, x, modulus=0x43, size=64):
    a = 0
    for j in range(mask.bit_length() - 1, -1, -1):
        a = multiply(a, x, modulus, size) ^ ((mask >> j) & 1)
    return a


def trace(x, n, modulus=0x43, size=64):
    r = 0
    for _ in range(n):
        r ^= x
        x = multiply(x, x, modulus, size)
    assert r in (0, 1)
    return r


def rank(cols):
    pivots = {}
    for v in cols:
        while v:
            k = v.bit_length() - 1
            if k in pivots:
                v ^= pivots[k]
            else:
                pivots[k] = v
                break
    return len(pivots)


def check_degree_six():
    assert all(power(a, 64) == a for a in range(64))
    exact_degree_six = {a for a in range(64)
                        if power(a, 8) != a and power(a, 4) != a}
    assert len(exact_degree_six) == 54
    orbits = []
    while exact_degree_six:
        a = min(exact_degree_six)
        orbit = {power(a, 2**k) for k in range(6)}
        assert len(orbit) == 6 and orbit <= exact_degree_six
        exact_degree_six -= orbit
        orbits.append(a)
    assert len(orbits) == 9
    rank_counts = Counter()
    for h in range(1, 64):
        hv = [evaluate(h, a) for a in orbits]
        assert all(v != 0 for v in hv)  # deg h <= 5, degree(a)=6
        inv_h2 = [power(v, 61) for v in hv]  # v^(-2) in F64
        cols = []
        for j in range(11):
            column = sum(trace(multiply(power(a, j), denom), 6) << k
                         for k, (a, denom) in enumerate(zip(orbits, inv_h2)))
            cols.append(column)
        r = rank(cols)
        assert rank(cols + [0x1ff]) == r + 1  # all nine inert impossible
        rank_counts[r] += 1
    assert rank_counts == {4: 3, 5: 60}, rank_counts
    print('hyperelliptic_h_count=63 rank_histogram=', dict(rank_counts),
          'all_9_inert_impossible=yes')


def check_degree_five_witness():
    # F32 = F2[u]/(u^5+u^2+1).  For y^2+y=x^9+x^5+1,
    # the affine trace equals 1 for every x in F32.
    n = 5
    traces = [trace(evaluate((1 << 9) | (1 << 5) | 1, x,
                             modulus=0x25, size=32), n,
                    modulus=0x25, size=32)
              for x in range(32)]
    assert all(power(x, 32, 0x25, 32) == x for x in range(32))
    assert traces == [1] * 32
    # The odd-degree Artin-Schreier equation has one point at infinity.
    N5 = 1 + 2 * traces.count(0)
    N1 = 1  # both affine x=0,1 give right side 1 (trace 1 over F2)
    assert N1 == N5 == 1
    print('degree_five_witness_N1=N5=1; genus=4; B5=0')


if __name__ == '__main__':
    check_degree_six()
    check_degree_five_witness()
    print('HYPERELLIPTIC_VERIFY_OK')
