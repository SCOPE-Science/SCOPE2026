#!/usr/bin/env python3
"""Finite cross-checks for minimal LSD-first shifted Thue--Morse DFAOs.

This script verifies finite instances of an analytically proved formula;
finite tests are not used as proof for arbitrary shifts.
"""
from collections import deque
from random import Random


def tm(n):
    assert n >= 0
    return n.bit_count() & 1


def transition(state, bit):
    d, e = state
    x = d + bit
    return (x // 2, e ^ (x & 1))


def build_dfa(c):
    initial = (c, 0)
    states = [initial]
    seen = {initial: 0}
    edge = []
    for state in states:
        nexts = []
        for b in (0, 1):
            nxt = transition(state, b)
            if nxt not in seen:
                seen[nxt] = len(states)
                states.append(nxt)
            nexts.append(seen[nxt])
        edge.append(tuple(nexts))
    return states, edge


def minimize_count(states, edges):
    """Moore-machine partition refinement of output equivalence."""
    classes = [tm(d) ^ e for d, e in states]
    while True:
        sig = [(classes[i], classes[edges[i][0]], classes[edges[i][1]])
               for i in range(len(states))]
        dictionary = {s: j for j, s in enumerate(sorted(set(sig)))}
        new = [dictionary[s] for s in sig]
        if all((classes[i] == classes[j]) == (new[i] == new[j])
               for i in range(len(states)) for j in range(i + 1, len(states))):
            return len(set(new))
        classes = new


def formula(c):
    if c == 0:
        return 2
    if c == 1:
        return 3
    if c == 2:
        return 5
    if c == 3:
        return 6
    k = c.bit_length() - 1
    total = 7
    for j in range(1, k):
        q, r = divmod(c, 1 << j)
        a = 2 - int(r == (1 << j) - 1)
        b = 0 if r == 0 else 1 if r == 1 else 2
        total += (a if q >= 3 else 0) + b
    return total


def direct_value(c, word):
    return tm(c + sum(int(b) << j for j, b in enumerate(word)))


def evaluate_dfa(states, edges, word):
    i = 0
    for b in word:
        i = edges[i][int(b)]
    d, e = states[i]
    return tm(d) ^ e


def main():
    state_cases = 0
    for c in range(4096):
        states, edges = build_dfa(c)
        expected = formula(c)
        assert len(states) == expected, (c, len(states), expected)
        assert minimize_count(states, edges) == expected, c
        state_cases += 1

    words = ['']
    for j in range(1, 10):
        words.extend(format(i, f'0{j}b')[::-1] for i in range(1 << j))
    input_checks = 0
    for c in range(96):
        states, edges = build_dfa(c)
        for word in words:
            assert evaluate_dfa(states, edges, word) == direct_value(c, word), (c, word)
            input_checks += 1

    block_cases = 0
    for k in range(3, 12):
        lo, hi = 1 << k, 1 << (k + 1)
        values = {c: formula(c) for c in range(lo, hi)}
        assert min(values.values()) == 2*k+3
        assert {c for c, v in values.items() if v == 2*k+3} == {lo}
        assert max(values.values()) == 4*k+1
        expected_max = set(range(3*(1 << (k-1))+2, hi, 4))
        assert {c for c, v in values.items() if v == 4*k+1} == expected_max
        assert len(expected_max) == 1 << (k-3)
        block_cases += len(values)

    rng = Random(4096)
    random_cases = 0
    for _ in range(300):
        c = rng.randrange(0, 1 << 100)
        states, edges = build_dfa(c)
        assert len(states) == formula(c)
        assert minimize_count(states, edges) == len(states)
        random_cases += 1

    print('VERIFY_OK')
    print('state_count_and_minimization_cases:', state_cases)
    print('direct_input_evaluation_cases:', input_checks)
    print('dyadic_block_extremizer_cases:', block_cases)
    print('large_shift_random_cases:', random_cases)
    print('small_state_counts:', [formula(c) for c in range(24)])
    print('dyadic_minimum_and_maximum_at_k_10:', 23, 41)


if __name__ == '__main__':
    main()
