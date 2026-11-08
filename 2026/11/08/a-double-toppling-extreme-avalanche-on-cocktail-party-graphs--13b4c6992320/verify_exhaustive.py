#!/usr/bin/env python3
"""Exhaustive recurrent-height and avalanche checker for cocktail-party sandpiles.
No external dependencies; independently enumerates all stable states for m=2,3,4.
"""
from itertools import product
from collections import Counter
from fractions import Fraction


def neighbors(m):
    return [tuple(j for j in range(2*m) if j != i and j//2 != i//2) for i in range(2*m)]


def burn_recurrent(a, adj):
    n=len(adj); deg=n-2; v=list(a)
    for j in adj[0]:v[j-1]+=1
    fired=[False]*n
    for _ in range(n-1):
        nxt=next((j for j in range(1,n) if not fired[j] and v[j-1]>=deg), None)
        if nxt is None: return False
        fired[nxt]=True
        v[nxt-1]-=deg
        for j in adj[nxt]:
            if j!=0:v[j-1]+=1
    return v==list(a)


def avalanche(a, adj):
    n=len(adj); d=n-2;v=list(a);v[0]+=1;t=[0]*(n-1)
    for _ in range(2*n+2):
        nxt=next((j for j in range(1,n) if v[j-1]>=d),None)
        if nxt is None:return tuple(t)
        v[nxt-1]-=d;t[nxt-1]+=1
        for j in adj[nxt]:
            if j!=0:v[j-1]+=1
    raise AssertionError('Unstable after bounded steps')


def predicted(m):
    tot=(2*m-2)**m*(2*m)**(m-2)
    ext=(2*m-3)**(m-1)*(2*m-1)**(m-2)
    mean=Fraction(2*m,2*m-2)
    return tot,ext,mean


def main():
 for m in (2,3,4):
    adj=neighbors(m); d=2*m-2
    ctr=Counter(); top_sums=0; nrec=0; max_states=0; bad=0
    for v in product(range(d), repeat=2*m-1):
       if not burn_recurrent(v,adj): continue
       nrec+=1
       t=avalanche(v,adj)
       top_sums+=sum(t)
       ctr[t]+=1
       if sum(t)==2*m:
           max_states+=1
           if t!=(2,)+(1,)*(2*m-2):bad+=1
       if max(t)>2 or any(k>1 for k in t[1:]):bad+=1
    total, extreme, mean=predicted(m)
    assert nrec==total,(m,nrec,total)
    assert max_states==extreme,(m,max_states,extreme)
    assert Fraction(top_sums,nrec)==mean,(m,top_sums,nrec,mean)
    assert bad==0,(m,bad)
    print('PASS m=',m,'recurrent=',nrec,'max_total=',2*m,'maximizers=',extreme,'p=',Fraction(extreme,total),'mean=',mean,'distinct_odometer_vectors=',len(ctr))
 print('ALL_EXHAUSTIVE_TESTS_PASS')

if __name__=='__main__':main()
