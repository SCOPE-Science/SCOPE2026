#!/usr/bin/env python3
import math

SQ2=math.sqrt(2.0)
VSTAR=1.0/SQ2

def gminus(v):
    s=math.sqrt(1.0-2.0*v*v)
    return 0.25*(1.0+2.0*v-s+math.log((1.0+s)/2.0))

def pminus(v):
    s=math.sqrt(1.0-2.0*v*v)
    return 0.5*(1.0+v/(1.0+s))

def gplus(v):
    s=math.sqrt(2.0*v*v-1.0)
    return 0.25+0.5*v+0.25*(math.log(v/SQ2)+s-math.atan(s))

def pplus(v):
    s=math.sqrt(2.0*v*v-1.0)
    return 0.5+(1.0+s)/(4.0*v)

def deriv(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

# Closed-form derivatives.
for v in (0.1,0.3,0.55,0.69):
    assert abs(deriv(gminus,v)-pminus(v))<2e-8
for v in (0.72,0.8,0.9,0.98):
    assert abs(deriv(gplus,v)-pplus(v))<2e-8

# Wall matching and the 3/2 singular coefficient.
gwall=(1.0+SQ2-math.log(2.0))/4.0
pwall=(2.0+SQ2)/4.0
for eps in (1e-4,4e-5,1e-5):
    for sign,fun in ((-1.0,gminus),(1.0,gplus)):
        v=VSTAR+sign*eps
        c=(fun(v)-gwall-pwall*(v-VSTAR))/(eps**1.5)
        assert abs(c-(2.0**0.25)/3.0)<0.01

# Hidden-region algebraic ratio.
for v in (0.72,0.8,0.9,0.98):
    s=math.sqrt(2.0*v*v-1.0)
    r=(v+s)/(1.0-v)
    assert abs(r*r/(1.0+r*r)-pplus(v))<2e-14

# The proposed source branch is genuinely different.
def source_proposed(v):
    s=math.sqrt(1.0-v*v)
    return 0.5*(1.0+v-s+math.log((1.0+s)/2.0))
assert gminus(0.7)-source_proposed(0.7)>0.008

# Finite checker recurrence: corroborative only.
def finite_g(T,v):
    a1=[0.0,0.0,0.0]
    a2=[0.0,0.0,1.0]
    root2=math.sqrt(2.0)
    for t in range(1,T):
        n=2*(t+1)+1
        b1=[0.0]*n
        b2=[0.0]*n
        for j in range(len(a1)):
            b1[j]=(a2[j]+a1[j])/root2
            b2[j+2]=(a2[j]-a1[j])/root2
        a1,a2=b1,b2
    total=0.0
    for j in range(2*T+1):
        x=j-T
        if 0<=x<=v*T and (x+T)%2==0:
            den=a1[j]*a1[j]+a2[j]*a2[j]
            if den:
                total += a2[j]*a2[j]/den
    return 2.0*total/T, sum(x*x for x in a1)+sum(x*x for x in a2)

val,norm=finite_g(2500,0.7)
assert abs(norm-1.0)<2e-12
assert abs(val-gminus(0.7))<0.01
assert abs(val-gminus(0.7)) < abs(val-source_proposed(0.7))
print('VERIFY_OK wall=%.15f finite_v07=%.15f norm=%.15f' % (gwall,val,norm))
