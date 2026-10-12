#!/usr/bin/env python3
"""Finite checks for normal someone-knows bundles and nested partition counts.

Run: python3 verify.py
All conclusions for arbitrary sets and arbitrary sizes require the written proof.
"""
from itertools import product
from math import comb


def partitions(n):
    if n == 0:
        yield ()
        return
    def rec(k, blocks):
        if k == n:
            yield tuple(tuple(b) for b in blocks)
        else:
            for b in range(len(blocks)):
                blocks[b].append(k)
                yield from rec(k + 1, blocks)
                blocks[b].pop()
            blocks.append([k])
            yield from rec(k + 1, blocks)
            blocks.pop()
    yield from rec(0, [])


def masks(p):
    return tuple(sum(1 << j for j in b) for b in p)


def classes(p, n):
    result = [0] * n
    for b in masks(p):
        for w in range(n):
            if b & (1 << w):
                result[w] = b
    assert all(result)
    return tuple(result)


def b_of(x, rows):
    return sum(1 << w for w in range(len(rows[0]))
               if any(cls[w] & x == cls[w] for cls in rows))


def local_minimum(rows, n):
    return all(any(all(cls[w] & other[w] == cls[w] for other in rows)
                   for cls in rows)
               for w in range(n))


def laminar_pair(p, q):
    return all(not (a & b) or a & b == a or a & b == b
               for a in masks(p) for b in masks(q))


def check():
    bell = {n: len(list(partitions(n))) for n in range(9)}
    counts = [1]
    for n in range(1, 9):
        counts.append(sum(comb(n - 1, m - 1) * (2 * bell[m] - 1) * counts[n - m]
                          for m in range(1, n + 1)))
    assert counts[:8] == [1, 1, 4, 19, 111, 774, 6229, 56529], counts
    print('EGF recurrence a(0..8):', counts)
    total_valuations = 0
    total_frames = 0
    for n in range(1, 7):
        parts = list(partitions(n))
        good = 0
        for p in parts:
            p_rows = classes(p, n)
            for q in parts:
                rows = (p_rows, classes(q, n))
                min_condition = local_minimum(rows, n)
                assert min_condition == laminar_pair(p, q)
                good += min_condition
                total_frames += 1
                if n <= 4:
                    normal = all(b_of(x & y, rows) == b_of(x, rows) & b_of(y, rows)
                                 for x in range(1 << n) for y in range(1 << n))
                    assert normal == min_condition, (n, p, q)
                    total_valuations += (1 << (2 * n))
                    if min_condition:
                        cap_rows = (tuple(p_rows[w] & rows[1][w] for w in range(n)),)
                        for x in range(1 << n):
                            assert b_of(x, rows) == b_of(x, cap_rows)
        assert good == counts[n], (n, good, counts[n])
        print(f'n={n}: {good} valid ordered partition pairs among {len(parts)**2}')
    for n in (2, 3, 4):
        parts = list(partitions(n))
        for triple in product(parts, repeat=3):
            rows = tuple(classes(p, n) for p in triple)
            min_condition = local_minimum(rows, n)
            normal = all(b_of(x & y, rows) == b_of(x, rows) & b_of(y, rows)
                         for x in range(1 << n) for y in range(1 << n))
            assert min_condition == normal
            total_valuations += 1 << (2 * n)
    print('Exhaustive two-agent profiles checked:', total_frames)
    print('Exhaustive meet-identity valuation pairs checked:', total_valuations)
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
