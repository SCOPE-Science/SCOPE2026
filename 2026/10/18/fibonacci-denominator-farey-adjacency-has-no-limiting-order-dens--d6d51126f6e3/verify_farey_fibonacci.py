#!/usr/bin/env python3
"""Independent exact tests of a Fibonacci-denominator Farey-adjacency law.

Run with Python 3.9+; uses only the standard library. Finite tests are
corroboration, not an infinite proof.
"""
from math import gcd


def fib_values(bound):
    p, q = 1, 2
    vals = [1]
    while q <= bound:
        vals.append(q)
        p, q = q, p + q
    return vals


def farey_denominators(n):
    """Actual full Farey sequence denominator order, including both endpoints."""
    if n == 1:
        return [1, 1]
    a, b, c, d = 0, 1, 1, n
    den = [b]
    while c <= n:
        den.append(d)
        k = (n + b) // d
        a, b, c, d = c, d, k*c-a, k*d-b
    return den


def q_pair(n):
    vals = fib_values(n)
    return sum(gcd(a,b) == 1 and a+b > n for a in vals for b in vals)


def q_actual(n):
    vals = set(fib_values(n))
    seq = farey_denominators(n)
    return sum(x in vals and y in vals for x,y in zip(seq,seq[1:]))


def theorem(n):
    fib = [0,1]
    while fib[-1] <= n:
        fib.append(fib[-1]+fib[-2])
    k = len(fib)-2  # F_k <= n < F_(k+1)
    assert k >= 6
    t = fib[k] + fib[k-2]
    e = max(fib[k-2], n-fib[k]+1)
    return (n >= t),e


def main():
    e = 0
    for n in range(1,451):
        q = q_actual(n)
        assert q == q_pair(n), (n,q,q_pair(n))
        e += (q == 2)
        if n >= 8:
            yes, exact_e = theorem(n)
            assert (q == 2) == yes, (n,q,yes)
            assert e == exact_e,(n,e,exact_e)
    for n in range(451,15001):
        q = q_pair(n)
        e += (q == 2)
        yes, exact_e = theorem(n)
        assert (q == 2) == yes,(n,q,yes)
        assert e == exact_e,(n,e,exact_e)
    print('FAREY_FIBONACCI_EXACT_REGRESSION_OK full_farey=450 gcd_pairs=15000')

if __name__ == '__main__':
    main()
