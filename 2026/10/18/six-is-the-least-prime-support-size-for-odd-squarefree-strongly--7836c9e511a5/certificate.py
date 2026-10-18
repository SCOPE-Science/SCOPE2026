#!/usr/bin/env python3
"""Exact arithmetic certificate: odd squarefree strongly pseudoperfect support bound."""
from math import isqrt, prod
from fractions import Fraction

def prime(n):
    if n<2:return False
    for p in range(2,isqrt(n)+1):
        if n%p==0:return False
    return True

def proper_pair_weights(n):
    return [(d,n//d,d+n//d) for d in range(1,isqrt(n)+1) if n%d==0 and d*d!=n]

def omission_subset(n, desired):
    # Strictly monotone DP: all weights positive and each complementary pair visited once.
    states={0: ()}
    for d,e,w in proper_pair_weights(n):
        for x,sol in tuple(states.items()):
            if x+w<=desired and x+w not in states:
                states[x+w]=sol+((d,e),)
    return states.get(desired)

# For odd squarefree 5-prime support, abundance forces (3,5,7,r,s).
# The fourth prime must be one of 11,13,17,19, and s <= floor[64(r+1)/(6r-64)].
# Each of the four larger alternative five-prime starting tuples is deficient.
for leading in ((5,7,11,13,17),(3,7,11,13,17),(3,5,11,13,17),(3,5,7,23,29)):
    h=prod(Fraction(p+1,p) for p in leading)
    assert h < 2, (leading,h)

r_limits={r:64*(r+1)//(6*r-64) for r in (11,13,17,19)}
assert r_limits == {11:384,13:64,17:30,19:25}
byr={};eligible={};solns=[];max_delta=0
for r,smax in r_limits.items():
    ps=[s for s in range(r+1,smax+1) if prime(s)]
    byr[r]=len(ps)
    eligible[r]=0
    for s in ps:
        n=3*5*7*r*s
        delta=4*6*8*(r+1)*(s+1)-2*n
        assert delta>=0
        if n%4==3:continue
        eligible[r]+=1
        max_delta=max(max_delta,delta)
        omitted=omission_subset(n,delta)
        if omitted is not None:solns.append((n,omitted))
assert byr == {11:71,13:12,17:3,19:1},byr
assert eligible == {11:37,13:6,17:1,19:1},eligible
assert sum(byr.values())==87 and sum(eligible.values())==45
assert not solns,solns

# The same exact omission criterion checks the six-support witness n=937365.
n=937365
ps=(3,5,11,13,19,23)
assert prod(ps)==n and all(prime(p) for p in ps)
delta=prod(p+1 for p in ps)-2*n
omitted=omission_subset(n,delta)
assert omitted is not None,(n,delta)
assert sum(d+e for d,e in omitted)==delta
assert len(proper_pair_weights(n))==32
print('sub-5-support maximal abundancies checked')
print('candidate counts by fourth prime:',byr)
print('admissible modulo 4:',eligible)
print('all 45 exact complementary-pair subset-sum problems: UNSAT')
print('max deficiency:',max_delta)
print('six-prime witness:',n,'sigma minus twice n:',delta)
print('omitted complementary pairs:',omitted)
print('verification: PASS')
