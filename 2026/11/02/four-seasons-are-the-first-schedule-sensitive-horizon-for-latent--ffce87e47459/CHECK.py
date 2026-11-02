#!/usr/bin/env python3
"""Exact arithmetic replay of the displayed four-season matrix identities.

Uses only Python's standard library. The universal conclusion is established by
algebra in RESULT.md; finite tests serve as reproducibility checks, not proof.
"""
from fractions import Fraction as F
from itertools import permutations, combinations, product


def mul(A, B):
    return ((A[0][0]*B[0][0] + A[0][1]*B[1][0],
             A[0][0]*B[0][1] + A[0][1]*B[1][1]),
            (A[1][0]*B[0][0] + A[1][1]*B[1][0],
             A[1][0]*B[0][1] + A[1][1]*B[1][1]))


def matrix(a, c, d, b):
    return ((a, b), (c, d))


def monodromy(a, c, d, sequence):
    P = ((F(1), F(0)), (F(0), F(1)))
    for b in sequence:
        P = mul(P, matrix(a, c, d, b))
    return P


def trace(P):
    return P[0][0] + P[1][1]


def det(P):
    return P[0][0]*P[1][1] - P[0][1]*P[1][0]


def expected_trace(a, c, d, sequence):
    n = len(sequence)
    S = sum(sequence)
    if n == 1:
        return a + d
    if n == 2:
        return a*a + d*d + c*S
    if n == 3:
        return a**3 + d**3 + c*(a+d)*S
    if n == 4:
        b1,b2,b3,b4 = sequence
        return (a**4 + d**4 + c*(a*a+a*d+d*d)*S
                + c*c*(b1*b3 + b2*b4))
    raise ValueError(n)


def tests():
    attempts = 0
    grid = (F(1,20),F(1,10),F(1,5),F(2,5),F(3,5),F(4,5))
    for a,c,d in product((F(1,4),F(1,2),F(3,4)),repeat=3):
        for bs in combinations(grid, 4):
            traces = {}
            for perm in permutations(bs):
                P = monodromy(a,c,d,perm)
                assert trace(P) == expected_trace(a,c,d,perm)
                expected_d = F(1)
                for b in perm:
                    expected_d *= (a*d-c*b)
                assert det(P) == expected_d
                q = perm[0]*perm[2] + perm[1]*perm[3]
                traces.setdefault(q, []).append(trace(P))
                attempts += 1
            assert len(traces) == 3
            assert sorted(len(v) for v in traces.values()) == [8,8,8]
            ordered = sorted(traces)
            assert all(all(x == trace_list[0] for x in trace_list)
                       for trace_list in traces.values())
            assert traces[ordered[0]][0] < traces[ordered[1]][0] < traces[ordered[2]][0]
        for n in (1,2,3):
            bs = grid[:n]
            vals = set()
            for perm in permutations(bs):
                P = monodromy(a,c,d,perm)
                assert trace(P) == expected_trace(a,c,d,perm)
                vals.add((trace(P),det(P)))
                attempts += 1
            assert len(vals) == 1
    a=d=c=F(1,2)
    low,high=F(1,20), F(1)
    alternating=monodromy(a,c,d,(low,high,low,high))
    grouped=monodromy(a,c,d,(low,low,high,high))
    D=F(81,25600)
    assert trace(alternating)==F(1861,1600)
    assert trace(grouped)==F(15,16)
    assert det(alternating)==det(grouped)==D
    assert F(1)-trace(alternating)+D==F(-4095,25600)
    assert F(1)-trace(grouped)+D==F(1681,25600)
    assert trace(grouped)<1
    print('OK: %d exact trace/determinant comparisons; three strict classes for each generic four-season set; sub-four permutation invariance; invasion reversal.' % attempts)


if __name__ == '__main__':
    tests()
