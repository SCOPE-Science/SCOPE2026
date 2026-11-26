#!/usr/bin/env python3
"""Bounded checks of graph-geodesic models and small literal-weight optima."""
from itertools import combinations, product
from functools import lru_cache
from math import factorial
from random import Random


def bits(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length()-1
        mask ^= b


def masks(n, edges):
    d = [[0 if i==j else n for j in range(n)] for i in range(n)]
    for i,j in edges:
        d[i][j] = d[j][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return {(i,j): sum(1<<k for k in range(n) if d[i][k]+d[k][j]==d[i][j])
            for i,j in combinations(range(n),2) if d[i][j]>1}


def pair(i,j):
    return (1<<i)|(1<<j)


def models(n, rules):
    return {x for x in range(1<<n) if all(x&a!=a or x&b==b for a,b in rules)}


def all_valid_rule_optimum(n, closed, known_upper_bound):
    # Model equivalence is weighted set cover of the nonconvex subsets.
    # Enumerate every possible valid nontrivial premise and non-overlapping
    # consequent. An optimal rule never pays for a repeated premise literal.
    nonmodels = [x for x in range(1<<n) if x not in closed]
    full = (1<<len(nonmodels))-1
    accepted = []
    for a in nonmodels:
        h = (1<<n)-1
        for x in closed:
            if x&a==a:
                h &= x
        heads = h ^ a
        b = heads
        while b:
            excludes = sum(1<<i for i,x in enumerate(nonmodels) if x&a==a and x&b!=b)
            assert excludes
            accepted.append((excludes, a.bit_count()+b.bit_count()))
            b = (b-1)&heads
    coverers = [sum(1<<j for j,(c,w) in enumerate(accepted) if c&(1<<i))
                for i in range(len(nonmodels))]

    @lru_cache(None)
    def at_budget(missing, available, budget):
        if not missing:
            return 1
        candidates = min((coverers[i]&available for i in bits(missing)), key=int.bit_count)
        ans = 0
        for j in bits(candidates):
            available ^= 1<<j
            covers, wt = accepted[j]
            if wt <= budget:
                ans += at_budget(missing & ~covers, available, budget-wt)
        return ans

    for budget in range(known_upper_bound+1):
        count = at_budget(full, (1<<len(accepted))-1, budget)
        if count:
            return budget,count
    raise AssertionError('candidate upper bound failed')


def cycle(n):
    I = masks(n, [(i,(i+1)%n) for i in range(n)])
    closed = models(n, [(pair(*p), h) for p,h in I.items()])
    opts = []
    for (i,j),h in I.items():
        a = pair(i,j)
        if 2*(j-i)==n:
            opts.append([(a,pair(u,v)) for u in range(i+1,j) for v in bits((h^a)&~((1<<j)-(1<<i)))])
        else:
            opts.append([(a,1<<w) for w in bits(h^a)])
    cost = 3*len(I)+(0 if n%2 else n//2)
    count = factorial((n-2)//2)**n
    if n%2:
        assert cost==3*n*(n//2-1)
    else:
        assert cost==n*(3*(n//2)-4)
    actual = 1
    for o in opts:
        actual *= len(o)
    assert actual==count
    rng = Random(n)
    selected = product(*opts) if n<=7 else [tuple(rng.choice(o) for o in opts) for _ in range(12)]
    tested = 0
    for rules in selected:
        assert sum(a.bit_count()+b.bit_count() for a,b in rules)==cost
        assert models(n,rules)==closed
        tested += 1
    if n<=5:
        assert all_valid_rule_optimum(n,closed,cost)==(cost,count)
    print('cycle',n,'optimum',cost,'total count',count,'bases model-checked',tested)


def crown(s):
    edges = [(i,s+j) for i in range(s) for j in range(s) if i!=j]
    intervals = masks(2*s,edges)
    closed = models(2*s, [(pair(*p),v) for p,v in intervals.items()])
    if s==4:
        a = pair(0,1)
        h = min((x for x in closed if x&a==a), key=int.bit_count)
        assert h==a|pair(6,7)
        for b in bits(h^a):
            t=a|(1<<b)
            assert [p for p in intervals if t&pair(*p)==pair(*p)]==[(0,1)]
        print('crown',s,'proper four-vertex hull blocks tightness')
        return
    rules = {(pair(i,s+i),1<<((i+1)%s)) for i in range(s)}
    for i,j in combinations(range(s),2):
        h = j if (j-i)%s==1 else i
        rules.add((pair(i,j),1<<(s+h)))
        rules.add((pair(i+s,j+s),1<<i))
    assert len(rules)==len(intervals)==s*s
    assert models(2*s,rules)==closed
    assert len(closed)==2+2*s+s*(s-1)
    print('crown',s,'tight cost',3*len(rules),'all subsets checked',1<<(2*s))


if __name__=='__main__':
    for n in range(3,11):
        cycle(n)
    for s in range(4,8):
        crown(s)
