"""Reproduce finite numerical checks for a quartic RTP stationary-density crossing proxy.

The exact theorem is analytical; these computations are diagnostic only.
Requires numpy and scipy.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar

v=1.0
ac=(3*math.sqrt(3)*v/2)**(1/3)
zstar=brentq(lambda z: 2*math.exp(z)*(z-1)+1,0.1,0.95)
assert abs(zstar-0.76803904701346)<1e-10

def proxy(a,gamma,h=1e-5):
    ell=brentq(lambda x: x*(x*x-a*a)-v,a,3.0)
    assert a>0 and gamma>0 and ell>a
    def rhs(x,y):
        f=a*a*x-x**3
        b=v*v-f*f
        assert b>0
        return [2*gamma*f/b,2*v*math.exp(y[0])/b]
    sol=solve_ivp(rhs,(0,ell-h),(0.,0.),rtol=2e-8,atol=1e-9,max_step=0.005)
    assert sol.success
    return float(sol.y[1,-1]+math.exp(sol.y[0,-1])/gamma)

results=[]
for eps in [0.03,0.01,0.003,0.001]:
    a=ac-eps
    delta=math.sqrt(2*ac*eps/3)
    res=minimize_scalar(lambda g:proxy(a,g),bounds=(0.005,0.24),method='bounded', options={'xatol':1e-6})
    assert res.success
    gam=res.x
    z=math.pi*gam/(math.sqrt(3)*ac*delta)
    tau=res.fun
    pred=math.pi/(math.sqrt(3)*ac*delta)*(2*math.exp(zstar)-1)/zstar
    assert tau>0 and abs(z-zstar)<0.22
    assert abs(tau/pred-1)<0.16
    assert proxy(a,gam*0.9)>tau and proxy(a,gam*1.1)>tau
    # Two endpoint cutoffs must yield consistent stationary-density proxies.
    alt=proxy(a,gam,h=1e-4)
    assert abs(tau-alt)/tau<2e-3
    results.append((eps,gam,z,tau,tau/pred))

assert all(abs(results[i+1][2]-zstar)<abs(results[i][2]-zstar) for i in range(3))
assert all(abs(results[i+1][4]-1)<abs(results[i][4]-1) for i in range(3))
print('Critical double-well optimal flip-rate checks: PASS')
print('universal critical z:',format(zstar,'.12f'))
for eps,gam,z,tau,ratio in results:
    print('epsilon=%.4g gamma*=%.9f z=%.9f proxy=%.6f ratio_to_limit=%.7f' %(eps,gam,z,tau,ratio))
print('Finite numerical checks support the asymptotic; they do not prove it.')
