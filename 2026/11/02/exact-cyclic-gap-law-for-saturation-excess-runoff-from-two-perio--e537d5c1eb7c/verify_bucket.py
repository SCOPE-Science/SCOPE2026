#!/usr/bin/env python3
"""Exact-rational cross-check of periodic two-pulse saturation-excess runoff."""
from fractions import Fraction as F

def evaluate(n,g,r,p):
    h=n-g
    assert n>=2 and 1<=g<=h and F(0)<r<1 and p>0
    p0=(1-r**n)/(1+r**g)
    p1=1-r**h
    assert p0<=p1
    if p<=p0:
        a=p*(1+r**g)/(1-r**n)
        b=p*(1+r**h)/(1-r**n)
        branch='dry'
    elif p<=p1:
        a=F(1)
        b=p+r**h
        branch='one'
    else:
        a=b=F(1)
        branch='two'
    def mi(q,v):return min(q,v)
    assert a==min(F(1),p+r**g*b), (n,g,r,p,'a')
    assert b==min(F(1),p+r**h*a), (n,g,r,p,'b')
    W=max(F(0),p+r**g*b-1)+max(F(0),p+r**h*a-1)
    L=p*(1+r**g)+r**n-1
    H=2*(p-1)+r**g+r**h
    predicted=max(F(0),L,H)
    assert W==predicted,(n,g,r,p,W,predicted)
    if branch=='dry':assert W==0
    elif branch=='one':assert W>0 and b<=1
    else:assert W>0 and a==b==1
    return W,branch


def run():
    checks=0
    for r in [F(1,5),F(1,3),F(1,2),F(2,3),F(3,4),F(9,10)]:
        for n in range(3,18):
            for p in [F(j,40) for j in range(1,101)]:
                last=None
                for g in range(1,n//2+1):
                    w,_=evaluate(n,g,r,p)
                    checks+=1
                    if last is not None:
                        assert w<=last
                        if w>0:assert w<last
                    last=w
    r=F(1,2);n=6;p=F(3,4)
    assert evaluate(n,1,r,p)[0]==F(9,64)
    assert evaluate(n,2,r,p)[0]==0
    assert evaluate(n,3,r,p)[0]==0
    assert (1-r**n)/(1+r)==F(21,32)
    assert (1-r**n)/(1+r**3)==F(7,8)
    # The balanced gap has no one-overflow regime.
    for r in [F(1,3),F(2,5),F(9,10)]:
        for g in range(1,12):
            n=2*g
            assert (1-r**n)/(1+r**g)==1-r**g
    print('PASS:',checks,'exact periodic-state and runoff cases; ordering, boundaries and example verified')
if __name__=='__main__':run()
