#!/usr/bin/env python3
"""Exact dynamic-programming cross-check of two-agent binary envy formulas."""
from itertools import product
from fractions import Fraction

types=((0,0),(1,0),(0,1),(1,1))

def opt_dp(seq):
    # pair (d1,d2) : own minus other value for agent 1 and 2 respectively
    states={(0,0):0}
    for a,b in seq:
        ns={}
        for (d1,d2),cost in states.items():
            for choice in (0,1):
                pair=(d1+a,d2-b) if choice==0 else (d1-a,d2+b)
                envy=max(0,-pair[0],-pair[1]); value=cost+envy
                if pair not in ns or value<ns[pair]:ns[pair]=value
        states=ns
    return min(states.values())

def formula(seq):
    seen_exclusive=False
    common=0
    cost=0
    for a,b in seq:
        if a!=b:seen_exclusive=True
        if a==b==1:common+=1
        if not seen_exclusive and common%2:cost+=1
    return cost

def constructive(seq):
    # If the first asymmetric good belongs only to agent 1, give the first common good to agent 2.
    # If only agent 2 likes it, give the first common good to agent 1.
    first=next((a for a,b in seq if a!=b),None)
    common=0;d1=d2=0;vals=[];choices=[]
    for a,b in seq:
        if a==b==1:
            common+=1
            if first==1:
                owner=1 if common%2 else 0
            else:
                owner=0 if common%2 else 1
        elif (a,b)==(1,0):owner=0
        elif (a,b)==(0,1):owner=1
        else:owner=0
        if owner==0:d1+=a;d2-=b
        else:d1-=a;d2+=b
        vals.append(max(0,-d1,-d2));choices.append(owner)
    return sum(vals),vals,choices

counts={}
for m in range(0,9):
    n=0
    for inds in product(range(4),repeat=m):
        seq=[types[i] for i in inds]
        f=formula(seq);p=opt_dp(seq);c,curve,alloc=constructive(seq)
        assert p==f==c,(seq,p,f,c,curve,alloc)
        n+=1
    counts[m]=n
    print('length',m,'full valuation sequences',n,'verified')
for horizon in range(2,31):
    # Type (1,1), then one of two exclusively valued types repeated.
    for fav in [(1,0),(0,1)]:
        seq=[(1,1)]+[fav]*(horizon-1)
        assert opt_dp(seq)==1
        # If shared item allocated to the only positive exclusive recipient, other agent envies forever.
        wrong=0 if fav==(1,0) else 1
        d1=d2=0;tot=0
        for t,(a,b) in enumerate(seq):
            own=wrong if t==0 else (0 if a else 1)
            if own==0:d1+=a;d2-=b
            else:d1-=a;d2+=b
            tot+=max(0,-d1,-d2)
        assert tot==horizon,(horizon,fav,tot)
    assert Fraction(1,1)+Fraction(horizon-1,2)==Fraction(horizon+1,2)
print('VERIFY_OK exhaustive_binary_profiles=',sum(counts.values()),' horizon_family=2..30 worst_deterministic_ratio=m worst_randomized_minimax=(m+1)/2',sep='')
