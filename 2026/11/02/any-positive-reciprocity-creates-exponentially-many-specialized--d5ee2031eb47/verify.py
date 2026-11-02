#!/usr/bin/env python3
"""Direct exact enumeration for a reciprocity model on directed rings."""
from itertools import product
from fractions import Fraction
from collections import defaultdict
from math import comb

def kernel_count(states, return_masks=False):
    n=len(states)
    out=[0]*n
    for i,t in enumerate(states):
        j=(i+1)%n
        if t != 1:out[i]|=1<<j # clockwise exists for t=0 or 2
        if t != 0:out[j]|=1<<i # anticlockwise exists for t=1 or 2
    ans=0
    masks=[]
    for mask in range(1,1<<n):
        if any((mask>>i)&1 and (out[i]&mask) for i in range(n)):
            continue
        if any(not ((mask>>i)&1) and not (out[i]&mask) for i in range(n)):
            continue
        ans+=1
        masks.append(mask)
    return masks if return_masks else ans

def expected_formula(n,r):
    a=(1+r)/2
    u=a*(2-a)
    v=a*a
    out=Fraction(0)
    for s in range(n//2+1):
        if (n-2*s)%3: continue
        t=(n-2*s)//3
        if t<0 or s+t==0:continue
        out+=Fraction(n*comb(s+t,s),s+t)*u**s*v**t
    return out

def check():
    rs=[Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]
    comparisons=0
    zeros=0
    for n in range(3,9):
        aggregate=defaultdict(lambda:[0,0])
        for states in product(range(3),repeat=n):
            b=states.count(2)
            k=kernel_count(states)
            aggregate[b][0]+=1 if k==0 else 0
            aggregate[b][1]+=k
            zeros+=1
            if k==0:
                assert n%2==1 and (states==(0,)*n or states==(1,)*n),(n,states)
            if b==0 and not(states==(0,)*n or states==(1,)*n):
                assert k==1,(n,states,k)
        for r in rs:
            E=sum(Fraction(weighted[1])*(r**b)*(((1-r)/2)**(n-b)) for b,weighted in aggregate.items())
            P0=sum(Fraction(weighted[0])*(r**b)*(((1-r)/2)**(n-b)) for b,weighted in aggregate.items())
            predicted=expected_formula(n,r)
            zero_pred=Fraction(2)*((1-r)/2)**n if n%2 else Fraction(0)
            assert E==predicted,(n,r,E,predicted)
            assert P0==zero_pred,(n,r,P0,zero_pred)
            comparisons+=2
        print('n=',n,'states=',3**n,'r=1/2 expected=',expected_formula(n,Fraction(1,2)))
    for tail in range(3):
        masks=kernel_count((0,1,2,2,2,2,0,1,tail),return_masks=True)
        assert len(masks)>=2
        for mask in masks:
            assert (mask>>1)&1 and (mask>>7)&1
            assert not((mask>>2)&1) and not((mask>>6)&1)
            internal={j for j in (3,4,5) if (mask>>j)&1}
            assert internal in ({4},{3,5})
            flipped=mask ^ ((1<<3)|(1<<4)|(1<<5))
            assert flipped in masks, (tail,mask,flipped)
    print('VERIFY_OK',zeros,'graphs,',comparisons,'exact rational expectation/nonexistence equalities; gadget flips 3/3')
if __name__=='__main__':check()
