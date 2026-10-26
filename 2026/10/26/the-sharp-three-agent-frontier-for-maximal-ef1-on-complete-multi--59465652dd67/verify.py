#!/usr/bin/env python3
"""Reproduce the complete-multipartite maximal-EF1 construction tests.

Run: python3 verify.py
No external modules or data are required.
"""
from itertools import product
from random import Random


def allocate(parts):
    """Return three bundles of item indices, or raise on invalid input."""
    data = []
    for part, weights in enumerate(parts):
        if any(w < 0 for w in weights):
            raise ValueError('negative weights are outside the theorem')
        data.append([(part, j, w) for j, w in enumerate(weights)])
    bundles = [[], [], []]
    large = next((part for part in data if len(part) >= 3), None)
    if large is not None:
        loads = [0, 0, 0]
        for item in large:
            k = min(range(3), key=lambda i: (loads[i], bool(bundles[i]), i))
            bundles[k].append(item)
            loads[k] += item[2]
    else:
        doublets = [part for part in data if len(part) == 2]
        if doublets:
            focus = max(doublets, key=lambda part: min(x[2] for x in part))
            bundles[0] = [focus[0]]
            bundles[1] = [focus[1]]
            other = next((part for part in data if part is not focus and part), None)
            if other is not None:
                bundles[2] = list(other)
        else:
            for i, part in enumerate(data[:3]):
                bundles[i] = list(part)
    return bundles


def check(parts, bundles):
    universe = {(p, j, w) for p, vs in enumerate(parts) for j, w in enumerate(vs)}
    assigned = [item for bundle in bundles for item in bundle]
    assert len(set(assigned)) == len(assigned) and set(assigned) <= universe
    assert all(len({x[0] for x in bundle}) <= 1 for bundle in bundles), 'infeasible independent set'
    residual = universe - set(assigned)
    for item in residual:
        for bundle in bundles:
            assert any(x[0] != item[0] for x in bundle), 'not maximal'
    values = [sum(item[2] for item in bundle) for bundle in bundles]
    for i in range(3):
        for j in range(3):
            after_one = values[j] - max((item[2] for item in bundles[j]), default=0)
            assert values[i] >= after_one, 'violates EF1'
    return True


def integer_partitions(n, lo=1):
    if n == 0:
        yield ()
    for k in range(lo, n + 1):
        for rest in integer_partitions(n - k, k):
            yield (k,) + rest


def exhaustive():
    total = 0
    branches = {'large': 0, 'doubleton': 0, 'singleton': 0}
    for m in range(0, 9):
        for shape in integer_partitions(m):
            for weights in product(range(3), repeat=m):
                parts = []
                j = 0
                for size in shape:
                    parts.append(tuple(weights[j:j+size]))
                    j += size
                result = allocate(parts)
                check(parts, result)
                branch = 'large' if any(len(x) >= 3 for x in parts) else ('doubleton' if any(len(x) == 2 for x in parts) else 'singleton')
                branches[branch] += 1
                total += 1
    return total, branches


def randomized():
    rng = Random(20261022)
    for _ in range(6000):
        n = rng.randint(0, 80)
        parts = []
        while n:
            sz = rng.randint(1, n)
            parts.append(tuple(rng.randint(0, 100000) for _ in range(sz)))
            n -= sz
        check(parts, allocate(parts))
    return 6000


def four_agent_counterexample():
    """Recheck the established 4-agent K(3,3) contrast by complete search."""
    weights = (2, 2, 2, 3, 3, 3)
    p = (0, 0, 0, 1, 1, 1)
    count_maximal = 0
    for assignment in product(range(5), repeat=6):
        bundles = [[j for j, agent in enumerate(assignment) if agent == i] for i in range(4)]
        if any(len({p[j] for j in bundle}) > 1 for bundle in bundles):
            continue
        leftover = [j for j, agent in enumerate(assignment) if agent == 4]
        if any(any(all(p[j] == p[g] for g in bundle) for bundle in bundles) for j in leftover):
            continue
        count_maximal += 1
        totals = [sum(weights[j] for j in bundle) for bundle in bundles]
        if all(totals[i] >= totals[j] - max((weights[g] for g in bundles[j]), default=0)
               for i in range(4) for j in range(4)):
            raise AssertionError('unexpected four-agent maximal EF1 allocation')
    return count_maximal




