"""Supplementary finite checks for the five-site shadow-fiber minimax theorem.
Standard-library only. Run: python CHECK.py. Finite checks do not prove the theorem.
"""
import math
import random

rng = random.Random(719026)
qc = (7 - 3 * math.sqrt(5)) / 2

def tau(q):
    s = 1 + q
    if q <= qc:
        return (s + math.sqrt(s*s-8*q))/4
    if q <= 1/3:
        return (s + math.sqrt(s*s-5*q))/5
    return q

def coeffs(x):
    return sum(x), x[0]*x[2]+x[0]*x[3]+x[1]*x[3]

def qmin(s,t):
    if t < s/4-1e-12 or t > s/2+1e-12:
        raise ValueError('out of range')
    return 2*s*t-5*t*t if t <= s/3 else t*(s-2*t)

checks=0
for q in [1e-4, 0.01, 0.05, 0.1, qc, .16,.2,.3,1/3,.34,.4,.75,.98]:
    t=tau(q);s=1+q
    assert t>=s/4-1e-10 and t<=s/2+1e-10
    checks+=1
    if q<=1/3:
        assert abs(qmin(s,t)-q)<2e-10,(q,t,qmin(s,t))
        checks+=1
        if q<qc-1e-10:
            r=s-2*t
            assert abs(coeffs((r,t,t,0))[1]-q)<2e-10
            checks+=1
        elif q>qc+1e-10:
            r=s-3*t
            assert r>-1e-10
            assert abs(coeffs((r,t,t,t))[1]-q)<2e-10
            checks+=2
    else:
        x=(q,(1-q)/2,(1-q)/2,q)
        ss,qq=coeffs(x)
        assert abs(ss-s)<2e-10 and abs(qq-q)<2e-10 and max(x)<=t+1e-10
        checks+=1
    for j in range(300):
        raw=[rng.random()+1e-5 for _ in range(4)]
        x=[s*z/sum(raw) for z in raw]
        mx=max(x)
        if mx<=s/2:
            assert coeffs(x)[1]>=qmin(s,mx)-1e-10
            checks+=1

for j in range(250):
    q=10**rng.uniform(-3,-.02)
    t=tau(q)
    s=1+q
    if q<=1/3 and q<=qc:
        r=s-2*t
        eps=min(1e-5,r*t/(3*(r+t)),t/100)
        x4=eps; x3=t
        x1=(q-eps*(s-t-eps))/t
        x2=s-x1-x3-x4
        assert min(x1,x2,x3,x4)>0
        assert abs(coeffs((x1,x2,x3,x4))[1]-q)<1e-12
        assert max(x1,x2,x3,x4)-t<1e-3
        checks+=3
print('CHECK_OK',checks,'cases; first transition',repr(qc))
