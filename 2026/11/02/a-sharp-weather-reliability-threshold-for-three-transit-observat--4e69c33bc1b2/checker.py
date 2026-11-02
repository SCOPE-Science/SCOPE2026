"""Exact rational check of three-window two-event coverage under independent misses.
Run: python checker.py. Finite checks corroborate, not replace, the proof.
"""
from fractions import Fraction as F
from itertools import product

def coverage(starts,ell,d):
    pts={F(0),F(1)}
    for a in starts:
        pts.add(a)
        pts.add((a+ell)%1)
    p=sorted(pts)
    ans=F(0)
    for lo,hi in zip(p,p[1:]):
        mid=(lo+hi)/2
        n=sum(((mid-a)%1)<ell for a in starts)
        prob=F(0) if n<2 else (d*d if n==2 else 3*d*d-2*d*d*d)
        ans+=(hi-lo)*prob
    return ans

def predicted(e,d):
    cluster=d*d*(3-2*d)*e
    if e<F(1,2):return cluster
    spread=d*d*(3*e-1) if e<=F(2,3) else d*d*(1+2*(1-d)*(3*e-2))
    return max(cluster,spread)

count=0
E=[F(1,5),F(2,5),F(1,2),F(3,5),F(2,3),F(3,4),F(9,10)]
D=[F(1,4),F(1,2),F(3,4),F(4,5),F(1)]
for e,d in product(E,D):
    p=predicted(e,d)
    assert coverage((F(0),F(0),F(0)),e,d)<=p
    assert coverage((F(0),F(1,3),F(2,3)),e,d)<=p
    assert max(coverage((F(0),F(0),F(0)),e,d),coverage((F(0),F(1,3),F(2,3)),e,d))==p
    count+=3
    for i in range(21):
        for j in range(21):
            q=coverage((F(0),F(i,21),F(j,21)),e,d)
            assert q<=p,(e,d,i,j,q,p)
            count+=1
print('PASS',count,'exact rational assertions')
