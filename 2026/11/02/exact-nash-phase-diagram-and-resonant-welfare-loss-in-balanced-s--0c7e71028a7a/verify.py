"""Exact finite checks for two-color signed coalition equilibria.

Run: python verify.py
Requires Python 3.9+ standard library only.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial


def partitions(n):
    """All set partitions in restricted-growth order, independently of the formula."""
    blocks = []
    def grow(i):
        if i == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for block in blocks:
            block.append(i)
            yield from grow(i + 1)
            block.pop()
        blocks.append([i])
        yield from grow(i + 1)
        blocks.pop()
    yield from grow(0)


def payoff(agent, coalition, m, q):
    return sum((q.denominator if (agent < m) != (peer < m) else -q.numerator)
               for peer in coalition if peer != agent)


def direct_nash(partition, m, q):
    for index, block in enumerate(partition):
        for agent in block:
            old = payoff(agent, block, m, q)
            if old < 0:  # moving to a fresh singleton
                return False
            for j, recipient in enumerate(partition):
                if j != index and payoff(agent, recipient + (agent,), m, q) > old:
                    return False
    return True


def predicted_nash(partition, m, q):
    sizes = []
    for block in partition:
        left = sum(v < m for v in block)
        right = len(block) - left
        if left != right:
            return False
        sizes.append(left)
    if q == 1:
        return True
    if q < 1:
        return (max(sizes) - min(sizes)) * (1 - q) <= q
    return max(sizes) * (q - 1) <= q


def social_welfare(partition, m, q):
    return sum(payoff(agent, block, m, q)
               for block in partition for agent in block)


def predicted_social_welfare(partition, m, q):
    total = 2 * q.numerator * m
    for block in partition:
        left = sum(v < m for v in block)
        right = len(block) - left
        size = left + right
        imbalance = left - right
        total += Fraction(q.denominator - q.numerator, 2) * size * size
        total -= Fraction(q.denominator + q.numerator, 2) * imbalance * imbalance
    return total


def profiles(m):
    def rec(index, remainder, current):
        if index > m:
            if remainder == 0:
                yield current
            return
        for c in range(remainder // index + 1):
            yield from rec(index + 1, remainder - index * c, current + (c,))
    yield from rec(1, m, ())


def formula_count(m, q):
    total = 0
    for cs in profiles(m):
        support = [j for j, c in enumerate(cs, 1) if c]
        if q < 1 and (max(support) - min(support)) * (1 - q) > q:
            continue
        if q > 1 and max(support) * (q - 1) > q:
            continue
        den = 1
        for j, c in enumerate(cs, 1):
            den *= factorial(c) * factorial(j) ** (2 * c)
        numerator = factorial(m) ** 2
        assert numerator % den == 0
        total += numerator // den
    return total


def welfare_bounds(m, q):
    if q < 1:
        return 2 * m * q.denominator, 2 * q.numerator * m + 2 * (q.denominator - q.numerator) * m * m
    if q == 1:
        return 2 * m * q.denominator, 2 * m * q.denominator
    K = q.numerator // (q.numerator - q.denominator)
    t, rem = divmod(m, K)
    return 2 * q.numerator * m + 2 * (q.denominator - q.numerator) * (t * K * K + rem * rem), 2 * m * q.denominator


def run():
    grid = [Fraction(1, 10), Fraction(1, 3), Fraction(1, 2),
            Fraction(2, 3), Fraction(3, 4), Fraction(4, 5),
            Fraction(1), Fraction(11, 10), Fraction(6, 5),
            Fraction(5, 4), Fraction(4, 3), Fraction(3, 2),
            Fraction(7, 4), Fraction(2), Fraction(5, 2), Fraction(3)]
    pcount = eqcount = 0
    for m in range(1, 6):
        cases = grid if m <= 4 else [Fraction(1, 3), Fraction(1), Fraction(4, 3), Fraction(2)]
        for q in cases:
            num = 0
            low = None
            high = None
            for P in partitions(2 * m):
                pcount += 1
                brute = direct_nash(P, m, q)
                formula = predicted_nash(P, m, q)
                assert brute == formula, (m, q, P, brute, formula)
                welfare = social_welfare(P, m, q)
                assert welfare == predicted_social_welfare(P, m, q)
                if brute:
                    eqcount += 1
                    num += 1
                    low = welfare if low is None else min(low, welfare)
                    high = welfare if high is None else max(high, welfare)
            assert num == formula_count(m, q), (m, q, num, formula_count(m,q))
            assert (low, high) == welfare_bounds(m, q), (m, q, low, high)
            print('m=%d q=%s equilibria=%d welfare=[%s,%s]' % (m, q, num, low, high))
    # Independently test the coefficient enumeration for larger sizes.
    for m in range(6, 12):
        for q in grid:
            n = formula_count(m, q)
            assert n >= factorial(m)
            if q == 1:
                assert n == sum(formula_count(m, r) for r in [q])
    print('PASS: %d complete partition/parameter checks, %d equilibrium incidences' % (pcount, eqcount))

if __name__ == '__main__':
    run()
