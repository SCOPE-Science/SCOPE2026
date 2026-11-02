#!/usr/bin/env python3
"""Independent exhaustive bit-level schedule and configuration cycle checker.
State bits 0..a-1 are A; a..a+b-1 are B. Scan order is 0-based vertex list.
"""
from itertools import permutations
from collections import Counter,defaultdict
from math import factorial,comb

def update(z,a,b,order):
    am=(1<<a)-1
    for v in order:
        if v<a:
            z ^= (((z>>a).bit_count()&1)<<v)
        else:
            z ^= (((z&am).bit_count()&1)<<v)
    return z

def observed(a,b,order):
    N=1<<(a+b)
    M=[update(z,a,b,order) for z in range(N)]
    assert len(set(M))==N
    counts=Counter()
    for v in range(N):
        y=M[v]; k=1
        while y!=v:
            y=M[y]; k+=1
            assert k<=4, (a,b,order,v)
        counts[k]+=1
    return counts

def predicted(a,b,order):
    N=a+b
    if N&1:
        return Counter({1:1<<(N-2),2:1<<(N-2),4:1<<(N-1)})
    r=sum(order[k]>=a for k in range(0,N,2))
    if (b-2*r)%3==0:
        return Counter({1:1<<(N-2),2:3<<(N-2)})
    return Counter({1:1<<(N-2),3:3<<(N-2)})

def expected_identity_schedules(a,b):
    N=a+b
    if N%2: return 0
    m=N//2
    return factorial(a)*factorial(b)*sum(comb(m,r)*comb(m,b-r) for r in range(max(0,b-m), min(m,b)+1) if (b-2*r)%3==0)

def main():
    n_schedules=n_states=0
    for a,b in [(1,1),(1,2),(1,3),(2,2),(2,3),(1,5),(2,4),(3,3),(3,4),(2,5)]:
        obs_orders=Counter()
        for order in permutations(range(a+b)):
            ob=observed(a,b,order)
            pred=predicted(a,b,order)
            assert ob==pred,(a,b,order,ob,pred)
            obs_orders['identity' if ((a+b)%2==0 and 2 in pred) else 'other']+=1
            n_schedules+=1;n_states+=1<<(a+b)
        if (a+b)%2==0:
            assert obs_orders['identity']==expected_identity_schedules(a,b),(a,b,obs_orders)
        print('a,b=',a,b,'schedules=',sum(obs_orders.values()),'classes=',dict(obs_orders))
    print('ASYNC_BIPARTITE_PARITY_VERIFY_OK','schedules=',n_schedules,'states_examined=',n_states)
if __name__=='__main__':main()
