#!/usr/bin/env python3
"""Standalone deterministic GeCo2 arithmetic checks (no external dependencies)."""
import math

checks=0

def verify(condition, message):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(message)

def phi(v):
    return -math.expm1(-v)/v if v > 0.0 else 1.0

def pars(z):
    u=math.exp(-z)
    t=z*(1+u)/2
    b=z*(1+u)-2*(1-u)
    return u,t,b

def scalar_step(x,z):
    _,t,b=pars(z)
    v=b*abs(x)/(1+abs(x))
    return x*(1-t*phi(v))

def source_step(y1,y2,z):
    """Exactly the two componentwise published stages, using h=z/2."""
    h=z/2
    a1=y2-y1
    a2=y1-y2
    q=phi(z)
    st1=y1+h*q*a1
    st2=y2+h*q*a2
    as1=st2-st1
    as2=st1-st2
    w1=2*q*a1-a1-as1
    w2=2*q*a2-a2-as2
    v=h*(max(w1,0.0)/y1+max(w2,0.0)/y2)
    return (y1+h*0.5*phi(v)*(a1+as1),y2+h*0.5*phi(v)*(a2+as2))

def bisect(f,lo,hi,its=120):
    vlo=f(lo);vhi=f(hi)
    verify(vlo*vhi<0,'bracket signs')
    for _ in range(its):
        mid=(lo+hi)/2
        if mid==lo or mid==hi: break
        if f(mid)*vlo>0:
            lo=mid;vlo=f(mid)
        else: hi=mid;vhi=f(mid)
    return (lo+hi)/2

zc=bisect(lambda z:z*(1+math.exp(-z))-4,3,4)
_,tc,bc=pars(zc)
verify(abs(zc-3.922359502743079)<2e-14,'critical step')
verify(abs(tc-2)<1e-13,'critical t')
verify(abs(1/bc-0.490294937842885)<1e-12,'critical coefficient')

for z in [zc,zc+0.01,4.0,5.0,10.0,20.0,100.0]:
    u,t,b=pars(z)
    verify(b>0 and t>=2-1e-12,'parameter positivity')
    for x in [-0.91,-0.65,-0.2,-0.05,0.0,0.05,0.2,0.65,0.91]:
        mass=3.75
        y1=mass*(1+x)/2
        y2=mass*(1-x)/2
        out1,out2=source_step(y1,y2,z)
        xx=(out1-out2)/mass
        verify(abs(out1+out2-mass)<2e-13*max(1,mass),'conservation')
        verify(out1>0 and out2>0,'positive updates')
        verify(abs(xx-scalar_step(x,z))<6e-14,'stage/scalar identity')
    if z>zc+1e-7:
        def eq(r):return t*phi(b*r/(1+r))-2
        rr=bisect(eq,1e-14,0.999999)
        verify(0<rr<1,'cycle in domain')
        verify(abs(scalar_step(rr,z)+rr)<1e-12,'positive cycle point')
        verify(abs(scalar_step(-rr,z)-rr)<1e-12,'negative cycle point')
        v=b*rr/(1+rr)
        mu=1-(2-t*math.exp(-v))*(1-v/b)
        verify(abs(mu)<1,'local multiplier')
        eps=1e-6
        derivative=(scalar_step(rr+eps,z)-scalar_step(rr-eps,z))/(2*eps)
        verify(abs(derivative+mu)<6e-7,'finite-difference derivative')

verify(abs(bisect(lambda r:pars(5.0)[1]*phi(pars(5.0)[2]*r/(1+r))-2,1e-12,0.999)-0.1864148067313465)<1e-12,'sample amplitude')
_,t100,b100=pars(100)
r100=bisect(lambda r:t100*phi(b100*r/(1+r))-2,0.01,0.9)
verify(abs(r100-1/3)<0.02,'stiff amplitude tendency')

# Critical 1/n convergence is a theorem, not proved by this finite check.
r=0.2
for i in range(20000):
    r=abs(scalar_step(r,zc))
verify(abs(20000*r-1/bc)<0.007,'finite-time critical asymptotic sanity check')
print('PASS: %d deterministic GeCo2 checks' % checks)
