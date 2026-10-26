"""Independent numerical checks for the clipped exponential Gaussian recurrence.

Numerical checks are illustrative; the analytic proof establishes all parameter ranges.
Run: python verify.py
"""
import math


def step(u, v, H, beta):
    z = math.expm1(u)
    if z > 0:
        q = min(H*z, beta)
    else:
        q = max(H*z, -beta)
    h = H if z == 0.0 else min(H, beta/abs(z))
    return u-q, v*(1-h*math.exp(u))


def trace(H,beta,u0,v0,n):
    u,v=u0,v0
    for _ in range(n):u,v=step(u,v,H,beta)
    return u,v


def run():
    checks=0
    # Exact peak of the mean multiplier, as a function of the covariance.
    for H in (0.1,0.7,1.0,1.4,1.9,2.0,3.2):
        for beta in (0.02,0.35,1.0,4.0,8.0):
            s=1+beta/H
            h=min(H,beta/abs(s-1))
            assert math.isclose(h*s,H+beta,rel_tol=5e-13)
            factor=abs(1-h*s)
            assert math.isclose(factor,abs(1-H-beta),rel_tol=5e-12,abs_tol=5e-13)
            for ss in (0.001,0.1,0.4,0.8,1,1.1,s/2,s,2*s,10*s,100*s):
                hh=H if ss==1 else min(H,beta/abs(ss-1))
                assert hh*ss <= H+beta+1e-12
                assert abs(1-hh*ss) <= max(1,H+beta-1)+1e-12
                checks+=2
            checks+=2

    # Global convergence of the normalized covariance for H up to 2.
    for H in (0.15,0.55,1.0,1.25,1.8,1.99,2.0):
        for beta in (0.04,0.5,1.0,3.0,8.0):
            for u0 in (-20,-7,-1.1,-0.2,0.15,0.73,3.2,25):
                u,_=trace(H,beta,u0,0.0,18000)
                tol = 0.025 if H==2 else 0.005
                assert abs(u)<tol,(H,beta,u0,u)
                checks+=1

    # Whenever H<2, mean converges even if transient amplification occurs.
    for H,beta,u0 in ((1.7,5.,4.),(1.2,8.,-10.),(0.65,3.,15.),(1.99,1.,0.1)):
        u,v=trace(H,beta,u0,1.,25000)
        assert abs(u)<0.005 and abs(v)<1e-8,(H,beta,u,v)
        checks+=2

    # H=2 is a sharp failure of global mean convergence, even when covariance is exact.
    for beta in (0.1,0.6,1.,3.):
        u,v=step(0.,2.,2.,beta)
        assert u==0. and v==-2.
        # Initial covariance e^beta reaches 1 in one step via the cap.
        u1,v1=step(beta,1.,2.,beta)
        assert abs(u1)<1e-11 and abs(v1)>1e-6,(beta,u1,v1)
        checks+=3

    # Flip normal form: sqrt(n) * |log covariance| approaches sqrt(3)/2.
    for beta in (0.2,0.7,3.0):
        un,vn=0.12,1.0
        saved=[]
        for n in range(1,160001):
            un,vn=step(un,vn,2.,beta)
            if n in (40000,80000,160000):
                saved.append((n,math.sqrt(n)*abs(un), abs(vn)*(n**1.5)))
        assert abs(saved[-1][1]-math.sqrt(3)/2)<0.012,(beta,saved)
        assert saved[0][2]>0 and 0.85<saved[-1][2]/saved[1][2]<1.15,(beta,saved)
        checks+=3

    # Beyond the frontier, an exact covariance can coexist with an expanding mean.
    for H in (2.01,2.5,3.0):
        u,v=trace(H,0.5,0.,1.,10)
        assert u==0. and abs(v)>1.,(H,u,v)
        checks+=1
    print('VERIFICATION_OK checks=',checks)

if __name__=='__main__':run()
