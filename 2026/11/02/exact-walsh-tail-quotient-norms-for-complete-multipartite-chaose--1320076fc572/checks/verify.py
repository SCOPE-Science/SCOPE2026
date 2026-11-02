#!/usr/bin/env python3
"""Exact standalone finite checks for multipartite Walsh-tail extremizers.

Stdlib only. Verifies all Fourier coefficients through target degree via
an integer Walsh-Hadamard transform; no floating-point or external data.
"""
from math import comb, prod
from fractions import Fraction
from itertools import product


def central(n):
    m = n // 2
    return Fraction(comb(2*m, m), 4**m)


def hadamard_inplace(arr):
    step = 1
    while step < len(arr):
        for begin in range(0, len(arr), 2*step):
            for k in range(begin, begin+step):
                a, b = arr[k], arr[k+step]
                arr[k], arr[k+step] = a+b, a-b
        step *= 2


def check(sizes):
    r = len(sizes)
    N = sum(sizes)
    assert 2 <= r <= N <= 12
    # bit 0 means sign +1; bit 1 means sign -1.
    groups = []
    t = 0
    for n in sizes:
        groups.append(tuple(range(t, t+n)))
        t += n
    alpha = prod((central(n) for n in sizes), start=Fraction(1))
    C = 1/alpha
    values = []
    dual_product = 0
    norm = 0
    total_abs = 0
    for word in range(1 << N):
        Ss = [sum(1 if not ((word >> i) & 1) else -1 for i in group)
              for group in groups]
        Q = prod(Ss)
        s = prod((1 if k > 0 else -1 if k < 0 else 0 for k in Ss))
        v = C.numerator * s  # values scaled by C.denominator
        values.append(v)
        dual_product += v * Q
        norm = max(norm, abs(v))
        total_abs += abs(Q)
    assert norm == C.numerator
    assert Fraction(total_abs, 1 << N) == prod(
        (n*central(n) for n in sizes), start=Fraction(1))
    assert Fraction(dual_product, C.denominator * (1 << N)) == prod(sizes)
    trans = values[:]
    hadamard_inplace(trans)
    edges = 0
    for freq, val in enumerate(trans):
        if freq.bit_count() > r:
            continue
        intended = (freq.bit_count() == r and all(
            sum((freq >> i) & 1 for i in group) == 1 for group in groups))
        edges += int(intended)
        assert val == ((1 << N) * C.denominator if intended else 0), (
            sizes, freq, val, intended)
    assert edges == prod(sizes)
    # Exact weighted L1 stability check for a nonzero higher-order perturbation.
    if N > r:
        perturb = Fraction(1, 3)
        upper = C + abs(perturb)
        gap = upper/C - 1
        distance = Fraction(0)
        for word, v in enumerate(values):
            Ss = [sum(1 if not ((word >> i) & 1) else -1 for i in group)
                  for group in groups]
            Q = prod(Ss)
            parity = (-1)**word.bit_count()
            f = Fraction(v, C.denominator) + perturb*parity
            target = Fraction(v, C.denominator)
            distance += abs(Q) * abs(f-target)
        distance /= 1 << N
        assert distance <= 2 * gap * C * Fraction(total_abs, 1 << N)
    return 1


def main():
    cases = []
    for r in (2, 3, 4):
        for sizes in product((1, 2, 3, 4), repeat=r):
            if sum(sizes) <= 11:
                cases.append(sizes)
    for c in cases:
        check(c)
    print("PASS exact Fourier, dual, optimizer, and stability checks:", len(cases), "cases")


if __name__ == '__main__':
    main()
