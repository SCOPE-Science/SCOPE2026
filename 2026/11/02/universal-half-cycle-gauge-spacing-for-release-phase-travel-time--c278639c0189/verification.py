"""Reproducible numerical cross-checks for a half-wave-symmetric flow theorem.
Only finite tests; the universal quantifiers are established analytically.
Requires Python 3, numpy, scipy.
"""
import math
from scipy.optimize import brentq

TAU=2*math.pi

def F(t,e,k):
    s=math.sin(t)
    if k==1:return e*s
    if k==3:return e*(s-s**3/3)
    if k==5:return e*(s-2*s**3/3+s**5/5)
    raise ValueError

def v(t,e,k):return 1+e*math.cos(t)**k

def roots(y,e,k):
    fast=brentq(lambda t:t+2*F(t/2,e,k)-y,0,TAU,xtol=5e-15)
    slow=brentq(lambda t:t-2*F(t/2,e,k)-y,0,TAU,xtol=5e-15)
    return fast,slow

def travel(phi,lam,e,k):
    # The integrated trajectory is x(t)=t+F(t)-F(phi).
    n=int(lam//TAU)
    y=lam-n*TAU
    if abs(y)<1e-13:return n*TAU
    small=brentq(lambda t:t+F(phi+t,e,k)-F(phi,e,k)-y,0,TAU,xtol=5e-15)
    return n*TAU+small

def delta(e,k):
    return brentq(lambda d:F(math.pi/2-d,e,k)-d,0,math.pi/2,xtol=5e-15)

n_checks=0
for k in (1,3,5):
 for e in (0.1,0.5,0.9):
    d=delta(e,k)
    a,b=roots(math.pi,e,k)
    assert abs((b-a)-4*d)<3e-12
    assert abs(a+b-2*math.pi)<3e-12
    n_checks+=2
    for y in (0.03,0.6,1.5,2.3,math.pi,4.,5.2,TAU-0.1):
        fast,slow=roots(y,e,k)
        assert 0<fast<=slow<TAU
        assert slow-fast<=4*d+1e-12
        if abs(y-math.pi)>1e-8:assert slow-fast<4*d-1e-8
        vals=[travel(TAU*j/64,y,e,k) for j in range(64)]
        assert min(vals)>=fast-2e-12 and max(vals)<=slow+2e-12
        assert abs(travel(-fast/2,y,e,k)-fast)<3e-12
        assert abs(travel(math.pi-slow/2,y,e,k)-slow)<3e-12
        n_checks+=5
    # Check exact length phase independence and cusp slope against direct roots.
    for m in (1,2,3):
        assert max(abs(travel(j*TAU/19,m*TAU,e,k)-m*TAU) for j in range(19))<1e-12
        for sign in (-1,1):
            h=3e-6*sign
            y=h if h>0 else TAU+h
            ff,ss=roots(y,e,k)
            slope=(ss-ff)/abs(h)
            target=2*e/(1-e**2)
            assert abs(slope-target)<5e-3
            n_checks+=2
    # Half-wave symmetric profile has same optimal sensor-length, not necessarily same width.
    assert d>0 and d<math.pi/2
    n_checks+=1

print('PASS',n_checks,'analytical-identity spot checks; profiles cos(t), cos(t)^3, cos(t)^5; contrasts 0.1, 0.5, 0.9')
for k in (1,3,5):
 e=.5; d=delta(e,k)
 print('profile',k,'contrast',e,'delta',format(d,'.12f'),'max_width',format(4*d,'.12f'))
