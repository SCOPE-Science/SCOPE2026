#!/usr/bin/env python3
"""Finite checks for weighted Dyck spin states and Pauli moments.

Requirements: Python 3 and numpy. These checks do not prove the infinite-size theorem.
"""
import math
import itertools
import numpy as np


def dyck_words(n):
    def rec(up, down, w):
        if up == down == n:
            yield tuple(w)
            return
        if up < n:
            yield from rec(up + 1, down, w + [0])
        if down < up:
            yield from rec(up, down + 1, w + [1])
    return list(rec(0, 0, []))


def partition_defect(w):
    down = 0
    inv = 0
    heights = 0
    h = 0
    for b in w:
        if b == 0:
            inv += down
            h += 1
        else:
            down += 1
            h -= 1
        heights += h
    return inv, heights


def staircase_poly(n):
    counts = {}
    def rec(prev, j, size):
        if j == n:
            counts[size] = counts.get(size, 0) + 1
            return
        for x in range(min(prev, n - 1 - j) + 1):
            rec(x, j + 1, size + x)
    rec(n - 1, 0, 0)
    return counts


def state(n, q):
    count = 2**(2*n)
    a = np.zeros(count, dtype=np.float64)
    for w in dyck_words(n):
        x = 0
        for b in w:
            x = (x << 1) | b
        defect, area = partition_defect(w)
        assert area == n*n - 2*defect
        a[x] = q**(defect / 2)
    return a / np.linalg.norm(a)


def fwht(a):
    a = np.array(a, copy=True)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            u = a[i:i+h].copy()
            v = a[i+h:i+2*h].copy()
            a[i:i+h] = u + v
            a[i+h:i+2*h] = u - v
        h *= 2
    return a


def pauli_moment(statevector, alpha):
    dim = len(statevector)
    mask = np.arange(dim)
    total = 0.
    norm2 = 0.
    for flip in range(dim):
        overlaps = statevector * statevector[mask ^ flip]
        fourier = fwht(overlaps)
        total += np.sum(np.abs(fourier)**(2*alpha))
        norm2 += np.dot(fourier, fourier)
    return float(total / dim), float(norm2 / dim)


def main():
    for n in range(1, 7):
        ws = dyck_words(n)
        poly = {}
        for w in ws:
            defect, area = partition_defect(w)
            assert area == n*n - 2*defect
            poly[defect] = poly.get(defect, 0) + 1
        assert poly == staircase_poly(n)
        assert len(ws) == math.comb(2*n, n) // (n+1)
        print('n', n, 'Catalan', len(ws), 'coefficients', [poly.get(k,0) for k in range(n)])
    q = 0.25
    for n in range(1, 5):
        f, f1 = pauli_moment(state(n,q), 2)
        assert abs(f1 - 1.) < 1e-10
        assert 0. < f <= 1. + 1e-10
        print('n', n, 'q', q, 'F2', format(f,'.12f'), 'M2', format(-math.log2(f), '.12f'))
        if n == 2:
            z = (1-q)/(1+q)
            s = 2*math.sqrt(q)/(1+q)
            assert abs(f - (1-z*z*s*s)) < 1e-12
    print('All finite checks passed; infinite-size statements use the separate analytic proof.')


if __name__ == '__main__':
    main()
