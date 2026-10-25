"""Independent exact-rational checks of a star opinion voter-model exit law.

Reconstructs the ORIGINAL (not h-transformed) finite Markov chain and
solves a linear system for every all-leaf terminal composition.
Run: python verify.py  (requires SymPy).
"""
from itertools import product
from math import factorial, comb
from sympy import Matrix, Rational, eye


def compositions(parts, total):
    if parts == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - parts + 2):
        for rest in compositions(parts - 1, total - first):
            yield (first,) + rest


def exact_exit_law(d, n):
    assert 2 <= d < n
    states = [x for s in range(d, n) for x in compositions(d, s)]
    targets = list(compositions(d, n))
    index = {x: idx for idx, x in enumerate(states)}
    end_index = {x: idx for idx, x in enumerate(targets)}
    M = eye(len(states))
    R = Matrix.zeros(len(states), len(targets))
    for x, u in index.items():
        s = sum(x)
        for i in range(d):
            for delta in (-1, 1):
                v = list(x)
                v[i] += delta
                if v[i] == 0:
                    continue  # losing any leaf excludes the target event
                v = tuple(v)
                weight = Rational(x[i], 2 * s)
                if sum(v) == n:
                    R[u, end_index[v]] += weight
                else:
                    M[u, index[v]] -= weight
    # Transition system P = R + Q P; solve over Q exactly.
    X = M.inv() * R
    start = index[(1,) * d]
    predicted = Rational(factorial(n - d) * factorial(2 * d - 1),
                         factorial(n + d - 1))
    for j, terminal in enumerate(targets):
        if X[start, j] != predicted:
            raise AssertionError((d, n, terminal, X[start, j], predicted))
    joint = sum(X[start, j] for j in range(len(targets)))
    assert joint == predicted * comb(n - 1, d - 1)
    return len(states), len(targets), predicted, joint


def main():
    tests = [(2, 3), (2, 4), (2, 5), (2, 7),
             (3, 4), (3, 5), (3, 7), (3, 8),
             (4, 5), (4, 6), (4, 7), (5, 6), (5, 7)]
    checks = 0
    for d, n in tests:
        count_states, count_ends, probability, joint = exact_exit_law(d, n)
        checks += count_ends
        print(f'd={d:2}, n={n:2}, transient={count_states:3}, '
              f'final={count_ends:3}, each={probability}, joint={joint}')
    print(f'PASS: {checks} exact terminal probabilities verified for {len(tests)} finite models.')


if __name__ == '__main__':
    main()
