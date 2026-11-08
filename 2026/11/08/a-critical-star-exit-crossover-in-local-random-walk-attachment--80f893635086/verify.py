#!/usr/bin/env python3
"""Exact, independent finite checks for star-exit law in locally sampled attachment.
Standard library only; does not replace the proof for unbounded graph sizes.
"""
from fractions import Fraction
from math import factorial, prod

checks=0

def check(condition, note=''):
    global checks
    assert condition, note
    checks += 1


def star(adj):
    n=len(adj)
    return n>=3 and sorted(map(len,adj)) == [1]*(n-1)+[n-1]


def attachment(adj, target):
    new=[set(x) for x in adj]
    new.append({target})
    new[target].add(len(adj))
    return tuple(frozenset(x) for x in new)


def all_successors(adj,q):
    """Enumerate starting vertices and their walk outcomes directly."""
    n=len(adj)
    result=[]
    for u in range(n):
        if q:
            result.append((attachment(adj,u),q/n))
        if q<1:
            for v in adj[u]:
                result.append((attachment(adj,v),(1-q)/Fraction(n*len(adj[u]))))
    check(sum((p for _,p in result),Fraction(0))==1)
    return result


def survival_by_graph(s,q,t):
    adj=tuple(frozenset(range(1,s+1)) if i==0 else frozenset([0]) for i in range(s+1))
    states={adj:Fraction(1)}
    for _ in range(t):
        nxt={}
        for g,prob in states.items():
            for h,p in all_successors(g,q):
                if star(h):
                    nxt[h]=nxt.get(h,Fraction(0))+prob*p
        states=nxt
    return sum(states.values(),Fraction(0))


def formula(s,q,t):
    v=Fraction(1)
    for j in range(s,s+t):
        v*=Fraction(j)*(1-q)/Fraction(j+1)+q/Fraction(j+1)
    return v


def fixed_q_bound(s,q,t):
    f=formula(s,q,t)
    base=Fraction(s,s+t)
    return base*(1-q)**t <= f <= base*(1-q*(1-Fraction(1,s)))**t

for s in range(2,7):
    for q in (Fraction(0),Fraction(1,7),Fraction(1,2),Fraction(4,5),Fraction(1)):
        for t in range(0,8):
            check(survival_by_graph(s,q,t)==formula(s,q,t),('graph comparison',s,q,t))
            check(fixed_q_bound(s,q,t),('tail bounds',s,q,t))
            if q==0:
                check(formula(s,q,t)==Fraction(s,s+t))
            if q==1:
                check(formula(s,q,t)==Fraction(factorial(s),factorial(s+t)))

# Independent recurrence and the Gamma-factor product with integer alpha=q/(1-q).
for s in range(2,9):
    for a in range(0,8):
        q=Fraction(a,a+1)
        for t in range(0,60):
            rhs=Fraction(1,(a+1)**t)*Fraction(prod(range(s+a,s+a+t)),prod(range(s+1,s+1+t)))
            check(formula(s,q,t)==rhs,('integer alpha',s,a,t))

for s in range(2,13):
    for t in range(1,15):
        check(formula(s,Fraction(0),t)>formula(s,Fraction(1,5),t)>formula(s,Fraction(1),t))

print('PASS',checks,'exact assertions')
