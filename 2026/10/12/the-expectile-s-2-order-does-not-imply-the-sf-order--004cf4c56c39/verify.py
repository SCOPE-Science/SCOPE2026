#!/usr/bin/env python3
from fractions import Fraction as F

Xv=[F(-83,100),F(123,100),F(135,100)]
Xp=[F(3,5),F(3,10),F(1,10)]
Yv=[F(-9,5),F(-2,5),F(9,10),F(5,1)]
Yp=[F(3,20),F(27,50),F(1,4),F(3,50)]

def mean(vals,ps): return sum((v*p for v,p in zip(vals,ps)),F(0))
def mad(vals,ps):
    m=mean(vals,ps)
    return sum((abs(v-m)*p for v,p in zip(vals,ps)),F(0))

def expectile(vals,ps,a):
    # Candidate from each support interval; exact rational arithmetic.
    m=len(vals)
    for j in range(m-1):
        PL=sum(ps[:j+1],F(0)); PR=sum(ps[j+1:],F(0))
        XL=sum((p*v for p,v in zip(ps[:j+1],vals[:j+1])),F(0))
        XR=sum((p*v for p,v in zip(ps[j+1:],vals[j+1:])),F(0))
        den=(1-a)*PL+a*PR
        e=((1-a)*XL+a*XR)/den
        if vals[j] <= e <= vals[j+1]: return e
    raise AssertionError((vals,ps,a))

def s2(vals,ps,a):
    lo=expectile(vals,ps,a); hi=expectile(vals,ps,1-a); mu=mean(vals,ps)
    return (hi+lo-2*mu)/(hi-lo)/(1-2*a)

def sx(a):
    if a < F(1,104): return (1784*a-127)/(5*(2*a-1)*(312*a+109))
    return F(1,5)

def sy(a):
    if a < F(2,11): return (5731*a-4683)/(5*(2*a-1)*(15037*a+2040))
    if a < F(210,859): return -(28246*a-953)/(10*(2*a-1)*(5154*a+1805))
    return F(19,50)

def transition(vals,ps,j):
    x=vals[j]
    L=sum((p*(x-v) for v,p in zip(vals,ps) if v<x),F(0))
    R=sum((p*(v-x) for v,p in zip(vals,ps) if v>x),F(0))
    return L/(L+R)

assert mean(Xv,Xp)==F(3,500)
assert mad(Xv,Xp)==F(627,625)
assert mean(Yv,Yp)==F(39,1000)
assert mad(Yv,Yp)==F(51291,50000)

# The relevant support-crossing levels.
assert transition(Xv,Xp,1)==F(103,104)  # upper expectile transition => a=1/104
assert transition(Yv,Yp,1)==F(210,859)
assert transition(Yv,Yp,2)==F(9,11)     # upper transition => a=2/11

# Independent exact evaluations of the piecewise s2 formulas.
tests=[F(1,500),F(1,100),F(1,10),F(1,5),F(1,4),F(2,5)]
for a in tests:
    if a<F(1,2):
        assert s2(Xv,Xp,a)==sx(a),(a,s2(Xv,Xp,a),sx(a))
        assert s2(Yv,Yp,a)==sy(a),(a,s2(Yv,Yp,a),sy(a))
        assert sy(a)>sx(a)

# All-interval sign certificates used in the proof.
# Piece 1 numerator has positive coefficients.
assert all(c>0 for c in [25037936,2566078,251367])
# Piece 2 quadratic has negative discriminant and positive leading coefficient.
disc=(-16688)**2-4*30074*2643
assert disc==-39452984 and disc<0
# Piece 3 quadratic is increasing for a>0 and already positive at 2/11.
a=F(2,11)
R=6872*a*a+8386*a-1521
assert R==F(27939,121)>0
# Piece 4 gap.
assert F(19,50)-F(1,5)==F(9,50)>0

# Endpoint profile gaps.
lim0X=(Xv[-1]+Xv[0]-2*mean(Xv,Xp))/(Xv[-1]-Xv[0])
lim0Y=(Yv[-1]+Yv[0]-2*mean(Yv,Yp))/(Yv[-1]-Yv[0])
assert lim0Y-lim0X==F(83789,370600)>0
FXmu=sum((p for v,p in zip(Xv,Xp) if v<mean(Xv,Xp)),F(0))
FYmu=sum((p for v,p in zip(Yv,Yp) if v<mean(Yv,Yp)),F(0))
assert (2*FYmu-1)-(2*FXmu-1)==F(9,50)>0

# Mean/MAD standardization and exact sf value at t=4/5.
def standardize(vals,ps):
    mu=mean(vals,ps); d=mad(vals,ps)
    return [(v-mu)/d for v in vals]

def stoploss(vals,ps,z):
    return sum((p*max(v-z,F(0)) for v,p in zip(vals,ps)),F(0))

def S_standard(vals,ps,t):
    sv=standardize(vals,ps)
    return (stoploss(sv,ps,t)-stoploss(sv,ps,-t))/t+1

Xs=standardize(Xv,Xp); Ys=standardize(Yv,Yp)
assert Xs==[F(-5,6),F(255,209),F(280,209)]
assert Ys==[F(-30650,17097),F(-21950,51291),F(350,417),F(6050,1251)]
t=F(4,5)
SX=S_standard(Xv,Xp,t); SY=S_standard(Yv,Yp,t)
assert SX==F(1,5)
assert SY==F(73441,569900)
gap=SX-SY
assert gap==F(40539,569900)>0
print(f"VERIFY_OK breaks=1/104,2/11,210/859 sf_gap={gap.numerator}/{gap.denominator}")
