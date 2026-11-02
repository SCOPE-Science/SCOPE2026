#!/usr/bin/env python3
"""Independent reduced-atom rank-two profile computation and finite comparisons."""
from itertools import product

def multiply(n,u,v):
    a,s=u; b,t=v
    return ((a + (-1 if s else 1)*b + n*s*t)%(2*n),s^t)

def diagram(n,x,y):
    # Reduced atomic basis; for groups these eight predicates determine all
    # equality and relational-multiplication atoms on 1,x,y.
    one=(0,0)
    return (x==one,y==one,x==y,
            multiply(n,x,x)==one,multiply(n,y,y)==one,
            multiply(n,x,y)==one,
            multiply(n,x,x)==y,multiply(n,y,y)==x)

def types(n):
    els=[(a,s) for a in range(2*n) for s in (0,1)]
    # Each possible first-round element is included; no orbit lemma assumed.
    return frozenset(frozenset(diagram(n,x,y) for y in els) for x in els)

def predicted(n):
    if n<=4:return ('exception',n)
    return ('tail',n%3==0,n%4==0)

if __name__=='__main__':
    reps={}
    for n in range(2,101):
        t=types(n)
        key=predicted(n)
        if key in reps: assert t==reps[key], (n,key,'false equivalence')
        else: reps[key]=t
    assert len(reps)==7
    assert len(set(reps.values()))==7,'classes not pairwise separated'
    print('reduced-basis all-x profiles: n=2..100; groups of order 8..400')
    for k in sorted(reps,key=str):print(str(k))
    print('seven classes: PASS')
