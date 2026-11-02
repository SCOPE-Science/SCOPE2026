"""Finite exact checks for fan/wheel fractional-hedonic welfare classification.

Run: python verify.py
The infinite-size theorem relies on its written inequality proof, not these checks.
"""
from fractions import Fraction
from functools import lru_cache


def graph(kind, m):
    n = m + 1
    edges = [(0, j) for j in range(1, n)]
    edges += [(j, j + 1) for j in range(1, m)]
    if kind == 'wheel':
        edges.append((m, 1))
    adj = [0] * n
    for i, j in edges:
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    return adj


def check(kind, m):
    adj = graph(kind, m)
    n = len(adj)
    lim = 1 << n
    size = [0] * lim
    edges_in = [0] * lim
    value = [Fraction(0)] * lim
    for mask in range(1, lim):
        b = mask & -mask
        u = b.bit_length() - 1
        rest = mask ^ b
        size[mask] = 1 + size[rest]
        edges_in[mask] = edges_in[rest] + (adj[u] & rest).bit_count()
        value[mask] = Fraction(2 * edges_in[mask], size[mask])

    if kind == 'fan':
        expected = Fraction(m, 2) + 1
        expected_count = m // 2
    elif m >= 5:
        expected = Fraction(m, 2) + 1
        expected_count = m
    elif m == 3:
        expected, expected_count = Fraction(3), 1
    else:
        expected, expected_count = Fraction(16, 5), 1

    best = Fraction(-1)
    count_best = 0
    count_nash_best = 0
    partitions_seen = 0

    def nash(partition):
        for coalition in partition:
            for u in range(n):
                if not coalition & (1 << u):
                    continue
                present = Fraction((adj[u] & coalition).bit_count(), size[coalition])
                if present < 0:
                    raise AssertionError('unexpected negative utility')
                for other in partition:
                    if other != coalition:
                        newcomer = Fraction((adj[u] & other).bit_count(), size[other] + 1)
                        if newcomer > present:
                            return False
        return True

    def rec(rem, partition, subtotal):
        nonlocal best, count_best, count_nash_best, partitions_seen
        if not rem:
            partitions_seen += 1
            if subtotal > best:
                best = subtotal
                count_best = 0
                count_nash_best = 0
            if subtotal == best:
                count_best += 1
                if nash(partition):
                    count_nash_best += 1
            return
        first = rem & -rem
        others = rem ^ first
        sub = others
        while True:
            c = sub | first
            rec(rem ^ c, partition + (c,), subtotal + value[c])
            if not sub:
                break
            sub = (sub - 1) & others

    rec(lim - 1, (), Fraction(0))
    assert best == expected, (kind, m, best, expected)
    assert count_best == expected_count, (kind, m, count_best, expected_count)
    assert count_nash_best == count_best, (kind, m, count_nash_best, count_best)
    print(f'{kind} m={m}: partitions={partitions_seen}, max={best}, '
          f'optimal={count_best}, Nash-stable optimal={count_nash_best}')


def main():
    for m in range(2, 10):
        check('fan', m)
    for m in range(3, 10):
        check('wheel', m)
    print('ALL EXACT FINITE CHECKS PASSED')


if __name__ == '__main__':
    main()
