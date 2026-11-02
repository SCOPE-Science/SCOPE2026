"""Exact finite checks for cyclic-vertex perturbations in fixed-indegree random mappings.

Run: python verify_mapping.py
Only the finite instances stated below are enumerated; the all-size theorem has a separate proof.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def e_polynomial(v):
    e = [1] + [0] * len(v)
    for x in v:
        for j in range(len(v), 0, -1):
            e[j] += x * e[j - 1]
    return e


def tails(v):
    n = len(v)
    e = e_polynomial(v)
    return [Fraction(1)] + [Fraction(e[k], comb(n, k)) for k in range(1, n + 1)] + [Fraction(0)]


def masses(v):
    t = tails(v)
    return [t[k] - t[k + 1] for k in range(1, len(v) + 1)]


def positive_compositions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
    else:
        for i in range(min(maxpart, n), 0, -1):
            for tail in positive_compositions(n - i, i):
                yield (i,) + tail


def degree_profiles(n):
    for p in positive_compositions(n):
        yield p + (0,) * (n - len(p))


def component_count(f):
    n = len(f)
    indeg = [0] * n
    for dest in f:
        indeg[dest] += 1
    todo = [i for i in range(n) if indeg[i] == 0]
    while todo:
        x = todo.pop()
        y = f[x]
        indeg[y] -= 1
        if indeg[y] == 0:
            todo.append(y)
    unseen = {i for i in range(n) if indeg[i] > 0}
    c = 0
    while unseen:
        c += 1
        x = next(iter(unseen))
        while x in unseen:
            unseen.remove(x)
            x = f[x]
    return c


def stirling_kernel(n):
    unsigned = [[0] * (n + 1) for _ in range(n + 1)]
    unsigned[0][0] = 1
    for k in range(1, n + 1):
        for j in range(1, k + 1):
            unsigned[k][j] = unsigned[k - 1][j - 1] + (k - 1) * unsigned[k - 1][j]
    return [[Fraction(unsigned[k][j], factorial(k)) for j in range(n + 1)]
            for k in range(n + 1)]


def component_masses(d):
    n = len(d)
    K = stirling_kernel(n)
    p = masses(d)
    return [sum(p[k-1] * K[k][j] for k in range(1, n + 1)) for j in range(1, n + 1)]


def count_cyclic(f):
    n = len(f)
    indeg = [0] * n
    for dest in f:
        indeg[dest] += 1
    todo = [i for i in range(n) if indeg[i] == 0]
    while todo:
        x = todo.pop()
        y = f[x]
        indeg[y] -= 1
        if indeg[y] == 0:
            todo.append(y)
    return sum(d > 0 for d in indeg)


def verify():
    checks = 0
    full_mappings = 0
    vectors = 0
    transfers = 0
    for n in range(2, 8):
        hist = defaultdict(lambda: [0] * (n + 1))
        component_hist = defaultdict(lambda: [0] * (n + 1))
        for f in product(range(n), repeat=n):
            d = [0] * n
            for v in f:
                d[v] += 1
            hist[tuple(d)][count_cyclic(f)] += 1
            component_hist[tuple(d)][component_count(f)] += 1
            full_mappings += 1
        for d, by_cyclic in hist.items():
            total = sum(by_cyclic)
            expected = masses(d)
            for k in range(1, n + 1):
                assert Fraction(by_cyclic[k], total) == expected[k - 1], (n, d, k)
                checks += 1
            expected_components = component_masses(d)
            for k in range(1, n + 1):
                assert Fraction(component_hist[d][k], total) == expected_components[k - 1]
                checks += 1
            vectors += 1

    lr_fail_at_5 = False
    for n in range(2, 12):
        any_lr_failure = False
        for d in degree_profiles(n):
            t0 = tails(d)
            p0 = masses(d)
            for i in range(n):
                for j in range(n):
                    if d[i] < d[j] + 2:
                        continue
                    h = d[i] - d[j] - 1
                    new = list(d)
                    new[i] -= 1
                    new[j] += 1
                    t1 = tails(new)
                    p1 = masses(new)
                    z0 = component_masses(d)
                    z1 = component_masses(new)
                    rest = [d[k] for k in range(n) if k not in (i, j)]
                    e = e_polynomial(rest)
                    delta = [Fraction(0)] * (n + 2)
                    for k in range(2, n + 1):
                        delta[k] = Fraction(h * e[k - 2], comb(n, k))
                        assert t1[k] - t0[k] == delta[k], (d, new, k)
                        checks += 1
                    signs = []
                    for k in range(1, n + 1):
                        dp = p1[k - 1] - p0[k - 1]
                        assert dp == delta[k] - delta[k + 1]
                        checks += 1
                        if dp:
                            signs.append(1 if dp > 0 else -1)
                    assert signs and signs[0] == -1 and signs[-1] == 1 and signs == sorted(signs)
                    checks += 1
                    assert sum(abs(x - y) for x, y in zip(p0, p1)) / 2 == max(delta)
                    checks += 1
                    comp_signs = [1 if y > x else -1 for x, y in zip(z0, z1) if x != y]
                    assert comp_signs == sorted(comp_signs) and comp_signs[0] == -1 and comp_signs[-1] == 1
                    checks += 1
                    assert sum(abs(x - y) for x, y in zip(z0, z1)) <= sum(abs(x - y) for x, y in zip(p0, p1))
                    checks += 1
                    t = n - d[i] - d[j]
                    bound = h * max(Fraction(comb(t, k), comb(n, k + 2)) for k in range(t + 1))
                    assert max(delta) <= bound
                    checks += 1
                    if all(x in (0, 1) for x in rest):
                        assert max(delta) == bound
                        checks += 1
                    # Likelihood-ratio order p0 -> p1 requires p1(k)/p0(k)
                    # to be nondecreasing wherever p0 is nonzero.
                    fail = any(p1[k] * p0[l] > p1[l] * p0[k]
                               for k in range(n) for l in range(k + 1, n))
                    if fail:
                        any_lr_failure = True
                    checks += 1
                    transfers += 1
        if n < 5:
            assert not any_lr_failure
        if n == 5:
            lr_fail_at_5 = any_lr_failure
    assert lr_fail_at_5
    a = (3, 2, 0, 0, 0)
    b = (3, 1, 1, 0, 0)
    assert masses(a) == [Fraction(2, 5), Fraction(3, 5), Fraction(0), Fraction(0), Fraction(0)]
    assert masses(b) == [Fraction(3, 10), Fraction(2, 5), Fraction(3, 10), Fraction(0), Fraction(0)]
    assert masses(b)[0] * masses(a)[1] > masses(b)[1] * masses(a)[0]
    checks += 4
    print('PASS', 'exact_assertions='+str(checks), 'enumerated_mappings='+str(full_mappings),
          'distinct_labeled_indegrees='+str(vectors), 'elementary_transfers='+str(transfers),
          'exhaustive_mapping_n=2..7', 'transfer_partitions_n=2..11',
          'LR_first_counterexample_n=5')


if __name__ == '__main__':
    verify()
