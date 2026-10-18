#!/usr/bin/env python3
"""Exact, dependency-free verification of the three-block Mersenne weight theorem.

Compares transfer-matrix coefficient predictions with exhaustive multiples
in the stated finite intervals, and checks the minimum/next-minimum formulas.
The finite experiment corroborates but does not replace the uniform proof.
"""
from collections import Counter


def polynomial(m):
    """[z^w] (M(z)^m)_(0,0) with M=[[3z,z^3],[1,3z^2]]."""
    current = {(0, 0): 1}
    transitions = {
        0: [(0, 3, 1), (1, 1, 3)],
        1: [(0, 1, 0), (1, 3, 2)],
    }
    for _ in range(m):
        nxt = {}
        for (carry, weight), count in current.items():
            for cnew, multiplicity, increment in transitions[carry]:
                key = (cnew, weight + increment)
                nxt[key] = nxt.get(key, 0) + count * multiplicity
        current = nxt
    return {weight: count for (carry, weight), count in current.items() if carry == 0}


def predicted(m):
    a = polynomial(m)
    out = Counter(a)
    out.update({3 * m - w: c for w, c in a.items()})
    out[3 * m] += 1
    return out


def direct(m):
    t = 1 << m
    modulus = t - 1
    return Counter((k * modulus).bit_count()
                   for k in range(1, t * t + t + 2))


def main():
    total = 0
    for m in range(1, 9):
        by_transfer = predicted(m)
        total += sum(by_transfer.values())
        by_arithmetic = direct(m)
        assert by_transfer == by_arithmetic, (m, by_transfer, by_arithmetic)
        assert sum(by_transfer.values()) == (1 << (2 * m)) + (1 << m) + 1
        assert by_transfer[m] == 3 ** m
        if m >= 2:
            assert by_transfer[m + 1] == m * 3 ** (m - 2)
            assert set(by_transfer) == set(range(m, 2*m+1)) | {3*m}
        assert by_transfer[3*m] == 1
        if m >= 2:
            t = 1 << m
            first = next(k for k in range(1, t * t + t + 2)
                         if (k * (t - 1)).bit_count() == m + 1)
            assert first == t + 3, (m, first)
        print(f'm={m}: {sum(by_transfer.values())} nonzero multiples; '
              f'weight histogram={dict(sorted(by_transfer.items()))}')
    print(f'ALL CHECKS PASSED: 8 values of m; {total} distinct positive multiples')


if __name__ == '__main__':
    main()
