#!/usr/bin/env python3
"""Finite reproducibility checks for the multiset-list plateau theorem."""
from itertools import combinations
from math import comb


def comps(total, arity):
    if arity == 1:
        yield (total,)
    else:
        for head in range(total + 1):
            for rest in comps(total - head, arity - 1):
                yield (head,) + rest


def descendants(codeword, k):
    for v in comps(k, len(codeword)):
        if all(a <= b for a, b in zip(v, codeword)):
            yield v


def construction(q, k, list_size, n):
    code = []
    for i in range(q):
        for j in range(list_size):
            x = [0] * q
            x[i] = n - j
            x[(i + 1) % q] = j
            code.append(tuple(x))
    if n == q * (k - 1):
        code.append((k - 1,) * q)
    return code


def maximum_parent_count(code, k):
    counts = {}
    for x in code:
        for y in descendants(x, k):
            counts[y] = counts.get(y, 0) + 1
    return max(counts.values(), default=0)


def exhaustive_optimum(q, k, list_size, n):
    candidates = list(comps(n, q))
    received = list(comps(k, q))
    masks = []
    for y in received:
        mask = 0
        for i, x in enumerate(candidates):
            if all(a <= b for a, b in zip(y, x)):
                mask |= 1 << i
        masks.append(mask)
    best = 0
    count_max = 0
    for choice in range(1 << len(candidates)):
        count = choice.bit_count()
        if count < best:
            continue
        if all((choice & mask).bit_count() <= list_size for mask in masks):
            if count > best:
                best, count_max = count, 0
            count_max += 1
    return best, count_max


def run():
    tested = 0
    tested_receivers = 0
    for q in range(3, 6):
        for k in range(2, 5):
            for list_size in range(2, k + 1):
                n0 = q * (k - 1)
                for n in (n0, n0 + 1, n0 + 3):
                    code = construction(q, k, list_size, n)
                    expected = q * list_size + int(n == n0)
                    assert len(code) == len(set(code)) == expected
                    assert all(len(x) == q and sum(x) == n for x in code)
                    assert maximum_parent_count(code, k) <= list_size
                    for x in code:
                        assert max(x) >= k or (n == n0 and x == (k - 1,) * q)
                    tested += 1
                    tested_receivers += len(list(comps(k, q)))
    exact = []
    for n in (3, 4):
        ans, num = exhaustive_optimum(3, 2, 2, n)
        assert ans == (7 if n == 3 else 6)
        exact.append((n, ans, num))
    print('CONSTRUCTION_CASES', tested)
    print('RECEIVER_VECTORS', tested_receivers)
    print('EXHAUSTIVE_SMALL_OPTIMA', exact)
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    run()
