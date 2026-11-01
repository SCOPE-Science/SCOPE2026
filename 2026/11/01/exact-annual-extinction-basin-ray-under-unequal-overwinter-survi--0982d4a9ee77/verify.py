"""Finite numerical diagnostics for an analytic seasonal competition separatrix theorem.
Python 3 standard library only. Numerical tests do not prove the infinite-time claims.
"""
from math import exp, log


def rk4(f, start, duration, steps=10000):
    step = duration / steps
    x = start
    for _ in range(steps):
        a = f(x)
        b = f(x + step*a/2)
        c = f(x + step*b/2)
        d = f(x + step*c)
        x += step * (a+2*b+2*c+d)/6
    return x


def slope(beta1,mu1,beta2,mu2,delta1,delta2,alpha,tau):
    A = beta2-mu2+mu1
    C = (beta1-mu1)-(beta2-mu2)
    s = delta1/delta2
    if abs(C)<1e-12:
        w = (1-1/s)/(A*tau-log(s))
    else:
        H = exp((A/beta1)*(log(s)+C*tau))
        w = (C/A)*(H-1)/(H-s)
    return w/alpha


def q_next(q,p):
    beta1,mu1,beta2,mu2,delta1,delta2,alpha,tau,xi=p
    A=beta2-mu2+mu1
    return (delta2/delta1)*rk4(lambda z: z*(A-beta1/(1+alpha*z)),q,tau)


def xy_next(x,y,p):
    beta1,mu1,beta2,mu2,delta1,delta2,alpha,tau,xi=p
    def rhs(state):
        x,y=state
        common=xi*(x+y)
        return (x*(beta1*x/(x+alpha*y)-mu1-common),y*(beta2-mu2-common))
    steps=10000
    dt=tau/steps
    for _ in range(steps):
        ax,ay=rhs((x,y))
        bx,by=rhs((x+dt*ax/2,y+dt*ay/2))
        cx,cy=rhs((x+dt*bx/2,y+dt*by/2))
        dx,dy=rhs((x+dt*cx,y+dt*cy))
        x+=dt*(ax+2*bx+2*cx+dx)/6
        y+=dt*(ay+2*by+2*cy+dy)/6
    return delta1*x,delta2*y


samples=[
 ('positive_C',(2.0,.3,1.2,.2,.4,.8,.9,1.5,.7)),
 ('zero_C',(2.,.2,2.,.2,.9,.4,.7,1.,.8)),
 ('negative_C',(1.5,.2,2.,.2,.99,.5,1.1,1.,.8)),
]
for label,p in samples:
    b1,m1,b2,m2,d1,d2,alpha,tau,xi=p
    assert 1<d2*exp((b2-m2)*tau)<d1*exp((b1-m1)*tau)
    q=slope(*p[:8])
    assert q>0
    residual=abs(q_next(q,p)/q-1)
    assert residual<2e-9,(label,residual)
    low=q/2
    high=2*q
    assert q_next(low,p)<low
    assert q_next(high,p)>high
    assert q_next(q*0.9,p)<q*0.9 and q_next(q*1.1,p)>q*1.1
    x,y=xy_next(1.,q,p)
    assert abs(y/x-q)/q<2e-8
    g1=b1-m1;g2=b2-m2
    k1=(d1*exp(g1*tau)-1)*(g1/(xi*(exp(g1*tau)-1)))
    k2=(d2*exp(g2*tau)-1)*(g2/(xi*(exp(g2*tau)-1)))
    assert k1>0 and k2>0
    print(label,'q_star',format(q,'.12f'),'annual_ratio_relative_error',format(residual,'.3e'),
          'axis_x',format(k1,'.8f'),'axis_y',format(k2,'.8f'),'PASS')
print('FINITE_NUMERIC_DIAGNOSTICS_PASS')
print('ALL_PARAMETER_GLOBAL_BASINS_REQUIRE_ANALYTIC_PROOF')
