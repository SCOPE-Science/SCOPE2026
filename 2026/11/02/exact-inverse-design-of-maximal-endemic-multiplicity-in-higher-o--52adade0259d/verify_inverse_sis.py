#!/usr/bin/env python3
"""Exact-rational checks of an inverse-design theorem for homogeneous simplicial SIS flows.

Requires only Python's standard library. Checks are finite corroboration, not a
substitute for the all-order coefficient-positivity argument.
"""
from fractions import Fraction as Q
from math import factorial
from random import Random


def multiply(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            out[i+j]+=u*v
    return out


def data(roots):
    m=len(roots)
    prod=[Q(1)]
    d=Q(1)
    for r in roots:
        assert Q(0)<r<Q(1)
        prod=multiply(prod,[-r,Q(1)])
        d*=1-r
    e=[Q(0)]*(m+1)
    e[0]=Q(1)
    for r in roots:
        for j in range(m,0,-1):
            e[j]+=r*e[j-1]
    p=[Q(0)]*m
    for j in range(1,m+1):
        p[j-1]=sum(((-1)**s)*e[s] for s in range(m-j+1))/d
    return prod,d,e,p


def check(roots):
    m=len(roots)
    prod,d,e,coeff=data(roots)
    assert d>0
    # (1-x)P(x)-1 = -prod(x-r_i)/prod(1-r_i)
    drift=multiply([Q(1),-Q(1)],coeff)
    drift[0]-=1
    assert drift==[-z/d for z in prod]
    # Reverse reconstruction: prescribed endemic roots force unique rates.
    assert coeff[-1]==1/d
    if m>=2:
        assert coeff[-2]==(1-sum(roots))/d
        assert (all(x>0 for x in coeff))==(sum(roots)<1)
    else:
        assert coeff[0]>0
    for i,r in enumerate(roots):
        assert sum(drift[j]*r**j for j in range(m+1))==0
        deriv=-r/d
        for k,s in enumerate(roots):
            if k!=i:deriv*=r-s
        assert deriv!=0
        assert (deriv<0)==((m-i-1)%2==0)
    return m


def main():
    totals={'families':0,'roots':0,'admissible':0,'inadmissible':0,'boundary':0}
    rng=Random(20261029)
    for m in range(1,16):
        for factor in [2,3,5,11]:
            roots=[Q(i,factor*m*(m+1)) for i in range(1,m+1)]
            totals['roots']+=check(roots);totals['families']+=1;totals['admissible']+=1
        if m>=2:
            roots=[Q(2*i,m*(m+1)) for i in range(1,m+1)]
            assert sum(roots)==1
            totals['roots']+=check(roots);totals['families']+=1;totals['boundary']+=1
            roots=[Q(1,2)+Q(i,4*(m+1)) for i in range(1,m+1)]
            assert sum(roots)>1
            totals['roots']+=check(roots);totals['families']+=1;totals['inadmissible']+=1
        for trial in range(150):
            values=sorted(rng.sample(range(1,5000),m))
            # A mixture of sums below and above one, all distinct and below one.
            if trial%2==0:
                den=sum(values)+rng.randrange(1,1000)
            else:
                den=max(values)+rng.randrange(1,1000)
            roots=[Q(v,den) for v in values]
            total=sum(roots)
            totals['roots']+=check(roots);totals['families']+=1
            if total<1:totals['admissible']+=1
            elif total==1:totals['boundary']+=1
            else:totals['inadmissible']+=1
    # Exact illustrative four-order family: 1/20, 1/10, 3/20, 1/5.
    roots=[Q(1,20),Q(1,10),Q(3,20),Q(1,5)]
    _,d,_,c=data(roots)
    assert sum(roots)==Q(1,2)
    assert all(z>0 for z in c)
    print('exact inverse-design checks:',totals)
    print('illustration roots:', [str(z) for z in roots])
    print('illustration normalized rates:', [str(z) for z in c])
    print('illustration raw simplex rates:', [str(factorial(i+1)*z) for i,z in enumerate(c)])
    print('illustration leading factor:',str(-1/d))
    print('PASS')

if __name__=='__main__':main()
