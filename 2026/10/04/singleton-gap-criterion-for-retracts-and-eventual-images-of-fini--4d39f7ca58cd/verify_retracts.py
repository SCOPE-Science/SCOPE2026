#!/usr/bin/env python3
from itertools import product


def elements(sizes):
    return [(i,a) for i,n in enumerate(sizes) for a in range(n)]


def leq(x,y):
    return x==y or x[0] < y[0]


def criterion(sizes, mask):
    E=elements(sizes)
    Y={E[j] for j in range(len(E)) if (mask>>j)&1}
    if not Y:
        return False
    ys=[sum(1 for x in Y if x[0]==i) for i in range(len(sizes))]
    S=[i for i,v in enumerate(ys) if v]
    if S[0]>0 and ys[S[0]]!=1:
        return False
    if S[-1]<len(sizes)-1 and ys[S[-1]]!=1:
        return False
    for a,b in zip(S,S[1:]):
        if b>a+1 and ys[a]!=1 and ys[b]!=1:
            return False
    return True


def has_retraction(sizes, mask):
    E=elements(sizes)
    Y=[E[j] for j in range(len(E)) if (mask>>j)&1]
    if not Y:
        return False
    Yset=set(Y)
    outside=[x for x in E if x not in Yset]
    for vals in product(Y, repeat=len(outside)):
        r={y:y for y in Y}
        r.update(zip(outside, vals))
        ok=True
        for x in E:
            for z in E:
                if leq(x,z) and not leq(r[x],r[z]):
                    ok=False; break
            if not ok: break
        if ok:
            return True
    return False


def check_case(sizes, expected):
    E=elements(sizes)
    good=0
    for mask in range(1,1<<len(E)):
        c=criterion(sizes,mask)
        r=has_retraction(sizes,mask)
        if c!=r:
            raise AssertionError((sizes,mask,c,r))
        good += int(c)
    if good!=expected:
        raise AssertionError((sizes,good,expected))
    print(f"{sizes}: {good} retract subsets")


cases=[
    ((2,2),13),
    ((2,2,2),53),
    ((2,3,2),96),
    ((1,2,2),25),
    ((2,1,2),28),
    ((1,2,3,1),78),
]
for sizes,expected in cases:
    check_case(sizes,expected)
print("VERIFY_OK")
