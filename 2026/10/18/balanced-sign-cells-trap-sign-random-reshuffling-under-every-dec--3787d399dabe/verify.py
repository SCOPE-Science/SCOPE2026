#!/usr/bin/env python3
"""Exact small-instance identity checks for balanced-sign SignRR trapping."""
from fractions import Fraction as Q
from itertools import permutations, product
from math import comb, log, pi

checks=0
for n in (2,4,6):
    p=n//2
    signs=(-1,)*p+(1,)*p
    schedules=[
        [Q(1,k+1) for k in range(n)],
        [Q(1,2*k+1) for k in range(n)],
        [Q(1) for k in range(n)],
        [Q(1) if k < n//2 else Q(1,3) for k in range(n)],
    ]
    for perm in set(permutations(signs)):
        assert sum(perm)==0
        pref=[]; running=0
        for a in perm:
            running += a
            pref.append(running)
        assert pref[-1]==0 and max(map(abs,pref))<=p
        checks+=1
        for g in schedules:
            lhs=sum((g[k]*perm[k] for k in range(n)),Q())
            rhs=sum(((g[k]-g[k+1])*pref[k] for k in range(n-1)),Q())
            assert lhs==rhs
            assert abs(lhs)<=p*(g[0]-g[-1])
            for end in range(1,n+1):
                pref_step=sum((g[k]*perm[k] for k in range(end)),Q())
                assert abs(pref_step)<=p*g[0]
                checks+=1
            checks+=1

for alpha in (Q(1,1),Q(3,4),Q(2,3)):
    # alpha=1 uses rational harmonic steps, others simply test
    # monotonicity with machine approximations after exact base checks.
    g=[1/(k+1)**float(alpha) for k in range(80)]
    assert all(g[k]>=g[k+1]>0 for k in range(79))
    x=2.
    for t in range(39):
        first=(1,2) if t%3 else (2,1)
        for j,index in enumerate(first):
            gradient=x-(5 if index==1 else -5)
            assert (gradient<0)==(index==1)
            x-=g[2*t+j]*(1 if gradient>0 else -1)
            assert 0 < x < 4
            checks+=1
    assert 1<=x<=3

# Exhaustive finite sign law: two-row order sequences have exactly the
# Rademacher series endpoint representation.
step=[Q(1,k+1) for k in range(24)]
delta=[step[2*t]-step[2*t+1] for t in range(12)]
for eps in product((-1,1),repeat=12):
    direct=Q(2)
    for t,e in enumerate(eps):
        first=(1,2) if e==1 else (2,1)
        for j,index in enumerate(first):
            direct -= step[2*t+j]*(-1 if index==1 else 1)
    formula=Q(2)+sum((Q(e)*d for e,d in zip(eps,delta)),Q())
    assert direct==formula and Q(1)<=direct<=Q(3)
    checks+=1

for N in (100,1000,10000):
    ds=[1/(2*t+1)-1/(2*t+2) for t in range(N)]
    assert abs(sum(ds)-log(2))<1/(2*N)
    assert abs(sum(d*d for d in ds)-(pi*pi/6-2*log(2)))<1/(6*N**3)
    checks+=2
print(f'PASS {checks} exact rational and finite numerical checks')
