#!/usr/bin/env python3
"""Independent numerical LP and direct constructive checks for linked-snake inballs.

Requires numpy and scipy. Run: python verify.py
Finite verification supplements, but does not replace, the all-dimensional proof.
"""
from itertools import product
from math import sqrt
import numpy as np
from scipy.optimize import linprog


def runs(bits):
    n = len(bits) + 1
    if n == 1:
        return []
    out = []
    left = 0
    for i in range(1, n):
        if i == n - 1 or bits[i] != bits[i - 1]:
            out.append((left, i))  # zero-indexed vertex interval
            left = i
    return out


def analytic(bits):
    n = len(bits) + 1
    lengths = [sqrt(n - i) for i in range(n)]
    weights = [2 * z for z in lengths]
    weights.extend((j - i) + lengths[i] + lengths[j]
                   for i, j in runs(bits))
    H = max(weights)
    return 1 / H


def canonical_center(bits):
    n = len(bits) + 1
    a = [sqrt(n - i) for i in range(n)]
    children = [[] for _ in range(n)]
    for i, sign in enumerate(bits):
        if sign == 0:
            children[i].append(i + 1)
        else:
            children[i + 1].append(i)
    L = [0.0] * n
    def f(i):
        if L[i] > 0:
            return L[i]
        L[i] = max([a[i]] + [1 + f(j) for j in children[i]])
        return L[i]
    for i in range(n):
        f(i)
    r = analytic(bits)
    t = [r * f(i) for i in range(n)]
    x = [bits[i] + t[i] - t[i + 1] for i in range(n - 1)] + [t[-1]]
    return r, np.array(x)


def original_halfspaces(bits):
    n = len(bits) + 1
    A, b = [], []
    for i in range(n):
        z = np.zeros(n)
        z[i:] = 1
        k = sum(bits[i:])
        A.extend((z.copy(), -z.copy()))
        b.extend((k + 1, -k))
        z = np.zeros(n)
        z[i] = 1
        A.extend((z.copy(), -z.copy()))
        b.extend((1, 0))
    return np.array(A), np.array(b)


def one_case(bits):
    n = len(bits) + 1
    r, x = canonical_center(bits)
    A, b = original_halfspaces(bits)
    normal = np.linalg.norm(A, axis=1)
    constructive_clearance = np.min((b - A @ x) / normal)
    assert constructive_clearance >= r - 1e-8, (bits, 'center', constructive_clearance, r)
    AA = np.column_stack((A, normal))
    objective = np.r_[np.zeros(n), -1.0]
    ans = linprog(objective, A_ub=AA, b_ub=b,
                  bounds=[(None, None)] * n + [(0, None)], method='highs')
    assert ans.success, (bits, ans.message)
    assert abs(ans.x[-1] - r) < 1e-7, (bits, ans.x[-1], r)
    return len(A)


def ehrhart_pair_check(n):
    if n < 4:
        return 0
    src = (1,) + (0,) * (n - 2)
    dst = (0,) * (n - 2) + (1,)
    count = 0
    for b in product((0, 1), repeat=n):
        A, rhs = original_halfspaces(src)
        x = np.array(b)
        if np.max(A @ x - rhs) > 0:
            continue
        t = [sum(b[i:]) - sum(src[i:]) for i in range(n)]
        tp = [1 - t[n - 1 - i] for i in range(n)]
        y = [dst[i] + tp[i] - tp[i + 1] for i in range(n - 1)] + [tp[-1]]
        AA, rr = original_halfspaces(dst)
        assert np.max(AA @ np.array(y) - rr) <= 0
        assert all(v in (0, 1) for v in y)
        count += 1
    assert analytic(src) > analytic(dst), (n, analytic(src), analytic(dst))
    return count


def main():
    cases = 0
    inequalities = 0
    for n in range(1, 11):
        for bits in product((0, 1), repeat=n - 1):
            inequalities += one_case(bits)
            cases += 1
    paired_vertices = sum(ehrhart_pair_check(n) for n in range(4, 10))
    print('PASS: profiles=', cases, 'shifted inequalities=', inequalities,
          'paired vertices=', paired_vertices)

if __name__ == '__main__':
    main()
