import math
import numpy as np
from scipy.integrate import solve_ivp

alpha=0.001
beta=0.09
mu=0.0002
gamma=0.0007
delta=0.004
c1=0.012
c2=0.006
rho=0.001
pc=1.0

m=min(mu,delta)
cmax=max(c1,c2)
D=alpha*delta+mu*gamma+mu*delta
Jalpha=(c1*(gamma+delta)+c2*alpha)/D
print(f"m={m:.10g}")
print(f"cmax={cmax:.10g}")
print(f"J_alpha={Jalpha:.12f}")


def solve_tc(p0,rho_value):
    def rhs(t,y):
        h,i,p=y
        lam=alpha+beta/(1+p)
        return [-lam*h-mu*h+gamma*i,
                lam*h-(gamma+delta)*i,
                -c1*h-c2*i-rho_value*p]
    def event(t,y):
        return y[2]-pc
    event.terminal=True
    event.direction=-1
    if rho_value>0:
        T=2*math.log(p0/pc)/rho_value+6000
    else:
        T=100000
    sol=solve_ivp(rhs,(0,T),(1.0,0.0,p0),events=event,
                  rtol=1e-10,atol=1e-12,max_step=5.0)
    return sol.t_events[0][0] if len(sol.t_events[0]) else math.inf

for p0 in [100.0,1000.0,10000.0,1000000.0]:
    tc=solve_tc(p0,rho)
    ideal=math.log(p0/pc)/rho
    print(f"rho>0 p0={p0:g} tc={tc:.12f} ideal={ideal:.12f} ratio={tc/ideal:.12f} deficit={ideal-tc:.12f}")


def solve_pinf(p0):
    def rhs(t,y):
        h,i,p=y
        lam=alpha+beta/(1+p)
        return [-lam*h-mu*h+gamma*i,
                lam*h-(gamma+delta)*i,
                -c1*h-c2*i]
    sol=solve_ivp(rhs,(0,100000),(1.0,0.0,p0),rtol=1e-10,atol=1e-12,max_step=10.0)
    return sol.y[2,-1], sol.y[0,-1]+sol.y[1,-1]

for p0 in [100.0,1000.0,10000.0]:
    pinf,S=solve_pinf(p0)
    used=p0-pinf
    print(f"rho=0 p0={p0:g} used={used:.12f} J_alpha={Jalpha:.12f} error={used-Jalpha:.12f} survivor={S:.3e}")

print(f"global_no_cross_sufficient_threshold={pc+cmax/m:.12f}")
