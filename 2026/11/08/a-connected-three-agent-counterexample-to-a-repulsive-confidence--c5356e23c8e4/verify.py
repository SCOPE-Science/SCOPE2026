#!/usr/bin/env python3
"""Exact replay of a signed bounded-confidence diameter counterexample."""
from fractions import Fraction as F
from itertools import product

EDGES = ((0, 1, -1), (1, 2, 1))

def direct_step(x, c, edges):
    """Literal signed increments and strict threshold in model (3.1)--(3.2)."""
    y=[]
    for i in range(len(x)):
        d=F(0); active=1
        for u,v,sgn in edges:
            if i not in (u,v):
                continue
            j=v if i==u else u
            g=x[j]-x[i]
            if abs(g)>=c:
                continue
            active+=1
            if sgn==1:
                M=g
            elif g>0:
                M=c-g
            elif g<0:
                M=-c-g
            else:
                M=c if j>i else -c
            d+=sgn*M
        y.append(x[i]+d/active)
    return tuple(y)

def average_step(x,c,edges):
    """Independently use the shifted-neighbor averaging representation."""
    y=[]
    for i in range(len(x)):
        targets=[x[i]]
        for u,v,sgn in edges:
            if i not in (u,v):
                continue
            j=v if i==u else u
            g=x[j]-x[i]
            if abs(g)>=c:
                continue
            if sgn>0:
                targets.append(x[j])
            elif g>0 or (g==0 and j>i):
                targets.append(x[j]-c)
            else:
                targets.append(x[j]+c)
        y.append(sum(targets,F(0))/len(targets))
    return tuple(y)

def width(x):
    return max(x)-min(x)

def check(x,c,edges):
    a=direct_step(x,c,edges)
    b=average_step(x,c,edges)
    assert a==b, (x,c,a,b)
    return a

count=0
c=F(1)
x=(F(0),F(1,4),F(7,4))
y=check(x,c,EDGES)
assert y==(F(-3,8),F(5,8),F(7,4))
assert check(y,c,EDGES)==y
assert width(x)==F(7,4) and width(y)==F(17,8)
assert width(y)>max(width(x),2*c)
count+=1
for c in (F(1,2),F(1),F(7,3)):
    for i in range(1,16):
        a=F(i,16)
        for j in range(1,40):
            b=F(j,20)
            if not (F(3,2)+a/2<b<2):
                continue
            x=(F(0),a*c,b*c)
            y=check(x,c,EDGES)
            assert y==((a-1)*c/2,(a+1)*c/2,b*c)
            assert check(y,c,EDGES)==y
            assert width(y)-max(width(x),2*c)==c*(b-F(3,2)-a/2)>0
            count+=1
# Two-vertex lower-size boundary is elementary and included as a finite sanity check.
for sgn in (-1,1):
    for x0,x1 in product([F(z,5) for z in range(-8,9)], repeat=2):
        state=(x0,x1)
        nxt=check(state,F(1),((0,1,sgn),))
        assert check(nxt,F(1),((0,1,sgn),))==nxt
        assert width(nxt)<=max(width(state),F(1))
        count+=1
print('VERIFY_OK',count,'exact-rational checks')
