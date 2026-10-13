#!/usr/bin/env python3
"""Independent finite checks for Heyting-algebra endomorphisms of weak orders.
Standard library only; run with Python 3.9+ as `python verify.py`.
The bounded-map enumerator and suffix-state recurrence use different algorithms.
"""
from itertools import product, combinations
from math import factorial, comb
from collections import Counter, defaultdict


def stirling(n, k):
    if n == k == 0: return 1
    if k == 0 or k > n: return 0
    tab = [[0] * (k + 1) for _ in range(n + 1)]
    tab[0][0] = 1
    for a in range(1, n + 1):
        for b in range(1, min(a, k) + 1):
            tab[a][b] = b * tab[a - 1][b] + tab[a - 1][b - 1]
    return tab[n][k]


def prepare(sizes):
    n = sum(sizes)
    level = tuple(i for i, z in enumerate(sizes) for _ in range(z))
    blocks = tuple(tuple(x for x in range(n) if level[x] == i) for i in range(len(sizes)))
    uppers = tuple(frozenset((x,)) | frozenset(y for y in range(n) if level[y] > level[x]) for x in range(n))
    return n, level, blocks, uppers


def upset_count(S, uppers):
    # Every nonempty upset has a unique lowest occupied level and a
    # nonempty subset of that level; higher occupied levels are complete.
    S = frozenset(S)
    sizes = Counter(len(uppers[x]) - 1 for x in S)
    # A fixed level has a fixed number of strict upper elements.
    return 1 + sum((2 ** v - 1) for v in sizes.values())


def suffix_census(sizes):
    n, level, blocks, uppers = prepare(sizes)
    states = {frozenset(): 1}
    for block in reversed(blocks):
        nxt = defaultdict(int)
        for S, ways in states.items():
            E = tuple(x for x in range(n) if uppers[x] == (S | frozenset((x,))))
            for k in range(1, min(len(E), len(block)) + 1):
                w = factorial(k) * stirling(len(block), k)
                for T in combinations(E, k):
                    nxt[S | frozenset(T)] += ways * w
        states = nxt
    return Counter({rank: sum(v for S, v in states.items() if upset_count(S, uppers) == rank)
                    for rank in {upset_count(S, uppers) for S in states}})


def brute_census(sizes):
    n, level, blocks, uppers = prepare(sizes)
    counts = Counter()
    for f in product(range(n), repeat=n):
        if all(frozenset(f[y] for y in uppers[x]) == uppers[f[x]] for x in range(n)):
            counts[upset_count(frozenset(f), uppers)] += 1
    return counts


def uniform_formula(m, h):
    out = Counter()
    for k in range(h - 1):
        out[2 + k * (2 ** m - 1)] += m * factorial(m) ** k
    for t in range(1, m + 1):
        out[(h - 1) * (2 ** m - 1) + 2 ** t] += (factorial(m) ** (h - 1)) * factorial(t) * comb(m, t) * stirling(m, t)
    return out


def all_compositions(n):
    if n == 0:
        yield ()
    else:
        for first in range(1, n + 1):
            for rest in all_compositions(n - first):
                yield (first,) + rest


def direct_implication_checks(sizes):
    n, level, blocks, uppers = prepare(sizes)
    U = [frozenset(i for i in range(n) if (mask >> i) & 1)
         for mask in range(1 << n)]
    U = [s for s in U if all(uppers[x] <= s for x in s)]
    imp = {(a, b): frozenset(x for x in range(n) if (uppers[x] & a) <= b) for a in U for b in U}
    checked = 0
    for f in product(range(n), repeat=n):
        # Test complete implication preservation independently, without invoking the p-morphism test.
        def preim(s): return frozenset(x for x in range(n) if f[x] in s)
        algebraic = all(preim(a) in U for a in U) and all(preim(imp[a, b]) == imp[preim(a), preim(b)] for a in U for b in U)
        bounded = all(frozenset(f[y] for y in uppers[x]) == uppers[f[x]] for x in range(n))
        assert algebraic == bounded, (sizes, f)
        checked += 1
    return checked


def main():
    cases = checked_functions = 0
    for n in range(1, 6):
        for sizes in all_compositions(n):
            assert suffix_census(sizes) == brute_census(sizes), sizes
            cases += 1
            checked_functions += n ** n
    print('NONUNIFORM_BRUTE_OK', 'level_vectors', cases, 'functions', checked_functions)
    uniform_checks = 0
    for m, h in [(2,1),(2,2),(2,3),(3,1),(3,2),(4,1)]:
        exact = brute_census((m,)*h)
        assert exact == uniform_formula(m, h), (m, h, exact, uniform_formula(m,h))
        print('UNIFORM', m, h, dict(sorted(exact.items())))
        uniform_checks += 1
    for m in (2,3,4,5):
        for h in range(1, 10):
            assert suffix_census((m,)*h) == uniform_formula(m,h), (m,h)
    print('UNIFORM_DP_OK', 36, 'BRUTE', uniform_checks)
    logic = sum(direct_implication_checks(s) for s in [(1,), (2,), (1,1), (2,1), (1,2), (2,2)])
    print('DIRECT_HEYTING_IMPLICATION_OK', 'functions',logic)
    print('VERIFY_OK')

if __name__ == '__main__': main()
