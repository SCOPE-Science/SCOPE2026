#!/usr/bin/env python3
"""Exhaustive finite-group checks of maximal-subgroup incidence formulas."""
from collections import Counter, deque
from itertools import product
from math import prod


def enumerate_group(moduli):
    labels = list(product(*[range(n) for n in moduli], [0, 1]))
    index = {v: i for i, v in enumerate(labels)}
    n = len(labels)
    mult = []
    for x in labels:
        r = []
        for y in labels:
            r.append(index[tuple((a + (-1 if x[-1] else 1) * b) % m
                                 for a, b, m in zip(x[:-1], y[:-1], moduli)) + (x[-1] ^ y[-1],)])
        mult.append(r)
    e = index[(0,) * len(moduli) + (0,)]
    inverse = [next(j for j in range(n) if mult[i][j] == e and mult[j][i] == e)
               for i in range(n)]
    return labels, mult, inverse, e


def all_subgroups(labels, mult, inv, e):
    n = len(labels)
    # All possible subgroups, generated incrementally; the generating set of a
    # known subgroup is replaced by its complete element set, so no structural
    # classification of generalized-dihedral subgroups is assumed.
    trivial = frozenset([e])
    visited = {trivial}
    queue = deque([trivial])
    while queue:
        H = queue.popleft()
        for g in range(n):
            if g in H:
                continue
            generators = tuple(H) + (g, inv[g])
            closure = {e}
            q = deque([e])
            while q:
                x = q.popleft()
                for s in generators:
                    y = mult[x][s]
                    if y not in closure:
                        closure.add(y)
                        q.append(y)
            K = frozenset(closure)
            if K not in visited:
                visited.add(K)
                queue.append(K)
    return visited


def theorem_profile(moduli):
    # prime factorization of each coordinate's order; d_p is number of factors
    # with a nonzero p-primary component in the invariant-factor list.
    rs = {}
    for n in moduli:
        p = 2
        while p * p <= n:
            if n % p == 0:
                rs[p] = rs.get(p, 0) + 1
                while n % p == 0:
                    n //= p
            p += 1
        if n > 1:
            rs[n] = rs.get(n, 0) + 1
    assert rs
    ps = sorted(rs)
    ms = {p: (p ** rs[p] - 1) // (p - 1) for p in ps}
    total = 1 + sum(p * ms[p] for p in ps)
    return rs, ms, total


def run_case(moduli):
    labels, mult, inv, e = enumerate_group(moduli)
    n = len(labels)
    subs = all_subgroups(labels, mult, inv, e)
    full = frozenset(range(n))
    maximals = [H for H in subs if H != full and not any(H < K < full for K in subs)]
    assert maximals
    Phi = set.intersection(*(set(H) for H in maximals))
    actual = [sum(i in H for H in maximals) for i in range(n)]
    rs, ms, expected_max = theorem_profile(moduli)
    assert len(maximals) == expected_max, (moduli, len(maximals), expected_max)
    ref_degree = sum(ms.values())
    for i, t in enumerate(labels):
        if t[-1]:
            predicted = ref_degree
        else:
            active = [p for p in rs if any(m % p == 0 and a % p != 0 for a, m in zip(t[:-1], moduli))]
            predicted = expected_max - sum(p ** rs[p] for p in active)
        assert actual[i] == predicted, (moduli, t, actual[i], predicted)
    nonFrattini = set(range(n)) - Phi
    ui = 1 + max(actual[i] for i in nonFrattini)
    predicted_ui = expected_max + 1 - min(p ** rs[p] for p in rs)
    assert ui == predicted_ui, (moduli, ui, predicted_ui)
    assert all(labels[i][-1] == 0 for i in Phi)
    print('CASE', 'x'.join(map(str, moduli)),
          'order', n, 'subgroups', len(subs), 'maximal', len(maximals),
          'phi', len(Phi), 'ui', ui,
          'incidence_profile', dict(sorted(Counter(actual).items())))


def main():
    for mods in [(2,), (4,), (2, 2), (2, 2, 2), (4, 2), (4, 4), (2, 3), (2, 3, 3), (3,), (9,), (3, 3), (9, 3), (3, 5), (3, 3, 3), (3, 3, 5), (5, 5)]:
        run_case(mods)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
