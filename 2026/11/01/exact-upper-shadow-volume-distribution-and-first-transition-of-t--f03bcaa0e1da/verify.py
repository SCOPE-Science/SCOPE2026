"""Reproducible finite diagnostics for the 24-cell's upper brightness tail.

The accompanying argument proves the formula; Monte Carlo is supplementary.
Requires Python 3.10+ standard library only.
"""
from collections import Counter
from itertools import permutations, product
from math import acos, asin, pi, sqrt
from random import Random

centers = sorted({tuple(p[i] * s[i] for i in range(4))
                  for p in permutations((3, 2, 1, 0))
                  for s in product((-1, 1), repeat=4)})
assert len(centers) == 192

def dot(v, w):
    return sum(x*y for x, y in zip(v, w))

pairs = Counter(dot(v, w) for i, v in enumerate(centers)
                for w in centers[i+1:])
assert sum(pairs.values()) == 192*191//2
assert max(pairs) == 13 and pairs[13] == 384
assert sorted(pairs, reverse=True)[:2] == [13, 12]
adj = [{j for j in range(192) if i != j and dot(centers[i], centers[j]) == 13}
       for i in range(192)]
assert all(len(n) == 4 for n in adj)
assert not any(k in adj[i] for i in range(192)
               for j in adj[i] for k in adj[j])

bmax = 2*sqrt(14)/3
h = sqrt(27/28)
q = 1/sqrt(28)
b1 = sqrt(6)
b2 = 2*sqrt(13)/3
assert abs(bmax*h-b1) < 1e-14
assert abs(b2/bmax-sqrt(13/14)) < 1e-14

def cap(s):
    return (acos(s)-s*sqrt(max(0, 1-s*s)))/pi

def lens(s):
    if s >= h:
        return 0.0
    y = h*sqrt(1-s*s)-q*s
    return (asin(y)-s*y/h)/pi

def survival(b):
    assert b2 <= b <= bmax
    s = b/bmax
    return 192*cap(s)-384*lens(s)

def simpson(f, hi, steps=4000):
    step=hi/steps
    return step/3*(f(0)+f(hi)+sum((4 if j%2 else 2)*f(j*step)
                          for j in range(1,steps)))
for b in [b2, 2.41, 2.43, 2.449, 2.46, 2.49]:
    s=b/bmax
    y=max(0, h*sqrt(1-s*s)-q*s)
    integral=2/pi*simpson(lambda t: sqrt(1-t*t)-(s+q*t)/h, y)
    assert abs(lens(s)-integral)<3e-11, (b,lens(s),integral)
    assert 0<=survival(b)<=1

rng=Random(20261027)
N=240000
thresholds=[b2, 2.41, 2.43, 2.46, 2.49]
counts=[0]*len(thresholds)
for _ in range(N):
    raw=[rng.gauss(0,1) for _ in range(4)]
    norm=sqrt(sum(t*t for t in raw))
    u=[x/norm for x in raw]
    vals=sorted((abs(x) for x in u),reverse=True)
    brightness=2/3*(3*vals[0]+2*vals[1]+vals[2])
    cauchy=sum(abs(u[i]+u[j])+abs(u[i]-u[j])
               for i in range(4) for j in range(i+1,4))/3
    orbit=2/3*max(dot(u,w) for w in centers)
    assert abs(brightness-cauchy)<2e-14
    assert abs(brightness-orbit)<2e-14
    for j,b in enumerate(thresholds):
        counts[j]+=brightness>=b
for b,count in zip(thresholds,counts):
    observed=count/N
    expected=survival(b)
    assert abs(observed-expected)<0.007, (b,observed,expected)
    print('threshold',round(b,9),'exact',round(expected,9),
          'sample',round(observed,9))

# The exact quadratic transition coefficient has the indicated finite-difference limit.
coefficient=192*sqrt(3)/pi
for eps in (0.001, 0.0003):
    b=b1-eps
    deficit=192*cap(b/bmax)-survival(b)
    measured=deficit/eps**2
    assert abs(measured/coefficient-1)<0.006, (eps,measured,coefficient)
print('VERIFY_OK: 192 centers, 384 triangle-free nearest edges, six lens integrals, '
      'five Monte Carlo tails, quadratic coefficient')
