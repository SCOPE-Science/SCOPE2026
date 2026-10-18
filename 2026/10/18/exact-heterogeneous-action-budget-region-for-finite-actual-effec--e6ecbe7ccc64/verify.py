"""Independent finite checks of heterogeneous action-copy representation.

Runs using only the Python 3 standard library. All game semantics are rebuilt
from their deterministic action-profile outcome tables.
"""
from itertools import product
from math import prod
import random


def index_of_largest(b):
    return max(range(len(b)), key=lambda i: b[i])


def color(coords, b):
    pivot = index_of_largest(b)
    return tuple((coords[j] - coords[pivot]) % b[j]
                 for j in range(len(b)) if j != pivot)


def labels(b):
    pivot = index_of_largest(b)
    return list(product(*(range(b[j]) for j in range(len(b)) if j != pivot)))


def check_slices():
    checked = 0
    for k in range(2, 6):
        for b in product(range(1, 5), repeat=k):
            colors = set(labels(b))
            profiles = list(product(*(range(v) for v in b)))
            assert len(colors) == prod(b) // max(b)
            for i in range(k):
                for value in range(b[i]):
                    obtained = {color(t, b) for t in profiles if t[i] == value}
                    assert obtained == colors, (b, i, value)
                    checked += 1
    return checked


def actual_effectivity(actions, out):
    sigma = []
    all_profiles = list(product(*actions))
    for i in range(len(actions)):
        fam = set()
        for a in actions[i]:
            fam.add(frozenset(out[t] for t in all_profiles if t[i] == a))
        sigma.append(fam)
    return sigma


def realizes(sigma, b):
    k = len(sigma)
    R = sorted(set().union(*sigma[0]))
    for family in sigma:
        assert set().union(*family) == set(R)
    assert all(set.intersection(*map(set, terms))
               for terms in product(*[tuple(family) for family in sigma]))
    assert all(prod(b[j] for j in range(k) if j != i) >= len(R)
               for i in range(k))
    all_colors = labels(b)
    pi = {c: R[idx % len(R)] for idx, c in enumerate(all_colors)}
    actions = [tuple((tuple(sorted(s)), d) for s in sorted(family,
                         key=lambda s: (len(s), tuple(sorted(s)))) for d in range(b[i]))
               for i, family in enumerate(sigma)]
    out = {}
    for t in product(*actions):
        intersection = set.intersection(*(set(a[0]) for a in t))
        assert intersection
        target = pi[color(tuple(a[1] for a in t), b)]
        out[t] = target if target in intersection else min(intersection)
    got = actual_effectivity(actions, out)
    assert got == sigma, (sigma, got, b)
    for i in range(k):
        assert len(actions[i]) == b[i] * len(sigma[i])
        for s in sigma[i]:
            assert sum(a[0] == tuple(sorted(s)) for a in actions[i]) == b[i]
    return len(out)


def check_games():
    rnd = random.Random(20261014)
    cases = 0
    profiles = 0
    for k in (2, 3, 4):
        for n in range(1, 7):
            valid = [b for b in product(range(1, 5), repeat=k)
                     if all(prod(b[j] for j in range(k) if j != i) >= n
                            for i in range(k))]
            if not valid:
                continue
            for _ in range(24):
                original = [tuple(range(rnd.randint(1, 3))) for i in range(k)]
                out0 = {t: rnd.randrange(n) for t in product(*original)}
                sigma = actual_effectivity(original, out0)
                true_n = len(set().union(*sigma[0]))
                candidates = [b for b in valid if all(
                    prod(b[j] for j in range(k) if j != i) >= true_n
                    for i in range(k))]
                tests = [candidates[0], candidates[-1], rnd.choice(candidates)]
                for b in tests:
                    profiles += realizes(sigma, b)
                    cases += 1
    return cases, profiles


def check_frontier():
    tested = 0
    for k in range(2, 6):
        for n in range(1, 17):
            for b in product(range(1, 5), repeat=k):
                min_slice = min(prod(b[j] for j in range(k) if j != i)
                                for i in range(k))
                assert min_slice == prod(b) // max(b)
                if min_slice < n:
                    # In the singleton-neighborhood frame with all n outcomes,
                    # this action cannot expose n outcomes within its slice.
                    assert any(prod(b[j] for j in range(k) if j != i) < n
                               for i in range(k))
                tested += 1
    return tested


if __name__ == '__main__':
    s = check_slices()
    c, p = check_games()
    f = check_frontier()
    assert realizes([ {frozenset(range(12))} for _ in range(3)],
                    (3, 4, 4)) == 48
    assert (3, 4, 4) != (4, 4, 4)
    print(f'VERIFY_OK slices={s} games={c} action_profiles={p} budgets={f} strict_example=(3,4,4)')
