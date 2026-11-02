#!/usr/bin/env python3
"""Numerical consistency tests of a telegraph-modulated elastic mode.

This independent finite test supplements, but does not certify, the proof.
Uses the Python standard library only.
"""
import math
import random


def growth(p,x,sigma,kappa,a,r):
    return -p*(sigma*x+kappa*x*x)-r+math.hypot(r,p*a*x)


def threshold_H(p,x,sigma,kappa,r):
    return (sigma+kappa*x)**2+2*r*(sigma+kappa*x)/(p*x)


def bisect_positive_zero(fun,left,right,iterations=100):
    fl=fun(left)
    fr=fun(right)
    assert fl*fr < 0, (left,right,fl,fr)
    for _ in range(iterations):
        mid=(left+right)/2
        fm=fun(mid)
        if fl*fm <= 0:
            right=mid
            fr=fm
        else:
            left=mid
            fl=fm
    return (left+right)/2


def critical_amplitude(p,sigma,kappa,r):
    fun=lambda x:kappa*x*x*(sigma+kappa*x)-r*sigma/p
    upper=1.0
    while fun(upper)<0:
        upper*=2.0
    x=bisect_positive_zero(fun,0,upper)
    return math.sqrt(threshold_H(p,x,sigma,kappa,r)),x


def critical_moment(sigma,kappa,a,r):
    assert a>sigma
    fun=lambda u:2*u**3-sigma*u*u-sigma*a*a
    u=bisect_positive_zero(fun,sigma,a)
    p=2*r*kappa*u/((u-sigma)*(a*a-u*u))
    return p,(u-sigma)/kappa


def exact_moment(p,x,sigma,kappa,a,r,t):
    o=math.hypot(r,p*a*x)
    # stable sum of two exponentials
    lead=-p*(sigma*x+kappa*x*x)-r+o
    tail=-p*(sigma*x+kappa*x*x)-r-o
    return 0.5*((1+r/o)*math.exp(lead*t)+(1-r/o)*math.exp(tail*t))


def rk4_telegraph_ode(p,x,sigma,kappa,a,r,t,steps):
    # Explicit Runge-Kutta 4 applied to two-state tilted backward equations.
    h=t/steps
    z=p*a*x
    A=p*(sigma*x+kappa*x*x)
    def f(u,v):
        return (-(A+r+z)*u+r*v,
                 r*u-(A+r-z)*v)
    u=v=1.0
    for _ in range(steps):
        a1,b1=f(u,v)
        a2,b2=f(u+h*a1/2,v+h*b1/2)
        a3,b3=f(u+h*a2/2,v+h*b2/2)
        a4,b4=f(u+h*a3,v+h*b3)
        u+=h*(a1+2*a2+2*a3+a4)/6
        v+=h*(b1+2*b2+2*b3+b4)/6
    return (u+v)/2


def finite_circle_threshold(L,sigma,kappa,a,r):
    if a<=sigma or L<=2*math.pi*math.sqrt(kappa/(a-sigma)):
        return math.inf
    total=math.floor(L*math.sqrt((a-sigma)/kappa)/(2*math.pi))+1
    values=[]
    for n in range(1,total+1):
        k=2*math.pi*n/L
        u=sigma+kappa*k*k
        if u<a:
            values.append(2*r*u/(k*k*(a*a-u*u)))
    return min(values) if values else math.inf


def curvature(sigma,kappa,a,r):
    pc,xstar=critical_moment(sigma,kappa,a,r)
    u=sigma+kappa*xstar
    Gpp=-1/u**2+1/(u-sigma)**2+2*(a*a+u*u)/(a*a-u*u)**2
    return pc*(2*kappa*math.sqrt(xstar))**2*Gpp


