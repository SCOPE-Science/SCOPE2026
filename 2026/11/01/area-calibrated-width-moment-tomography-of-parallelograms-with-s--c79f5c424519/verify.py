#!/usr/bin/env python3
"""Independent numerical spot checks for the analytic width-moment identities.
All universal assertions in the accompanying paper use calculus, not this test.
"""
import math
import random

PI = math.pi

def analytic(S, A, t):
    theta = math.asin(min(1.0, A/t))
    corr = (math.sin(theta)+(PI/2-theta)*math.cos(theta))/PI
    return S*S/2 + t*(2*corr-1)

def derivative(A, t):
    theta = math.asin(min(1.0,A/t))
    if abs(theta-PI/2)<1.e-12:
        return 4/PI-1
    return 2/PI*(math.sin(theta)+(PI/2-theta)/math.cos(theta))-1

def lower_constant(delta):
    if delta == 1:
        return 4/PI-1
    theta = math.asin(delta)
    return 2/PI*(delta+(PI/2-theta)/math.sqrt(1-delta*delta))-1

def quadrature(a,b,theta,n=8192):
    step=PI/n
    return sum((a*abs(math.cos((j+.5)*step))+b*abs(math.cos((j+.5)*step-theta)))**2 for j in range(n))*step/PI

rnd=random.Random(29370)
count=0
for i in range(400):
    a=.2+2.8*rnd.random();b=.2+2.8*rnd.random()
    theta=.02+(PI/2-.02)*rnd.random()
    S=a+b;A=a*b*math.sin(theta);t=a*b
    exact=analytic(S,A,t)
    direct=quadrature(a,b,theta)
    assert abs(exact-direct)<7e-8 * max(1,exact), (a,b,theta,exact,direct)
    count+=1
    if A<S*S/4-1e-12:
        delta=4*A/(S*S)
        lower=lower_constant(delta)
        upper=4/PI-1
        d=derivative(A,t)
        assert 0<lower-1e-12<=d+1e-12<=upper+1e-12
        count+=1
        lo=A;hi=S*S/4
        val=exact
        for _ in range(70):
            mid=(lo+hi)/2
            if analytic(S,A,mid)<val:lo=mid
            else:hi=mid
        rec=(lo+hi)/2
        assert abs(t-rec)<1e-10 * max(1,t)
        count+=1
for S in (1,2,3):
    for delta in (.05,.2,.45,.65,.9):
        A=delta*S*S/4
        t_lo=A;t_hi=S*S/4
        assert analytic(S,A,t_lo)<analytic(S,A,t_hi)
        eps=(t_hi-t_lo)*1e-5
        if eps>0:
            slope=(analytic(S,A,t_hi)-analytic(S,A,t_hi-eps))/eps
            assert abs(slope-lower_constant(delta))<1e-4
            count+=1
print('VERIFY_OK', count)
