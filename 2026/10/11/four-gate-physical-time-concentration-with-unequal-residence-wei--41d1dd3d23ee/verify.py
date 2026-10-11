"""Numerical consistency checks of the four-gate cubic oscillator.

Finite computations test identities and the approach toward an asymptotic law;
the theorem's limit is established analytically, not by this checker.
"""
from math import pi, sin, cos, sqrt, atan

LAM = 1.25
KAP = 2.4
ETA = 0.4
OMG = 1.4

def f(theta):
    return KAP + ETA * cos(2*theta) + 0.5 * OMG * sin(4*theta)

def g(theta, eps):
    return eps + OMG * sin(2*theta)**2

def deriv(theta, u, eps):
    return 2*(LAM-f(theta)*u)/g(theta,eps)

def rk4(theta,u,step,eps):
    k1=deriv(theta,u,eps)
    k2=deriv(theta+step/2,u+step*k1/2,eps)
    k3=deriv(theta+step/2,u+step*k2/2,eps)
    k4=deriv(theta+step,u+step*k3,eps)
    return u +step*(k1+2*k2+2*k3+k4)/6

def integrate(eps,steps):
    h=2*pi/steps
    u=LAM/KAP
    for _ in range(2):
        for i in range(steps):
            u=rk4(i*h,u,h,eps)
    start=u
    period=0.0
    masses=[0.0]*4
    halfcauchy=[0.0]*4
    width=sqrt(eps/(4*OMG))
    for i in range(steps):
        th=(i+0.5)*h
        un=rk4(i*h,u,h/2,eps)
        dt=h/(un*g(th,eps))
        period+=dt
        j=round(th/(pi/2))%4
        masses[j]+=dt
        center=(j*pi/2)
        diff=((th-center+pi)%(2*pi))-pi
        if abs(diff)<width:
            halfcauchy[j]+=dt
        u=rk4(i*h,u,h,eps)
    exact=2*pi*KAP/(LAM*sqrt(eps*(eps+OMG)))
    assert abs(start-u)<1e-9
    assert abs(period-exact)/exact < 5e-5,(period,exact)
    return period,masses,halfcauchy

def check_polar_polynomial():
    for x,y in [(0.7,-0.9),(1.1,0.3),(-0.4,1.5),(2.0,1.0)]:
        r2=x*x+y*y
        theta=__import__('math').atan2(y,x)
        eps=0.21
        p=LAM*x-(KAP*r2+ETA*(x*x-y*y))*x-2*OMG*x*x*y-eps*r2*y
        q=LAM*y-(KAP*r2+ETA*(x*x-y*y))*y+2*OMG*x*y*y+eps*r2*x
        rdot=(x*p+y*q)/sqrt(r2)
        ang=(x*q-y*p)/r2
        assert abs(rdot-sqrt(r2)*(LAM-f(theta)*r2))<1e-10
        assert abs(ang-r2*g(theta,eps))<1e-10

if __name__=='__main__':
    check_polar_polynomial()
    for eps,n in [(0.045,60000),(0.003,120000)]:
        T,m,c=integrate(eps,n)
        target=[(KAP+ETA)/(4*KAP),(KAP-ETA)/(4*KAP),
                (KAP+ETA)/(4*KAP),(KAP-ETA)/(4*KAP)]
        r=[x/T for x in m]
        print('epsilon',eps,'period',round(T,8),
              'sector_measures',[round(z,5) for z in r],
              'target',[round(z,5) for z in target],
              'within_Cauchy_unit_scale',round(sum(c)/T,5))
        if eps<0.005:
            assert max(abs(r[j]-target[j]) for j in range(4))<0.02
            assert abs(sum(c)/T-0.5)<0.035
    print('CHECK_OK')
