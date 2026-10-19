#!/usr/bin/env python3
"""Finite corroboration of the binary adjacent-pair spectrum collision theorem."""
from collections import Counter,defaultdict
from math import comb,pi
from itertools import product

def fingerprint(word):
    c=[0,0,0,0]
    for x,y in zip(word,word[1:]): c[2*x+y]+=1
    return tuple(c)

def direct(n):
    hist=Counter(fingerprint(w) for w in product((0,1),repeat=n))
    return sum(v*v for v in hist.values())

def run_sum(n):
    N=n-1
    total=2
    for t in range(1,N//2+1):
        for a in range(N-2*t+1):
            b=N-2*t-a
            z=comb(a+t,t)*comb(b+t-1,t-1)+comb(a+t-1,t-1)*comb(b+t,t)
            total+=z*z
    for t in range((N-1)//2+1):
        for a in range(N-2*t):
            b=N-2*t-1-a
            z=comb(a+t,t)*comb(b+t,t)
            total+=2*z*z
    return total

def transfer(n):
    # Dynamic coefficient extraction in the Fourier transfer matrix, rather than enumeration of words.
    d={(a,a,0,0):1 for a in (0,1)}
    for _ in range(1,n):
        e=defaultdict(int)
        for (start,last,zeros,ones),count in d.items():
            for nxt in (0,1):
                e[start,nxt,zeros+(last==0 and nxt==0),ones+(last==1 and nxt==1)]+=count
        d=e
    outcomes=defaultdict(int)
    for (start,last,zeros,ones),count in d.items():
        outcomes[last-start,zeros,ones]+=count
    return sum(v*v for v in outcomes.values())

for n in range(2,17):
    d=direct(n)
    r=run_sum(n)
    t=transfer(n)
    assert d==r==t,(n,d,r,t)
    if n in (2,3,8,12,16): print('n=%d collisions=%d probability=%.12f'%(n,d,d/(4**n)))

for n in (20,30,60,100,160):
    s=run_sum(n)
    asym=n*s/(4**n)
    print('n=%d n_times_collision_probability=%.12f target=%.12f'%(n,asym,3/(4*pi)))
    assert abs(asym-3/(4*pi))<.025 if n>=60 else True
print('ALL FINITE CHECKS PASSED')
