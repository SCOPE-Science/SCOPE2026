#!/usr/bin/env python3
"""Independent finite tests of consecutive Pell-type p-Frobenius thresholds.

No external dependencies. Finite checks are supplementary to the proof.
"""
from math import gcd


def pell(u, n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, u * b + a
    return a


def threshold(u, A, B, y, p):
    r = y // u
    q = p if r >= p else B + p - r - 1
    return B * y + A * q


def expected_frobenius(u, i, A, B, p):
    k = A // u
    if p <= k:
        return B * (A + u * p - 1) - A
    if p == k + 1:
        return B * (2 * A - 1) - (A if i % 2 else 0)
    raise ValueError('out of claimed range')


def count_direct(A, B, C, N):
    if N < 0:
        return 0
    count = 0
    for z in range(N // C + 1):
        R = N - z * C
        for y in range(R // B + 1):
            if (R - y * B) % A == 0:
                count += 1
    return count


def run():
    cases = 0
    residue_layer_checks = 0
    boundary_checks = 0
    global_checks = 0
    direct_checks = 0
    for u in range(2, 9):
        for i in range(2, 6):
            A, B, C = (pell(u, j) for j in (i, i + 1, i + 2))
            if A * B > 160000:
                continue
            assert gcd(A, B) == 1 and C == A + u * B
            assert A % u == i % 2
            k = A // u
            pmax = k + 1
            largest_T = max(threshold(u, A, B, y, pmax) for y in range(A))
            Nmax = largest_T + A
            ways = [0] * (Nmax + 1)
            ways[0] = 1
            for d in (A, B, C):
                for N in range(d, Nmax + 1):
                    ways[N] += ways[N - d]
            for p in range(pmax + 1):
                Ts = [threshold(u, A, B, y, p) for y in range(A)]
                predicted = expected_frobenius(u, i, A, B, p)
                assert max(Ts) - A == predicted
                assert Ts.count(max(Ts)) == 1
                for y, T in enumerate(Ts):
                    assert T <= Nmax and ways[T] >= p + 1
                    assert T < A or ways[T - A] <= p
                    residue_layer_checks += 1
                    boundary_checks += 2 if T >= A else 1
                assert max(j for j, d in enumerate(ways) if d <= p) == predicted
                assert ways[predicted] == p
                global_checks += 1
            for N in range(0, min(Nmax, 1500) + 1, 29):
                assert count_direct(A, B, C, N) == ways[N]
                direct_checks += 1
            cases += 1
    assert cases >= 12
    print('PASS')
    print('parameter_cases:', cases)
    print('residue_layer_thresholds:', residue_layer_checks)
    print('boundary_inequalities:', boundary_checks)
    print('global_extrema:', global_checks)
    print('independent_direct_counts:', direct_checks)
    print('The infinite theorem is established by the written proof, not finite testing.')


if __name__ == '__main__':
    run()
