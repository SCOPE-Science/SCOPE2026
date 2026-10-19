#!/usr/bin/env python3
"""Exact integer audit of two well-specified binary16 logistic maps.

No floating-point operations or third-party dependencies are used.
State indices are the nonnegative IEEE 754 binary16 bit patterns 0..0x3c00,
including +0, subnormals, and +1.  Subtraction and products are treated as
exact rationals before rounding at the explicitly indicated locations.
"""
from bisect import bisect_left
from collections import Counter
from fractions import Fraction
from hashlib import sha256

N = 0x3c01
Q = 1 << 24
W_TOTAL = 1 << 25
QVAL = []
for bits in range(N):
    exp = (bits >> 10) & 31
    frac = bits & 1023
    QVAL.append(frac if exp == 0 else (1024 + frac) * (1 << (exp - 1)))
assert QVAL[0] == 0 and QVAL[-1] == Q
assert all(QVAL[i] < QVAL[i + 1] for i in range(N - 1))


def round16(num, den=1):
    """Round the nonnegative rational num/den, measured in 2^-24 units.

    Nearest, ties to even (least significant significand bit = bit-pattern
    parity); values remain in [0,1] for calls below.
    """
    assert den > 0 and 0 <= num <= Q * den
    ceil_q = (num + den - 1) // den
    hi = bisect_left(QVAL, ceil_q)
    if hi == 0:
        return 0
    if hi == N:
        return N - 1
    lo = hi - 1
    dl = num - den * QVAL[lo]
    dh = den * QVAL[hi] - num
    assert dl >= 0 and dh >= 0
    if dl < dh:
        return lo
    if dl > dh:
        return hi
    return lo if lo % 2 == 0 else hi


def transitions():
    one = []
    staged = []
    for q in QVAL:
        # Single RN16 evaluation of the exact rational 4x(1-x).
        one.append(round16(4 * q * (Q - q), Q))
        # RN16[4 * RN16(x * RN16(1-x))], with all rounds separate.
        s = QVAL[round16(Q - q)]
        p = QVAL[round16(q * s, Q)]
        staged.append(round16(4 * p))
    return one, staged


def decompose(t):
    n = len(t)
    basin = [-1] * n
    distance = [0] * n
    cycles = []
    for initial in range(n):
        if basin[initial] >= 0:
            continue
        path = []
        position = {}
        j = initial
        while basin[j] == -1 and j not in position:
            position[j] = len(path)
            path.append(j)
            j = t[j]
        if basin[j] != -1:
            idx = basin[j]
            d = distance[j]
            for k in reversed(path):
                d += 1
                basin[k] = idx
                distance[k] = d
        else:
            cut = position[j]
            cycle = tuple(path[cut:])
            idx = len(cycles)
            cycles.append(cycle)
            for k in cycle:
                basin[k] = idx
            d = 0
            for k in reversed(path[:cut]):
                d += 1
                basin[k] = idx
                distance[k] = d
    # Independent invariants for each directed functional edge.
    for i, j in enumerate(t):
        assert basin[i] == basin[j]
        if distance[i]:
            assert distance[i] == distance[j] + 1
        else:
            assert distance[j] == 0
    return cycles, basin, distance


def weighted_statistics(t):
    cycles, basin, dist = decompose(t)
    # Voronoi cell lengths of initial rounding for a uniform real x in [0,1]
    # are W[i]/(2*Q), using midpoint boundaries and endpoint truncation.
    w = [QVAL[1] - QVAL[0]]
    w += [QVAL[i + 1] - QVAL[i - 1] for i in range(1, N - 1)]
    w += [QVAL[-1] - QVAL[-2]]
    assert sum(w) == W_TOTAL
    counts = Counter(basin)
    weights = Counter()
    for i in range(N):
        weights[basin[i]] += w[i]
    means = [Fraction(sum(QVAL[i] for i in cycle), Q * len(cycle))
             for cycle in cycles]
    global_mean = sum((Fraction(weights[k], W_TOTAL) * means[k]
                       for k in range(len(cycles))), Fraction())
    desc = sorted([(len(c), counts[k], weights[k],
                    max(dist[i] for i in range(N) if basin[i] == k),
                    min(c), str(means[k]))
                   for k, c in enumerate(cycles)])
    edge_digest = sha256(b''.join(k.to_bytes(2, 'little') for k in t)).hexdigest()
    return dict(cycles=cycles, basin=basin, distance=dist,
                rows=desc, mean=global_mean, digest=edge_digest,
                maximum_entry=max(dist))


def verify():
    f, g = transitions()
    A, B = weighted_statistics(f), weighted_statistics(g)
    assert sum(i != j for i, j in zip(f, g)) == 2774
    assert sum((A['basin'][i] == A['basin'][0]) !=
               (B['basin'][i] == B['basin'][0]) for i in range(N)) == 10194
    assert sorted(len(c) for c in A['cycles']) == [1, 1, 5]
    assert sorted(len(c) for c in B['cycles']) == [1, 1, 40]
    assert A['maximum_entry'] == 109 and B['maximum_entry'] == 83
    assert A['mean'] == Fraction(19241579, 4294967296)
    assert B['mean'] == Fraction(11845614952233, 35184372088832)
    assert sorted((p, s, w) for p,s,w,*_ in A['rows']) == sorted([
        (1,15236,33285590), (1,8,25258), (5,117,243584)])
    assert sorted((p, s, w) for p,s,w,*_ in B['rows']) == sorted([
        (1,5092,11340767), (1,2,22528), (40,10267,22191137)])
    # Verify all cycle links close and every state reaches its assigned cycle.
    for tr, res in ((f, A), (g, B)):
        for cycle in res['cycles']:
            assert all(tr[cycle[i]] == cycle[(i+1)%len(cycle)]
                       for i in range(len(cycle)))
        assert sum(len(c) for c in res['cycles']) <= N
        for i in range(N):
            k = i
            for _ in range(res['distance'][i]):
                k = tr[k]
            assert k in res['cycles'][res['basin'][i]]
    for name, res in (('single_final_round', A), ('staged_rounds', B)):
        print(name)
        print('  (period, basin_states, initial_weight_2^-25, max_entry, '
              'smallest_cycle_bitpattern, cycle_average)=')
        for row in res['rows']:
            print(' ',row)
        print('  exact_uniform_start_Cesaro_mean=', res['mean'])
        print('  decimal=', format(float(res['mean']), '.17g'))
        print('  max_entry=', res['maximum_entry'])
        print('  all_edge_bytes_sha256=', res['digest'])
    print('different_transitions=',sum(i!=j for i,j in zip(f,g)))
    print('changed_zero_basin_memberships=',10194)
    print('all exact integer assertions passed')

def native_float16_crosscheck():
    """Optional independent hardware-style NumPy implementation of every edge.

    The single-round path computes exact binary16 dyadic products in binary64,
    which has ample precision for this polynomial of an 11-bit significand.
    """
    import numpy as np
    arr = np.arange(N, dtype=np.uint16).view(np.float16)
    one = (np.float64(4) * np.float64(arr) *
           (np.float64(1) - np.float64(arr))).astype(np.float16)
    staged = np.float16(np.float16(arr * np.float16(np.float16(1) - arr)) * np.float16(4))
    a, b = transitions()
    assert np.array_equal(one.view(np.uint16), np.asarray(a, dtype=np.uint16))
    assert np.array_equal(staged.view(np.uint16), np.asarray(b, dtype=np.uint16))
    print('native NumPy float16 comparison: all 30722 directed edges agree')

if __name__ == '__main__':
    verify()
    import sys
    if '--native' in sys.argv:
        native_float16_crosscheck()
