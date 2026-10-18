#!/usr/bin/env python3
"""Deterministic tests for planar-section topology of convex-meridian toroids.
Only geometric computations; no external dependencies beyond numpy/scipy.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

def support(s,c,a,b,kind):
    if kind=='ellipse': return math.hypot(a*s,b*c)
    if kind=='rectangle': return a*abs(s)+b*abs(c)
    if kind=='diamond': return max(a*abs(s),b*abs(c))
    raise ValueError(kind)

def law(R,a,b,kind):
    assert R>a>0 and b>0
    H=lambda th:support(math.sin(th),math.cos(th),a,b,kind)
    f=lambda th:H(th)-R*math.sin(th)
    theta=brentq(f,1e-12,math.pi/2)
    C=quad(lambda th:H(th)*math.sin(th),0,math.pi/2,epsabs=2e-12,points=[math.atan2(b,a)] if kind=='diamond' else None)[0]
    Z=C+math.pi*R/4
    A=quad(lambda th:f(th)*math.sin(th),0,theta,epsabs=2e-12)[0]
    B=Z-2*C+A  # int (R sin-H) sin dtheta + positive part correction
    one=1-(A+B)/Z
    return theta,C,Z,np.array([A/Z,one,B/Z])

def topo_bruteforce(R,a,b,kind,th,t,N=2001):
    # Directly sample the meridian feasibility for 2001 azimuths.
    u=np.linspace(0,2*math.pi,N,endpoint=False)
    v=np.cos(u)
    s,c=math.sin(th),math.cos(th)
    H=np.array([support(s*z,c,a,b,kind) for z in v])
    feasible=np.logical_and(t>=R*s*v-H,t<=R*s*v+H)
    if feasible.all(): return 0 # annulus
    transition=np.count_nonzero(feasible != np.roll(feasible,1))
    # if no near tangency or undersampling, each feasible azimuth arc corresponds to a disk
    return transition//2

def topo_formula(R,a,b,kind,th,t):
    v=R*math.sin(th); H=support(math.sin(th),math.cos(th),a,b,kind)
    if abs(t)>v+H:return -1
    if H>v and abs(t)<H-v:return 0
    if v>H and abs(t)<v-H:return 2
    return 1

def run():
    rng=np.random.default_rng(18832026)
    comparisons=0
    max_mc=0
    for kind,a,b,R in [
        ('ellipse',1.0,1.0,2.0),('ellipse',1.0,0.75,2.4),
        ('ellipse',1.6,0.7,2.5),('ellipse',0.8,1.5,1.4),
        ('rectangle',1.0,0.55,2.2),('diamond',1.0,1.25,2.5)]:
        th,C,Z,p=law(R,a,b,kind)
        assert abs(p.sum()-1)<1e-11 and np.min(p)>0
        assert abs(p[0]-p[2]-(C-math.pi*R/4)/Z)<3e-11
        # Probe planar topology via fine-grid feasible-azimuth count, away from transitions.
        for _ in range(150):
            ang=rng.uniform(0.01,math.pi/2-.01)
            t=rng.uniform(-1.1*(R*math.sin(ang)+support(math.sin(ang),math.cos(ang),a,b,kind)),1.1*(R*math.sin(ang)+support(math.sin(ang),math.cos(ang),a,b,kind)))
            guess=topo_formula(R,a,b,kind,ang,t)
            if guess==-1:continue
            h=support(math.sin(ang),math.cos(ang),a,b,kind)
            if min(abs(abs(t)-(R*math.sin(ang)+h)), abs(abs(t)-abs(R*math.sin(ang)-h)))<.01:continue
            actual=topo_bruteforce(R,a,b,kind,ang,t)
            assert actual==guess,(kind,a,b,R,ang,t,actual,guess)
            comparisons+=1
        # Weighted conditioned on hit: draw theta from sin theta*(R sin theta + H),
        # then t uniform in conditional support.
        grid=np.linspace(0,math.pi/2,4001)
        w=np.sin(grid)*(R*np.sin(grid)+np.array([support(math.sin(x),math.cos(x),a,b,kind) for x in grid]))
        cdf=np.cumsum((w[1:]+w[:-1])*.5*np.diff(grid))
        cdf=np.r_[0,cdf/cdf[-1]]
        n=75000
        u=rng.random(n)
        ang=np.interp(u,cdf,grid)
        hh=np.array([support(math.sin(x),math.cos(x),a,b,kind) for x in ang]);vs=R*np.sin(ang)
        off=(2*rng.random(n)-1)*(vs+hh)
        ann=((hh>vs)&(np.abs(off)<hh-vs)).mean()
        two=((vs>hh)&(np.abs(off)<vs-hh)).mean()
        empirical=np.array([ann,1-ann-two,two])
        max_mc=max(max_mc,np.max(np.abs(empirical-p)))
        assert np.max(np.abs(empirical-p))<.013,(kind,p,empirical)
        print('case',kind,'axes',a,b,'R',R,'exact',np.round(p,7),'MC',np.round(empirical,7))
    # Inverse: reconstruct support H at several angles by A'(R) and known moment C.
    errors=[]
    for a,b in [(1.0,1.0),(.65,1.45),(1.55,.85)]:
        for theta in [0.23,0.42,0.75,1.12,1.4]:
            R=support(math.sin(theta),math.cos(theta),a,b,'ellipse')/math.sin(theta)
            assert R>a
            C=law(R,a,b,'ellipse')[1]
            step=R*2e-5
            def A(r):
                _,cc,z,p=law(r,a,b,'ellipse')
                assert abs(cc-C)<1e-9
                return z*p[0]
            derivative=(A(R+step)-A(R-step))/(2*step)
            # unique inversion of F from differentiated annulus numerator
            F=lambda x:x/2-math.sin(2*x)/4
            theta_est=brentq(lambda x:F(x)+derivative,0,math.pi/2)
            errors.append(abs(theta_est-theta));assert abs(theta_est-theta)<2e-6,(a,b,theta,theta_est)
    print('TOROID_TOPOLOGY_INVERSE_OK brute_comparisons',comparisons,'max_MC_error',round(float(max_mc),6),'inverse_tests',len(errors),'max_inverse_error',max(errors))

if __name__=='__main__':run()
