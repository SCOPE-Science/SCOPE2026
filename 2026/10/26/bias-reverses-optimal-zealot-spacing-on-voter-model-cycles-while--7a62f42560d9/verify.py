#!/usr/bin/env python3
"""Exact checks for the biased two-zealot cycle voter model.

Run with standard Python 3. No external packages are required.
"""
from collections import defaultdict, deque
from fractions import Fraction
import json


def z(length, ratio):
    return sum((ratio ** j for j in range(length)), Fraction())


def mean(length, ratio):
    return sum((j * ratio ** j for j in range(length)), Fraction()) / z(length, ratio)


def pmf(n, a, ratio):
    b = n - a
    out = defaultdict(Fraction)
    for i in range(a):
        for j in range(b):
            out[1 + i + j] += ratio ** (i + j) / (z(a, ratio) * z(b, ratio))
    return out


def configuration(n, a, i, j):
    x = [None] * n
    x[0] = 1
    x[a] = 0
    for h in range(1, a):
        x[h] = int(h <= i)
    for h in range(1, n-a):
        x[n-h] = int(h <= j)
    return tuple(x)


def full_stationarity(n, a, plus, minus):
    r = Fraction(plus, minus)
    free = [v for v in range(n) if v not in (0, a)]
    states = []
    for code in range(1 << len(free)):
        x = [None] * n
        x[0], x[a] = 1, 0
        for idx, v in enumerate(free):
            x[v] = (code >> idx) & 1
        states.append(tuple(x))
    index = {state: i for i, state in enumerate(states)}
    weights = {}
    den = z(a, r) * z(n-a, r)
    for i in range(a):
        for j in range(n-a):
            weights[configuration(n, a, i, j)] = r ** (i+j) / den
    assert len(weights) == a*(n-a)
    assert sum(weights.values()) == 1
    generator_balance = [Fraction() for _ in states]
    reversed_edges = [[] for _ in states]
    edge_count = 0
    for x in states:
        u = index[x]
        for v in free:
            for w in ((v-1)%n, (v+1)%n):
                if x[v] == x[w]:
                    continue
                y = list(x)
                y[v] = x[w]
                y = tuple(y)
                t = index[y]
                rate = plus if x[w] == 1 else minus
                generator_balance[t] += weights.get(x, Fraction()) * rate
                generator_balance[u] -= weights.get(x, Fraction()) * rate
                reversed_edges[t].append(u)
                edge_count += 1
    assert all(v == 0 for v in generator_balance)
    reached = {index[x] for x in weights}
    q = deque(reached)
    while q:
        for s in reversed_edges[q.popleft()]:
            if s not in reached:
                reached.add(s)
                q.append(s)
    assert len(reached) == len(states)
    dist = pmf(n, a, r)
    direct = defaultdict(Fraction)
    for x, w in weights.items():
        direct[sum(x)] += w
    assert dict(dist) == dict(direct)
    assert sum(Fraction(k)*w for k, w in dist.items()) == 1+mean(a,r)+mean(n-a,r)
    assert dist[1] == 1/den
    assert dist[n-1] == r**(n-2)/den
    return len(states), len(weights), edge_count


def placement_checks(n, r):
    data = [(a,pmf(n,a,r),mean(a,r)+mean(n-a,r)) for a in range(1,n//2+1)]
    for (a,x,m),(b,y,mm) in zip(data,data[1:]):
        assert b==a+1
        if r>1:
            assert m>mm
        elif r<1:
            assert m<mm
        else:
            assert m==mm
        assert x[1]>y[1]
        assert x[n-1]>y[n-1]
    assert all(sum(w.values())==1 for a,w,m in data)
    if r==1:
        assert all(m==Fraction(n-2,2) for a,w,m in data)
    return max(0,len(data)-1)


def run():
    count={'full_generators':0,'full_states':0,'full_stationary_support_states':0,
           'full_directed_flips':0,'placement_comparisons':0,'pmf_mass_cases':0}
    for n in range(3,10):
        for a in range(1,n):
            for plus,minus in ((1,1),(1,2),(2,1),(3,2),(2,3)):
                states,support,flips = full_stationarity(n,a,plus,minus)
                count['full_generators']+=1
                count['full_states']+=states
                count['full_stationary_support_states']+=support
                count['full_directed_flips']+=flips
    for n in range(4,41):
        for r in (Fraction(1,5),Fraction(2,3),Fraction(1),Fraction(3,2),Fraction(4)):
            count['placement_comparisons']+=placement_checks(n,r)
            count['pmf_mass_cases']+=1
    print(json.dumps({'status':'passed','checks':count,'parameters':{
        'full_generator_order': '3 through 9 vertices; every zealot spacing',
        'full_generator_persuasion_ratios':'1, 1/2, 2, 3/2, 2/3',
        'placement_order':'4 through 40 vertices',
        'placement_ratios':'1/5, 2/3, 1, 3/2, 4',
        'arithmetic':'exact rational; full generator balances, full-state reachability and distributions'}},sort_keys=True,indent=2))

if __name__=='__main__':
    run()
