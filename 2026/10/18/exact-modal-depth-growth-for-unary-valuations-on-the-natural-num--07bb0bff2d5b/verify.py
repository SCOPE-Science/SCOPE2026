#!/usr/bin/env python3
"""Finite-chain checks for the one-generator modal-depth profile.

Run with Python 3: python verify_modal_chain.py
The infinite claims depend on the accompanying proof, not this finite test.
"""
from itertools import product


def box(a, n):
    # Reflexive forward order: x R y iff x <= y.
    ans = 0
    for i in range(n):
        if all((a >> j) & 1 for j in range(i, n)):
            ans |= 1 << i
    return ans


def run_count(word):
    return 1 + sum(word[i] != word[i - 1] for i in range(1, len(word)))


def refinements(word, depth):
    # Independent semantic d-types: a color and the set of successor (d-1)-types.
    n = len(word)
    labels = list(word)
    for _ in range(depth):
        raw = [(labels[i], frozenset(labels[i:])) for i in range(n)]
        coding = {x: j for j, x in enumerate(dict.fromkeys(raw))}
        labels = [coding[x] for x in raw]
    return len(set(labels))


def boolean_atoms(generators, n):
    patterns = {}
    for i in range(n):
        pat = tuple((s >> i) & 1 for s in generators)
        patterns[pat] = patterns.get(pat, 0) | (1 << i)
    return list(patterns.values())


def closure_size(p, n):
    # Build the Boolean algebra of modal generators; add a box image when missing.
    g = [p]
    while True:
        atoms = boolean_atoms(g, n)
        current = {0}
        for atom in atoms:
            current.update({u | atom for u in tuple(current)})
        new = next((box(x, n) for x in current if box(x, n) not in current), None)
        if new is None:
            return len(current)
        g.append(new)


def run_tests():
    cases = 0
    for n in range(1, 9):
        for word in product((0, 1), repeat=n):
            p = sum(bit << i for i, bit in enumerate(word))
            r = run_count(word)
            actual = closure_size(p, n)
            assert actual == 2**r, (n, word, 'algebra', actual, 2**r)
            for d in range(n + 2):
                actual_types = refinements(word, d)
                expected_types = 1 if r == 1 else min(r, d+2)
                assert actual_types == expected_types, (n, word, d, actual_types, expected_types)
            cases += 1
    for n in range(9, 101):
        word = [i % 2 for i in range(n)]
        for d in (0, 1, 2, n // 2, n-3, n-2, n, n+3):
            assert refinements(word, d) == min(n, d+2)
    print(f'VERIFY_OK: {cases} exhaustive finite colored-chain cases (n<=8), 92 longer alternating chains.')


if __name__ == '__main__':
    run_tests()
