"""Finite exhaustive verifier of BLAL implication tables on small chains.

The 11 identities and 3 quasi-identities are those in Cornejo et al.,
International Journal of Approximate Reasoning 195 (2026), Theorem 16.
Python 3 standard library only. Execute: python checker.py
"""
from itertools import product


def table(n, lower):
    """Fill the strict lower triangle in lexicographic row order."""
    entries = [(x, y) for x in range(n) for y in range(x)]
    assert len(lower) == len(entries)
    t = [[n - 1 if x <= y else -1 for y in range(n)]
         for x in range(n)]
    for (x, y), value in zip(entries, lower):
        assert 0 <= value < n - 1
        t[x][y] = value
    return t


def violation(t):
    """Return the first failed BLAL axiom, or None if all hold."""
    n, top = len(t), len(t) - 1
    p = lambda x, y: t[x][y]
    for x, y, z in product(range(n), repeat=3):
        eq = (
            p(min(x, y), x),                               # E1
            p(min(x, y), y),                               # E2
            p(p(z, x), p(p(z, y), p(z, min(x, y)))),         # E3
            p(x, max(x, y)),                               # E4
            p(y, max(x, y)),                               # E5
            p(p(x, z), p(p(y, z), p(max(x, y), z))),         # E6
            p(x, x),                                       # E7
            p(p(x, y), p(p(y, z), p(x, z))),                 # E8
            p(p(y, z), p(p(x, y), p(x, z))),                 # E9
            p(0, x),                                       # E10
            p(x, p(0, 0)),                                 # E11
        )
        for i, lhs in enumerate(eq, 1):
            if lhs != top:
                return f'E{i}', (x, y, z), lhs
        if x == top and p(x, y) == top and y != top:
            return 'QE1', (x, y, z), None
        if x == top and p(p(x, x), x) != top:
            return 'QE2', (x, y, z), None
        if p(x, y) == top and p(y, x) == top and x != y:
            return 'QE3', (x, y, z), None
    return None


def valid_tuples(n):
    """Complete search justified by implication/order equivalence.

    Each BLAL implication takes value n-1 precisely where x<=y.
    Only n(n-1)/2 strict lower-triangle cells remain, each in
    {0,...,n-2}; their exhaustive product has (n-1)^(n(n-1)/2)
    elements, with the empty product interpreted as one.
    """
    count = n * (n - 1) // 2
    return [tuple(v) for v in product(range(n - 1), repeat=count)
            if violation(table(n, v)) is None]


def dominates(a, b):
    return all(x >= y for x, y in zip(a, b))


def main():
    classes = {n: valid_tuples(n) for n in (1, 2, 3, 4)}
    assert {n: len(v) for n, v in classes.items()} == {1: 1, 2: 1, 3: 4, 4: 25}
    assert classes[3] == [(0, 0, 0), (0, 0, 1),
                          (1, 0, 1), (1, 1, 1)]
    assert all(dominates(b, a) or dominates(a, b)
               for a, b in product(classes[3], repeat=2))
    A = (1, 1, 1, 1, 1, 2)
    B = (2, 1, 1, 0, 1, 2)
    C = (1, 0, 1, 0, 1, 2)
    D = (1, 1, 1, 0, 1, 1)
    M = (1, 1, 1, 0, 1, 2)
    assert all(t in classes[4] for t in (A, B, C, D))
    assert all(dominates(u, v) for u in (A, B) for v in (C, D))
    assert tuple(min(a, b) for a, b in zip(A, B)) == M
    assert tuple(max(c, d) for c, d in zip(C, D)) == M
    assert violation(table(4, M)) == ('E8', (3, 2, 0), 1)
    # Confirm the missing extrema directly against the *entire* poset.
    possible_joins = [u for u in classes[4]
                      if all(dominates(u, v) for v in (C, D))
                      and all(dominates(v, u) for v in (A, B))]
    possible_meets = [u for u in classes[4]
                      if all(dominates(v, u) for v in (A, B))
                      and all(dominates(u, v) for v in (C, D))]
    assert not possible_joins and not possible_meets
    print('ALL_CHECKS_OK counts=(1,1,4,25) candidates=(1,1,8,729)')
    print('BLAL_C4 witness A,B,C,D valid; M invalid at E8(3,2,0)=1')
    print('No join of C,D and no meet of A,B')


if __name__ == '__main__':
    main()
