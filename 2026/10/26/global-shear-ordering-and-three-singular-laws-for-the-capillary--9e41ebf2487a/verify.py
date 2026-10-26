#!/usr/bin/env python3
"""Finite independent checks of a water-wave stationary selector; Python standard library only."""
import math

def A(x):
    if x < 1e-3: return 1 + x*x/3 - x**4/45 + 2*x**6/945
    return x/math.tanh(x)
def R(x):
    if x < 1e-3: return 1/3 - 2*x*x/45 + 2*x**4/315 - 4*x**6/4725
    if x > 300: return 1/(2*x)
    return (1/(x*math.tanh(x)) - 1/math.sinh(x)**2)/2
def P(x):
    if x < 1e-3: return 1 + x**4/45 - 4*x**6/945
    return A(x)-x*x*R(x)
def d(p,g):
    t=math.sqrt(g*g+4*p)
    return (t+g)/(2*p) if g>=0 else 2/(t-g)
def phase(x,B,g):
    p=A(x)
    t=math.sqrt(g*g+4*p*(1+B*x*x))
    return (t+g)/(2*p) if g>=0 else 2*(1+B*x*x)/(t-g)
def sel(x,g):return R(x)*d(P(x),g)**2
def bisect(B,g):
    lo=1e-7;hi=1.
    while sel(hi,g)>=B:
        hi*=2
        assert hi<1e9
    assert sel(lo,g)>B
    for _ in range(90):
        mid=(lo+hi)/2
        if sel(mid,g)>B:lo=mid
        else:hi=mid
    return (lo+hi)/2

def close(a,b,atol=1e-9,rtol=2e-8):
    assert math.isfinite(a) and math.isfinite(b)
    assert abs(a-b)<=atol+rtol*max(abs(a),abs(b)),(a,b)

n=0
for g in [-5.,-2.,-0.5,0.,1.,4.,10.]:
    c0=d(1,g);bc=c0*c0/3
    for frac in [.03,.3,.7,.95,.99]:
        B=bc*frac;x=bisect(B,g); c=phase(x,B,g)
        close(A(x)*c*c-g*c,1+B*x*x,rtol=2e-11)
        close(P(x)*c*c-g*c,1,rtol=2e-10)
        close(B,sel(x,g),rtol=2e-12)
        for s in [.25,.75,1.3,2.5]:
            assert phase(s*x,B,g)>c*(1+1e-14),(B,g,x,s)
        n+=1
    for frac in [1.,1.2,2.]:
        B=bc*frac
        vals=[phase(x,B,g) for x in [1e-4,.015,.1,.4,1,4,15,90]]
        assert all(a<b for a,b in zip(vals,vals[1:])),(B,g,vals)
        n+=1
for B in [.02,.1,.5,2.]:
    gc=(3*B-1)/math.sqrt(3*B)
    xs=[bisect(B,gc+shift) for shift in [.1,.25,.5,1,2,5,10]]
    assert all(x<y for x,y in zip(xs,xs[1:])),(B,xs)
    n+=1
for g in [-2.,0.,1.,3.]:
    c0=d(1,g);bc=c0*c0/3
    for eta in [1e-2,2e-3,4e-4]:
        x=bisect(bc*(1-eta),g)
        pred=math.sqrt(7.5*eta)
        assert abs(x/pred-1)<1.5*eta
        n+=1
for g in [-3.,-1.,0.,2.,5.]:
    for B in [1e-3,1e-4,1e-5,1e-6]:
        c0=d(1,g)
        if B>=c0*c0/3:continue
        x=bisect(B,g)
        asym=B**(-.5)+g/math.sqrt(2)*B**(-.25)-g**3/(16*math.sqrt(2))*B**.25
        assert abs(x-asym)< max(1,abs(g)**4)*3*math.sqrt(B),(g,B,x,asym)
        n+=1
B=.1
for g in [20,40,100,500,1000,5000]:
    x=bisect(B,g)
    pred=(2/B)**(1/3)*g**(2/3)
    assert abs(x/pred-1)<max(.3,10*g**(-2/3)),(g,x,pred)
    n+=1
print('PASS:',n,'parameter families; exact identities, global comparisons, shear order and three asymptotic regimes')
