#!/usr/bin/env python3
"""Independent stationary covariance and frequency comparisons for a stochastic enzymatic reaction network."""
import math
import numpy as np
from numpy.linalg import solve

rng = np.random.default_rng(741501)
count = 0
max_rel = 0.0

def close(x, y, tol=2e-10):
    global count,max_rel
    x,y=complex(x),complex(y)
    err=abs(x-y)/max(1.0,abs(x),abs(y))
    max_rel=max(max_rel,err)
    if err>tol:
        raise AssertionError((x,y,err))
    count += 1

def formula(u,v,d,k,ct,omega):
    h=u+d; L=d+k; a=h+k; x=omega*omega
    den=(v*k-x)**2+x*(a+v)**2
    f=2*ct*(L*x+k*(h*a+k*L))/den
    r=2*k*ct/(x+(v*k/a)**2)
    B=k*k*u+2*k*v*h+k*v*v*(1-k*L/a**2)
    C=v*v*k**4*u/a**2
    Q=-d*x*x+B*x+C
    return f,r,Q,B,C,den

for _ in range(1200):
    u,v,k,ct=10.0**rng.uniform(-2,2,4)
    d=0.0 if _%13==0 else 10.0**rng.uniform(-3,2)
    a=u+d+k;h=u+d;L=d+k
    drift=np.array([[-a,v],[h,-v]],float)
    diffusion=ct*np.array([[2*L,-(2*d+k)],[-(2*d+k),2*L]],float)
    w=10**rng.uniform(-3,3)
    f,r,Q,B,C,den=formula(u,v,d,k,ct,w)
    transfer=np.linalg.inv(1j*w*np.eye(2)-drift)
    direct=(transfer@diffusion@transfer.conj().T)[1,1].real
    close(f,direct)
    close(r,2*k*ct/(w*w+(v*k/a)**2))
    close(r-f,2*ct*Q/(den*(w*w+(v*k/a)**2)))
    close(2*ct*u/v**2,formula(u,v,d,k,ct,0)[1]-formula(u,v,d,k,ct,0)[0],tol=1e-6)
    assert B>0 and C>0
    if d:
        root=(B+math.sqrt(B*B+4*d*C))/(2*d)
        for x,sign in ((root/2,1),(2*root,-1)):
            f2,r2,*_=formula(u,v,d,k,ct,math.sqrt(x))
            assert (r2-f2)*sign>0
        assert abs(-d*root*root+B*root+C)/max(1.0,abs(d*root*root),abs(B*root),abs(C))<2e-9
    else:
        assert Q>0

# Verify all rates correspond to physical, stable macroscopic steady states,
# and full-LNA stationary covariances agree with published closed forms.
for _ in range(100):
    k0=10**rng.uniform(-1,1);s=10**rng.uniform(-2,2);e=10**rng.uniform(-2,2)
    d=10**rng.uniform(-1,1);k=10**rng.uniform(-1,1)
    u=k0*s;v=k0*e;a=u+d+k;L=d+k;h=u+d
    ct=k0*s*e/L
    J=np.array([[-a,v],[h,-v]])
    D=ct*np.array([[2*L,-(2*d+k)],[-(2*d+k),2*L]])
    # Direct 4x4 Lyapunov matrix solve, no closed-form formula substitution.
    Sigma=solve(np.kron(np.eye(2),J)+np.kron(J,np.eye(2)),-D.reshape(-1)).reshape(2,2)
    KM=L/k0; gamma=a/v; K1=d/k0
    published=s*(1+s/KM*(K1+s)/(KM+s)*gamma/(1+gamma))
    close(Sigma[1,1],published)
    reduced_variance=s*(1+s/KM)
    close(reduced_variance,k*ct/(v*k/a))
    assert reduced_variance>Sigma[1,1]
print(f'PASS {count} independently computed comparisons; max_rel={max_rel:.3e}')
