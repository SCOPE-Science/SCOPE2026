"""Reproducibility checks for global-coalition partitions of balanced four-partite graphs.

Requires Python 3.10+, numpy and scipy. The mathematical proof is in RESULT.md.
"""
from itertools import product
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def predicted(q):
    return max(2*q, 3*q-3, 4*q-8)


def blocks_witness(q, t):
    """Construct the lower-bound partition using t complementary support blocks."""
    assert q >= t or (q >= t-1 and t == 4)
    V = [list(range(q*i, q*(i+1))) for i in range(4)]
    H = [[] for _ in range(t)]
    leftovers = []
    for j in range(4):
        if j < t:
            available = iter(V[j])
            for i in range(t):
                if i != j:
                    H[i].append(next(available))
            leftovers.extend([1 << v for v in available])
        else:
            for i in range(t):
                H[i].append(V[j][i])
            H[0].extend(V[j][t:])
    return [sum(1 << x for x in h) for h in H] + leftovers


def is_global_direct(mask, q):
    N = 4*q
    for v in range(N):
        if mask & (1 << v):
            continue
        if not any((mask & (1 << w)) and (v//q != w//q) for w in range(N)):
            return False
        if not any((mask & (1 << w)) and (v//q == w//q) for w in range(N)):
            return False
    return True


def is_valid_direct(blocks, q):
    full = (1 << (4*q)) - 1
    aggregate = 0
    for b in blocks:
        if not b or aggregate & b or is_global_direct(b, q):
            return False
        aggregate |= b
    if aggregate != full:
        return False
    return all(any(i != j and is_global_direct(b | c, q)
                   for j, c in enumerate(blocks)) for i, b in enumerate(blocks))


def independent_partition_enumeration(q):
    """Enumerate every unlabelled set partition of the original labelled vertices."""
    N = 4*q
    parts = [1]
    best = 0
    checked = 0

    def rec(v):
        nonlocal best, checked
        if v == N:
            checked += 1
            if len(parts) > best and is_valid_direct(parts, q):
                best = len(parts)
            return
        bit = 1 << v
        for i in range(len(parts)):
            parts[i] |= bit
            rec(v+1)
            parts[i] ^= bit
        parts.append(bit)
        rec(v+1)
        parts.pop()

    rec(1)
    return best, checked


def independent_support_integer_program(q):
    """Exact support-count optimization, distinct from direct vertex partitions.

    x[S] counts classes with part-support S, y[S] records whether x[S]>0.
    The integrality constraints and matching-partner constraints are explicit.
    """
    supports = tuple(range(1, 15))
    J = len(supports)
    rows, lows, highs = [], [], []

    def add(row, lo=-np.inf, hi=np.inf):
        rows.append(row)
        lows.append(lo)
        highs.append(hi)

    for i in range(4):
        row = np.zeros(2*J)
        row[:J] = [(s >> i) & 1 for s in supports]
        add(row, 1, q)
    for j, S in enumerate(supports):
        # y[S] <= x[S] <= 4q y[S]
        row = np.zeros(2*J)
        row[j] = 1
        row[J+j] = -4*q
        add(row, hi=0)
        row = np.zeros(2*J)
        row[j] = -1
        row[J+j] = 1
        add(row, hi=0)
        # An active support needs an active partner whose union is all 4 parts.
        row = np.zeros(2*J)
        row[J+j] = 1
        for k, T in enumerate(supports):
            if (S | T) == 15:
                row[J+k] -= 1
        add(row, hi=0)
    objective = np.zeros(2*J)
    objective[:J] = -1
    bounds = Bounds(np.zeros(2*J), np.array([4*q]*J + [1]*J))
    model = LinearConstraint(np.array(rows), lows, highs)
    result = milp(objective, integrality=np.ones(2*J), bounds=bounds,
                  constraints=model, options={'time_limit':30, 'mip_rel_gap':0.0})
    assert result.success, result.message
    value = -float(result.fun)
    assert abs(value-round(value)) < 1e-7
    return round(value)


def main():
    for q in [1, 2]:
        best, partitions = independent_partition_enumeration(q)
        assert best == predicted(q), (q, best)
        print('DIRECT_ORIGINAL_GRAPH_PARTITIONS_OK', q, partitions, best)
    for q in range(1, 26):
        options = [1] if q == 1 else [2] + ([3] if q >= 3 else []) + ([4] if q >= 4 else [])
        witness_sizes = []
        for t in options:
            blocks = blocks_witness(q, t)
            assert is_valid_direct(blocks, q), (q, t)
            witness_sizes.append(len(blocks))
            if t >= 2:
                assert len(blocks) == t + t*(q-t+1)
            else:
                assert len(blocks) == q+1
        assert max(witness_sizes) == predicted(q)
        value = independent_support_integer_program(q)
        assert value == predicted(q), (q, value, predicted(q))
        print('INDEPENDENT_MIXED_INTEGER_SUPPORT_OPTIMUM_OK',q,value)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