def run():
    rnd=random.Random(20261028)
    total=0
    for _ in range(200):
        sigma,kappa,a,r,p=(10**rnd.uniform(-.8,.7) for _ in range(5))
        ac,xc=critical_amplitude(p,sigma,kappa,r)
        hc=threshold_H(p,xc,sigma,kappa,r)
        assert abs(ac**2-hc)<1e-10*max(1,hc)
        assert threshold_H(p,xc*.98,sigma,kappa,r)>hc
        assert threshold_H(p,xc*1.02,sigma,kappa,r)>hc
        assert growth(p,xc,sigma,kappa,ac*.9999,r)<0
        assert growth(p,xc,sigma,kappa,ac*1.0001,r)>0
        total+=5
    for _ in range(170):
        sigma,kappa,r=(10**rnd.uniform(-.8,.6) for _ in range(3))
        a=sigma*(1+rnd.uniform(.02,1.7))
        pc,xc=critical_moment(sigma,kappa,a,r)
        assert abs(growth(pc,xc,sigma,kappa,a,r))<1e-8*max(1,pc)
        assert growth(pc*.99,xc,sigma,kappa,a,r)<0
        assert growth(pc*1.01,xc,sigma,kappa,a,r)>0
        assert growth(pc,xc*.99,sigma,kappa,a,r)<0
        assert growth(pc,xc*1.01,sigma,kappa,a,r)<0
        total+=5
    for _ in range(220):
        sigma,kappa,a,r,p=(10**rnd.uniform(-.6,.5) for _ in range(5))
        x=10**rnd.uniform(-.5,.3)
        t=rnd.uniform(.005,.35)
        closed=exact_moment(p,x,sigma,kappa,a,r,t)
        rk4=rk4_telegraph_ode(p,x,sigma,kappa,a,r,t,800)
        assert math.isclose(closed,rk4,rel_tol=1e-9,abs_tol=1e-10),(closed,rk4)
        assert closed>0
        total+=2
    for _ in range(120):
        sigma,kappa,r=(10**rnd.uniform(-.4,.5) for _ in range(3))
        a=sigma*(1+rnd.uniform(.1,1.3))
        L0=2*math.pi*math.sqrt(kappa/(a-sigma))
        assert math.isinf(finite_circle_threshold(L0*.99,sigma,kappa,a,r))
        assert math.isinf(finite_circle_threshold(L0,sigma,kappa,a,r))
        eps=1e-5*L0
        pcL=finite_circle_threshold(L0+eps,sigma,kappa,a,r)
        coeff=r*kappa*L0/(2*(a-sigma)**2)
        assert abs(pcL*eps/coeff-1)<3e-4, (pcL,eps,coeff)
        assert math.isfinite(finite_circle_threshold(L0*1.2,sigma,kappa,a,r))
        total+=4
    for _ in range(100):
        sigma,kappa,r=(10**rnd.uniform(-.25,.25) for _ in range(3))
        a=sigma*(1+rnd.uniform(.2,1.2))
        pc,xc=critical_moment(sigma,kappa,a,r)
        kstar=math.sqrt(xc)
        fpp=curvature(sigma,kappa,a,r)
        assert fpp>0
        L=rnd.uniform(350,700)
        pcL=finite_circle_threshold(L,sigma,kappa,a,r)
        theta=L*kstar/(2*math.pi)
        d=abs(theta-round(theta))
        predicted=pc+2*math.pi**2*fpp*d*d/L**2
        # Parameter-uniform coefficient is not claimed; check a modest fixed
        # relative tolerance to the leading 1/L^2 correction instead.
        assert abs(pcL-predicted)<max(3e-4,10*fpp/L**2),(pcL,predicted)
        total+=2
    for p in (1,2,3,5,10):
        ac,xc=critical_amplitude(p,1.,.5,.7)
        assert ac>1
        print(f'p={p} critical_amplitude={ac:.10f} critical_squared_wave_number={xc:.10f}')
        total+=1
    for eps in (.1,.04,.02,.01):
        pc,xc=critical_moment(1.,.5,1+eps,.7)
        assert abs(pc*eps*eps-4*.7*.5)<5*eps
        print(f'a=1+{eps:.3f} critical_moment={pc:.10f} scaled={pc*eps*eps:.10f}')
        total+=1
    print(f'PASS {total} deterministic assertions')

if __name__=='__main__':run()
