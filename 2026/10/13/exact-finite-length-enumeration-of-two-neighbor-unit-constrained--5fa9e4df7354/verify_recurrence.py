#!/usr/bin/env python3
"""Exact integer checks for two-neighbor unit rank-modulation constraint."""
from math import factorial
from itertools import permutations
from functools import lru_cache

def add(*p):
    out=[0]*max(map(len,p))
    for a in p:
        for j,v in enumerate(a):out[j]+=v
    return out

def mult_x(a):return [0]+a

def factor(a):
    b=mult_x(a)
    c=[0,0]+a
    return add([2*x for x in b],[-x for x in c])

def polynomials(N):
    q={1:[1],2:[0,4,-2],3:[0,2,4,-2]}
    for m in range(4,N):q[m]=add(mult_x(q[m-1]),factor(q[m-2]))
    return q

def formula(n,q):
    return sum(a*factorial(n-i) for i,a in enumerate(q[n-1]))

def brute(n):
    s=0
    for p in permutations(range(n)):
        good=[abs(a-b)==1 for a,b in zip(p,p[1:])]
        s+=all(good[j] or good[j+1] for j in range(n-2))
    return s

@lru_cache(None)
def dp(mask,last,good,n):
    if mask==(1<<n)-1:return 1
    ret=0
    for k in range(n):
        if mask>>k&1:continue
        ng=int(abs(last-k)==1)
        if good or ng:ret+=dp(mask|(1<<k),k,ng,n)
    return ret

def subset_dp(n):
    dp.cache_clear()
    return sum(dp(1<<k,k,1,n) for k in range(n))

def verify():
    q=polynomials(101)
    expect={2:2,3:6,4:18,5:52,6:170,7:550,8:1972,9:6998,10:27106}
    for n in range(2,15):
        v=formula(n,q)
        if n in expect:assert v==expect[n]
        if n<=10:assert v==brute(n)
        if n<=14:assert v==subset_dp(n)
        print(n,v)
    for n in [20,30,50,100]:print(n,formula(n,q))
    print('VERIFIED unit two-neighbor formula via brute and subset DP')
if __name__=='__main__':verify()
