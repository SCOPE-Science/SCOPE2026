"""Exact finite checks for degree-one vertices in uniformly rooted labeled forests.

Uses independent parent-function enumeration, and finite multinomial/occupancy
recurrences. Run: python forest_verify.py
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product

checks = 0


def root_singleton_law(k, r):
    state = {(k, 0): Fraction(1)}  # (empty boxes, singleton boxes)
    for _ in range(r):
        nxt = defaultdict(Fraction)
        for (empty, single), mass in state.items():
            nxt[(empty - 1, single + 1)] += mass * Fraction(empty, k)
            nxt[(empty, single - 1)] += mass * Fraction(single, k)
            nxt[(empty, single)] += mass * Fraction(k - empty - single, k)
        state = {key: mass for key, mass in nxt.items() if mass}
    law = defaultdict(Fraction)
    for (_, single), mass in state.items():
        law[single] += mass
    return dict(law)


def nonroot_empty_law(m, t):
    state = {m: Fraction(1)}
    for _ in range(t):
        nxt = defaultdict(Fraction)
        for empty, mass in state.items():
            nxt[empty - 1] += mass * Fraction(empty, m)
            nxt[empty] += mass * Fraction(m - empty, m)
        state = {key: mass for key, mass in nxt.items() if mass}
    return state


def predicted_law(k, m, r):
    assert 1 <= r <= m
    roots = root_singleton_law(k, r)
    nonroots = nonroot_empty_law(m, m-r)
    result = defaultdict(Fraction)
    for a, pa in roots.items():
        for b, pb in nonroots.items():
            result[a+b] += pa*pb
    return {x:p for x,p in result.items() if p}


def actual_laws(n, k):
    roots = set(range(k))
    nonroots = list(range(k, n))
    choices = [[i for i in range(n) if i != v] for v in nonroots]
    counts = defaultdict(lambda:defaultdict(int))
    total = 0
    for assigned in product(*choices):
        parent = dict(zip(nonroots, assigned))
        ok = True
        for x in nonroots:
            v = x
            seen = set()
            while v not in roots:
                if v in seen:
                    ok = False
                    break
                seen.add(v)
                v = parent[v]
            if not ok:
                break
        if not ok:
            continue
        total += 1
        outdegree = [0]*n
        for p in assigned:
            outdegree[p] += 1
        root_edges = sum(outdegree[j] for j in roots)
        leaves = sum(outdegree[j] == 1 for j in roots)
        leaves += sum(outdegree[j] == 0 for j in nonroots)
        counts[root_edges][leaves] += 1
    return total, counts


def stoch_increase(low, high):
    return all(sum(p for x, p in high.items() if x >= z)
               >= sum(p for x,p in low.items() if x >= z)
               for z in range(max(max(low),max(high))+2))


for n in range(3, 9):
    for k in range(1, n-1):
        m = n-k
        count, by_root = actual_laws(n,k)
        assert count == k*n**(m-1), (n,k,count)
        checks += 1
        for r in range(1,m+1):
            expected = predicted_law(k,m,r)
            sample_total = sum(by_root[r].values())
            assert sample_total > 0
            obtained = {z:Fraction(num,sample_total) for z,num in by_root[r].items()}
            assert obtained == expected, (n,k,r,obtained,expected)
            checks += len(set(expected)|set(obtained))

for k in range(1,16):
    for m in range(2,19):
        one = predicted_law(k,m,1)
        two = predicted_law(k,m,2)
        assert stoch_increase(one, two) == (m <= 2*k), (k,m)
        checks += 1
        if k >= 2:
            prior = one
            for r in range(1,m):
                after = predicted_law(k,m,r+1)
                mean_before = sum(x*p for x,p in prior.items())
                mean_after = sum(x*p for x,p in after.items())
                assert mean_after > mean_before, (k,m,r)
                checks += 1
                prior = after
            if k <= m-2:
                first = predicted_law(k,m,k)
                next_ = predicted_law(k,m,k+1)
                assert first.get(k+m-1,0) > 0
                assert next_.get(k+m-1,0) == 0
                assert not stoch_increase(first,next_)
                checks += 3
print('PASS:', checks, 'exact assertions')
