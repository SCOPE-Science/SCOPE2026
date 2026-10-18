#!/usr/bin/env python3
"""Exact, finite regression tests for the Moser--de Bruijn coefficient-three theorem.

Run: python3 verify.py. Requires Python 3 standard library only.
Finite checks supplement, but do not replace, the symbolic carry proof.
"""
from collections import Counter


def moser_set(k):
    return [sum(((a >> j) & 1) * 4**j for j in range(k)) for a in range(1 << k)]


def carry_count(n, k):
    u, v = 1, 0
    for j in range(k):
        d = (n >> (2*j)) & 3
        if d == 0:
            u, v = u, u + v
        elif d == 1:
            u, v = u + v, v
        elif d == 2:
            u, v = v, 0
        else:
            u, v = u, 0
    return u


def theoretical_H(k):
    a, b = 1, 0
    for _ in range(k):
        a, b = 2*a + 2*b, a + 2*b
    return a + b


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def witness_digits(k):
    if k == 0:
        return []
    if k == 1:
        return [1]
    if k % 2 == 0:
        return [0, 1] * (k // 2)
    return [0, 0, 1] + [0, 1] * ((k - 3) // 2)


def from_least_digits(digits):
    return sum(d * 4**j for j, d in enumerate(digits))


def run():
    all_pairs = 0
    for k in range(0, 8):
        ss = moser_set(k)
        counter = Counter(a + 3*b for a in ss for b in ss)
        assert all(0 <= n < 4**k for n in range(4**k) if n in counter) or k == 0
        # If n < 4**k, digits above k cannot contribute to a+3b.
        small = {n: count for n, count in counter.items() if n < 4**k}
        assert len(small) == theoretical_H(k), (k, len(small), theoretical_H(k))
        for n in range(4**k):
            assert small.get(n, 0) == carry_count(n, k), (k, n)
        assert max(small.values()) == fibonacci(k + 1), k
        all_pairs += len(ss)**2
    for k in range(0, 22):
        # Independent recursion-only enumeration checks maximal u.
        state = {(1, 0)}
        for _ in range(k):
            state = {(u, u+v) for u,v in state} | {(u+v, v) for u,v in state} | {(v,0) for u,v in state} | {(u,0) for u,v in state}
        assert max(u for u,v in state) == fibonacci(k + 1), k
        witness = from_least_digits(witness_digits(k))
        assert witness < 4**k and carry_count(witness,k) == fibonacci(k+1), k
    print('MOSER_COEFFICIENT_THREE_EXACT_REGRESSION_OK k=0..7 brute; k=0..21 states; pairs=', all_pairs)


if __name__ == '__main__':
    run()
