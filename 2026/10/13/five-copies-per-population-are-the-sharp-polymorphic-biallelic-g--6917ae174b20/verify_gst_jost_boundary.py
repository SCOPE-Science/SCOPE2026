#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

def canon(m,a,b):
    c=[]
    for x,y in ((a,b),(b,a),(m-a,m-b),(m-b,m-a)):
        c.append(tuple(sorted((x,y))))
    return min(c)

def vals(m,a,b):
    p=Fraction(a,m); q=Fraction(b,m)
    hs=p*(1-p)+q*(1-q)
    r=(p+q)/2
    ht=2*r*(1-r)
    dst=ht-hs
    gst=dst/ht
    D=2*dst/(1-hs)
    d=abs(a-b); t=abs(a+b-m)
    gst2=Fraction(d*d, m*m-t*t)
    D2=Fraction(2*d*d, m*m+d*d+t*t)
    assert gst==gst2 and D==D2
    return gst,D,d,t

def sign(x): return (x>0)-(x<0)

all_revs={}
for m in range(2,6):
    reps=sorted({canon(m,a,b) for a in range(1,m) for b in range(1,m)})
    rev=[]
    for x,y in combinations(reps,2):
        gx,dx,_,_=vals(m,*x); gy,dy,_,_=vals(m,*y)
        if sign(gx-gy)*sign(dx-dy)<0:
            rev.append((x,y,(gx,dx),(gy,dy)))
    all_revs[m]=rev

assert all_revs[2]==[]
assert all_revs[3]==[]
assert all_revs[4]==[]
assert all_revs[5]==[((1,2),(2,3),(Fraction(1,21),Fraction(1,15)),(Fraction(1,25),Fraction(1,13)))]

# Structural fixed-gap antimonotonicity check over a broad finite range.
for m in range(3,41):
    reps=sorted({canon(m,a,b) for a in range(1,m) for b in range(1,m)})
    for x,y in combinations(reps,2):
        gx,dx,gapx,tx=vals(m,*x); gy,dy,gapy,ty=vals(m,*y)
        if gapx==gapy and gapx>0 and tx!=ty:
            # Larger pooled-frequency imbalance t raises GST and lowers D.
            assert sign(gx-gy)==sign(tx-ty)
            assert sign(dx-dy)==-sign(tx-ty)

# Explicit reversal family for every m>=5.
for m in range(5,101):
    A=(1,2)
    if m%2:
        h=(m-1)//2
        B=(h,h+1)
    else:
        h=m//2
        B=(h-1,h)
    gA,dA,gapA,tA=vals(m,*A)
    gB,dB,gapB,tB=vals(m,*B)
    assert gapA==gapB==1 and tA>tB
    assert gA>gB and dA<dB

print('VERIFY_OK')
print('first_positive-grid_reversal_denominator',5)
print('unique_first_pair',all_revs[5][0])
print('fixed_gap_formula','GST=d^2/(m^2-t^2), D=2d^2/(m^2+d^2+t^2)')
