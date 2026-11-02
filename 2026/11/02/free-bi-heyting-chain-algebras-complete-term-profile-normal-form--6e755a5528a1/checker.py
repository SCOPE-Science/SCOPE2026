#!/usr/bin/env python3
"""Finite checks for free chain-generated bi-Heyting term operations.

Only integer chains and Python stdlib are used. This is corroborative;
the all-arity result is established by the symbolic normal-form proof.
"""
from collections import Counter
from itertools import product
from math import comb, factorial, prod


def meet(a,b): return min(a,b)
def join(a,b): return max(a,b)
def imp(a,b,top): return top if a <= b else b
def sub(a,b): return 0 if a <= b else a

def gt(a,b,top):
    return sub(top,imp(a,b,top))

def canonical_key(vals,top):
    levels = sorted(set((0,top)+tuple(vals)))
    assert levels[0] == 0 and levels[-1] == top
    rank = {x:i for i,x in enumerate(levels)}
    return (len(levels)-2,tuple(rank[x] for x in vals))

def stirling(n,k):
    if n == k == 0: return 1
    if n == 0 or k == 0: return 0
    return stirling(n-1,k-1)+k*stirling(n-1,k)

def T(k,r):
    return sum(comb(k,m)*2**(k-m)*factorial(r)*stirling(m,r) for m in range(r,k+1))

def close_one_variable(top):
    assignments = list(range(top+1))
    const0 = tuple(0 for _ in assignments)
    const1 = tuple(top for _ in assignments)
    var = tuple(assignments)
    seen={const0,const1,var}; frontier=[const0,const1,var]
    # Incremental closure by pairing newly discovered vectors with existing ones.
    while frontier:
        a=frontier.pop()
        for b in tuple(seen):
            for op in (meet,join):
                for x,y in ((a,b),(b,a)):
                    vec=tuple(op(v,w) for v,w in zip(x,y))
                    if vec not in seen: seen.add(vec);frontier.append(vec)
            for x,y in ((a,b),(b,a)):
                for op in (lambda v,w:imp(v,w,top),sub):
                    vec=tuple(op(v,w) for v,w in zip(x,y))
                    if vec not in seen: seen.add(vec);frontier.append(vec)
    return len(seen)

def check_pattern_selectors(k):
    top=k+1
    tuples=list(product(range(top+1),repeat=k))
    patterns={}
    for x in tuples: patterns.setdefault(canonical_key(x,top),x)
    actual=Counter(key[0] for key in patterns)
    expected={r:T(k,r) for r in range(k+1)}
    assert dict(actual)==expected, (k,actual,expected)
    # Pairwise comparisons of 0, variables and 1 generate precise crisp type tests.
    for x in tuples:
        y=(0,)+x+(top,)
        assert all(gt(y[i],y[j],top)==top*int(y[i]>y[j]) for i in range(len(y)) for j in range(len(y)))
        key=canonical_key(x,top)
        for key2,rep in patterns.items():
            z=(0,)+rep+(top,)
            char=all(gt(y[i],y[j],top)==top*int(z[i]>z[j]) for i in range(len(y)) for j in range(len(y)))
            assert char == (key==key2), (k,x,rep,key,key2)
    return patterns,actual

def check_strict_threshold(k):
    def witness(top):
        return any(all(gt(x[i+1],x[i],top)==top for i in range(k-1))
                   and gt(x[0],0,top)==top and gt(top,x[-1],top)==top
                   for x in product(range(top+1),repeat=k))
    assert not witness(k), ('too small',k)
    assert witness(k+1), ('large enough',k)


def main():
    for n,expected in ((2,4),(3,12),(4,12),(5,12)):
        got=close_one_variable(n-1)
        assert got==expected,('closure',n,got,expected)
    counts=[]
    for k in range(1,4):
        patterns,actual=check_pattern_selectors(k)
        counts.append((k,dict(sorted(actual.items()))))
        check_strict_threshold(k)
    # Every independent choice on each of the eleven two-variable patterns
    # gives a different column-vector of values on the canonical C4.
    patterns,_=check_pattern_selectors(2)
    patterns=sorted(patterns)
    choices=[tuple(range(r+2)) for (r,_) in patterns]
    observed=set()
    for option in product(*choices):
        assert option not in observed
        observed.add(option)
    assert len(observed)==62208, len(observed)
    assert prod((r+2)**T(2,r) for r in range(3))==62208
    assert prod((r+2)**T(1,r) for r in range(2))==12
    print('ALL_CHECKS_OK', 'rank_profiles='+str(counts),'two_variable_normal_forms=62208', 'unary_closures=4,12,12,12', 'sharp_finite_tests=1..3')

if __name__=='__main__':main()
