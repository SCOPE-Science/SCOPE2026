"""Exact finite checks of the two-seat reciprocal-EJR reduction."""
from fractions import Fraction
from itertools import combinations, product
from random import Random


def subsets(items):
    return [frozenset(S) for k in range(1, len(items) + 1)
            for S in combinations(items, k)]


def check(n, h, support):
    voters = frozenset(range(n))
    candidates = range(len(h))
    pairs = list(combinations(candidates, 2))
    unanimous_units = sum(h[c] == 1 and support[c] == voters for c in candidates)
    affirmative = {v: frozenset(c for c in candidates if v in support[c]) for v in voters}
    demands = []
    for group in subsets(voters):
        common = frozenset.intersection(*(affirmative[v] for v in group))
        for T in subsets(common):
            if n * sum(1 / h[c] for c in T) <= 2 * len(group):
                demands.append((group, len(T)))

    def representation(pair, group):
        return max(len(affirmative[v].intersection(pair)) for v in group)

    q = {pair: sum(h[c] for c in pair) for pair in pairs}
    jr = {pair for pair in pairs
          if all(representation(pair, group) >= 1 for group, _ in demands)}
    ejr = {pair for pair in pairs
           if all(representation(pair, group) >= seats for group, seats in demands)}
    if unanimous_units < 2:
        assert jr == ejr
    else:
        assert ejr == {pair for pair in jr if support[pair[0]] & support[pair[1]]}
        assert max(q[pair] for pair in ejr) == 2
    top = max(q.values())
    opt_jr = max(q[pair] for pair in jr)
    opt_ejr = max(q[pair] for pair in ejr)
    assert opt_jr == opt_ejr
    for pair in jr:
        if q[pair] == opt_jr:
            for a in pair:
                assert any(a in R and q[R] == opt_ejr for R in ejr)
    bound = Fraction(3*n-2, 4*(n-1))
    assert opt_ejr >= bound * top
    for pair in pairs:
        if q[pair] == top:
            assert any(set(pair).intersection(R) and q[R] >= bound * top for R in ejr)
    return opt_ejr / top, jr, ejr


def main():
    grid = tuple(map(Fraction, ['1/3', '3/4', '1']))
    count = 0
    for n, m in ((2, 3), (3, 3), (2, 4)):
        for support in product(subsets(range(n)), repeat=m):
            for h in product(grid, repeat=m):
                check(n, h, support)
                count += 1
    rng = Random(260908830)
    for n in range(4, 8):
        choices = subsets(range(n))
        for _ in range(60):
            m = rng.randint(2, 6)
            check(n, rng.choices(grid, k=m), rng.choices(choices, k=m))
    for n in range(2, 11):
        p, bloc = frozenset({0}), frozenset(range(1, n))
        tau = Fraction(n, 2*(n-1))
        ratio, _, _ = check(n, [Fraction(1), Fraction(1), tau], [p, p, bloc])
        assert ratio == Fraction(3*n-2, 4*(n-1))
    p, q = frozenset({0}), frozenset({1})
    _, jr, ejr = check(2, list(map(Fraction, [1, 1, '1/2', '1/2'])), [p|q, p|q, p, q])
    assert (2, 3) in jr - ejr
    print(f'EXACT_OK exhaustive={count} sampled=240 sharp=9 separation=1')


if __name__ == '__main__':
    main()
