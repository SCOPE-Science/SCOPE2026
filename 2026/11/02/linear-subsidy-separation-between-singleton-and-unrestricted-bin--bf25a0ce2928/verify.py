#!/usr/bin/env python3
"""Exhaustive, symmetry-reduced checks for two approval classes.
Each distribution of indistinguishable A- and B-goods across labeled agents
is represented by two weak compositions. No assumption of subsidy integrality
is made by the mathematics: for each fixed allocation, integer difference
constraints yield the coordinatewise-minimal integral subsidy vector.
"""
from itertools import product
from math import comb


def distributions(total, positions):
    if positions == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for tail in distributions(total-x, positions-1):
                yield (x,) + tail


def least_subsidy(x, y, r):
    n = 2*r
    value = lambda i,j: x[j] if i < r else y[j]
    own = [value(i,i) for i in range(n)]
    money = [0]*n
    for _ in range(n):
        update = [max(0,*(money[j]+value(i,j)-own[i] for j in range(n))) for i in range(n)]
        if update == money:
            return sum(money),tuple(money)
        money = update
    update = [max(0,*(money[j]+value(i,j)-own[i] for j in range(n))) for i in range(n)]
    if update != money:
        return None,None
    return sum(money),tuple(money)


def check(r):
    n=2*r
    best_any=n*n; best_one=n*n
    witnesses=0; counts=0; housecounts=0
    for x in distributions(1,n):
        for y in distributions(n-1,n):
            counts+=1
            amount,money=least_subsidy(x,y,r)
            if amount is not None:
                if amount<best_any:
                    best_any=amount; witnesses=0
                if amount==best_any:
                    witnesses+=1
            if all(xx+yy==1 for xx,yy in zip(x,y)):
                housecounts+=1
                if amount is not None:
                    best_one=min(best_one,amount)
    assert best_any==r if r>=3 else (1 if r==2 else 0),(r,best_any)
    assert best_one==2*r-1,(r,best_one)
    print(f'r={r} n={n} allocations_reduced={counts} house_reduced={housecounts} unrestricted={best_any} house={best_one} unrestricted_witnesses={witnesses}')

for r in (2,3,4):check(r)
print('VERIFY_OK')
