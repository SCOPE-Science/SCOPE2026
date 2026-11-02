#!/usr/bin/env python3
"""Reproducible exact integer checks for reciprocal interval exchanges.

Use: python3 verify_periods.py.  No third-party packages are required.
The finite checks complement, but do not replace, the proof for every n.
"""
from math import gcd, lcm
from fractions import Fraction


def reverse_exchange(lengths):
    """Permutation of unit cells for a reversed half-open interval exchange."""
    boundaries = [0]
    for length in lengths:
        assert type(length) is int and length > 0
        boundaries.append(boundaries[-1] + length)
    full = boundaries[-1]
    shifts = [full - boundaries[k+1] - boundaries[k] for k in range(len(lengths))]
    result = []
    for j in range(full):
        k = next(k for k in range(len(lengths)) if boundaries[k] <= j < boundaries[k+1])
        result.append(j + shifts[k])
    assert sorted(result) == list(range(full)), "must permute all cells"
    return result, shifts


def cycles_of_permutation(mapping):
    seen = set()
    cycles = []
    for start in range(len(mapping)):
        if start in seen:
            continue
        cur = start
        length = 0
        while cur not in seen:
            seen.add(cur)
            length += 1
            cur = mapping[cur]
        assert cur == start
        cycles.append((start, length))
    assert len(seen) == len(mapping)
    return cycles


def three_interval_example(n):
    g = gcd(n, 3)
    D = n*(n+1)*(n+2)*(n+3)//(2*g)
    original = [Fraction(1, n+2)-Fraction(1, n+3),
                Fraction(1, n+1)-Fraction(1, n+2),
                Fraction(1, n)-Fraction(1, n+1)]
    lengths = [int(D*f) for f in original]
    assert all(D*f == length for f, length in zip(original, lengths))
    a,b,c = lengths
    assert (a,b,c) == (n*(n+1)//(2*g), n*(n+3)//(2*g),
                       (n+2)*(n+3)//(2*g))
    assert gcd(a+b, b+c) == 1
    assert a+b+c == 3*(n+1)*(n+2)//(2*g)
    return lengths


def main():
    checked = 0
    for n in range(1, 51):
        lengths = three_interval_example(n)
        mapping, shifts = reverse_exchange(lengths)
        a,b,c = lengths
        assert shifts == [b+c,c-a,-a-b]
        assert cycles_of_permutation(mapping) == [(0,sum(lengths))]
        checked += 1

    D = lcm(7,8,9,10,11)
    lengths = [int(D*(Fraction(1,k)-Fraction(1,k+1)))
               for k in (10,9,8,7)]
    assert D == 27720 and lengths == [252,308,385,495]
    mapping, shifts = reverse_exchange(lengths)
    assert shifts == [1188,628,-65,-945]
    assert cycles_of_permutation(mapping) == [(0,694),(1,373),(2,373)]
    assert Fraction(sum(lengths),D) == Fraction(4,77)
    assert Fraction(746,D) + Fraction(694,D) == Fraction(4,77)
    print(f'PASS: {checked} complete three-interval unit-cell permutations;')
    print('PASS: four-interval permutation of 1440 unit cells, cycles 694,373,373;')
    print('PASS: exact reciprocal endpoint lengths and period measure counts.')

if __name__ == '__main__':
    main()
