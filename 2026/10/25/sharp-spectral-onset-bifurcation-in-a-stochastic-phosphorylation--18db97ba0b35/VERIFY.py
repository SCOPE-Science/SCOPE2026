#!/usr/bin/env python3
"""Reproduce exact modal onset in the four-cycle plus symmetric binary process."""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

checks=0
def check(cond,msg):
    global checks
    assert cond,msg
    checks+=1

def spectrum(a,b,r,omega):
    c=a*a+b*b
    x=omega*omega
    d=a*a-b*b
    return a*(c+x)/(x*x+2*d*x+c*c)+r/(4*r*r+x)

def coeffs(a,b,r):
    c=a*a+b*b; d=a*a-b*b; e=3*b*b-a*a
    A=4*a*r+c
    B=4*a*r*(e-4*r*r)-2*c*d
    C=16*a*r**3*e-c**3
    return A,B,C

def H(a,b,r):
    A,B,C=coeffs(a,b,r)
    return C+max(B,0)**2/(4*A)

def r0(a,b):
    e=3*b*b-a*a
    if e<=0: return float('inf')
    return ((a*a+b*b)**3/(16*a*e))**(1/3)

def threshold(a,b):
    check(3*b*b>a*a, 'oscillatory cycle requirement')
    hi=r0(a,b)
    return brentq(lambda r:H(a,b,r),hi*0.1,hi,xtol=1e-14)

def h(z):
    return 2**(2/3)*(3*z-1)**(2/3)-(1+z)**2/(3*z-1)-2*(1-z)

zc=brentq(h,1/3+1e-6,1-1e-8,xtol=1e-15)
thetac=math.sqrt(zc)
print('zcritical =',format(zc,'.15f'),'theta critical =',format(thetac,'.15f'))
check(0.954<thetac<0.955,'critical bias interval')
check(h(zc+0.00001)>0 and h(zc-0.00001)<0,'critical sign')

for a,b in [(1,.8),(1,.95),(1,.96),(1,.99),(2,1.98),(1,-.99)]:
    r=threshold(a,b);r_z=r0(a,b)
    A,B,C=coeffs(a,b,r)
    if abs(b/a)<=thetac-1e-6:
        check(abs(r-r_z)<1e-11,'continuous threshold follows curvature criterion')
    elif abs(b/a)>=thetac+1e-6:
        check(r+1e-7<r_z,'discontinuous threshold precedes curvature threshold')
        xj=B/(2*A)
        check(xj>0 and abs(C+B*xj-A*xj*xj)<1e-8,'positive tied spectral peak')
    for ratio in [.8,.99,1,1.01,1.2]:
        rr=ratio*r
        hc=H(a,b,rr)
        if ratio<1: check(hc<0,'sharp negative side')
        elif ratio>1: check(hc>0,'sharp positive side')
        else: check(abs(hc)<1e-8,'critical zero')
        for x in [.0001,.01,.09,.2,.5,.9,1.8,3.0]:
            A1,B1,C1=coeffs(a,b,rr)
            c=a*a+b*b;d=a*a-b*b
            F=C1+B1*x-A1*x*x
            delta_formula=x*F/(4*rr*c*(x+4*rr*rr)*(x*x+2*d*x+c*c))
            delta=spectrum(a,b,rr,math.sqrt(x))-spectrum(a,b,rr,0)
            check(abs(delta-delta_formula)<2e-12,'symbolic spectral identity')
    print('a=',a,'b=',b,'r*=',format(r,'.12f'),'r0=',format(r_z,'.12f'),'jump-omega=',format(math.sqrt(max(B,0)/(2*A)),'.12f'))

# Direct 8x8 generator resolvent checks: independent of source spectrum formula.
def direct_spectrum(a,b,r,omega):
    kp=(a+b)/2; km=(a-b)/2
    Qx=np.zeros((4,4))
    for i in range(4):
        Qx[i,(i+1)%4]=kp
        Qx[i,(i-1)%4]=km
        Qx[i,i]=-a
    Qy=np.array([[-r,r],[r,-r]])
    Q=np.kron(Qx,np.eye(2))+np.kron(np.eye(4),Qy)
    f=np.array([v+y-1.5 for v in (0,1,2,1) for y in (0,1)],dtype=float)
    M=-Q.astype(complex)+1j*omega*np.eye(8)
    if omega==0:
        M=M+np.ones((8,8))/8
    sol=np.linalg.solve(M,f)
    return 2*(np.vdot(f,sol)/8).real
for a,b,r in [(1,.8,.5),(1,.99,.6295),(2,1.9,1.45)]:
    for w in [0,.02,.1,.25,.7,1.5,5]:
        got=direct_spectrum(a,b,r,w)
        wanted=spectrum(a,b,r,w)
        check(abs(got-wanted)<3e-12,'eight-state generator resolvent')

# Independent positive-frequency maxima, not using polynomial F.
for b in [.8,.96,.99]:
    r=threshold(1,b)
    for rfactor in [.98,1.02]:
        rr=r*rfactor
        maximized=minimize_scalar(lambda w:-spectrum(1,b,rr,w),bounds=(0,2),method='bounded',options={'xatol':1e-12})
        gain=max(-maximized.fun-spectrum(1,b,rr,0),0)
        check((gain>1e-8)==(rfactor>1),'direct global frequency search')
        if rfactor>1:check(maximized.x>1e-3,'positive peak')
        print('b=',b,'rate=',rr,'positive gain=',gain,'maximizing omega=',maximized.x)
print('VERIFICATION PASS:',checks,'assertions')
