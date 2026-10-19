"""Reproduce exact overlap coefficients, ODE jamming, and independent lattice simulations.
Requires Python 3, numpy, scipy. No external datasets or services.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp

def coefficients(n, parity, rate=(2,3)):
    """A trimer starting at r has rate depending on r mod 2.
    Return sum of rates grouped by union length and first-site parity.
    """
    acc={}
    s=parity
    for r in range(s-2,s+n):
        left=min(s,r);right=max(s+n-1,r+2)
        k=(right-left+1,left%2)
        acc[k]=acc.get(k,0)+rate[r%2]
    return acc

def check_interval_equations():
    a,b=2,3
    for n in range(2,18):
        for s in [0,1]:
            actual=coefficients(n,s,(a,b))
            def add(out,k,v):out[k]=out.get(k,0)+v
            exp={}
            start=lambda k:(a,b)[k%2]
            if n%2==0:
                add(exp,(n+2,s),(a+b))
                add(exp,(n+1,1-s),start(s-1))
                add(exp,(n+1,s),start(s+n-2))
                if n>=4:add(exp,(n,s),(n-2)//2*(a+b))
            else:
                add(exp,(n+2,s),2*start(s))
                add(exp,(n+1,1-s),start(s-1))
                add(exp,(n+1,s),start(s+n-2))
                m=(n-1)//2
                add(exp,(n,s),m*start(s)+(m-1)*start(s+1))
            exp={k:v for k,v in exp.items() if v}
            assert exp==actual,(n,s,actual,exp)
    print('Exact generator overlap/union coefficients passed: n=2..17, both parities')

def theory(eps):
    def deriv(t,y):
        A,B0,B1,I0,I1=y
        z=math.exp(-(1+eps)*t)
        c0=math.exp(-t)*B0
        c1=math.exp(-eps*t)*B1
        return (-(1+eps)*z*A-c0-eps*c1,
                -2*z*B0-2*eps*math.exp(-eps*t)*A,
                -2*eps*z*B1-2*math.exp(-t)*A,
                c0,eps*c1)
    T=36 if eps==0 else max(36,36/eps)
    sol=solve_ivp(deriv,(0,T),(1,1,1,0,0),rtol=1e-11,atol=2e-13)
    assert sol.success and sol.y.min()>=-1e-9
    return 1-1.5*(sol.y[3,-1]+sol.y[4,-1])

def simulate(n,eps,reps=640,seed=2026):
    rng=np.random.default_rng(seed);v=[]
    for _ in range(reps):
        T=rng.exponential(size=n)
        if eps==0:T[1::2]=math.inf
        else:T[1::2]/=eps
        free=np.ones(n,dtype=bool)
        for i in np.argsort(T):
            if T[i]==math.inf:break
            j=(i+1)%n;k=(i+2)%n
            if free[i] and free[j] and free[k]:
                free[i]=free[j]=free[k]=False
        v.append(free.mean())
    return float(np.mean(v)),float(np.std(v,ddof=1)/math.sqrt(reps))

if __name__=='__main__':
    check_interval_equations()
    j0=0.25+0.75*math.exp(-2)
    jplus=0.25-0.75*math.exp(-2)
    assert abs(theory(0)-j0)<3e-10
    assert abs(theory(1)-0.17634703682266166)<3e-10
    assert abs(theory(0.001)-jplus)<0.00013
    print('Exact boundary zero-rate',j0,'right limit',jplus,'jump',1.5*math.exp(-2))
    for eps in (0,0.001,0.02,1):
        exact=theory(eps)
        sim,se=simulate(1000,eps)
        assert abs(sim-exact)<6*se+0.0002,(eps,exact,sim,se)
        print('rate',eps,'ODE',format(exact,'.10f'),'simulation',format(sim,'.10f'),'standard error',format(se,'.6f'))
    print('ALL CHECKS PASSED; Monte Carlo validates finite-size instances only.')
