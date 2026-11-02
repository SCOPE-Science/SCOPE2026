"""Deterministic numerical corroboration for two-point harmonic-measure observation.
Analytical proof is independent of these finite tests.
"""
import math
import numpy as np
from scipy.optimize import brentq

ncheck=0

def chk(test, label=''):
    global ncheck
    assert bool(test), label
    ncheck+=1

def p(r, x):
    return (1-r*r)/(1+r*r-2*r*np.cos(x))

def h(r,a,t):
    return 0.5*(p(r,t-a)+p(r,t+a))

def phases(r,a):
    k=(1+r*r)/(2*r)
    c=math.cos(a)
    cc=(-k+math.sqrt(k*k+8))/2
    bimodal=c < cc - 1e-13
    if not bimodal: return False, 0.0, 0.0, cc
    s=math.sin(a)
    if c<1e-9: um=0.0
    else: um=(k-s*math.sqrt(k*k-c*c))/c
    thm=math.acos(max(-1,min(1,um)))
    th0=math.acos(max(-1,min(1,k*c+c*c-1)))
    return True,thm,th0,cc

def F(r,x):
    # Continuous lifted primitive of the Poisson kernel.
    y=(x+math.pi)%(2*math.pi)-math.pi
    m=math.floor((x+math.pi)/(2*math.pi))
    return 2*math.atan(((1+r)/(1-r))*math.tan(y/2))+2*math.pi*m

def interval_mass(r,a,lo,hi):
    return (F(r,hi-a)-F(r,lo-a))/(2*math.pi)

def optimum(r,a,rho):
    b,tm,t0,cc=phases(r,a)
    if not b or rho >= t0/math.pi:
        beta=math.pi*rho
        return (interval_mass(r,a,-beta,beta), [(0,beta)])
    gap=math.pi*rho
    left=max(0.,tm-gap)
    right=min(tm,math.pi-gap)
    lo=brentq(lambda u:h(r,a,u)-h(r,a,u+gap),left,right,xtol=1e-13)
    hi=lo+gap
    v=interval_mass(r,a,lo,hi)+interval_mass(r,a,-hi,-lo)
    return v, [(lo,hi)]

for r in [0.1,0.2,0.5,0.75,0.9]:
    k=(1+r*r)/(2*r)
    cs=(-k+math.sqrt(k*k+8))/2
    crit=math.acos(cs)
    for a in [0.1*crit,0.8*crit,crit+0.1*(math.pi/2-crit),crit+0.5*(math.pi/2-crit),math.pi/2]:
        b,tm,t0,_=phases(r,a)
        c=math.cos(a)
        if b:
            chk(0<tm<math.pi,'mode interior')
            chk(0<t0<=math.pi+1e-12,'critical area')
            chk(abs(h(r,a,0)-h(r,a,t0))<1e-8,'level crossing')
            chk(h(r,a,tm)>h(r,a,0)+1e-12,'peak rise')
        else:
            chk(abs(t0)<1e-14,'one-band classification')
            chk(h(r,a,0)>h(r,a,0.02),'unimodal head')
        for rho in [0.03,0.12,0.3,0.57,0.84,0.97]:
            val,regions=optimum(r,a,rho)
            chk(0<val<1+1e-12,'mass bounds')
            if b and rho < t0/math.pi:
                lo,hi=regions[0]
                chk(lo>=-1e-9 and hi <= math.pi+1e-9, 'two-arc geometry')
                chk(abs(hi-lo-math.pi*rho)<1e-11,'two-arc length')
                chk(abs(h(r,a,lo)-h(r,a,hi))<1e-9, 'equal threshold')
            else:
                chk(abs(regions[0][1]-math.pi*rho)<1e-12,'single-arc length')
            chk(val+1e-10>=interval_mass(r,a,-math.pi*rho,math.pi*rho),'connected penalty')
            # Discrete bathtub optimum: take fixed-count highest midpoint samples.
            n=8192
            ts=-math.pi+(np.arange(n)+0.5)*(2*math.pi/n)
            mix=h(r,a,ts)
            j=int(round(rho*n)); ix=np.argpartition(mix,-j)[-j:]
            grid_opt=float(np.sum(mix[ix])/n)
            chk(abs(val-grid_opt)<0.0009, 'discrete bathtub value')
            mean1=float(np.sum(p(r,ts[ix]-a))/n)
            mean2=float(np.sum(p(r,ts[ix]+a))/n)
            chk(abs(mean1-mean2)<0.003,'reflection-balanced finite grid')

# A few finite-difference checks of the rational derivative polynomial.
for r,a in [(0.2,0.3),(0.5,1.0),(0.9,0.5)]:
    c=math.cos(a); s=math.sin(a); k=(1+r*r)/(2*r); C=(1-r*r)/(2*r)
    for u in [-0.91,-0.4,0.0,0.4,0.91]:
        Q=lambda x:x*x-2*k*c*x+k*k-s*s
        H=lambda x:C*(k-c*x)/Q(x)
        Fpoly=c*u*u-2*k*u+c*(k*k+s*s)
        der=C*Fpoly/Q(u)**2
        approx=(H(u+1e-6)-H(u-1e-6))/(2e-6)
        chk(abs(der-approx)<1e-5*(1+abs(der)),'rational derivative')
print(f'PASS {ncheck} deterministic assertions')
