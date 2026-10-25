"""Independent finite checks for the mathematical identities in RESULT.md.
Uses Python 3 standard library; finite checks do not prove asymptotic claims.
"""
from itertools import combinations, permutations
from fractions import Fraction
from math import comb, exp, log, sqrt
import random

def falling(n,k):
    if k>n: return 0
    r=1
    for j in range(k): r*=n-j
    return r

def delta(values, labels):
    n=len(values)
    full=max(values)-min(values)
    restricted=max(abs(values[i]-values[j]) for i in range(n) for j in range(i+1,n) if labels[i]!=labels[j])
    return full-restricted

def cap_count(values,h):
    hi=max(values); lo=min(values)
    return sum((v>=hi-h or v<=lo+h) for v in values)

def assignments(counts):
    n=sum(counts)
    def rec(rest,used,prefix):
        if not rest:
            yield tuple(prefix)
        else:
            c=rest[0]
            for chosen in combinations(range(n),c):
                if not set(chosen).isdisjoint(used):continue
                a=prefix[:]
                for j in chosen:a[j]=len(counts)-len(rest)
                yield from rec(rest[1:],used|set(chosen),a)
    yield from rec(counts,set(),[-1]*n)

checks=0
for counts in [(2,1,1),(2,2,1),(3,2,1),(3,2,2),(2,2,2)]:
    n=sum(counts);values=[-3.2+6.7*i/(n-1) for i in range(n)]
    configs=list(assignments(counts))
    assert len(configs)>0
    for h in [0.,.17,.58,1.1,2.2,6.5]:
        k=cap_count(values,h)
        actual=Fraction(sum(delta(values,a)>h+1e-9 for a in configs),len(configs))
        predicted=Fraction(sum(falling(c,k) for c in counts),falling(n,k))
        assert actual==predicted,(counts,h,k,actual,predicted)
        checks+=1

transfers=0
for n in range(5,20):
    for p in range(2,n-1):
        for q in range(2,min(p,n-p)+1):
            if p+q>n-1: continue
            # At least three nonempty blocks: residual n-p-q >0.
            for k in range(2,n+1):
                old=falling(p,k)+falling(q,k)
                new=falling(p+1,k)+falling(q-1,k)
                assert new>=old,(p,q,k)
                if k==2:assert new>old
                transfers+=1

# Exact integration of limiting survival, via Simpson's rule.
def survival(t,p):
    z=exp(t)
    return sum((v/(v+(1-v)*z))**2 for v in p)
for props in [(0.5,0.3,0.2),(0.25,0.25,0.25,0.25),(0.9,0.05,0.05)]:
    steps=60000;h=40/steps
    sm=survival(0,props)+survival(40,props)
    for k in range(1,steps):
        sm+=(4 if k%2 else 2)*survival(k*h,props)
    numeric=h*sm/3
    closed=-1-sum(log(1-v) for v in props)
    assert abs(numeric-closed)<1e-8,(props,numeric,closed)
    assert abs(survival(0,props)-sum(v*v for v in props))<1e-12
    checks+=1

# Brute graph max, rather than rank-cap identity, for finite Gaussian sample.
rng=random.Random(192643)
counts=(3,3,4);n=sum(counts);fixed_labels=tuple(j for c,v in enumerate(counts) for j in [c]*v)
positive=0;M=6000
for z in range(M):
    x=[rng.gauss(0,1) for _ in range(n)]
    d=delta(x,fixed_labels)
    assert d>=-1e-12
    if d>1e-10:positive+=1
want=sum(c*(c-1) for c in counts)/(n*(n-1))
assert abs(positive/M-want)<0.025,(positive/M,want)
print(f'VERIFY_OK exact_conditional_cases={checks} transfer_cases={transfers} montecarlo={M} positive_fraction={positive/M:.5f} expected={want:.5f}')
