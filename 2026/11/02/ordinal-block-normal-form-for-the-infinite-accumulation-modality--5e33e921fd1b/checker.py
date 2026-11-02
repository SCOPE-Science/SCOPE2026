#!/usr/bin/env python3
"""Finite-alphabet analogue of the omega-accumulation tail calculation.

The theorem concerns infinite neighborhood intersections. This checker only
verifies the finite threshold-m analogue; it is not a transfinite proof.
"""
from itertools import combinations


def direct_derivative(A, N, m):
    return frozenset(x for x in range(N)
                     if sum(a <= x for a in A) >= m)


def predicted_first(A, N, m):
    elements = sorted(A)
    if len(elements) < m:
        return frozenset()
    return frozenset(range(elements[m - 1], N))


def predicted_iterated(A, N, m, stage):
    if stage == 0:
        return frozenset(A)
    elements = sorted(A)
    if len(elements) < m:
        return frozenset()
    start = elements[m - 1] + (stage - 1) * (m - 1)
    return frozenset(range(start, N))


def main():
    cases = 0
    comparisons = 0
    for N in range(0, 11):
        for m in range(2, 8):
            for mask in range(1 << N):
                A = frozenset(x for x in range(N) if mask & (1 << x))
                assert direct_derivative(A, N, m) == predicted_first(A, N, m)
                comparisons += 1
                B = A
                for stage in range(1, N + 3):
                    B = direct_derivative(B, N, m)
                    assert B == predicted_iterated(A, N, m, stage), (N, m, mask, stage)
                    comparisons += 1
                cases += 1
    # Closed-form ranks for finite threshold-m analogues.
    for N in range(0, 100):
        for m in range(2, 12):
            A = frozenset(range(N))
            count = 0
            while A:
                A = direct_derivative(A, N, m)
                count += 1
            if N == 0:
                expected = 0
            else:
                # At stage j, the first retained index is j*(m-1).
                expected = (N - 1) // (m - 1) + 1
            assert count == expected, (N,m,count,expected)
    print(f'ALL_CHECKS_OK subsets={cases} derivative_comparisons={comparisons} ranks=1100')


if __name__ == '__main__':
    main()
