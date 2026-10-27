#!/usr/bin/env python3
"""Reproduce finite checks of the exact recurrent-state census for crown majority dynamics.

For each n, one binary integer encodes n labeled left spins in low n bits and n
right spins in high n bits. The graph has precisely the edges (L_i,R_j), i != j.
No external Python packages are required.
"""
from math import comb
from collections import Counter


def next_state(state, n):
    mask = (1 << n) - 1
    a, b = state & mask, state >> n
    weight_a, weight_b = a.bit_count(), b.bit_count()
    next_a = next_b = 0
    degree = n - 1
    for i in range(n):
        ai, bi = (a >> i) & 1, (b >> i) & 1
        left_neighbour_ones = weight_b - bi
        right_neighbour_ones = weight_a - ai
        if 2 * left_neighbour_ones > degree or (2 * left_neighbour_ones == degree and ai):
            next_a |= 1 << i
        if 2 * right_neighbour_ones > degree or (2 * right_neighbour_ones == degree and bi):
            next_b |= 1 << i
    return next_a | (next_b << n)


def expected_counts(n):
    if n % 2 == 0:
        s = comb(n, n // 2) + 2
        return s, s*s
    m = (n - 1) // 2
    return 2 * (m+2) * comb(n,m) + 2, 2 * (m+2) * comb(n,m) + 4


def verify():
    for n in range(3, 10):
        fixed = periodic = 0
        types = Counter()
        for state in range(1 << (2*n)):
            y = next_state(state,n)
            z = next_state(y,n)
            if y == state: fixed += 1
            if z == state:
                periodic += 1
                types[1 if y == state else 2] += 1
                if n%2:
                    mask=(1 << n)-1
                    if y != state:
                        assert (state & mask, state >> n) in {(0,mask),(mask,0)}
            if n % 2 == 0:
                assert next_state(z,n) == y, (n,state)
        fx, recur = expected_counts(n)
        assert (fixed, periodic) == (fx, recur), (n,fixed,periodic,fx,recur)
        assert periodic-fixed == (recur-fx)
        print(f"n={n} fixed={fixed} recurrent={periodic} primitive_2cycles={(periodic-fixed)//2} PASS")
    print("All exhaustive checks passed for n=3,...,9.")

if __name__ == '__main__':
    verify()
