#!/usr/bin/env python3
"""Self-contained exact checks for the balanced-cut path-graph-state law.

The finite enumeration supports, but does not replace, the analytic asymptotic proof.
"""
from collections import Counter, defaultdict
from itertools import permutations
from fractions import Fraction
from math import comb, factorial


def transfer_counts(n):
    counts = defaultdict(int)
    for b in (0, 1):
        counts[(b, 0, b, 0)] += 1
    for _ in range(n - 1):
        next_counts = defaultdict(int)
        for (last, used, cardinality, matched), ways in counts.items():
            for b in (0, 1):
                take = int(last != b and not used)
                next_counts[(b, take, cardinality + b, matched + take)] += ways
        counts = next_counts
    result = Counter()
    for (_, _, cardinality, matched), ways in counts.items():
        result[(cardinality, matched)] += ways
    return result


def binary_cut_rank(mask, n):
    pivots = {}
    rank = 0
    for v in range(n):
        if not (mask >> v) & 1:
            continue
        row = 0
        for w in (v - 1, v + 1):
            if 0 <= w < n and not ((mask >> w) & 1):
                row |= 1 << w
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                rank += 1
                break
            row ^= pivots[pivot]
    return rank


def permutation_sign(p):
    inversions = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inversions & 1 else 1


def characteristic_determinant(lam, z, t):
    # det(lam*I - T), in the state order (0,0),(0,1),(1,0),(1,1)
    T = [[1, 0, 0, z*t], [1, 0, z, 0], [0, t, z, 0], [1, 0, z, 0]]
    a = [[(lam if i == j else 0) - T[i][j] for j in range(4)] for i in range(4)]
    total = 0
    for p in permutations(range(4)):
        product = permutation_sign(p)
        for i, j in enumerate(p):
            product *= a[i][j]
        total += product
    return total


def run():
    # Degree <= 4 in every indeterminate, so agreement at five distinct values
    # of each variable certifies the exact polynomial identity.
    for lam in range(5):
        for z in range(5):
            for t in range(5):
                expected = lam * (lam**3 - (1 + z) * lam**2 + z*(1 - 2*t)*lam + t*z*(z + 1))
                assert characteristic_determinant(lam, z, t) == expected

    for n in range(2, 15):
        law = transfer_counts(n)
        assert sum(law.values()) == 2**n
        direct = Counter((mask.bit_count(), binary_cut_rank(mask, n)) for mask in range(1 << n))
        assert law == direct, (n, law, direct)
        if n >= 4 and n % 2 == 0:
            m = n // 2
            assert law[(m, 1)] == 2
            assert law[(m, m)] == 2**m
            assert sum(v for (k, r), v in law.items() if k == m) == comb(n, m)
    law = transfer_counts(12)
    assert {r: law[(6, r)] for r in range(1, 7)} == {1: 2, 2: 28, 3: 152, 4: 358, 5: 320, 6: 64}

    # Cumulant Hessian from implicit differentiation of the transfer cubic,
    # at (lambda,z,t)=(2,1,1), in logarithmic coordinates x=log z,y=log t.
    # Evaluate first and second derivatives of
    # P(lambda,e^x,e^y) = lambda^3-(1+z)*lambda^2
    #                       + z*(1-2t)*lambda + t*z*(z+1)
    # at lambda=2, x=y=0. These are *derivatives of P*, not
    # the unknown derivatives of its analytic eigenvalue root.
    P_l, P_x, P_y = Fraction(3), Fraction(-3), Fraction(-2)
    P_ll, P_lx, P_ly = Fraction(8), Fraction(-5), Fraction(-2)
    P_xx, P_xy, P_yy = Fraction(-1), Fraction(-1), Fraction(-2)
    lx, ly = -P_x/P_l, -P_y/P_l
    lxx = -(P_ll*lx*lx + 2*P_lx*lx + P_xx)/P_l
    lxy = -(P_ll*lx*ly + P_lx*ly + P_ly*lx + P_xy)/P_l
    lyy = -(P_ll*ly*ly + 2*P_ly*ly + P_yy)/P_l
    Hxx = lxx / 2 - lx**2 / 4
    Hxy = lxy / 2 - lx*ly / 4
    Hyy = lyy / 2 - ly**2 / 4
    assert (Hxx, Hxy, Hyy) == (Fraction(1,4), Fraction(0), Fraction(2,27))
    print('VERIFY_OK: exact transfer determinant, binary cut-rank enumeration n=2..14, endpoints, log-Hessian')

if __name__ == '__main__':
    run()
