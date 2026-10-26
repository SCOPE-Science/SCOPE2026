"""Reproducible finite-time second-moment checks for a harmonic run-and-tumble particle.
Only numerical checks; the theorem relies on the analytic comparison proof.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def propagate_constant(t, k, alpha, a0, b0, v=1.0):
    delta = k + alpha
    beq = v / delta
    aeq = v * beq / k
    b = beq + (b0 - beq) * math.exp(-delta * t)
    if abs(2*k-delta) < 1e-11:
        remainder = t * math.exp(-2*k*t)
    else:
        remainder = math.exp(-2*k*t)*math.expm1((2*k-delta)*t) / (2*k-delta)
    a = a0*math.exp(-2*k*t)+aeq*(-math.expm1(-2*k*t)) + 2*v*(b0-beq)*remainder
    return np.array([a,b])


def integrate_schedule(schedule, init, v=1.0):
    state=np.asarray(init, dtype=float)
    for duration,k,alpha in schedule:
        state=solve_ivp(lambda t,ab: [-2*k*ab[0]+2*v*ab[1],v-(k+alpha)*ab[1]],
                        (0,duration),state,rtol=5e-12,atol=5e-13).y[:,-1]
    return state


def check():
    n=0
    for k,alpha in [(1,1),(1,3),(2,2),(3,1),(1.5,1.5),(2.5,5.0),(0.6,1.6)]:
        for t in [0,0.01,0.25,0.7,2.0]:
            exact=propagate_constant(t,k,alpha,0.5,0.5)
            computed=integrate_schedule([(t,k,alpha)],(0.5,0.5)) if t>0 else np.array([0.5,0.5])
            assert np.allclose(exact,computed,atol=2e-10,rtol=2e-10),(k,alpha,t,exact,computed)
            n+=1
    rng=np.random.default_rng(20261019)
    minimum=(0.75,0.4)
    maximum=(3.0,4.8)
    for i in range(300):
        parts=int(rng.integers(2,9))
        schedule=[]
        for _ in range(parts):
            schedule.append((float(rng.uniform(0.005,0.65)),float(rng.uniform(minimum[0],maximum[0])),float(rng.uniform(minimum[1],maximum[1]))))
        total=sum(z[0] for z in schedule)
        mid=integrate_schedule(schedule,(0.5,0.5))[0]
        low=propagate_constant(total,maximum[0],maximum[1],0.5,0.5)[0]
        up=propagate_constant(total,minimum[0],minimum[1],0.5,0.5)[0]
        assert low-2e-9 <= mid <= up+2e-9,(i,low,mid,up)
        n+=1
    for i in range(25):
        T=float(rng.uniform(0.01,4))
        lo=propagate_constant(T,*maximum,0.5,0.5)[0]
        hi=propagate_constant(T,*minimum,0.5,0.5)[0]
        target=(lo+hi)/2
        func=lambda theta:propagate_constant(T,minimum[0]+theta*(maximum[0]-minimum[0]),minimum[1]+theta*(maximum[1]-minimum[1]),0.5,0.5)[0]-target
        root=brentq(func,0,1,xtol=1e-13)
        assert abs(func(root))<=1e-11
        n+=1
    # A compression time optimality witness from a stationary initial law.
    ki, ai, v = 1.0,1.0,1.0
    a0=v*v/(ki*(ki+ai)); b0=v/(ki+ai)
    target=0.17
    tau=brentq(lambda t:propagate_constant(t,*maximum,a0,b0)[0]-target,1e-12,10)
    assert 0<tau<10
    for t in np.linspace(0,tau-1e-5,101):
        assert propagate_constant(t,*maximum,a0,b0)[0]>target
        n+=1
    print(f'{n} analytic/independent-ODE/reachability checks passed; compression optimum t={tau:.12f}')

if __name__=='__main__':
    check()
