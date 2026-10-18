#!/usr/bin/env python3
"""Independent, exact checks for cotransitivity in finite rooted-star Heyting algebras.

Run: python3 verify_apartness.py
No external packages are required.
"""
from itertools import product


def check(m):
    assert 1 <= m <= 7
    leaf_count = 1 << m
    root_bit = leaf_count
    all_leaves = leaf_count - 1
    entire_poset = root_bit | all_leaves
    upsets = list(range(leaf_count)) + [entire_poset]
    n = len(upsets)

    def leq(a, b):
        return a & ~b == 0

    # Build the implication by its universal right-adjoint property,
    # independently of any formulas used to prove the theorem.
    implication = [[0] * n for _ in range(n)]
    for i, a in enumerate(upsets):
        for j, b in enumerate(upsets):
            admissible = [v for v in upsets if leq(a & v, b)]
            maxima = [v for v in admissible
                      if all(leq(w, v) for w in admissible)]
            assert len(maxima) == 1
            implication[i][j] = maxima[0]

    by_value = {v: i for i, v in enumerate(upsets)}
    negation = [implication[i][by_value[0]] for i in range(n)]
    apartness = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            biconditional = implication[i][j] & implication[j][i]
            apartness[i][j] = negation[by_value[biconditional]]

    failed_triples = 0
    for i, j, k in product(range(n), repeat=3):
        lhs = apartness[i][j]
        rhs = apartness[i][k] | apartness[k][j]
        failed_triples += not leq(lhs, rhs)

    # Weak excluded middle uses neg(x) OR neg(neg(x)), not x OR neg(x).
    failed_wem = 0
    for i in range(n):
        second = negation[by_value[negation[i]]]
        if negation[i] | second != entire_poset:
            failed_wem += 1

    expected_failed_triples = (leaf_count - 2) * (leaf_count + 3)
    expected_wem_true = 3
    assert failed_triples == expected_failed_triples, (m, failed_triples)
    assert n - failed_wem == expected_wem_true, (m, failed_wem)
    return n ** 3, failed_triples, failed_wem


def main():
    total = 0
    for m in range(1, 8):
        triples, failures, wem_failures = check(m)
        total += triples
        print('m={} elements={} triples={} cotrans_fail={} wem_fail={}'.format(
            m, (1 << m) + 1, triples, failures, wem_failures))
    print('VERIFY_OK cases=7 triples={} direct_implication=YES WEM=YES'.format(total))


if __name__ == '__main__':
    main()
