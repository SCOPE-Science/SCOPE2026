#!/usr/bin/env python3
"""Exact rational checks of upper constructions; not a proof of the continuum theorem."""
from fractions import Fraction as F

def pack(a):
    assert a >= 1
    big=(F(0),F(0),a)
    if a<=3:
        L=a+2
        small=[(F(j),a+F(i),F(1)) for i in range(2) for j in range(3)]
        small += [(a,F(0),F(1)),(a+1,F(0),F(1))]
    elif a<=4:
        L=F(5)
        small=[(F(j),F(4),F(1)) for j in range(5)]
        small += [(F(4),F(j),F(1)) for j in range(3)]
    else:
        L=a+1
        small=[(F(j),a,F(1)) for j in range(5)]
        small += [(a,F(j),F(1)) for j in range(3)]
    return L,[big]+small

def disjoint(q,r):
    x,y,s=q;u,v,t=r
    return x+s<=u or u+t<=x or y+s<=v or v+t<=y

def test(a):
    L,p=pack(a)
    assert len(p)==9
    assert L==max(a+1,min(a+2,F(5)))
    for x,y,s in p:
        assert s>0 and 0<=x and 0<=y and x+s<=L and y+s<=L
    for i in range(9):
        for j in range(i): assert disjoint(p[i],p[j]),(a,i,j,p)

if __name__=='__main__':
    vals=['1','11/10','3/2','2','299/100','3','301/100','7/2','399/100','4','401/100','5','10','100']
    for s in vals: test(F(s))
    print('PASS: 14 exact rational parameters; 9 squares and 36 pairwise relations each.')
