#!/usr/bin/env python3
"""Exact-rational checks for two-pair quota lotteries (public, standard library only)."""
from fractions import Fraction as F
from itertools import combinations

PAIRS = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
COST_COUNT = (0,2,1,1,0,0)
COST_EVENT = (0,1,1,1,0,0)
ROWS = [tuple(int(i in p) for p in PAIRS) for i in range(3)] + [(1,)*6]


def solve_square(a, b):
    n=len(b)
    x=[[F(v) for v in a[i]]+[F(b[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if x[i][j]),None)
        if pivot is None:return None
        x[j],x[pivot]=x[pivot],x[j]
        z=x[j][j]
        x[j]=[v/z for v in x[j]]
        for i in range(n):
            if i==j:continue
            z=x[i][j]
            if z:x[i]=[u-z*v for u,v in zip(x[i],x[j])]
    return tuple(x[i][-1] for i in range(n))


def exact_lp_min(r,cost):
    b=tuple(r[:3])+(F(1),)
    best=None
    for columns in combinations(range(6),4):
        a=[[ROWS[i][j] for j in columns] for i in range(4)]
        sol=solve_square(a,b)
        if sol is None or any(x<0 for x in sol):continue
        v=sum(cost[j]*x for j,x in zip(columns,sol))
        if best is None or v<best:best=v
    assert best is not None,(r,'no vertex')
    return best


def closed_form_lottery(r):
    a,b,c,d=r
    z=F(0)
    if b+c>=1:
        p=(a,z,z,b+c-1,1-a-c,1-b)
    else:
        p=(1-d,z,1-b-c,z,b+d-1,c)
    return p


def verify_one(r):
    a,b,c,d=r
    assert F(0)<=a<=b<F(1) and F(0)<=c<=d<F(1)
    assert sum(r)==2
    p=closed_form_lottery(r)
    assert all(0<=x<=1 for x in p),(r,p)
    assert sum(p)==1
    assert tuple(sum(p[j] for j,P in enumerate(PAIRS) if i in P) for i in range(4))==r,(r,p)
    true=min(exact_lp_min(r,COST_COUNT),exact_lp_min(r,COST_EVENT))
    predicted=abs(b+c-1)
    assert true==predicted,(r,true,predicted)
    assert exact_lp_min(r,COST_COUNT)==predicted
    assert exact_lp_min(r,COST_EVENT)==predicted
    assert sum(COST_COUNT[j]*x for j,x in enumerate(p))==predicted
    assert sum(COST_EVENT[j]*x for j,x in enumerate(p))==predicted


def main():
    total=0
    for denom in (6,12,18):
        pairs=[(F(a,denom),F(b,denom)) for a in range(denom) for b in range(a,denom)]
        for a,b in pairs:
            for c,d in pairs:
                if a+b+c+d!=2:continue
                verify_one((a,b,c,d));total+=1
    print('PASS: exact independent LP-vertex and constructive checks for',total,'ordered rational residue profiles')
    sample=(F(3,20),F(17,20),F(1,4),F(3,4))
    verify_one(sample)
    print('PASS: explicit strict four-party instance',sample,'optimal envy',abs(sample[1]+sample[2]-1))

if __name__=='__main__':main()
