#!/usr/bin/env python3
"""Exact enumeration of preconditional operations on finite Boolean powersets.

All operations and direct axiom tests use integer bit masks. Python 3 standard
library only. Counts are of operations on an explicitly labelled atom set.
"""
from itertools import product, permutations
from collections import Counter


def subs(a, n):
    return tuple(x for x in range(1 << n) if x & a == x)


def row_choices(a, n):
    full = (1 << n) - 1
    domain = subs(a, n)
    if a == full:
        yield {t: t for t in domain}
        return
    options = []
    for t in domain:
        choices = tuple(y for y in range(full + 1)
                        if (y & t) == t and (t != 0 or (y & a) == 0))
        if t == a:
            choices = (full,)
        options.append(choices)
    for values in product(*options):
        f = dict(zip(domain, values))
        # Consequent monotonicity, followed by the d=a instance of P5.
        if any((f[u] & f[v]) != f[u]
               for u in domain for v in domain if (u & v) == u):
            continue
        if any(f[a & f[t]] != f[t] for t in domain):
            continue
        yield f


def iff_direct_axioms(table, n):
    top = (1 << n) - 1
    def imp(a, b):
        return table[a][a & b]
    for a in range(top + 1):
        if imp(top, a) != a or imp(a, a) != top:
            return False
        if a & imp(a, 0):
            return False
        for b in range(top + 1):
            if (a & b) & imp(a, b) != (a & b):
                return False
            if imp(a, b) & imp(a, a & b) != imp(a, b):
                return False
            for c in range(top + 1):
                if (imp(a, b & c) & imp(a, b)) != imp(a, b & c):
                    return False
                d = a & b
                rhs = imp(d, c)
                if (imp(a, rhs) & rhs) != imp(a, rhs):
                    return False
    return True


def is_f(table, n):
    top = (1 << n) - 1
    neg = lambda a: table[a][0]
    return all(a & neg(neg(a)) == a for a in range(top + 1))


def census(n):
    top = (1 << n) - 1
    rows = {a: tuple(row_choices(a, n)) for a in range(top + 1)}
    # Work in subset-size order so all proper subset rows are determined first.
    order = sorted(rows, key=lambda a: (a.bit_count(), a))
    chosen = {}
    total_t = total_f = 0
    fib_t = Counter()
    fib_f = Counter()

    def dfs(j):
        nonlocal total_t, total_f
        if j == len(order):
            assert iff_direct_axioms(chosen, n)
            total_t += 1
            key = tuple(chosen[a][0] for a in range(top + 1))
            fib_t[key] += 1
            if is_f(chosen, n):
                total_f += 1
                fib_f[key] += 1
            return
        a = order[j]
        for f in rows[a]:
            # All P5 inequalities involving a as the larger antecedent.
            if any((f[a & val] & val) != f[a & val]
                   for d, g in chosen.items() if (d & a) == d
                   for val in g.values()):
                continue
            chosen[a] = f
            dfs(j + 1)
            del chosen[a]

    dfs(0)
    return total_t, total_f, fib_t, fib_f, rows


def directed_orbit_table(n=3):
    assert n == 3
    directed = tuple((i, j) for i in range(3) for j in range(3) if i != j)
    coatoms = (3, 5, 6)
    coatom_rows = {a: tuple(row_choices(a, 3)) for a in coatoms}

    def local_counts(mask):
        singles = {1 << i: sum(1 << j for t, (u, j) in enumerate(directed)
                                if u == i and (mask >> t) & 1)
                   for i in range(3)}
        return tuple(sum(all((f[a & singles[d]] & singles[d]) == f[a & singles[d]]
                             for d in singles if (a & d) == d)
                         for f in coatom_rows[a]) for a in coatoms)

    def transform(mask, perm):
        edge = {(u, v) for i, (u, v) in enumerate(directed) if (mask >> i) & 1}
        return sum(1 << i for i, (u, v) in enumerate(directed)
                   if (perm.index(u), perm.index(v)) in edge)

    seen = set()
    table = []
    for mask in range(64):
        if mask in seen:
            continue
        orbit = {transform(mask, p) for p in permutations(range(3))}
        seen |= orbit
        counts = local_counts(mask)
        table.append((mask, len(orbit), *counts))
    return table


if __name__ == '__main__':
    for n, expected in ((1, (1, 1)), (2, (4, 2)), (3, (7820, 1021))):
        T, F, fib_t, fib_f, rows = census(n)
        print('atoms', n, 'T', T, 'F', F, 'T-negations', len(fib_t),
              'F-negations', len(fib_f))
        assert (T, F) == expected
        if n == 3:
            assert len(fib_t) == 125 and len(fib_f) == 8
            assert Counter(fib_f.values()) == Counter({729: 1, 81: 3, 16: 3, 1: 1})
            assert max(fib_f.values()) == 729
            tab = directed_orbit_table()
            assert len(tab) == 16 and sum(r[1] for r in tab) == 64
            assert sum(r[1] * r[2] * r[3] * r[4] for r in tab) == 7820
            print('directed_orbits', tab)
    print('BOOLEAN_PRECONDITIONAL_BINARY_CENSUS_OK')