def monotone_construct(parts, value):
    """Construct for one common normalized monotone set valuation."""
    groups = []
    offset = 0
    for p in parts:
        groups.append(list(range(offset, offset + p)))
        offset += p
    bundles = [[], [], []]
    big = next((g for g in groups if len(g) >= 3), None)
    if big is not None:
        for good in big:
            k = min(range(3), key=lambda i: (value(bundles[i]), bool(bundles[i]), i))
            bundles[k].append(good)
    else:
        doubles = [g for g in groups if len(g) == 2]
        if doubles:
            a = max(doubles, key=lambda g: min(value([g[0]]), value([g[1]])))
            bundles[0], bundles[1] = [a[0]], [a[1]]
            b = next((g for g in groups if g is not a and g), None)
            if b is not None:
                bundles[2] = list(b)
        else:
            for i, group in enumerate(groups[:3]):
                bundles[i] = list(group)
    return bundles


def monotone_verify(parts, value, bundles):
    size = sum(parts)
    groups = [next((i for i, acc in enumerate([sum(parts[:j+1]) for j in range(len(parts))]) if k < acc), -1) for k in range(size)]
    flat = [g for B in bundles for g in B]
    assert all(0 <= g < size for g in flat) and len(flat) == len(set(flat))
    assert all(len({groups[g] for g in B}) <= 1 for B in bundles)
    for item in range(size):
        if item not in flat:
            assert all(any(groups[g] != groups[item] for g in B) for B in bundles)
    for i in range(3):
        for j in range(3):
            assert not bundles[j] or any(value(bundles[i]) >= value([x for x in bundles[j] if x != item]) for item in bundles[j])
    return True


def monotone_trials():
    rng = Random(29471)
    trials = 0
    for m in range(0, 9):
        for _ in range(450):
            n = m
            parts = []
            while n:
                k = rng.randint(1, n)
                parts.append(k)
                n -= k
            # v(S) = max { base(T): T subseteq S }; this spans all monotone set functions.
            base = [0] + [rng.randint(0, 100) for _ in range((1 << m) - 1)]
            vals = base[:]
            for bit in range(m):
                for mask in range(1 << m):
                    if mask & (1 << bit):
                        vals[mask] = max(vals[mask], vals[mask ^ (1 << bit)])
            def value(seq):
                mask = 0
                for g in seq:
                    mask |= 1 << g
                return vals[mask]
            monotone_verify(parts, value, monotone_construct(parts, value))
            trials += 1
    # All monotone Boolean functions on four labeled goods.
    m = 4
    for bits in range(1 << (1 << m)):
        if bits & 1:
            continue
        truth = [((bits >> mask) & 1) for mask in range(1 << m)]
        if any(truth[mask] > truth[mask | (1 << i)] for mask in range(1 << m) for i in range(m) if not (mask & (1 << i))):
            continue
        for shape in integer_partitions(m):
            def value(seq):
                mask = 0
                for g in seq:
                    mask |= 1 << g
                return truth[mask]
            monotone_verify(shape, value, monotone_construct(shape, value))
            trials += 1
    return trials

if __name__ == '__main__':
    total, breakdown = exhaustive()
    random_count = randomized()
    bad4 = four_agent_counterexample()
    monotone_count = monotone_trials()
    print('PASS exhaustive', total, 'instances; branch counts', breakdown)
    print('PASS randomized', random_count, 'instances')
    print('PASS common monotone set valuation', monotone_count, 'instances')
    print('PASS four-agent K(3,3) contrast;', bad4, 'maximal allocations, none EF1')
