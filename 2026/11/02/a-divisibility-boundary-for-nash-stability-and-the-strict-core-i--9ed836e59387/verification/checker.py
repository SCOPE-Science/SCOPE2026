#!/usr/bin/env python3
"""Finite checks for the complete-bipartite fractional-hedonic divisibility theorem.

No external packages; the mathematical all-size results are proved in RESULT.md.
"""
from math import factorial
from fractions import Fraction


def partitions(n):
    """Generate every unlabeled partition of n labeled players once."""
    if n == 0:
        yield []
        return
    blocks = [[0]]
    def rec(i):
        if i == n:
            yield tuple(tuple(block) for block in blocks)
            return
        for block in blocks:
            block.append(i)
            yield from rec(i + 1)
            block.pop()
        blocks.append([i])
        yield from rec(i + 1)
        blocks.pop()
    yield from rec(1)


def direct_stable(blocks, a):
    """Utility-based test, NOT using the determinant criterion."""
    pairs = [(sum(v < a for v in block), sum(v >= a for v in block))
             for block in blocks]
    for index, block in enumerate(blocks):
        x, y = pairs[index]
        for player in block:
            is_left = player < a
            num = y if is_left else x
            for j, (u, v) in enumerate(pairs):
                if j == index:
                    continue
                target_num = v if is_left else u
                if target_num * (x + y) > num * (u + v + 1):
                    return False
            # Becoming singleton yields zero, never a strict gain here.
    return True


def determinant_stable(blocks, a):
    pairs = [(sum(v < a for v in block), sum(v >= a for v in block))
             for block in blocks]
    if any(x == 0 or y == 0 for x, y in pairs):
        return False
    for i, (x, y) in enumerate(pairs):
        for u, v in pairs[i+1:]:
            d = x * v - y * u
            if not (-min(x, v) <= d <= min(y, u)):
                return False
    return True


def welfare(blocks, a):
    result = Fraction(0)
    for block in blocks:
        x = sum(i < a for i in block)
        y = len(block) - x
        result += Fraction(2 * x * y, x + y)
    return result


def formula_count(a, q):
    c = [Fraction(0) for _ in range(a + 1)]
    c[0] = Fraction(1)
    for n in range(1, a + 1):
        c[n] = sum(Fraction(r, factorial(r) * factorial(q*r)) * c[n-r]
                   for r in range(1, n+1)) / n
    count = factorial(a) * factorial(q*a) * c[a]
    assert count.denominator == 1
    return count.numerator


def explicit_witness(a, b):
    """Assume 2 <= a <= b and b mod a != 0."""
    q, r = divmod(b, a)
    assert 1 <= r < a and q >= 1
    # Labelled singleton A blocks, B members assigned in consecutive groups.
    sizes = [q] * (a - r) + [q + 1] * r
    blocks = []
    k = a
    for i, size in enumerate(sizes):
        blocks.append((i,) + tuple(range(k, k + size)))
        k += size
    assert k == a + b
    return tuple(blocks)


def main():
    total = 0
    stable_total = 0
    cases = 0
    for n in range(2, 11):
        for a in range(1, n // 2 + 1):
            b = n - a
            cases += 1
            count = 0
            for blocks in partitions(n):
                total += 1
                direct = direct_stable(blocks, a)
                det = determinant_stable(blocks, a)
                assert direct == det, (a, b, blocks, direct, det)
                if direct:
                    stable_total += 1
                    count += 1
                    if b % a == 0:
                        assert all(sum(v >= a for v in block) == (b // a) *
                                   sum(v < a for v in block) for block in blocks)
                        assert welfare(blocks, a) == Fraction(2*a*b, a+b)
            if b % a == 0:
                assert count == formula_count(a, b // a), (a, b, count)
            else:
                witness = explicit_witness(a, b)
                assert direct_stable(witness, a) and determinant_stable(witness, a)
                q, r = divmod(b, a)
                opt_gap = Fraction(2*a*b, a+b) - welfare(witness, a)
                assert opt_gap == Fraction(2*r*(a-r),
                           (q+1)*(q+2)*((q+1)*a+r)), (a,b,opt_gap)
                assert opt_gap > 0
            print(f'{a},{b}: equilibria={count}, divisible={b%a == 0}')
    print(f'PASS: {cases} parameter pairs, {total} labeled partitions, '
          f'{stable_total} Nash-stable incidences, direct deviations = determinant '
          'and divisibility/generating-function/witness checks all passed')

if __name__ == '__main__':
    main()
