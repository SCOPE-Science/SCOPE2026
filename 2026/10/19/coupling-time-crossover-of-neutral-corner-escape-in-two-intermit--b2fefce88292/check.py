"""Standalone numerical cross-checks for two-site intermittent neutral-branch scaling.
Numerical tests are not proofs of infinite-time or area assertions.
"""
from math import sqrt

P=1.5

def field(x,y,rho):
    return (x**P+rho*(y-x), y**P+rho*(x-y))

def rk4(x,y,rho,steps=20000):
    dt=1.0/steps
    for _ in range(steps):
        k1=field(x,y,rho)
        k2=field(x+dt*k1[0]/2,y+dt*k1[1]/2,rho)
        k3=field(x+dt*k2[0]/2,y+dt*k2[1]/2,rho)
        k4=field(x+dt*k3[0],y+dt*k3[1],rho)
        x+=dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
        y+=dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        if max(x,y)>1e8:
            return None
    return x,y

def discrete(x,y,eps,steps):
    for _ in range(steps):
        a=(1-eps)*x+eps*y
        b=(1-eps)*y+eps*x
        x=a+a**P/steps
        y=b+b**P/steps
        if max(x,y)>1e8:
            return None
    return x,y

def check():
    beta=P-1
    a=beta**(-1/beta)
    assert abs(a-4)<1e-14
    assert abs(a*a-16)<1e-14
    assert abs(2*a*a-32)<1e-14
    u=rk4(3,3,2,steps=20000)
    scalar=(1/sqrt(3)-.5)**(-2)
    assert u is not None and abs(u[0]-scalar)<1e-4 and abs(u[1]-scalar)<1e-4
    assert 2/sqrt(5)<1 # uncoupled initial (5,0) blows up before time 1
    continuum=rk4(5,0,2,steps=20000)
    assert continuum is not None and 10<continuum[0]<200 and continuum[1]>0
    approx=discrete(5,0,2/8000,8000)
    assert approx is not None and max(abs(approx[j]-continuum[j]) for j in (0,1))<3.0
    strong=discrete(5,0,.1,8000)
    lim=(1/sqrt(2.5)-.5)**(-2)
    assert strong is not None and max(abs(strong[j]-lim) for j in (0,1))<1.0
    print('VERIFY_OK: scalar threshold, endpoint areas, ODE response, finite- and strong-coupling discrete trajectories')

if __name__=='__main__':
    check()
