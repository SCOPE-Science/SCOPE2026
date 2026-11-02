#!/usr/bin/env python3
"""Exact-rational checks for order robustness of fully funded preallocations."""
from fractions import Fraction as F
from itertools import combinations

def charge(balance, support, cost):
    """Return residual balances, or None when supporters cannot fund cost."""
    b=list(balance)
    if cost>sum((b[i] for i in support),F(0)):
        return None
    if not cost:
        return b
    cap=sorted({b[i] for i in support})
    prev=F(0)
    rem=cost
    for level in cap:
        active=sum(1 for i in support if b[i]>prev)
        increment=(level-prev)*active
        if rem<=increment:
            rho=prev+rem/active
            return [max(F(0),v-rho) if i in support else v for i,v in enumerate(b)]
        rem-=increment
        prev=level
    assert rem==0
    return [F(0) if i in support else v for i,v in enumerate(b)]

def two_order(n,S,T,u,v,h=F(1)):
    def do(seq):
        b=[h]*n
        for supp,cost in seq:
            b=charge(b,supp,cost)
            if b is None:
                return None
        return tuple(b)
    return do([(S,u),(T,v)]),do([(T,v),(S,u)])

def laminar(S,T):
    return S<=T or T<=S or S.isdisjoint(T)

def check():
    cases=fully=laminar_cases=cross_cases=cross_witnesses=0
    for n in range(1,7):
        ss=[frozenset(i for i in range(n) if m>>i&1) for m in range(1,1<<n)]
        for j,S in enumerate(ss):
            for T in ss[j+1:]:
                cases+=1
                if laminar(S,T):
                    laminar_cases+=1
                else:
                    cross_cases+=1
                # Exact fractional cost profiles, sample enough distinct scales
                for u0 in (1,2,3,4,5,6,7,8,9,11,13,15,17):
                    for v0 in (1,2,3,4,5,6,7,8,9,11,13,15,17):
                        u,v=F(u0,10),F(v0,10)
                        if u+v>n:
                            continue
                        a,b=two_order(n,S,T,u,v)
                        if a is not None and b is not None:
                            fully+=1
                            if laminar(S,T):
                                assert a==b,(n,S,T,u,v,a,b)
                if not laminar(S,T):
                    k=len(S&T); a=len(S-T); b=len(T-S)
                    s,t=len(S),len(T)
                    eps=min(F(1,100), (F(s,s+k)-F(1,2))/3, (F(t,t+k)-F(1,2))/3, (F(n,s+t)-F(1,2))/3)
                    assert eps>0
                    theta=F(1,2)+eps
                    ba,bb=two_order(n,S,T,theta*s,theta*t)
                    assert ba is not None and bb is not None and ba!=bb,(n,S,T,theta,ba,bb)
                    z=next(iter(S-T))
                    assert ba[z]>bb[z] and ba[z]>0
                    w=(ba[z]+bb[z])/2
                    assert w>0 and sum(ba)>=w and (ba[z]>=w>bb[z])
                    cross_witnesses+=1
    print('VERIFY_OK support_pairs=',cases,'fully_funded_cost_profiles=',fully,
          'laminar_pairs=',laminar_cases,'crossing_pairs=',cross_cases,
          'crossing_constructed_witnesses=',cross_witnesses)
    # human-sized instance, costs 6/5,6/5 and 3/10
    S=frozenset((0,1)); T=frozenset((1,2))
    a,b=two_order(3,S,T,F(6,5),F(6,5))
    assert a==(F(2,5),F(0),F(1,5))
    assert b==(F(1,5),F(0),F(2,5))
    assert a[0]>=F(3,10)>b[0]
    print('WITNESS_OK',a,b,'third_project_cost=3/10')
if __name__=='__main__': check()
