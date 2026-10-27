#!/usr/bin/env python3
"""Exact finite-relation certificate for finite-ring Rule 30 image counts."""
from collections import deque


def local_rule(a, b, c):
    return a ^ (b | c)


def label_matrices():
    result = [0, 0]
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                row, col = 2 * a + b, 2 * b + c
                result[local_rule(a, b, c)] |= 1 << (4 * row + col)
    return result


def boolean_multiply(x, y):
    z = 0
    for row in range(4):
        for mid in range(4):
            if x & (1 << (4 * row + mid)):
                z |= ((y >> (4 * mid)) & 15) << (4 * row)
    return z


def relation_automaton():
    labels = label_matrices()
    identity = sum(1 << (5 * k) for k in range(4))
    states = [identity]
    index = {identity: 0}
    edges = []
    for relation in states:  # list grows until the full reachable closure is obtained
        successors = []
        for generator in labels:
            product = boolean_multiply(relation, generator)
            if product not in index:
                index[product] = len(states)
                states.append(product)
            successors.append(index[product])
        edges.append(tuple(successors))
    accepted = [int(any(x & (1 << (5 * i)) for i in range(4))) for x in states]
    assert labels == [49665, 450]
    assert len(states) == len(edges) == 41
    assert sum(accepted) == 30
    assert all(boolean_multiply(states[i], labels[k]) == states[edges[i][k]]
               for i in range(41) for k in (0, 1))
    return edges, accepted


def image_and_orphan_counts(edges, accepted, max_n):
    populations = [0] * len(edges)
    populations[0] = 1
    counts = [0] * (max_n + 1)
    for n in range(max_n + 1):
        counts[n] = (1 << n) - sum(populations[i] * accepted[i]
                                       for i in range(len(populations)))
        if n < max_n:
            next_pop = [0] * len(edges)
            for i, multiplicity in enumerate(populations):
                for nxt in edges[i]:
                    next_pop[nxt] += multiplicity
            populations = next_pop
    return counts


def direct_ring_image_size(n):
    outputs = set()
    for config in range(1 << n):
        bit = lambda i: (config >> (i % n)) & 1
        output = sum(local_rule(bit(i - 1), bit(i), bit(i + 1)) << i
                     for i in range(n))
        outputs.add(output)
    return len(outputs)


def main():
    edges, accepted = relation_automaton()
    d = image_and_orphan_counts(edges, accepted, 70)
    assert d[0] == 0
    assert d[1:7] == [1, 1, 3, 5, 6, 12]
    # This is an all-n certificate: the 41-state transition matrix forces
    # every scalar output sequence to satisfy its degree-41 characteristic
    # polynomial (Cayley-Hamilton). The proposed order-six recurrence error
    # is another such scalar sequence, so its first 41 zeros imply all zeros.
    for n in range(1, 42):
        assert d[n + 6] - d[n + 5] - 3 * d[n + 3] + d[n + 2] + 2 * d[n] == 0
    # Independent exact formula via the three algebraic roots of
    # t^3-t^2-2: their n-th power sum satisfies the following recurrence.
    power_sums = [3, 1, 1]
    for n in range(3, 71):
        power_sums.append(power_sums[n - 1] + 2 * power_sums[n - 3])
    for n in range(1, 71):
        correction = -1 if n % 3 == 0 else 1
        assert (power_sums[n] + correction) % 2 == 0
        assert d[n] == (power_sums[n] + correction) // 2
    for n in range(1, 14):
        assert (1 << n) - direct_ring_image_size(n) == d[n]
    print('VERIFY_OK monoid_states=41 recurrence_initial_shifts=41 direct_rings=1..13 ' 
          'power_sum_cases=70 image_sizes_n8_n12_n16=223,3816,63199')


if __name__ == '__main__':
    main()
