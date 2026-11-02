#!/usr/bin/env python3
"""Exact checks for the cyclic-drift uniform-refresh birthday law.

Standard-library only. The analytical result is proved separately; these
finite checks test its normalization and path interpretation.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, prod

COUNT=0

def assert_equal(a,b,description):
    global COUNT
    COUNT += 1
    assert a==b, f'{description}: {a} != {b}'

def survival_formula(n,t,q):
    if t >= n:
        return Fraction(0)
    return sum((Fraction(comb(t,k)) * q**k * (1-q)**(t-k)
                * Fraction(prod(n-t+j for j in range(k)),n**k))
               for k in range(t+1))

def survival_direct(n,t,q):
    # All distinct states so far; X_0=0.
    d={(0,1): Fraction(1)}
    for step in range(t):
        e={}
        for (x,mask),p in d.items():
            y=(x+1)%n
            if not (mask & (1<<y)):
                key=(y,mask|1<<y)
                e[key]=e.get(key,Fraction())+p*(1-q)
            for y in range(n):
                if not (mask & (1<<y)):
                    key=(y,mask|1<<y)
                    e[key]=e.get(key,Fraction())+p*q/n
        d=e
    return sum(d.values(),Fraction())

def nonoverlap_count(n,t,reset_indices):
    count=0
    k=len(reset_indices)
    for dests in product(range(n),repeat=k):
        x=0
        seen={0}
        it=iter(dests)
        ok=True
        for s in range(1,t+1):
            x=next(it) if s in reset_indices else (x+1)%n
            if x in seen:
                ok=False
                break
            seen.add(x)
        count+=int(ok)
    return count

def run():
    for n in range(2,8):
        for t in range(n):
            for k in range(t+1):
                expected=prod(n-t+j for j in range(k))
                for reset_indices in combinations(range(1,t+1),k):
                    got=nonoverlap_count(n,t,set(reset_indices))
                    assert_equal(got,expected,('arcs',n,t,reset_indices))
            for q in (Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(3,4),Fraction(1)):
                assert_equal(survival_formula(n,t,q),survival_direct(n,t,q),('walk',n,t,q))
        for q in (Fraction(0),Fraction(1,2),Fraction(1)):
            s=[survival_formula(n,t,q) for t in range(n+1)]
            assert_equal(all(s[j]>=s[j+1] for j in range(n)),True,('time',n,q))
            assert_equal(sum(s[t-1]-s[t] for t in range(1,n+1)),1,('normalization',n,q))
        for t in range(1,n):
            grid=[survival_formula(n,t,Fraction(q,20)) for q in range(21)]
            assert_equal(all(grid[j]>grid[j+1] for j in range(20)),True,('reset-monotone',n,t))
    print(f'PASS: {COUNT} exact comparisons')

if __name__=='__main__':
    run()
