#!/usr/bin/env python3
"""Exact finite-state certificate for total perfect codes on C_8 square C_t.

Each state is an ordered pair of eight-bit vertical columns (a,b).
The unique possible successor is (b,c), with c_i=1-a_i-b_(i-1)-b_(i+1).
A successor exists only when all eight c_i are Boolean.
The directed graph has at most one outgoing arrow from any state.
"""
from collections import Counter

R = 8
MASK = (1 << R) - 1
N_STATES = 1 << (2 * R)

def rotate(b, k):
    return ((b << k) | (b >> (R-k))) & MASK

def successor(state):
    a, b = state >> R, state & MASK
    left, right = rotate(b, 1), rotate(b, R-1)
    if (a & left) or (a & right) or (left & right):
        return -1
    return (b << R) | (MASK ^ (a | left | right))

def functional_cycles(next_state):
    done = bytearray(len(next_state))
    cycles = []
    for root in range(len(next_state)):
        if done[root]:
            continue
        path, at = [], {}
        v = root
        while v >= 0 and not done[v] and v not in at:
            at[v] = len(path)
            path.append(v)
            v = next_state[v]
        if v in at:
            cycles.append(tuple(path[at[v]:]))
        for u in path:
            done[u] = 1
    return cycles

def main():
    next_state = [successor(s) for s in range(N_STATES)]
    cycles = functional_cycles(next_state)
    period_counts = Counter(map(len, cycles))
    periodic_states = sum(map(len, cycles))
    assert period_counts == {4:4, 8:16}, period_counts
    assert periodic_states == 144
    assert len(cycles) == 20
    assert len({v for cy in cycles for v in cy}) == periodic_states
    assert all(next_state[cy[i]] == cy[(i+1) % len(cy)]
               for cy in cycles for i in range(len(cy)))
    # Every valid periodic orbit has one of the two lengths, hence is
    # fixed by the t-th iterate only when its length divides t.
    for t in range(3, 41):
        counted = sum(len(cy) for cy in cycles if t % len(cy) == 0)
        expected = (144 if t % 8 == 0 else 16 if t % 4 == 0 else 0)
        assert counted == expected
    print('states', N_STATES)
    print('defined_transitions', sum(s >= 0 for s in next_state))
    print('cycle_length_multiplicities', dict(sorted(period_counts.items())))
    print('periodic_states', periodic_states)
    print('canonical_cycle_minima (decimal state integers)')
    for cy in sorted(cycles, key=lambda c: (len(c), min(c))):
        print(len(cy), min(cy))
    print('count(t)=144 if 8|t; 16 if 4|t and 8 does not divide t; 0 otherwise')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
