"""Finite checks for reachability-preorder collapse in directed graphs.

Usage: python3 verify_three_layer.py
No external packages or network access are required.
"""
from itertools import product
from math import factorial, log
from random import Random


def closure_and_profile(n, arc_bits):
    reach = [(1 << i) for i in range(n)]
    indeg = [0] * n
    outdeg = [0] * n
    k = 0
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if (arc_bits >> k) & 1:
                reach[u] |= 1 << v
                outdeg[u] += 1
                indeg[v] += 1
            k += 1
    for pivot in range(n):
        mask = 1 << pivot
        for u in range(n):
            if reach[u] & mask:
                reach[u] |= reach[pivot]
    sources = sum(d == 0 for d in indeg)
    sinks = sum(d == 0 for d in outdeg)
    canonical = all(reach[u] ==
                    sum((1 << v) for v in range(n)
                        if v == u or (outdeg[u] and indeg[v]))
                    for u in range(n))
    half_condition = True
    for u in range(n):
        if outdeg[u] and reach[u].bit_count() <= n // 2:
            half_condition = False
        predecessors = sum(bool(reach[v] & (1 << u)) for v in range(n))
        if indeg[u] and predecessors <= n // 2:
            half_condition = False
    return sources, sinks, canonical, half_condition


def exhaustive():
    for n in range(1, 5):
        number_arcs = n * (n - 1)
        count = 0
        canonical = 0
        half = 0
        sum_source = 0
        sum_sink = 0
        sum_product = 0
        for bits in range(1 << number_arcs):
            s, t, c, h = closure_and_profile(n, bits)
            assert not h or c, ('half-condition failure', n, bits)
            count += 1
            canonical += c
            half += h
            sum_source += s
            sum_sink += t
            sum_product += s * t
        # Every arc is equally likely at p=1/2.
        q = 0.5
        expectation_source = n * q ** (n - 1)
        expectation_product = (n * q ** (2 * (n - 1)) +
                               n * (n - 1) * q ** (2 * n - 3)) if n > 1 else 1
        assert abs(sum_source / count - expectation_source) < 1e-12
        assert abs(sum_sink / count - expectation_source) < 1e-12
        assert abs(sum_product / count - expectation_product) < 1e-12
        print(f'EXHAUSTIVE_OK n={n} graphs={count} canonical={canonical} half={half}')


def random_checks():
    rng = Random(314159265)
    for n in (20, 40, 80):
        p = log(n) / n
        samples = 120
        canonical_count = 0
        half_count = 0
        for _ in range(samples):
            bits = 0
            k = 0
            for u in range(n):
                for v in range(n):
                    if u == v:
                        continue
                    if rng.random() < p:
                        bits |= 1 << k
                    k += 1
            s, t, c, h = closure_and_profile(n, bits)
            assert not h or c
            canonical_count += c
            half_count += h
        print(f'SAMPLED_OK n={n} trials={samples} canonical={canonical_count} half={half_count}')


if __name__ == '__main__':
    exhaustive()
    random_checks()
    print('THREE_LAYER_PREORDER_CHECK_OK')
