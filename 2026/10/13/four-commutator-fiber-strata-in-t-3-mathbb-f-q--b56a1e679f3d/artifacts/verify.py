#!/usr/bin/env python3
from itertools import product
from collections import Counter

def expected(q, x, y, z):
    if x == 0 and z == 0 and y == 0:
        return q**3 * ((q*q+q-1)**2 + q*q*(q-1))
    if x == 0 and z == 0:
        return q**3 * (q*q-1) * (q*q+2*q-1)
    if x == 0 or z == 0:
        return q**3 * (q*q-1) * (q*q+q-1)
    return q**3 * (q*q-1)**2

def enumerate_effective(q):
    # Counts after quotienting the two irrelevant common diagonal shifts.
    vec = list(product(range(q), repeat=5))
    counts = Counter()
    for al, be, p, h, r in vec:
        for ga, de, s, t, u in vec:
            x = (al*s-ga*p) % q
            z = (be*u-de*r) % q
            y = ((al+be)*t-(ga+de)*h+p*u-s*r) % q
            counts[(x,y,z)] += 1
    for x,y,z in product(range(q), repeat=3):
        got = counts[(x,y,z)]
        want = expected(q,x,y,z)
        assert got == want, (q,(x,y,z),got,want)
    return Counter(counts.values())

def direct_q2():
    q=2
    mats=[]
    for a1,p,h,a2,r,a3 in product(range(q), repeat=6):
        mats.append((a1,p,h,a2,r,a3))
    counts=Counter()
    for A in mats:
        a1,p,h,a2,r,a3=A
        for B in mats:
            b1,s,t,b2,u,b3=B
            x=((a1-a2)*s-(b1-b2)*p)%q
            z=((a2-a3)*u-(b2-b3)*r)%q
            y=((a1-a3)*t-(b1-b3)*h+p*u-s*r)%q
            counts[(x,y,z)]+=1
    for c,n in counts.items():
        assert n == q*q*expected(q,*c), (c,n,q*q*expected(q,*c))
    assert sum(counts.values()) == q**12
    return Counter(counts.values())

for q in (2,3,5):
    hist=enumerate_effective(q)
    print('EFFECTIVE',q,sorted(hist.items()))
print('DIRECT_Q2',sorted(direct_q2().items()))
for q in range(2,21):
    f0=q**5*((q*q+q-1)**2+q*q*(q-1))
    fc=q**5*(q*q-1)*(q*q+2*q-1)
    f1=q**5*(q*q-1)*(q*q+q-1)
    f2=q**5*(q*q-1)**2
    total=f0+(q-1)*fc+2*q*(q-1)*f1+q*(q-1)**2*f2
    assert total == q**12
print('WEIGHTED_SUM_OK q=2..20')
print('VERIFY_OK')
