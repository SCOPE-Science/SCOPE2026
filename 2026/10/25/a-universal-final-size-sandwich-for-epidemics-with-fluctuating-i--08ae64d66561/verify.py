#!/usr/bin/env python3
"""Independent numerical illustration of the analytic stationary-risk final-size sandwich."""
from math import exp, isfinite

def rhs(y,k):
    a,b,i=y
    return (-.5*i*a+k*(b-a),-3.*i*b+k*(a-b),i*(.5*a+3.*b)-i)

def rk4(y,h,k):
    q=rhs(y,k)
    b=[v+h*t/2 for v,t in zip(y,q)]
    r=rhs(b,k)
    c=[v+h*t/2 for v,t in zip(y,r)]
    s=rhs(c,k)
    d=[v+h*t for v,t in zip(y,s)]
    t=rhs(d,k)
    return [v+h*(q[j]+2*r[j]+2*s[j]+t[j])/6 for j,v in enumerate(y)]

def attack(k,h):
    y=[.4975,.4975,.005]
    steps=int(110/h)
    for _ in range(steps): y=rk4(y,h,k)
    assert min(y)>-1e-9, y
    assert y[2]<1e-11,(k,h,y)
    return 1-y[0]-y[1]

def root(f,lo=0.,hi=2.):
    assert f(lo)<0<f(hi)
    for _ in range(120):
        mid=(lo+hi)/2
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

gamma=1.
S0=.995
I0=.005
z0=root(lambda z:gamma*z-I0-S0+S0*(exp(-.5*z)+exp(-3*z))/2)
zh=root(lambda z:gamma*z-I0-S0+S0*exp(-1.75*z))
vals={k:(attack(k,.01),attack(k,.005)) for k in [0.,.2,1.,5.]}
assert z0<vals[.2][1]<zh,(z0,vals,zh)
assert all(abs(x-y)<2e-7 for x,y in vals.values()),vals
assert abs(vals[0.][1]-z0)<1e-7,(vals[0.],z0)
assert vals[.2][1]>vals[0.][1] and vals[5.][1]>vals[1.][1]>vals[.2][1]
assert abs(vals[.2][1]-.63132193)<.00005, vals[.2]
print('PASS: two independent step sizes, risk-switching example, root bounds and conservation')
print('frozen:',z0,'switching:',vals[.2][1],'homogeneous:',zh)
