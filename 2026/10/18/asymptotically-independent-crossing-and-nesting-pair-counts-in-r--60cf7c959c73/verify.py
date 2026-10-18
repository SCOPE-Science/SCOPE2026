#!/usr/bin/env python3
"""Exact finite matching tests for crossing/nesting pair-count dependence."""
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction as F
from math import comb

def matchings(points):
    if not points:
        yield ()
        return
    a=points[0]
    for j in range(1,len(points)):
        b=points[j]
        for other in matchings(points[1:j]+points[j+1:]):
            yield ((a,b),)+other

def classify(e,f):
    a,b=e; c,d=f
    if a>c:
        a,b,c,d=c,d,a,b
    if a<c<b<d:
        return 'cross'
    if a<c<d<b:
        return 'nest'
    return 'separate'

def counts(m):
    cc=nn=0
    for a,b in combinations(m,2):
        t=classify(a,b)
        cc+=(t=='cross')
        nn+=(t=='nest')
    return cc,nn

asserts=0
for n in range(2,7):
    obs=[counts(m) for m in matchings(tuple(range(2*n)))]
    k=len(obs)
    assert k>0 and k==__import__('math').factorial(2*n)//(2**n*__import__('math').factorial(n))
    xs=[F(a) for a,b in obs];ys=[F(b) for a,b in obs]
    mx=sum(xs)/k;my=sum(ys)/k
    vx=sum((x-mx)**2 for x in xs)/k
    vy=sum((y-my)**2 for y in ys)/k
    cv=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/k
    assert mx==my==F(n*(n-1),6); asserts+=1
    assert vx==vy==F(n*(n-1)*(n+3),45); asserts+=1
    assert cv==F(-n*(n-1),18); asserts+=1
    assert cv/vx==F(-5,2*(n+3)); asserts+=1
    print('n=',n,'matchings=',k,'covariance=',cv,'correlation=',cv/vx)

# Distinguishable chord-endpoint arrangements: all 6! / 2!^3 = 90 distinct words.
words=set(permutations('AABBCC'))
assert len(words)==90
mix=ss=0
for w in words:
    loc={c:[i for i,a in enumerate(w) if a==c] for c in 'ABC'}
    left,right=tuple(loc['A']),tuple(loc['B'])
    ab=classify(left,right)
    ac=classify(left,tuple(loc['C']))
    mix+=(ab=='cross' and ac=='nest')
    ss+=(ab=='cross' and ac=='cross')
assert F(mix,90)==F(1,9);asserts+=1
assert F(ss,90)==F(2,15);asserts+=1
print('three-chord shared probabilities',F(mix,90),F(ss,90))
print('PASS',asserts,'exact group assertions; matched every perfect matching through n=6')
