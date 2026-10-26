"""Reproducibility checks for fourth-cumulant sign and optimal-drag asymptotics.
Uses two independent exact moment schemes. Dependencies: numpy, scipy.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp

checks=0

def close(a,b,rtol=1e-8,atol=1e-11):
    global checks
    assert np.isclose(a,b,rtol=rtol,atol=atol),(a,b)
    checks+=1

def J_opt(k,g,T):
    # Ordered four-point cumulant recursion; past weighting is 2exp(kt).
    A=2/(k+g)
    B=2/(k+g)**2
    C=4/((k+g)**2*(3*k+g))
    J=2/(k*(k+g)**2*(3*k+g))
    if not T:return J
    def f(_,y):
        a,b,c,j=y
        return [1-g*a,a-2*g*b,b-g*c,c]
    sol=solve_ivp(f,(0,T),[A,B,C,J],rtol=1e-12,atol=1e-13)
    assert sol.success
    return sol.y[3,-1]

def moment_opt(k,g,T):
    # Independent first-four moments from the full two-state Markov generator.
    M=[1.0]
    N=[0.0]
    for n in range(1,5):
        N.append(n*M[n-1]/(n*k+g))
        M.append(N[n-1]/k)
    m0=[(2**n)*M[n] for n in range(5)]
    q0=[(2**n)*N[n] for n in range(5)]
    state=m0+q0
    def f(_,y):
        m=y[:5];q=y[5:]
        dm=[0]+[n*q[n-1] for n in range(1,5)]
        dq=[-g*q[0]]+[n*m[n-1]-g*q[n] for n in range(1,5)]
        return dm+dq
    sol=solve_ivp(f,(0,T),state,rtol=1e-12,atol=1e-13)
    assert sol.success
    m=sol.y[:5,-1]
    return m[4]-3*m[2]**2,m[2]

def variance_opt(k,g,T):
    # Total variance of noise divided by c^2; unit telegraph amplitude.
    A=2*T/g-2*(-math.expm1(-g*T))/g**2 \
      +4*(-math.expm1(-g*T))/(g*(k+g))+4/(k*(k+g))
    return A

def J_cyclic(k,g,t):
    # Two opposite trap jumps. Telegraph weighting is k*(kernel_0-kernel_t).
    a=-k*math.expm1(-k*t)
    A=a/(k+g)
    B=a*a/(2*(k+g)**2)
    C=a**3/(2*(k+g)**2*(3*k+g))
    J=a**4/(8*k*(k+g)**2*(3*k+g))
    def f(s,y):
        a0,b,c,j=y
        w=-k*math.exp(-k*(t-s))
        return [w-g*a0,w*a0-2*g*b,w*b-g*c,w*c]
    sol=solve_ivp(f,(0,t),[A,B,C,J],rtol=1e-12,atol=1e-13,max_step=t/250)
    assert sol.success
    return sol.y[3,-1]

if __name__=='__main__':
    # Exact moment recursion vs ordered cumulant cascade, independent implementations.
    for k in (.4,1,2,4.5):
        for g in (.3,1,2.5):
            for T in (.1,.75,2.5,7):
                j=J_opt(k,g,T)
                cumul,variance=moment_opt(k,g,T)
                close(cumul,-48*j,rtol=7e-8,atol=8e-10)
                close(variance,variance_opt(k,g,T),rtol=7e-9)
                assert cumul<0 and j>0
                checks+=1
    # Analytic stationarity at zero drag duration.
    for k,g in ((.4,.7),(1,1),(2.1,.8)):
        close(-48*J_opt(k,g,0),-96/(k*(k+g)**2*(3*k+g)))
    # The exact two-time telegraph cumulant is positive at short cyclic pulse delays.
    for delta in (.1,.5,1.5):
        limit=4*(1-math.exp(-delta))*(3*math.exp(-delta)-1)
        for k in (20,50,100,200):
            val=-48*J_cyclic(k,1,delta)
            if delta<math.log(3):
                assert val>0
            else:
                assert val<0
            checks+=1
        close(-48*J_cyclic(2000,1,delta),limit,rtol=.05,atol=.04)
    # Exact finite T fourth-cumulant coefficient and asymptotic normalized kurtosis.
    for k,g,D,omega in ((.5,.7,.2,1),(2.,1.,.5,1.3),(3,1.5,0.,.7)):
        target=-6*omega**4/(g**3*(D+omega**2/g)**2)
        ratios=[]
        for T in (200,500):
            c=1/(T+2/k)
            v=c*c*(omega*omega*variance_opt(k,g,T)+2*D*(T+2/k))
            k4=-48*c**4*omega**4*J_opt(k,g,T)
            ratios.append(T*k4/v**2)
            assert k4<0 and v>0
            checks+=1
        assert abs(ratios[1]-target)<abs(ratios[0]-target)
        close(ratios[1],target,rtol=.03)
    print('PASS',checks,'deterministic checks')
    print('cyclic example k=20 gamma=1 delta=0.5, kappa4/a^4omega^4:',-48*J_cyclic(20,1,.5))
