"""Checks of exact algebra and diagnostic trajectories for a mean-field incremental-opinion model.
Python: sympy, numpy, scipy. Numerical checks are diagnostic, not proofs.
"""
import math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp


def rhs(k, q):
    deficit = sum(d * q[d] for d in range(1, 2*k+1))
    v = deficit/(2*k)
    u = 1-v
    z = np.empty_like(q)
    z[0] = u*q[1]-v*q[0]
    for d in range(1,2*k):
        z[d] = u*q[d+1]+v*q[d-1]-q[d]
    z[-1] = v*q[-2]-u*q[-1]
    return z


def check_symbolic(k):
    q=sp.symbols('q0:'+str(2*k+1))
    v=sum(d*q[d] for d in range(1,2*k+1))/sp.Integer(2*k)
    u=1-v
    f=[u*q[1]-v*q[0]]
    for d in range(1,2*k):
        f.append(u*q[d+1]+v*q[d-1]-q[d])
    f.append(v*q[2*k-1]-u*q[2*k])
    f=[sp.expand(x.subs(q[0],1-sum(q[1:]))) for x in f]
    assert sp.expand(sum(f))==0
    a=sp.Rational(2*k-1,2*k)
    c=[0,sp.Integer(1)]
    for d in range(2,2*k+1):
        c.append(2*k*c[-1]+d)
    h=sum(c[d]*q[d] for d in range(1,2*k+1))
    hp=sum(c[d]*f[d] for d in range(1,2*k+1))
    # The projected nonlinear remainder must have no linear or constant terms.
    remainder=sp.Poly(sp.expand(hp+a*h),*q[1:])
    assert all(sum(m)>=2 for m,coef in remainder.terms())
    mat=sp.zeros(2*k,2*k)
    for i in range(2*k):
        for j in range(2*k):
            mat[i,j]=sp.diff(f[i+1],q[j+1]).subs({z:0 for z in q[1:]})
    eig=mat.eigenvals()
    assert eig.get(-a)==1
    assert eig.get(-1)==2*k-1
    assert sp.simplify((sp.Matrix(c[1:]).T*mat+a*sp.Matrix(c[1:]).T))==sp.zeros(1,2*k)
    print('SYMBOLIC',k,'eigenvalues',eig,'positive left coefficients',c[1:])


def run(k):
    y=np.zeros(2*k+1)
    y[0]=.7;y[1]=.28;y[-1]+=.02
    times=[15.,20.,25.]
    sol=solve_ivp(lambda t,z:rhs(k,z),(0,25),y,t_eval=times,method='DOP853',rtol=1e-12,atol=1e-23,max_step=.06)
    assert sol.success,sol.message
    a=(2*k-1)/(2*k)
    for t,z in zip(sol.t,sol.y.T):
        C=z[1]*math.exp(a*t)
        if k==1:
            B=z[-1]*math.exp(t)/t
            print('k=1 t',t,'penultimate C',C,'resonant q_-k e^t /t',B,'target from C',C*C/2)
        else:
            B=z[-1]*math.exp(t)
            resid=[]
            for d in range(2,2*k+1):
                v=z[d]*math.exp(t)*math.factorial(2*k-d)/(t**(2*k-d))
                resid.append(round(v,8))
            print('k',k,'t',t,'penultimate C',C,'extreme B',B,'cascade amplitudes',resid)
    assert np.all(sol.y>=-1e-12)


if __name__=='__main__':
    for k in (1,2,3,4,5):check_symbolic(k)
    for k in (1,2,3):run(k)
    print('PASS symbolic matrix identities and finite-time diagnostic trajectories')
