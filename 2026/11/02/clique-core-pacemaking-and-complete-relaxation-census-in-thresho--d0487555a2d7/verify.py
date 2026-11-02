#!/usr/bin/env python3
"""Finite cohort certificate verifier for three-state threshold-two GHM on split graphs.

Run: python3 verify.py
Only the standard Python library is required. The adjacency condition is independently
implemented in `vertex_step`, while `cohort_step` operates on six initial-color cohorts.
"""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRIPLES = [t for t in itertools.product(range(3), repeat=3) if any(t)]
INITIAL = tuple([0, 1, 2, 0, 1, 2])


def cohort_start(m):
    return tuple(INITIAL[i] if m[i] else -1 for i in range(6))


def cohort_step(m, w):
    # A resting clique vertex does not contribute to the excited-neighbor count.
    # Mass two denotes any mass >= 2, sufficient for the threshold test.
    ec = sum(m[i] for i in range(3) if w[i] == 1)
    ei = sum(m[i] for i in range(3, 6) if w[i] == 1)
    out = []
    for i, color in enumerate(w):
        if color == -1:
            out.append(-1)
        elif color == 1:
            out.append(2)
        elif color == 2:
            out.append(0)
        elif i < 3:
            out.append(int(ec + ei >= 2))
        else:
            out.append(int(ec >= 2))
    return tuple(out)


def calculate(m):
    w = cohort_start(m)
    seen = {}
    trajectory = []
    while w not in seen:
        assert len(trajectory) < 730
        seen[w] = len(trajectory)
        trajectory.append(w)
        w = cohort_step(m, w)
    return (seen[w], len(trajectory) - seen[w], trajectory)


def microscopic_step(x, a):
    # A separate vertex-by-vertex implementation using explicit edge adjacency.
    n = len(x)
    z = []
    for i in range(n):
        if x[i] == 1:
            z.append(2)
        elif x[i] == 2:
            z.append(0)
        else:
            neighbors = (j for j in range(n) if j != i and (i < a or j < a))
            hits = sum(x[j] == 1 for j in neighbors)
            z.append(1 if hits >= 2 else 0)
    return tuple(z)


def microscopic_orbit(x, a):
    visited = {}
    while x not in visited:
        visited[x] = len(visited)
        assert len(visited) <= 25
        x = microscopic_step(x, a)
    return visited[x], len(visited) - visited[x]


def signature(x, a):
    return tuple(min(2, x[:a].count(i)) for i in range(3)) + tuple(
        min(2, x[a:].count(i)) for i in range(3)
    )


def whole_rotation(m):
    u = m[:3]
    v = m[3:]
    return all(
        (not u[j] or u[(j + 1) % 3] + v[(j + 1) % 3] >= 2)
        and (not v[j] or u[(j + 1) % 3] >= 2)
        for j in range(3)
    )


def coefficient_weight(n, t):
    # The coefficient n![z^n] product_j Phi_{min(2,t_j)}(z).
    # Each exact count >=2 represents its entire threshold-equivalent class.
    def comps(n, cap):
        return [k for k in range(n+1) if min(k, 2) == cap]
    result = 0
    for a in comps(n,t[0]):
        for b in comps(n-a,t[1]):
            c = n-a-b
            if min(c,2) == t[2]:
                result += math.factorial(n) // (math.factorial(a)*math.factorial(b)*math.factorial(c))
    return result


def main():
    obj=json.loads((HERE/'certificate.json').read_text(encoding='utf8'))
    cases=obj['cases']
    assert len(cases)==26**2==676
    seen=set(); hist=Counter(); cycles3=[]; longest=[]
    for case in cases:
        m=tuple(case['m']); t,p,path=calculate(m)
        assert m[:3] in TRIPLES and m[3:] in TRIPLES
        assert m not in seen
        seen.add(m)
        assert (t,p)==(case['t'],case['p'])
        assert path==[tuple(v) for v in case['trajectory']]
        assert 0<=t<=5 and p in (1,3)
        assert ((t,p)==(0,3)) == whole_rotation(m)
        hist[(t,p)]+=1
        if t==5: longest.append(m)
        if t==0 and p==3: cycles3.append(m)
    assert len(seen)==676
    assert hist=={(0,1):4,(0,3):53,(1,1):60,(1,3):18,
                  (2,1):240,(2,3):18,(3,1):170,(3,3):18,
                  (4,1):67,(5,1):28}
    assert (2,1,0,0,1,2) in longest
    # Verify that every possible signature supporting a three-cycle has
    # clique minimum size >= 4, with independent minimum >= 2 at size four.
    assert all(sum(m[:3])>=4 and (sum(m[:3])>=5 or sum(m[3:])>=2) for m in cycles3)
    assert (0,2,2,2,0,0) in cycles3
    assert (1,2,2,1,0,0) in cycles3
    # Exhaustively compare quotient trajectories against vertex trajectories.
    microscopic_checked=0
    for a in range(1,9):
        for b in range(1,10-a):
            for x in itertools.product(range(3),repeat=a+b):
                assert microscopic_orbit(x,a)==calculate(signature(x,a))[:2]
                microscopic_checked+=1
    assert microscopic_checked==sum((n-1)*3**n for n in range(2,10))
    # Independent exact counting check using all vertex configurations on small sizes.
    for a,b in ((1,1),(2,3),(3,3),(4,2),(5,1),(4,4)):
        predicted=Counter()
        for m in seen:
            wa=coefficient_weight(a,m[:3]);wb=coefficient_weight(b,m[3:])
            if wa and wb: predicted[calculate(m)[:2]]+=wa*wb
        actual=Counter()
        for x in itertools.product(range(3),repeat=a+b):
            actual[microscopic_orbit(x,a)]+=1
        assert actual==predicted and sum(actual.values())==3**(a+b)
        assert actual.get((0,3),0)%3==0
    print('SPLIT_GHM_THRESHOLD_TWO_ALL_CHECKS_PASSED')
    print('signatures=676; cycle_support=1,3; max_first_periodic_entry=5')
    print('first_entry_period_histogram=',sorted((list(k),v) for k,v in hist.items()))
    print('microscopic_states_exhausted=',microscopic_checked)
    print('composition_count_checks=6; periodic_three_minimal_witnesses=(4,2),(5,1)')

if __name__=='__main__': main()
