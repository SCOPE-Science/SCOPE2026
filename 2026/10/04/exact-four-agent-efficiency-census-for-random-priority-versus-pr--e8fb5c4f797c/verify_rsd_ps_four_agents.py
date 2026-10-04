#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction

N=4
ORDERS=list(permutations(range(N)))
PRIORITIES=ORDERS

def rsd_counts(P):
    c=[[0]*N for _ in range(N)]
    for pr in PRIORITIES:
        free=[1]*N
        for i in pr:
            pref=P[i]
            if free[pref[0]]: o=pref[0]
            elif free[pref[1]]: o=pref[1]
            elif free[pref[2]]: o=pref[2]
            else: o=pref[3]
            c[i][o]+=1; free[o]=0
    return c

def ps(P):
    rem=[Fraction(1)]*N
    a=[[Fraction(0)]*N for _ in range(N)]
    t=Fraction(0)
    while t<1:
        ch=[0]*N; rates=[0]*N
        for i in range(N):
            pref=P[i]
            o=pref[0] if rem[pref[0]] else pref[1] if rem[pref[1]] else pref[2] if rem[pref[2]] else pref[3]
            ch[i]=o; rates[o]+=1
        dt=min(rem[o]/rates[o] for o in range(N) if rates[o])
        for i,o in enumerate(ch): a[i][o]+=dt
        for o in range(N):
            if rates[o]: rem[o]-=dt*rates[o]
        t+=dt
    return a

def oe(P,rp):
    reach=[[False]*N for _ in range(N)]
    for i,pref in enumerate(P):
        for kb,b in enumerate(pref):
            if rp[i][b]:
                for a in pref[:kb]: reach[a][b]=True
    for k in range(N):
        for i in range(N):
            if reach[i][k]:
                rik=reach[i]
                rkk=reach[k]
                for j in range(N):
                    if rkk[j]: rik[j]=True
    return not any(reach[i][i] for i in range(N))

def equal(A,R):
    return all(A[i][o]*24==R[i][o] for i in range(N) for o in range(N))

def psdom(P,A,R):
    strict=False
    for i,pref in enumerate(P):
        xa=Fraction(0); xr=0
        for o in pref[:-1]:
            xa+=A[i][o]; xr+=R[i][o]
            lhs=xa*24
            if lhs<xr: return False
            if lhs>xr: strict=True
    return strict

hist=Counter()
for P in product(ORDERS, repeat=N):
    R=rsd_counts(P); A=ps(P); O=oe(P,R)
    if equal(A,R):
        hist[("equal",O)]+=1
    elif psdom(P,A,R):
        hist[("ps_sd_dominates",O)]+=1
    else:
        hist[("incomparable",O)]+=1

target=Counter({
("equal",True):72288,
("incomparable",True):190512,
("incomparable",False):57312,
("ps_sd_dominates",False):11664})
assert hist==target, (hist,target)
assert sum(hist.values())==331776
assert sum(v for (c,o),v in hist.items() if not o)==68976
assert Fraction(68976,331776)==Fraction(479,2304)
assert Fraction(11664,331776)==Fraction(9,256)
assert Fraction(11664,68976)==Fraction(81,479)
print("VERIFY_OK")
print("classification",dict(hist))
print("rsd_ordinally_inefficient","68976","prob","479/2304")
print("ps_sd_dominates_rsd","11664","prob","9/256")
print("ps_dom_share_of_rsd_inefficient","81/479")
