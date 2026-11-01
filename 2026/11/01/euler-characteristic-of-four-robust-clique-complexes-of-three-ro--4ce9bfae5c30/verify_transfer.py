#!/usr/bin/env python3
"""Exact integer transfer certificate for four-robust complexes on 3-by-n grids.

Publicly reproducible mathematics only. Python standard library suffices.
"""
from collections import deque
from math import comb

ROW_INDEPENDENT_MASKS = (0, 1, 2, 4, 5)
ALL_COLUMN_SELECTIONS = range(8)
START = (0, -1, -1, -1, -1)


def advance(state, selection):
    """Best independent-set size ending in each exact mask, capped at four."""
    next_state = []
    for tail in ROW_INDEPENDENT_MASKS:
        if tail & ~selection:
            next_state.append(-1)
            continue
        predecessors = [score for prev, score in zip(ROW_INDEPENDENT_MASKS, state)
                        if score >= 0 and (prev & tail) == 0]
        next_state.append(min(4, max(predecessors) + tail.bit_count())
                          if predecessors else -1)
    return tuple(next_state)


def build_matrix():
    states = [START]
    index = {START: 0}
    queue = deque([START])
    rows = []
    raw_transitions = 0
    while queue:
        state = queue.popleft()
        row = {}
        for selection in ALL_COLUMN_SELECTIONS:
            after = advance(state, selection)
            if max(after) >= 4:
                continue
            if after not in index:
                index[after] = len(states)
                states.append(after)
                queue.append(after)
            j = index[after]
            row[j] = row.get(j, 0) + (-1 if selection.bit_count() & 1 else 1)
            raw_transitions += 1
        rows.append(row)
    assert len(rows) == len(states) and len(states) == len(index)
    return states, rows, raw_transitions


def apply(rows, vector):
    return [sum(weight * vector[j] for j, weight in row.items())
            for row in rows]


def main():
    states, matrix, edges = build_matrix()
    assert len(states) == 54, len(states)
    assert edges == 260, edges
    # A(A-I)^4 1 = 0: an exact, finite, 54-component certificate.
    vector = [1] * len(states)
    v = [vector]
    for _ in range(5):
        vector = apply(matrix, vector)
        v.append(vector)
    assert any(sum((-1)**(4-k) * comb(4, k) * v[k][j]
                   for k in range(5)) != 0 for j in range(len(states))), \
           'Unexpectedly stronger identity before shift'
    assert all(sum((-1)**(4-k) * comb(4, k) * v[k+1][j]
                   for k in range(5)) == 0 for j in range(len(states)))
    assert [v[n][0] for n in range(1, 5)] == [0, 0, 4, 20]
    for n in range(1, 31):
        # Independent forward propagation computes weighted sums of allowed
        # selected vertex sets, rather than reusing the backward vector.
        masses = [0] * len(states)
        masses[0] = 1
        for _ in range(n):
            nxt = [0] * len(states)
            for i, mass in enumerate(masses):
                for j, weight in matrix[i].items():
                    nxt[j] += mass * weight
            masses = nxt
        observed = sum(masses)
        predicted = comb(2*n-2, 3) if n >= 3 else 0
        assert observed == predicted, (n, observed, predicted)
    print('PASS: 54 reachable states and 260 admissible unaggregated transitions')
    print('PASS: all 54 components of A(A-I)^4 1 vanish exactly over integers')
    print('PASS: initial values t(1..4) = 0, 0, 4, 20')
    print('PASS: independent forward signed count for n=1..30')
    print('PROVED: t(n)=binom(2n-2,3) for all integers n>=1')


if __name__ == '__main__':
    main()
