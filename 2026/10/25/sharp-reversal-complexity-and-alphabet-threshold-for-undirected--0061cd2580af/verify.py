"""Finite checks for reversal of complete involutive-transition automata.

This enumerator is not used as a substitute for the all-parameter proof.
Run with Python 3.9 or later: python verify.py
"""
from collections import deque
from itertools import product, combinations
from math import comb


def generators(n):
    u = tuple((-i) % n for i in range(n))
    v = tuple((1 - i) % n for i in range(n))
    w = tuple(1 if i == 0 else 0 if i == 1 else i for i in range(n))
    return (u, v, w)


def image(S, p):
    return frozenset(p[i] for i in S)


def orbit_and_transitions(n, F, gens):
    start = frozenset(F)
    states = [start]
    lookup = {start: 0}
    edges = []
    for S in states:
        row = []
        for p in gens:
            T = image(S, p)
            if T not in lookup:
                lookup[T] = len(states)
                states.append(T)
            row.append(lookup[T])
        edges.append(tuple(row))
    return states, edges


def minimized_count(states, edges, initial_state):
    """Refine equality-of-future-language equivalence, without group theory."""
    accepting = tuple(initial_state in S for S in states)
    colors = tuple(int(x) for x in accepting)
    while True:
        signatures = [(colors[i], tuple(colors[j] for j in edges[i]))
                      for i in range(len(states))]
        representatives = {s: j for j, s in enumerate(sorted(set(signatures)))}
        nxt = tuple(representatives[s] for s in signatures)
        if len(set(nxt)) == len(set(colors)):
            return len(set(nxt))
        colors = nxt


def apply(q, w, gens):
    for letter in w:
        q = gens[letter][q]
    return q


def involutions(n):
    """Enumerate each involution, including fixed points, once."""
    def rec(unused, mapping):
        if not unused:
            yield tuple(mapping)
            return
        a = min(unused)
        rem = unused - {a}
        mapping[a] = a
        yield from rec(rem, mapping)
        for b in rem:
            mapping[a], mapping[b] = b, a
            yield from rec(rem - {b}, mapping)
        mapping[a] = -1
    yield from rec(set(range(n)), [-1] * n)


def check():
    triples = 0
    membership = 0
    max_states = 0
    for n in range(2, 10):
        gens = generators(n)
        for p in gens:
            assert sorted(p) == list(range(n))
            assert all(p[p[i]] == i for i in range(n))
        for m in range(1, n):
            F = frozenset(range(m))
            states, edges = orbit_and_transitions(n, F, gens)
            assert len(states) == comb(n, m), (n, m, len(states))
            assert minimized_count(states, edges, 0) == comb(n, m)
            assert all(image(image(S, p), p) == S
                       for S in states for p in gens)
            for length in range(8):
                for word in product(range(3), repeat=length):
                    lhs = apply(0, word[::-1], gens) in F
                    S = F
                    for letter in word:
                        S = image(S, gens[letter])
                    assert lhs == (0 in S), (n, m, word)
                    membership += 1
            triples += 1
            max_states = max(max_states, len(states))

    # Exhaustively inspect every two-letter involution pair through five states.
    # For transitive input actions, the reversed subset orbit cannot exceed 2n;
    # the central binomial maximum is unattained for n=4 and n=5.
    pairs = 0
    for n in range(2, 6):
        ps = list(involutions(n))
        for p in ps:
            for q in ps:
                singleton_orbit, _ = orbit_and_transitions(n, {0}, (p, q))
                if len(singleton_orbit) != n:
                    continue
                assert all(p[p[i]] == i and q[q[i]] == i for i in range(n))
                for m in range(1, n):
                    S, edges = orbit_and_transitions(n, range(m), (p, q))
                    assert len(S) <= 2 * n
                    assert minimized_count(S, edges, 0) == len(S)
                    if n in (4, 5) and m in (n // 2, (n + 1) // 2):
                        assert len(S) < comb(n, m)
                pairs += 1
    print('VERIFY_OK', 'parameters', triples,
          'word_membership_checks', membership,
          'exhaustive_transitive_two_letter_pairs', pairs,
          'largest_witness_reverse', max_states)


if __name__ == '__main__':
    check()
