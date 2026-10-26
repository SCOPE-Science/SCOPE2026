"""Analytical and event-driven checks for a transparent gated Brownian target."""
from math import sqrt, exp, log, isclose
from random import Random
from decimal import Decimal, localcontext

def closed(D, x0, a, b, r):
    lam=a+b
    rho=sqrt(r/(r+lam))
    F=exp(-x0*sqrt((r+lam)/D))
    pa=1-a*(1-F)/(2*(r+lam)*(1+rho))
    pi=1-(F+a/(r+lam)*(1-F))/(2*(1+rho))
    pe=(b*pa+a*pi)/lam
    return pa,pi,pe

def renewal(D,x0,a,b,r):
    """Independent high-precision two-state matrix renewal from bare modes."""
    with localcontext() as ctx:
        ctx.prec=70
        D,x0,a,b,r=map(lambda x:Decimal(str(x)),(D,x0,a,b,r))
        k=(r/D).sqrt(); h=((r+a+b)/D).sqrt()
        E=(-k*x0).exp(); F=(-h*x0).exp()
        H=((b*h*E+a*k*F)/(a*k+b*h),b*(h*E-k*F)/(a*k+b*h))
        G=((b*E+a*F)/(a+b),b*(E-F)/(a+b))
        f=[(H[j]+G[j])/2 for j in range(2)]
        den=r*(r+a+b)
        K=[[(r+b)/den,a/den],[b/den,(r+a)/den]]
        L=[[K[i][j]-H[i]*K[0][j] for j in range(2)] for i in range(2)]
        A=[[Decimal(int(i==j))-r*L[i][j] for j in range(2)] for i in range(2)]
        det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
        assert det>0,det
        return (float((f[0]*A[1][1]-A[0][1]*f[1])/det),
                float((A[0][0]*f[1]-A[1][0]*f[0])/det))

def simulate(D,x0,a,b,r,n=4000,seed=5151):
    """Exact event-time simulation, not an Euler discretization."""
    rng=Random(seed); good=0
    for _ in range(n):
        x=x0; gate_A = rng.random()<b/(a+b)
        for event in range(50000):
            intensity=r+(a if gate_A else b)
            dt=rng.expovariate(intensity)
            y=x+sqrt(2*D*dt)*rng.gauss(0,1)
            crossed=(x*y<=0 or rng.random()<exp(-abs(x*y)/(D*dt))) if gate_A else False
            if crossed:
                good += int(x>0)
                break
            if rng.random()<r/intensity:
                x=x0
            else:
                x=y; gate_A=not gate_A
        else:
            raise AssertionError('unusually long simulated trajectory')
    return good/n

def run():
    count=0
    for D in (0.3,1.0,4.0):
        for x0 in (0.2,0.8,2.0):
            for a,b in ((0.3,1.5),(1.0,1.0),(2.8,0.2)):
                for r in (0.0001,0.1,0.7,4.0,30.0):
                    pa,pi,pe=closed(D,x0,a,b,r)
                    qa,qi=renewal(D,x0,a,b,r)
                    assert abs(pa-qa)<5e-10,(D,x0,a,b,r,pa,qa)
                    assert abs(pi-qi)<5e-10,(D,x0,a,b,r,pi,qi)
                    assert .5-1e-12<=pa<=1 and .5-1e-12<=pi<=1
                    assert abs(pe-(b*pa+a*pi)/(a+b))<1e-12
                    count+=4
    for D,x0,a,b in ((1,1,1,1),(.4,.5,2,1),(3,2,.1,5)):
        prev=(0,0,0)
        for i in range(1,200):
            r=10**(-7+i*0.055)
            vals=closed(D,x0,a,b,r)
            assert all(vals[j]>prev[j] for j in range(3))
            prev=vals
            count+=3
        r=1e7
        pa,pi,pe=closed(D,x0,a,b,r)
        for p in (pa,pi,pe):
            assert abs((1-p)*r-a/4)<1e-5
            count+=1
        small=1e-10; pe0=1-a/(2*(a+b));pe=closed(D,x0,a,b,small)[2]
        assert abs((pe-pe0)/sqrt(small)-a/(2*(a+b)**1.5))<0.002
        count+=1
    for gamma in (0.3,1.0,4.0):
        theory=closed(1,1,gamma,gamma,1)[2]
        empirical=simulate(1,1,gamma,gamma,1,4000,int(gamma*1000)+282)
        assert abs(empirical-theory)<0.035,(gamma,empirical,theory)
        count+=1
    print('PASS',count,'analytical, boundary-mode, monotonicity, asymptotic, and stochastic checks')
if __name__=='__main__':run()
