"""Independent reproducibility checks for alternating-rate trimer adsorption.

Requires Python 3.10+, NumPy and SciPy. Execute: python trimer_verify.py.
"""
from functools import lru_cache
from fractions import Fraction
from math import exp
import numpy as np
from scipy.integrate import solve_ivp


def closed_ode(a, b, t_end=35.0):
    def rhs(t, y):
        u, v, i0, i1 = y
        z0 = a * exp(-a*t) * u*u
        z1 = b * exp(-b*t) * v*v
        return (-b*exp(-b*t)*v -a*exp(-(a+b)*t)*u,
                -a*exp(-a*t)*u -b*exp(-(a+b)*t)*v,z0,z1)
    out = solve_ivp(rhs, (0, t_end), (1,1,0,0), rtol=1e-12, atol=3e-14,
                    dense_output=True, max_step=min(.2, 1.0/max(a,b)))
    assert out.success
    return out


def exact_finite_ring(n, a, b):
    # Independent first-arrival CTMC: choose the first successful triple by its rate.
    assert n%2 == 0 and n>=6
    masks=[sum(1<<((j+d)%n) for d in range(3)) for j in range(n)]
    rates=[Fraction(a if j%2==0 else b) for j in range(n)]
    @lru_cache(None)
    def work(occupied):
        valid=[j for j in range(n) if masks[j]&occupied==0]
        total=sum((rates[j] for j in valid),Fraction(0))
        if not valid: return Fraction(0),Fraction(0)
        e=o=Fraction(0)
        for j in valid:
            p=rates[j]/total
            x,y=work(occupied|masks[j])
            e+=p*(x+(j%2==0))
            o+=p*(y+(j%2==1))
        return e,o
    e,o=work(0)
    return (Fraction(2*e+o,n//2),Fraction(e+2*o,n//2),work.cache_info().currsize)


def simulate_ring(n, a, b, reps, seed):
    rng=np.random.default_rng(seed)
    cov=np.zeros(2)
    for _ in range(reps):
        clock=rng.exponential(1/np.array([a,b]*(n//2)))
        taken=np.zeros(n,dtype=np.bool_)
        for j in np.argsort(clock):
            idx=np.array([j,(j+1)%n,(j+2)%n]);
            if not np.any(taken[idx]):taken[idx]=True
        cov += (np.count_nonzero(taken[0::2]),np.count_nonzero(taken[1::2]))
    return cov/(reps*(n//2))


def main():
    cnt=0
    for a,b in [(1,1),(1,2),(1,5),(3,1)]:
        out=closed_ode(a,b,t_end=35/min(a,b))
        u,v,i0,i1=out.y[:,-1]
        c0,c1=2*i0+i1,i0+2*i1
        print('rates',a,b,'limiting coverage',c0,c1)
        # Finite-ring first-event arithmetic converges to infinite-lattice formula.
        errors=[]
        for n in (6,8,10,12,14,16,18):
            x,y,num=exact_finite_ring(n,a,b)
            err=max(abs(float(x)-c0),abs(float(y)-c1))
            errors.append(err)
            print(' ',n,'exact fractions',str(x),str(y),'error',round(err,9),'states',num)
            assert 0<=x<=1 and 0<=y<=1
            cnt+=4
        assert errors[-1]<.0007,errors
        cnt+=1
        approx=simulate_ring(300,a,b,500,seed=1498+a+b)
        print(' Monte Carlo',approx)
        assert max(abs(approx-np.array((c0,c1))))<.015
        cnt+=2
    # Independent exact b=0 fast-stage dimer correspondence.
    import math
    e2=math.exp(-2)
    for s in (.1, .5, 1, 2, 4):
        eps=.0001
        out=closed_ode(1,eps,t_end=s/eps)
        u,v,i0,i1=out.y[:,-1]
        target0=1-e2*exp(-s)
        target1=(1-e2)/2 +2*e2*(1-exp(-s))
        obs0,obs1=2*i0+i1,i0+2*i1
        print('slow',s,'computed',obs0,obs1,'target',target0,target1)
        assert abs(obs0-target0)<.0002 and abs(obs1-target1)<.0002
        cnt+=2
    print('PASS',cnt,'independent conditions and numerical comparisons')
if __name__=='__main__': main()
