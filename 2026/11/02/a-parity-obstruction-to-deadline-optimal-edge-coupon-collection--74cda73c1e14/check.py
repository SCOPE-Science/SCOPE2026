#!/usr/bin/env python3
"""Exact finite checks for edge-drawing coverage design; stdlib only.

Finite checks illustrate the universal analytic arguments and do not replace them.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial
from random import Random

CHECKS=0

def verify(condition, description=''):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(description or f'check {CHECKS} failed')

def cover_prob(n,edges,weights,t):
    assert sum(weights)==1 and len(edges)==len(weights)
    states={0:Q(1)}
    target=(1<<n)-1
    for _ in range(t):
        nxt={}
        for mask,pm in states.items():
            for (u,v),w in zip(edges,weights):
                if w:
                    nm=mask | (1<<u) | (1<<v)
                    nxt[nm]=nxt.get(nm,Q(0))+pm*w
        states=nxt
    return states.get(target,Q(0))

def coupon_prob(b,t):
    # P(all b categories seen after t draws), Stirling recurrence
    vals=[0]*(b+1);vals[0]=1
    for _ in range(t):
        nxt=[0]*(b+1)
        for k in range(b+1):
            nxt[k]+=k*vals[k]
            if k<b: nxt[k+1]+=(k+1)*vals[k]  # surjection count recurrences times binomial counts
        vals=nxt
    # above counts onto maps into individual selected categories: b! S(t,b)
    return Q(vals[b],b**t)

def bipartite(a,b):
    return [(i,a+j) for i in range(a) for j in range(b)]

def cycle(n):
    return [(i,(i+1)%n) for i in range(n)]

def min_edgecovers(n,edges):
    min_size=(n+1)//2
    return [s for s in combinations(range(len(edges)),min_size) if len({v for j in s for v in edges[j]})==n]

rng=Random(41248)
for a,b in [(2,2),(2,3),(2,4),(3,3),(3,4)]:
    edges=bipartite(a,b)
    for t in range(b,b+5):
        target=coupon_prob(b,t)
        # sample matching saturating the smaller part, plus distinct matches for all B
        chosen=[i%a for i in range(b)]
        ws=[Q(0) for _ in edges]
        for j,i in enumerate(chosen): ws[i*b+j]=Q(1,b)
        verify(cover_prob(a+b,edges,ws,t)==target,f'optimal bipartite a={a} b={b} t={t}')
        for r in range(8):
            ints=[rng.randint(0,11) for _ in edges]
            if not any(ints): ints[0]=1
            q=[Q(k,sum(ints)) for k in ints]
            verify(cover_prob(a+b,edges,q,t)<=target,f'nonoptimal b={b} t={t}')
        # uniform whole graph test
        verify(cover_prob(a+b,edges,[Q(1,len(edges))]*len(edges),t)<=target)

# Direct independent enumeration of small odd-cycle minimum covers.
for n in [7,9,11,13]:
    m=(n-1)//2
    edges=cycle(n)
    covers=min_edgecovers(n,edges)
    verify(len(covers)==n,f'count minimum edge covers C{n}')
    k=m+1
    first_uniform=Q(factorial(k),n**m)
    sparse=Q(factorial(k),k**k)
    verify(sparse>first_uniform,f'odd C{n} first deadline strict')
    if n<=9:
        uniform=[Q(1,n)]*n
        inds=set(covers[0]); support=[Q(1,k) if j in inds else Q(0) for j in range(n)]
        verify(cover_prob(n,edges,uniform,k)==first_uniform)
        verify(cover_prob(n,edges,support,k)==sparse)
        # The uniform design gains at late deadlines (n=7,9)
        t=180
        verify(cover_prob(n,edges,uniform,t)>cover_prob(n,edges,support,t),f'late deadline C{n}')

# Test strict uniform vertex marginals for odd cycles.
for n in [7,9,11]:
    for r in range(100):
        ints=[rng.randint(0,10) for _ in range(n)]
        if not any(ints): ints[0]=1
        p=[Q(x,sum(ints)) for x in ints]
        hazards=[p[(i-1)%n]+p[i] for i in range(n)]
        verify(sum(hazards)==2)
        if p!=[Q(1,n)]*n:verify(min(hazards)<Q(2,n))

print(f'OK: {CHECKS} exact-rational checks')
