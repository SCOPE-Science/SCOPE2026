"""Exact-arithmetic reproducibility checks for an n-patch Holling-II biomass allocation theorem.

The mathematical proof is in RESULT.md; tests do not replace the global argument.
Run: python3 checker.py
"""
from fractions import Fraction as Q
from itertools import product

total=0

def check(statement):
    global total
    assert statement
    total += 1

def F(x,r,K,c,h):
    return r*x-r*x*x/K-c*x/(1+h*x)

def G(k,B,r,K,c,h):
    return r*B-r*B*B/(K*k)-c*B/(1+h*B/k)

def C(k,B,r,K,h):
    return (r/K)/h*(1+h*B/k)*(1+h*B/(k+1))

cases=[(Q(6),Q(1),Q(20),Q(1,2)),
       (Q(3,2),Q(7,4),Q(8,3),Q(3,5)),
       (Q(17,5),Q(5,3),Q(13,7),Q(4,9))]
for n in range(2,10):
    for B,r,K,h in cases:
        th={k:C(k,B,r,K,h) for k in range(1,n)}
        for k in range(1,n-1):
            check(th[k]>th[k+1])
        for winner in range(1,n+1):
            low=th[winner] if winner<n else Q(0)
            high=th[winner-1] if winner>1 else None
            c=(low+high)/2 if high is not None else low+1
            check(all((j==winner)==(G(j,B,r,K,c,h)==max(G(t,B,r,K,c,h) for t in range(1,n+1))) for j in range(1,n+1)))
            for k in range(1,n):
                exact_diff=G(k,B,r,K,c,h)-G(k+1,B,r,K,c,h)
                algebraic=(B*B/(k*(k+1)))*(c*h/((1+h*B/k)*(1+h*B/(k+1)))-r/K)
                check(exact_diff==algebraic)
        for pivot in range(1,n):
            c=th[pivot]
            vals={k:G(k,B,r,K,c,h) for k in range(1,n+1)}
            maximum=max(vals.values())
            check([k for k in range(1,n+1) if vals[k]==maximum]==[pivot,pivot+1])

# Discrete grids independently test the full simplex, not only equal-support candidates.
for n in range(2,5):
    B,r,K,h=cases[0]
    for c in [Q(1,5),Q(3,10),Q(2,5),Q(3,5),Q(6,5),Q(7,20),Q(1,2)]:
        target=max(G(k,B,r,K,c,h) for k in range(1,n+1))
        def compositions(parts,left):
            if parts==1:
                yield (left,)
            else:
                for first in range(left+1):
                    for tail in compositions(parts-1,left-first):
                        yield (first,)+tail
        for values in compositions(n,12):
            x=[B*v/12 for v in values]
            check(sum(F(t,r,K,c,h) for t in x)<=target)

# Exact staircase example with five habitats, B=6, r=1, K=20, h=1/2.
B,r,K,h=cases[0]
check([C(k,B,r,K,h) for k in range(1,5)]==[Q(1),Q(1,2),Q(7,20),Q(7,25)])
for c,winner in [(Q(1,5),5),(Q(3,10),4),(Q(2,5),3),(Q(3,5),2),(Q(6,5),1)]:
    check(max(range(1,6),key=lambda k:G(k,B,r,K,c,h))==winner)
print('PASS',total,'exact rational assertions')
