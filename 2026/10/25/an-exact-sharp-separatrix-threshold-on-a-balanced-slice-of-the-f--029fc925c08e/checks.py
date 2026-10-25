"""Reproducible finite checks for a four-oscillator phase-balance separatrix.
This code corroborates, but does not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks

def reduced(alpha, x):
    d,u,v=x
    return np.array([-4*math.cos(alpha)*math.sin(d)*math.cos(u)*math.cos(v),
                     -2*math.sin(u)*math.cos(v)*math.cos(d+alpha),
                     -2*math.sin(v)*math.cos(u)*math.cos(d-alpha)])

def full(alpha, th):
    return np.array([math.sin(th[(j-1)%4]-th[j]+alpha)+math.sin(th[(j+1)%4]-th[j]+alpha) for j in range(4)])

def projection(y):
    return np.array([(y[1]+y[3]-y[0]-y[2])/2,
                     (y[0]-y[2])/2,(y[1]-y[3])/2])

def invariants(alpha, x):
    d,u,v=x
    a=math.tan(alpha)
    s=math.sqrt(math.sin(d))
    return np.array([math.sin(u)/s*math.exp(a*(d-math.pi/2)/2),
                     math.sin(v)/s*math.exp(-a*(d-math.pi/2)/2)])

rng=np.random.default_rng(20261022)
for k in range(400):
    alpha=float(rng.uniform(.03,1.45))
    delta=float(rng.uniform(.15,3.0)); u=float(rng.uniform(-1.4,1.4));v=float(rng.uniform(-1.4,1.4))
    th=np.array([u,delta+v,-u,delta-v]); r=projection(full(alpha,th)); rr=reduced(alpha,[delta,u,v]);
    assert max(abs(r-rr)) < 8e-14
    x=np.array([delta,u,v]); der=rr
    h=1e-6
    gradient=np.array([(invariants(alpha,x+h*np.eye(3)[i])-invariants(alpha,x-h*np.eye(3)[i]))/(2*h) for i in range(3)])
    assert max(abs(gradient.T@der))<1e-7

alpha=.4
c=math.cos(alpha)
a=math.tan(alpha)
critical=(c*math.exp(alpha*a))**(-.5)
assert 0<critical<1
cases={'synchronization':.90, 'separatrix':critical, 'periodic':(critical+1)/2}
for label,rho in cases.items():
    x0=np.array([math.pi/2,math.asin(rho),math.asin(rho)])
    tf=12 if label=='separatrix' else 45
    sol=solve_ivp(lambda t,y:reduced(alpha,y), [0,tf],x0,rtol=5e-11,atol=5e-12,max_step=.06)
    assert sol.success
    if label=='synchronization':
        assert sol.y[0,-1]<1e-10
    elif label=='separatrix':
        assert abs(sol.y[0,-1]-(math.pi/2-alpha))<.003
        assert abs(sol.y[1,-1]-math.pi/2)<.003
    else:
        peaks,_=find_peaks(sol.y[0])
        periods=np.diff(sol.t[peaks])
        assert len(periods)>=3
        assert max(periods)-min(periods)<.12
        assert (max(sol.y[0])-min(sol.y[0]))>.01
        assert max(np.linalg.norm(invariants(alpha,sol.y[:,i])-invariants(alpha,x0)) for i in range(sol.y.shape[1]))<2e-7
    print(label, 'rho',f'{rho:.12g}', 'delta_final',f'{sol.y[0,-1]:.12g}')
print('critical',format(critical,'.15g'))
print('CHECKS_PASS')
