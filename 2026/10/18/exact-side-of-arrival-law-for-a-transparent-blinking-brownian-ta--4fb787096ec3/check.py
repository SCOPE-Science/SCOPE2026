"""Standalone numerical checks for a transparent two-state gated Brownian target.

Python 3.10+, standard library only. Run: python check.py.
The Monte Carlo bridge test is finite empirical evidence, not a proof.
"""
import math
import random


def formula(alpha,beta,r,x0,D):
    lam=alpha+beta
    z=math.sqrt(r/(r+lam))
    h=math.exp(-x0*math.sqrt((r+lam)/D))
    A=alpha*(1-z)*(1-h)/(2*lam)
    I=(1-z)*(alpha+(r+beta)*h)/(2*lam)
    E=beta/lam*A+alpha/lam*I
    return A,I,E


def pieces(alpha,beta,r,x0,D):
    lam=alpha+beta
    kap=math.sqrt(r/D)
    mu=math.sqrt((r+lam)/D)
    t=math.exp(-mu*x0)
    c=(kap/mu-1)/(2*lam)
    e=(kap/mu+1)/(2*lam)
    b=beta/lam
    gA=-alpha*c
    gI=-c*(alpha+r*t)
    uA=gA+alpha*c*t
    uI=gI-beta*c*t
    def eval(x):
        if x>=0:
            k=c*math.exp(-mu*x)
            return (gA+alpha*k,gI-beta*k),(-mu*alpha*k,+mu*beta*k), (mu*mu*alpha*k,-mu*mu*beta*k)
        z=math.exp(kap*x);w=e*math.exp(mu*x)
        return (gA+b*z+alpha*w,gI+b*z-beta*w), (kap*b*z+mu*alpha*w,kap*b*z-mu*beta*w), (kap*kap*b*z+mu*mu*alpha*w,kap*kap*b*z-mu*mu*beta*w)
    return eval,(uA,uI),(gA,gI)


def bridge_trial(alpha,beta,r,x0,D,rng):
    x=x0; active=(rng.random()<beta/(alpha+beta))
    for _ in range(100000):
        tr=rng.expovariate(r)
        tg=rng.expovariate(alpha if active else beta)
        dt=min(tr,tg)
        y=x+rng.gauss(0,math.sqrt(2*D*dt))
        if active and (x*y<=0 or rng.random()<math.exp(-x*y/(D*dt))):
            return int(x<0)
        x=x0 if tr<tg else y
        if tg<tr:active=not active
    raise RuntimeError('undetected after event limit')


def close(a,b,tol=1.e-9):
    if abs(a-b)>tol: raise AssertionError((a,b,tol))


def test():
    assertions=0
    for alpha,beta,r,x0,D in [(1,2,.5,1,1),(1,1,3,.6,1),(.4,2,5,1,.5),(1,1,.03,1,1),(3,5,1,1,1)]:
        A,I,E=formula(alpha,beta,r,x0,D)
        lam=alpha+beta;kap=math.sqrt(r/D);mu=math.sqrt((r+lam)/D)
        t=math.exp(-mu*x0);z=kap/mu
        close(E,alpha/(2*lam)*(1-z)*(1+r/lam*t));assertions+=1
        assert 0<A<1 and 0<I<1 and 0<E<.5;assertions+=1
        f,u,g=pieces(alpha,beta,r,x0,D)
        for a,b in zip(u,(A,I)):close(a,b);assertions+=1
        for a,b in zip(f(x0)[0],u):close(a,b);assertions+=1
        hi=f(1.e-10)[0];lo=f(-1.e-10)[0]
        close(hi[0],0,1e-8);close(lo[0],1,1e-8);assertions+=2
        close(hi[1],lo[1],1e-8);close(f(1e-10)[1][1],f(-1e-10)[1][1],1e-8);assertions+=2
        for x in [-3.,-1.,-.5,.01,.2,.8,2.]:
            val,der,sec=f(x)
            Ra=D*sec[0]+alpha*(val[1]-val[0])+r*(u[0]-val[0])
            Ri=D*sec[1]+beta*(val[0]-val[1])+r*(u[1]-val[1])
            close(Ra,0,1e-10);close(Ri,0,1e-10);assertions+=2
    for alpha,beta,x0,D in [(1,2,1,1),(.1,.2,.2,3),(12,4,3,.8)]:
        vals=[formula(alpha,beta,r,x0,D)[2] for r in [1e-5,.01,.1,1,5,50,1e3,1e5]]
        assert all(vals[i]>vals[i+1] for i in range(len(vals)-1));assertions+=1
        close(vals[-1]*1e5,alpha/4,1.e-2);assertions+=1
    for piI,r,x0,D in [(.5,1,1,1),(.3,4,1.5,2),(.8,.2,.7,1)]:
        vals=[formula(piI*lam,(1-piI)*lam,r,x0,D)[2] for lam in [.001,.1,1,10,100,10000,1e8]]
        assert all(vals[i]<vals[i+1] for i in range(len(vals)-1));assertions+=1
        close(vals[-1],piI/2,4e-5);assertions+=1
    for ell in [.2,1.,2.]:
        rr=1e7; xx=ell/math.sqrt(rr)
        close(formula(1,2,rr,xx,1)[2],math.exp(-ell)/12,2e-5);assertions+=1
    print('Analytic boundary, generator, normalization, monotonicity, and limits:',assertions,'checks passed')
    for k,(alpha,beta,r,x0,D) in enumerate([(1,2,.5,1,1),(1,1,3,.6,1),(.4,2,5,1,.5),(1,1,.03,1,1)]):
        rng=random.Random(9247+k);N=12000
        hits=sum(bridge_trial(alpha,beta,r,x0,D,rng) for _ in range(N))
        phat=hits/N;p=formula(alpha,beta,r,x0,D)[2]
        sd=math.sqrt(p*(1-p)/N)
        print('Bridge Monte Carlo',k+1,'predicted',round(p,7),'measured',round(phat,7),'standard_error',round(sd,7))
        assert abs(phat-p)<6*sd+.003
    print('All four independent Brownian-bridge simulation comparisons passed.')


if __name__=='__main__':test()
