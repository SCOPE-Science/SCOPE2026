#!/usr/bin/env python3
"""Independent finite-state checks of the prism Greenberg--Hastings extinction census."""
from itertools import product

C=tuple((a,b) for a in range(3) for b in range(3))
def g(a,b): return int(a==0 and b==1)-int(a==1 and b==0)
def flat(x,y):
    return g(x[0],y[0])+g(y[0],y[1])-g(x[1],y[1])-g(x[0],x[1])==0
EDGES=tuple(tuple((j,g(x[0],y[0])) for j,y in enumerate(C) if flat(x,y)) for x in C)

def winding_count(n):
    ans=0
    for start in range(9):
        dp={(start,0):1}
        for _ in range(n):
            nxt={}
            for (s,w),a in dp.items():
                for t,d in EDGES[s]: nxt[t,w+d]=nxt.get((t,w+d),0)+a
            dp=nxt
        ans+=dp.get((start,0),0)
    return ans

def cycle_test(top,bottom):
    n=len(top)
    col=tuple(zip(top,bottom))
    for i in range(n):
        if not flat(col[i],col[(i+1)%n]): return False
    return sum(g(top[i],top[(i+1)%n]) for i in range(n))==0

def iterate(top,bottom):
    n=len(top)
    nt=[]; nb=[]
    for row,other in ((top,bottom),(bottom,top)):
        for i,x in enumerate(row):
            if x==1: y=2
            elif x==2: y=0
            else: y=int(1 in (row[(i-1)%n],row[(i+1)%n],other[i]))
            (nt if row is top else nb).append(y)
    return tuple(nt),tuple(nb)

def brute_count(n):
    good=0; sync=0
    horizon=n+6
    for vector in product(range(3), repeat=2*n):
        top=tuple(vector[:n]);bottom=tuple(vector[n:]);
        c=cycle_test(top,bottom)
        good+=c
        for _ in range(horizon):top,bottom=iterate(top,bottom)
        is_sync=len(set(top+bottom))==1
        sync+=is_sync
        if c!=is_sync:
            raise AssertionError((n,vector,'flat',c,'sync',is_sync))
    return good,sync

if __name__=='__main__':
    print('nine column states:',C)
    print('flat directed transitions:',sum(map(len,EDGES)))
    for n in range(3,7):
        a=winding_count(n)
        b,c=brute_count(n)
        assert a==b==c
        print(f'n={n}, trace-coefficient={a}, direct-flat={b}, dynamic-extinction={c}, total={9**n}')
    print('DYNAMICAL AND TRANSFER CHECKS PASS')
