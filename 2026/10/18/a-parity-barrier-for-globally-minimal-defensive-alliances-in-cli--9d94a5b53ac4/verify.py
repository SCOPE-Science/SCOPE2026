"""Independent exhaustive check of globally minimal defensive alliances.

Usage: python verify.py
No external libraries are required.
"""
from collections import Counter
from itertools import combinations, product
from math import comb, prod


def adjacency(block_sizes):
    count = 1 + sum(block_sizes)
    adj = [0] * count
    begin = 1
    for width in block_sizes:
        vertices = range(begin, begin + width)
        for vertex in vertices:
            adj[0] |= 1 << vertex
            adj[vertex] |= 1
            for other in vertices:
                if vertex != other:
                    adj[vertex] |= 1 << other
        begin += width
    return adj


def global_minimal_sets(block_sizes):
    adj = adjacency(block_sizes)
    count = len(adj)
    has_alliance_subset = bytearray(1 << count)
    minima = set()
    checked = 0
    for mask in range(1, 1 << count):
        checked += 1
        members = [i for i in range(count) if mask & (1 << i)]
        defensive = all(
            2 * (adj[v] & mask).bit_count() + 1 >= adj[v].bit_count()
            for v in members
        )
        contains_proper = any(
            has_alliance_subset[mask ^ (1 << v)] for v in members
        )
        if defensive and not contains_proper:
            minima.add(mask)
        has_alliance_subset[mask] = defensive or contains_proper
    return minima, checked


def predicted_sets(block_sizes):
    blocks = []
    lo = 1
    for m in block_sizes:
        blocks.append(tuple(range(lo, lo + m)))
        lo += m
    minima = set()
    for b, m in zip(blocks, block_sizes):
        for group in combinations(b, m // 2 + 1):
            minima.add(sum(1 << v for v in group))
    if sum(m % 2 for m in block_sizes) <= 1:
        for groups in product(*[
            list(combinations(b, m // 2))
            for b, m in zip(blocks, block_sizes)
        ]):
            minima.add(1 | sum(1 << v for group in groups for v in group))
    return minima


def coefficient_formula(block_sizes):
    result = Counter()
    for m in block_sizes:
        result[m // 2 + 1] += comb(m, m // 2 + 1)
    if sum(m % 2 for m in block_sizes) <= 1:
        result[1 + sum(block_sizes) // 2] += prod(
            comb(m, m // 2) for m in block_sizes
        )
    return result


def check():
    count_profiles = 0
    count_subsets = 0
    count_minima = 0
    for length in (2, 3, 4):
        for sizes in product((2, 3, 4, 5), repeat=length):
            if sum(sizes) > 12:
                continue
            found, checked = global_minimal_sets(sizes)
            expected = predicted_sets(sizes)
            if found != expected:
                raise AssertionError((sizes, sorted(found ^ expected)))
            observed = Counter(mask.bit_count() for mask in found)
            assert observed == coefficient_formula(sizes), (sizes, observed)
            count_profiles += 1
            count_subsets += checked
            count_minima += len(found)
    for r in range(2, 8):
        for k in range(1, 8):
            sizes = (2 * k,) * r
            pol = coefficient_formula(sizes)
            assert pol[k+1] >= r*comb(2*k,k+1)
            assert pol[r*k+1] >= comb(2*k,k)**r
            odd = coefficient_formula((2*k+1,)*r)
            assert odd == Counter({k+1: r*comb(2*k+1,k+1)})
    print('VERIFICATION_OK profiles=%d vertex_subsets=%d actual_minima=%d parity_profiles=42' %
          (count_profiles, count_subsets, count_minima))


if __name__ == '__main__':
    check()
