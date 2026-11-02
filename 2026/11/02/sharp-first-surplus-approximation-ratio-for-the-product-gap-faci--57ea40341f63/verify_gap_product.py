"""Exact reproducibility checks of the first-surplus Product-Gap ratio.
Requires only Python 3 standard library. All fractions are rational.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def direct(gaps):
    k = len(gaps)
    pts = [F(0)]
    for gap in gaps:
        pts.append(pts[-1] + gap)
    weights, costs = [], []
    for missing in range(k+1):
        chosen = [pts[j] for j in range(k+1) if j != missing]
        weight = F(1)
        for a,b in zip(chosen,chosen[1:]):
            weight *= b-a
        weights.append(weight)
        costs.append(min(abs(pts[missing]-v) for v in chosen))
    return sum(w*c for w,c in zip(weights,costs))/sum(weights)


def formula(gaps):
    k = len(gaps)
    invsum = sum(F(1,g) for g in gaps)
    adjacent = sum(F(min(a,b),max(a,b)) for a,b in zip(gaps,gaps[1:]))
    return (k+1+adjacent)/(2*invsum)


def verify(gaps):
    k=len(gaps)
    d=direct(gaps)
    f=formula(gaps)
    assert d==f, (gaps,d,f)
    assert d/min(gaps)<=F(2*k-1,2), (gaps,d)

n=0
for k in range(2,7):
    for gaps in product((1,2,3),repeat=k):
        verify(tuple(map(F,gaps)))
        n+=1
r=Random(431029)
for k in range(2,12):
    for j in range(200):
        gaps=tuple(F(r.randint(1,10**5),r.randint(1,10**4)) for _ in range(k))
        verify(gaps)
        n+=1
for k in range(2,12):
    for N in (100,1000,100000):
        gaps=(F(1,N),)+(F(1),)*(k-1)
        expected=F((2*k-1)*N+1,2*(N+k-1))
        assert direct(gaps)/min(gaps)==expected
        assert expected<F(2*k-1,2)
        n+=1
print(f'PASS: {n} exact nondegenerate profiles; direct weighted selection agrees with derived formula; upper bound holds; endpoint sequence has its stated exact ratio.')
