#!/usr/bin/env python3
"""Exact finite verification for two projective-plane coverage-time comparisons.
Only standard-library integer and rational arithmetic is used.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb

checks = 0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def points(q):
    def normalize(v):
        first = next(z for z in v if z != 0)
        inverse = pow(first, -1, q)
        return tuple((z * inverse) % q for z in v)
    return sorted({normalize(v) for v in product(range(q), repeat=3) if any(v)})

def projective_lines(q):
    pts = points(q)
    lines = []
    for a in pts:
        mask = sum(1 << i for i,p in enumerate(pts)
                   if sum(x*y for x,y in zip(a,p)) % q == 0)
        lines.append(mask)
    check(len(pts) == q*q + q + 1, 'point count')
    check(len(set(lines)) == len(pts), 'distinct lines')
    for line in lines:
        check(line.bit_count() == q+1, 'line size')
    for i,j in combinations(range(len(pts)),2):
        check(sum(bool((L >> i)&1 and (L >> j)&1) for L in lines) == 1,
              'every point pair on unique line')
    return lines

def signed_avoidance(lines,n):
    counter=Counter()
    for mask in range(1,1<<n):
        avoided=sum((mask & L)==0 for L in lines)
        counter[avoided]+=1 if mask.bit_count()%2 else -1
    return dict(sorted(counter.items()))

def full_coefficients(n,k):
    c=Counter()
    for s in range(1,n+1):
        r=comb(n-s,k) if n-s>=k else 0
        c[r]+=(-1)**(s+1)*comb(n,s)
    return dict(sorted(c.items()))

def tail(c,n,t):
    if t==0: return Q(1)
    return sum(Q(a*r**t,n**t) for r,a in c.items())

def expectation(c,n):
    return Q(1)+sum(Q(a*r,n-r) for r,a in c.items() if r>0)

def coverage_dp(blocks,n,t):
    counts={0:1}
    for step in range(t):
        nxt=defaultdict(int)
        for mask,ways in counts.items():
            for block in blocks:
                nxt[mask|block]+=ways
        counts=nxt
    return Q(counts.get((1<<n)-1,0),len(blocks)**t)

l2=projective_lines(2)
l3=projective_lines(3)
c2=signed_avoidance(l2,7)
c3=signed_avoidance(l3,13)
f2=full_coefficients(7,3)
f3=full_coefficients(13,4)
check(c2=={0:-6,1:21,2:-21,4:7},'Fano signed line-avoidance spectrum')
check(c3=={0:-38,1:130,2:-78,3:-182,4:234,6:-78,9:13},
      'ternary projective-plane signed line-avoidance spectrum')
check(f2=={0:15,1:-35,4:35,10:-21,20:7},'7-point full spectrum')
check(f3=={0:-220,1:715,5:-1287,15:1716,35:-1716,70:1287,126:-715,
           210:286,330:-78,495:13},'13-point full spectrum')
# Difference:  PG(2,q) tail minus all-size-(q+1)-subsets tail.
for t in range(0,24):
    d2=tail(c2,7,t)-tail(f2,35,t)
    d3=tail(c3,13,t)-tail(f3,715,t)
    if t<=2: check(d2==0,'Fano equal early tail')
    if t>=3: check(d2>0,'Fano strict stochastic domination')
    if t<=3: check(d3==0,'ternary plane equal early tail')
    if t==4: check(d3==Q(-15480,2924207),'ternary negative first tail')
    if t==5: check(d3==Q(2178216,418161601),'ternary positive fifth tail')
    if t==6: check(d3==Q(10152590256,1494927723575),'ternary positive sixth tail')
    if t>=5: check(d3>0,'ternary plane positive later tail')
    if t>=1:
        check(d2==Q(7*(3*5**t-5*4**t+5),35**t), 'Fano closed gap formula')

b7=(Q(234)-286*Q(21,22)**7-182*Q(3,4)**7-78*Q(1,2)**7
    -1287*Q(7,22)**7-1716*Q(3,44)**7-715*Q(1,220)**7)
check(b7==Q(980071992656237,453519616000000),'exact uniform lower bound at t=7')
check(b7>0,'uniform lower bound positive')
for t in range(7,24):
    b=(Q(234)-286*Q(21,22)**t-182*Q(3,4)**t-78*Q(1,2)**t
       -1287*Q(7,22)**t-1716*Q(3,44)**t-715*Q(1,220)**t)
    d=tail(c3,13,t)-tail(f3,715,t)
    check(d / Q(220,715)**t >= b, 'lower-envelope inequality')
    check(b>=b7, 'lower-envelope monotone')

check(expectation(c2,7)==Q(163,30),'published Fano mean')
check(expectation(f2,35)==Q(85691,15810),'published full seven mean')
check(expectation(c3,13)==Q(43633,4620),'published ternary projective-plane mean')
check(expectation(f3,715)==Q(1746879067753,185252315340),'published full thirteen mean')

# A separate time-step recurrence checks the exact inclusion-exclusion identities.
for n,lines,k,c,den,times in [(7,l2,3,c2,7,[3,4]),(13,l3,4,c3,13,[4,5])]:
    for t in times:
        check(coverage_dp(lines,n,t)==1-tail(c,den,t), 'independent projective-plane DP')
for n,k,coeff,den,times in [(7,3,f2,35,[3,4]),(13,4,f3,715,[4,5])]:
    blocks=[sum(1<<i for i in C) for C in combinations(range(n),k)]
    check(len(blocks)==den,'complete full sample support')
    for t in times:
        check(coverage_dp(blocks,n,t)==1-tail(coeff,den,t), 'independent full-model DP')

print('Verified finite-projective-plane tail comparison')
print('PG(2,2) signed avoidance coefficients:',c2)
print('PG(2,3) signed avoidance coefficients:',c3)
print('PG(2,3) delta(4):',tail(c3,13,4)-tail(f3,715,4))
print('PG(2,3) delta(5):',tail(c3,13,5)-tail(f3,715,5))
print('PG(2,3) delta(6):',tail(c3,13,6)-tail(f3,715,6))
print('Positive lower envelope B(7):',b7)
print('Exact assertions passed:',checks)
