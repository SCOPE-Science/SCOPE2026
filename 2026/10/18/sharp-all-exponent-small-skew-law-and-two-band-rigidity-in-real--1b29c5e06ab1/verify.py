#!/usr/bin/env python3
"""Finite diagnostic checks for sharp skew first-order coefficient (not an infinite proof)."""
import math,random
from scipy.optimize import brentq

def param(p):
    assert p>1 and p!=2
    def logcosh(t):return math.logaddexp(t,-t)-math.log(2) if hasattr(math,'logaddexp') else (abs(t)+math.log1p(math.exp(-2*abs(t)))-math.log(2))
    g=lambda s:logcosh((p-1)*s)-logcosh(s)-math.log(p-1)
    hi=1.
    while g(hi)*(p-2)<0: hi*=2
    root=brentq(g,0,hi,xtol=1e-14)
    t=math.exp(-root)
    c=t*abs(1-t**(p-2))/(1+t**p)
    return t,c,root

random.seed(20261015)
checks=0
for p in [1.2,1.5,1.8,1.95,2.05,2.3,3,4,6,10,20]:
    t,c,s=param(p)
    assert abs(math.cosh((p-1)*s)/(math.cosh(s))-(p-1))<1e-9
    a=(1+t**p)**(-1/p); b=t*a
    sg=1 if p>2 else -1
    xx=(a,b); yy=(-sg*b,sg*a)
    D=sum(math.copysign(abs(x)**(p-1),x)*y-math.copysign(abs(y)**(p-1),y)*x for x,y in zip(xx,yy))
    assert abs(D+2*c)<1e-10,(p,D,c)
    for j in range(200):
        r=math.exp(random.uniform(-12,12)); f=r*abs(1-r**(p-2))/(1+r**p)
        assert f<=c+1e-11,(p,r,f,c)
        checks+=1
    for tau in (1e-3,1e-4):
        u=(sum(abs(x+tau*y)**p for x,y in zip(xx,yy)))**(1/p)
        v=(sum(abs(tau*x-y)**p for x,y in zip(xx,yy)))**(1/p)
        assert abs(u-v)<1e-10
        assert abs((1-u)/tau-c)<.1,(p,tau,u,c)
        checks+=1
assert abs(param(4)[1]-1/(2*math.sqrt(2)))<1e-12
assert abs(param(6)[1]-.5)<1e-12
print('CHECK_OK',checks)
