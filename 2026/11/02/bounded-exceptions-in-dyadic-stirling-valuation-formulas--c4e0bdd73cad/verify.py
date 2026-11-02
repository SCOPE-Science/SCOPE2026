#!/usr/bin/env python3
"""Finite recurrence checks for the theorem on dyadic Stirling valuations.

Only mathematical reproducibility data are contained here.  The infinite
statement relies on the algebraic partition-sum proof, not this finite test.
"""
from math import comb, factorial, prod
from fractions import Fraction

MOD = 1 << 32

def v2(x):
    if x == 0:
        return 32  # Undefined above the modulus; assert predicted < 32.
    return (x & -x).bit_length() - 1


def enumerate_partitions_up_to(weight, part_size=1, multiplicities=()):
    if part_size > weight:
        yield multiplicities
        return
    for count in range(weight // part_size + 1):
        yield from enumerate_partitions_up_to(
            weight - part_size * count, part_size + 1,
            multiplicities + (count,)
        )

def stirling_partition_identity(n, k):
    """Exactly replay the rational partition identity from the proof."""
    r = n-k
    total = Fraction(0)
    for u in enumerate_partitions_up_to(r):
        d = sum(u)
        multinomial = factorial(d) // prod(factorial(x) for x in u)
        denominator = prod((i+1)**x for i,x in enumerate(u,1))
        total += Fraction((-1)**d*comb(n+d,n)*multinomial,denominator)
    return (-1)**r*comb(n,k)*factorial(r)*total

def verify_partition_identity():
    count = 0
    for n in range(1,11):
        row = [0] * (n+1)
        row[0] = 1
        for m in range(1,n+1):
            for k in range(m,0,-1):
                row[k] = row[k-1] + k*row[k]
            row[0] = 0
        for k in range(1,n+1):
            assert stirling_partition_identity(n,k) == row[k]
            count += 1
    assert count == 55
    return count

def main():
    identity_count = verify_partition_identity()
    tests = certified = disagreements = 0
    for c in range(1, 13):
        for h in range(1, 8):
            q = 1 << h
            n = c * q
            row = [0] * (n + 1)
            row[0] = 1
            for m in range(1, n + 1):
                for k in range(m, 0, -1):
                    row[k] = (row[k-1] + k * row[k]) % MOD
                row[0] = 0
            bad = 0
            t = [v2(comb(2*c-b-1, c)) for b in range(c)]
            envelope = (c-1) + sum(max(2*x-1, 0) for x in t)
            for k in range(1, n + 1):
                b = (k - 1) // q
                a = k - b*q
                expected = k.bit_count() - c.bit_count() + v2(comb(2*n-k, n))
                assert 0 <= expected < 32, (c, h, k, expected)
                observed = v2(row[k])
                if a < q:
                    carry = v2(comb(2*c-b-1,c))
                    assert v2(comb(2*n-k, n)) == carry
                    guaranteed = q-a >= 2*t[b]
                else:
                    guaranteed = False
                if guaranteed:
                    certified += 1
                    assert observed == expected, (c,h,k,observed,expected)
                if observed != expected:
                    bad += 1
                    assert not guaranteed, (c,h,k)
                tests += 1
            assert bad <= envelope, (c,h,bad,envelope)
            disagreements += bad
    assert tests == 19812, tests
    assert certified == 18537, certified
    assert disagreements == 433, disagreements
    print('VERIFY_OK tests=%d certified=%d observed_disagreements=%d identity_pairs=%d' %
          (tests, certified, disagreements, identity_count))

if __name__ == '__main__':
    main()
