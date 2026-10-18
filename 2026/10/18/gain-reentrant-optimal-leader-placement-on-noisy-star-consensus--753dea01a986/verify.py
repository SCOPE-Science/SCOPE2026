"""Exact-rational verification for finite-gain leader placement on a unit star.

Python standard library only. This finite test does not replace the all-order
Schur-complement proof.
"""
from fractions import Fraction as Q
from itertools import combinations


def star_matrix(n, leaders, gain):
    A = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        A[0][0] += 1
        A[i][i] += 1
        A[0][i] -= 1
        A[i][0] -= 1
    for i in leaders:
        A[i][i] += gain
    return A


def trace_inverse(A):
    n = len(A)
    M = [[Q(A[i][j]) for j in range(n)] +
         [Q(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        p = next(j for j in range(i, n) if M[j][i])
        M[i], M[p] = M[p], M[i]
        lead = M[i][i]
        M[i] = [x / lead for x in M[i]]
        for j in range(n):
            if j == i:
                continue
            coeff = M[j][i]
            if coeff:
                M[j] = [a - coeff*b for a,b in zip(M[j], M[i])]
    return sum((M[i][n+i] for i in range(n)), Q(0))


def schur_trace(n, q, gain, center):
    count = q - int(center)
    m = n - 1
    s1 = Q(m-count) + count/(1+gain)
    s2 = Q(m-count) + count/(1+gain)**2
    D = m + int(center)*gain - s1
    assert D > 0
    return s1 + (1+s2)/D


def difference(n, q, k):
    return ((1+k)**2 * (2*q-n) + k*q*(q-1)) / (
        q*(1+k)*(q+k))

checks = 0
for n in range(3, 15):
    for q in range(1, n):
        for k in [Q(1,10),Q(1,3),Q(1),Q(3),Q(10)]:
            selections = [(0,) + tuple(range(1,q)), tuple(range(1,q+1))]
            for leaders in selections:
                trace = trace_inverse(star_matrix(n, leaders, k))
                target = schur_trace(n, q, k, 0 in leaders)
                assert trace == target, (n,q,k,leaders,trace,target)
                checks += 1
            assert schur_trace(n, q, k, True) - schur_trace(n,q,k,False) == difference(n,q,k)
            checks += 1

# Exhaust all 35 placements for the smallest reentrant example.
for k, preferred_center in [(Q(1,10), True), (Q(1), False), (Q(10), True)]:
    values = []
    for leaders in combinations(range(7),3):
        value = trace_inverse(star_matrix(7, leaders, k))
        values.append((value, 0 in leaders))
        assert value == schur_trace(7, 3, k, 0 in leaders)
        checks += 1
    min_value = min(x for x,_ in values)
    assert all((x==min_value) == (c==preferred_center) for x,c in values)

assert schur_trace(7,3,Q(1),True) == Q(31,4)
assert schur_trace(7,3,Q(1),False) == Q(23,3)
assert difference(7,3,Q(1)) == Q(1,12)
# At the reciprocal algebraic thresholds k=2+-sqrt(3), the
# polynomial  k^2 - 4k + 1 vanishes; the discriminant is 12.
assert (Q(2)**2 - 4*Q(2) + 1) == -3
assert (Q(1)+Q(1))**2 == 4
print(f"VERIFY_OK rational_inverse_and_orbit_cases={checks} n=3..14; reentrant_example=n7_q3")
