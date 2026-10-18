#!/usr/bin/env python3
"""Independent finite checks of analytic sign, center-zero, and derivative identities."""
import cmath
import math

def zak(t, xi, atoms, h):
    amin = min(a for a, _ in atoms)
    cutoff = max(8, math.ceil(math.sqrt(54.0 / (amin*h*h)) + 3))
    return math.sqrt(h) * sum(
        w * math.exp(-a*(h*(t-k))**2) * cmath.exp(2j*math.pi*k*xi)
        for a, w in atoms for k in range(-cutoff, cutoff+1)
    )

def derivatives(t,xi,atoms,h):
    amin=min(a for a,_ in atoms)
    K=max(8,math.ceil(math.sqrt(54/(amin*h*h))+3))
    dt=0j; dtheta=0j
    for a,w in atoms:
        for k in range(-K,K+1):
            z=math.sqrt(h)*w*math.exp(-a*(h*(t-k))**2)*cmath.exp(2j*math.pi*k*xi)
            dt += -2*a*h*h*(t-k)*z
            dtheta += 1j*k*z
    return dt,dtheta

suites=[([(0.8,1.)],1.), ([(1.,1.),(100.,1.)],1.),
        ([(0.4,1.2),(3.,0.7),(30.,4.)],1.3),
        ([(0.7,0.6),(1.5,1.5),(2.,0.7)],1.1),
        ([(1.,1.),(10.,1.)],0.8), ([(0.5,2.),(1.5,1.),(5.,0.2)],2.1)]
count=0
for atoms,h in suites:
    for t in [i/24 for i in range(1,24)]:
        for xi in [j/30 for j in range(1,15)]:
            z=zak(t,xi,atoms,h)
            assert z.imag>1e-10, ('interior sign',atoms,h,t,xi,z)
            assert zak(t,1-xi,atoms,h).imag < -1e-10
            count+=2
    for t in [i/40 for i in range(20)]:
        assert zak(t,.5,atoms,h).real>1e-11, ('half frequency left',atoms,h,t)
        assert zak(1-t,.5,atoms,h).real < -1e-11
        count+=2
    for xi in [i/26 for i in range(26)]:
        assert zak(0,xi,atoms,h).real>0
        count+=1
    center=zak(.5,.5,atoms,h)
    assert abs(center) < 1e-10
    dt,dth=derivatives(.5,.5,atoms,h)
    assert dt.real < -1e-10 and abs(dt.imag)<1e-10
    assert dth.imag < -1e-10 and abs(dth.real)<1e-10
    det=dt.real*dth.imag-dt.imag*dth.real
    assert det > 1e-20
    count+=5
for a in [.02,.2,1,4,30,100]:
    dt,dth=derivatives(.5,.5,[(a,1)],1.)
    assert abs(dt+2j*a*dth)<1e-8
    count+=1
x=.1
u=math.exp(-x*x);v=math.exp(-100*x*x)
g=u+v; gp=-2*x*(u+100*v);gpp=(4*x*x-2)*u+(4*10000*x*x-200)*v
assert g*gpp-gp*gp>40
print('VERIFY_OK',count,'finite Gaussian-mixture Zak checks; strict-sector tests, center zero, Jacobian, Gaussian derivative identity, and non-logconcavity')
