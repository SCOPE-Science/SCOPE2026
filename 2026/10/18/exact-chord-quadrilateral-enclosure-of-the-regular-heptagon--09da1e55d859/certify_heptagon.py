#!/usr/bin/env python3
"""Pure-rational finite certificate for minimum chord quadrilateral of a regular heptagon.

Angles are in radians. Machin's identity, an alternating arctangent series and
Taylor's theorem supply rational enclosures; no floating-point decision is used.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial

SCALE=10**20
EPS=F(1,10**18)

def atan_bounds(x,N=32):
    s=F(0)
    for k in range(2*N):
        z=x**(2*k+1)/F(2*k+1)
        s += z if k%2==0 else -z
    # even number of terms => lower; next term positive => upper
    return s,s+x**(4*N+1)/F(4*N+1)

a,b=atan_bounds(F(1,5))
c,d=atan_bounds(F(1,239))
pi_lo,pi_hi=16*a-4*d,16*b-4*c
assert F(3141592653589793,10**15) < pi_lo < pi_hi < F(3141592653589794,10**15)
pi_mid=(pi_lo+pi_hi)/2
assert pi_hi-pi_lo < F(1,10**40)

def taylor_trig(x):
    cs=F(0);sn=F(0)
    for k in range(40):
        cs += (-1)**k*x**(2*k)/factorial(2*k)
        sn += (-1)**k*x**(2*k+1)/factorial(2*k+1)
    # Taylor remainder: |x|<=7; first omitted terms bounded by 7^80/80!
    assert abs(x) < 7
    assert F(7**80, factorial(80)) < F(1,10**45)
    return sn,cs

def rounding(f):
    # nearest rational on mesh 10^-20, with exact tie treatment.
    k=(f*SCALE+F(1,2)).numerator//(f*SCALE+F(1,2)).denominator
    return F(k,SCALE)

S={};C={}
for k in range(14):
    ss,cc=taylor_trig(pi_mid*k/7)
    S[k]=rounding(ss);C[k]=rounding(cc)
    assert abs(S[k]-ss) < EPS/4 and abs(C[k]-cc)<EPS/4
# Errors from evaluating at pi_mid rather than pi are bounded by 2|pi-pi_mid|;
# Taylor remainders are < 10^-45; rounding was checked exactly above.
assert 2*(pi_hi-pi_lo)+F(1,10**45) < EPS/4

class I:
    def __init__(self,a,b=None):
        self.lo=F(a);self.hi=F(a if b is None else b)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=asI(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-asI(o)
    def __rsub__(self,o):return asI(o)+-self
    def __mul__(self,o):
        o=asI(o);v=[x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asI(o);assert o.lo>0 or o.hi<0
        return self*I(F(1,o.hi),F(1,o.lo))

def asI(x):return x if isinstance(x,I) else I(x)

def trigI(d,is_sin):
    x=(S if is_sin else C)[d]
    return I(x-EPS,x+EPS)

def area_bound(ind):
    acc=I(0)
    for idx,j in enumerate(ind):
        k=ind[(idx+1)%4]
        g=(k-j)%14
        assert 1<=g<=6
        hj=I(1) if j%2==0 else trigI(1,False)
        hk=I(1) if k%2==0 else trigI(1,False)
        acc+= (hj*hk-(hj*hj+hk*hk)*F(1,2)*trigI(g,False))/trigI(g,True)
    return acc

best=(1,3,7,11)
bestval=area_bound(best)
# Geometric lower bound for any degenerate (three-side) enclosure:
# an enclosing triangle also encloses the inball of radius cos(pi/7).
assert trigI(1,False).lo>F(9,10)
assert bestval.hi<F(7,2)
assert 5*F(9,10)**2>F(7,2)  # 3 sqrt(3) > 5.
for d in range(1,7):
    assert trigI(d,True).lo>0
# Area of the regular heptagon: 7 sin(pi/7) cos(pi/7).
hept_area=7*trigI(1,True)*trigI(1,False)
ratio=bestval/hept_area
assert ratio.lo>F(12588,10000) and ratio.hi<F(12589,10000)
assert ratio.hi<F(63,50) # < 3/sqrt(5), since 63^2*5 < 9*50^2.
valid_count=0
win=[]
min_margin=None
for ind in combinations(range(14),4):
    gaps=[(ind[(i+1)%4]-j)%14 for i,j in enumerate(ind)]
    if max(gaps)>=7:continue
    valid_count+=1
    if all(j%2==1 for j in ind) and sorted(gaps)==[2,4,4,4]:
        win.append(ind)
    else:
        value=area_bound(ind)
        margin=value.lo-bestval.hi
        if min_margin is None or margin<min_margin:min_margin=margin
        assert margin>F(1,40),(ind,float(margin))
assert valid_count==511,(valid_count,win)
assert len(win)==7,(win,len(win))
assert best in win
assert min_margin>F(1,40)
print('PASS: 511 bounded four-normal selections; exactly seven minimizers.')
print('PASS: minimizer ratio lies strictly between 1.2588 and 1.2589.')
print('PASS: each of 504 alternatives exceeds the optimum by > 1/40.')
print('PASS: all inequalities certified in exact rational arithmetic.')
print('min margin enclosure lower decimal:', format(float(min_margin),'.12f'))
print('minimizer indices:',win)
