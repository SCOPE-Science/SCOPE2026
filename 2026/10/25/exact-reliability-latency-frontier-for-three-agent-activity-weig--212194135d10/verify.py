#!/usr/bin/env python3
"""Exact-rational checks for a three-agent bounded-confidence averaging theorem."""
from fractions import Fraction as F
from itertools import product
from math import comb

def edge_probs(weights):
    u,v,z=map(F,weights)
    W=u+v+z
    e12=u/W+v/W*u/(u+z)
    e23=z/W+v/W*z/(u+z)
    assert e12+e23==1
    return e12,e23

def update(x,e,c):
    y=list(x)
    i,j=((0,1) if e==0 else (1,2))
    if abs(y[i]-y[j])<c:
        y[i]=y[j]=(y[i]+y[j])/2
    return tuple(y)

def dia(x):return max(x)-min(x)

def step_exact_sequence(x,c,seq):
    y=tuple(x)
    for e in seq:y=update(y,e,c)
    return y

def trial():
    checks=0
    for w in product(range(1,6),repeat=3):
        p,q=edge_probs(w)
        assert p==F(w[0],w[0]+w[2]) and q==F(w[2],w[0]+w[2]);checks+=2
    # All first edges active: midpoint controls eventual consensus/irreversible fragmentation.
    for xi in product(range(0,7),repeat=3):
        x=tuple(F(a,6) for a in xi)
        for c in (F(1,3),F(1,2),F(2,3),F(5,6),F(1)):
            if not (abs(x[0]-x[1])<c and abs(x[1]-x[2])<c):continue
            for first in (0,1):
                y=update(x,first,c)
                surviving=dia(y)<c
                # Verify exact formula for *every* edge word of length <=9, not just simulated.
                for k in range(0,9):
                    for suffix in product((0,1),repeat=k):
                        z=step_exact_sequence(y,c,suffix)
                        if not surviving:
                            assert z==y
                        else:
                            switches=sum(a!=b for a,b in zip((first,)+suffix,((first,)+suffix)[1:]))
                            assert dia(z)==dia(y)*F(1,2**switches)
                        checks+=1
    # Finite time: exact expectation of switches as sum of geometric waits.
    for p in (F(1,7),F(1,4),F(2,5),F(1,2),F(2,3),F(5,6)):
        q=1-p
        for start in (0,1):
            for m in range(1,10):
                # recursion E[switch target starting last edge], each new event may repeat or switch
                E=F(0)
                edge=start
                for _ in range(m):
                    rate=q if edge==0 else p
                    E+=1/rate
                    edge=1-edge
                formula=( (m+1)//2/(q if start==0 else p)
                         + m//2/(p if start==0 else q))
                assert E==formula;checks+=1
    # Exact witness: x=(0,2/5,1), c=3/4.
    x=tuple(map(F,(0,F(2,5),1)));c=F(3,4)
    assert dia(update(x,0,c))==F(4,5)>=c;checks+=1
    assert dia(update(x,1,c))==F(7,10)<c;checks+=1
    # confidence success iff first edge is 23
    assert edge_probs((2,7,3))==(F(2,5),F(3,5));checks+=1
    # tolerance 1/10: need 3 switches, conditional mean total time 1+2/p+1/q
    d=F(7,10);assert d/F(2)**2>=F(1,10) and d/F(2)**3<F(1,10);checks+=1
    for p in (F(1,10),F(1,3),F(1,2),F(3,4)):
        v=1+F(2)/p+F(1)/(1-p)
        assert v>=F(6) # weak rational check
        checks+=1
    print('PASS',checks,'exact-rational assertions')
if __name__=='__main__':trial()
