#!/usr/bin/env python3
"""Finite checks for prime-root state complexity of permutation languages.

Uses independent direct permutation enumeration and DFA partition refinement.
"""
from itertools import permutations
from math import factorial


def compose(g, h):
    """Standard function composition: (g o h)(i) = g(h(i))."""
    return tuple(g[h[i]] for i in range(len(g)))


def pow_zero(g, exponent):
    x = 0
    for _ in range(exponent):
        x = g[x]
    return x


def cycle_permutation(n, seq):
    g = list(range(n))
    for a, b in zip(seq, seq[1:] + seq[:1]):
        g[a] = b
    return tuple(g)


def transposition(n, a, b):
    g = list(range(n))
    g[a], g[b] = g[b], g[a]
    return tuple(g)


def witness(n, p, h):
    if h[0] == 0:
        a = next(i for i in range(1, n) if h[i] != i)
        b = h[a]
        filler = [i for i in range(1, n) if i not in (a, b)][:p-3]
        return cycle_permutation(n, [0, a] + filler + [b])
    if pow_zero(h, p) != 0:
        return tuple(range(n))
    a = h[0]
    b = next(i for i in range(n) if h[i] == 0)
    return transposition(n, a, b)


def test_constructive_witnesses():
    total = 0
    for n in range(3, 9):
        for p in (3, 5, 7):
            if p > n:
                continue
            for h in permutations(range(n)):
                if h == tuple(range(n)):
                    continue
                g = witness(n, p, h)
                before = (pow_zero(g, p) == 0)
                after = (pow_zero(compose(g, h), p) == 0)
                assert before != after, (n, p, g, h)
                total += 1
    return total


def minimize_group_automaton(n, p):
    group = list(permutations(range(n)))
    index = {g: i for i, g in enumerate(group)}
    sigma = cycle_permutation(n, list(range(n)))
    tau = transposition(n, 0, 1)
    step = [[index[compose(letter, g)] for letter in (sigma, tau)] for g in group]
    accepting = [int(pow_zero(g, p) == 0) for g in group]
    # Independent reachable-state BFS, then ordinary Moore minimization.
    initial = index[tuple(range(n))]
    reached = {initial}
    fringe = [initial]
    for q in fringe:
        for dest in step[q]:
            if dest not in reached:
                reached.add(dest)
                fringe.append(dest)
    assert len(reached) == factorial(n)
    blocks = accepting[:]
    rounds = 0
    while True:
        keys = [(blocks[q], blocks[step[q][0]], blocks[step[q][1]]) for q in range(len(group))]
        distinct = {key: i for i, key in enumerate(sorted(set(keys)))}
        next_blocks = [distinct[key] for key in keys]
        rounds += 1
        if len(set(next_blocks)) == len(set(blocks)):
            assert all((blocks[i] == blocks[j]) == (next_blocks[i] == next_blocks[j])
                       for i in range(len(group)) for j in range(i+1, len(group)))
            return len(set(next_blocks)), rounds
        blocks = next_blocks


def main():
    total = test_constructive_witnesses()
    print('explicit distinguishing witnesses checked:', total)
    for n in range(3, 7):
        for p in (3, 5):
            if p <= n:
                states, rounds = minimize_group_automaton(n, p)
                assert states == factorial(n), (n, p, states)
                print('n=%d p=%d minimal=%d moore_rounds=%d' % (n,p,states,rounds))
    print('ALL PRIME-ROOT CHECKS PASSED')


if __name__ == '__main__':
    main()
