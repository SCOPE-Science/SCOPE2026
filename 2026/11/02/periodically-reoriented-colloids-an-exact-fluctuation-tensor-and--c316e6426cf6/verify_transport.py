"""Reproduce analytic drift, covariance, and unique anisotropy maximizer.

Requires Python >=3.10 and NumPy >=1.22. The Monte Carlo checks are
finite diagnostics, not proofs of the asymptotic theorems.
"""
import math
import numpy as np

J = np.array([[0., -1.], [1., 0.]])
I = np.eye(2)

def rot(phi):
    c, s = np.cos(phi), np.sin(phi)
    return np.array([[c, -s], [s, c]])

def theory(K, h, m, temp, phi0, tau):
    d = temp*m
    z = d*tau
    R0 = rot(phi0)
    E = K-np.outer(h,h)/m
    a = R0@(-J@h/m)
    v = (math.exp(-z)-1)*a/tau
    e2 = math.exp(-2*z)
    e4 = math.exp(-4*z)
    cF = (a@a)*(1-e4)*I/2+(e4-e2)*np.outer(a,a)
    avgE = np.trace(E)*I/2 +(1-e4)/(4*z)*R0@(E-np.trace(E)*I/2)@R0.T
    gamma = cF/tau+2*temp*avgE
    return v, gamma

def trial(K,h,m,temp,phi0,tau,nsamp=90000,steps=80,seed=311):
    rng=np.random.default_rng(seed)
    E=K-np.outer(h,h)/m
    e,l=np.linalg.eigh(E)
    assert min(e)>0
    SQ=l@np.diag(np.sqrt(e))@l.T
    dt=tau/steps
    phi=np.full(nsamp,phi0)
    M=np.zeros((nsamp,2))
    for _ in range(steps):
        c,s=np.cos(phi), np.sin(phi)
        w=(rng.standard_normal((nsamp,2))@SQ.T)*math.sqrt(2*temp*dt)
        M[:,0]+=c*w[:,0]-s*w[:,1]
        M[:,1]+=s*w[:,0]+c*w[:,1]
        phi+=math.sqrt(2*temp*m*dt)*rng.standard_normal(nsamp)
    a=(-J@h/m)
    c,s=np.cos(phi),np.sin(phi)
    F=np.column_stack((c*a[0]-s*a[1],s*a[0]+c*a[1]))
    Y=F-(rot(phi0)@a)+M
    return Y.mean(axis=0)/tau,np.cov(Y.T)/tau

def check():
    exact=0
    for k in [1.2, 2.0, 5.5]:
        for m in [0.4, 1.7]:
            for h in [np.array([0.35,-0.16]), np.array([0.0,0.0])]:
                K=np.eye(2)*k
                if np.min(np.linalg.eigvalsh(K-np.outer(h,h)/m))<=0: continue
                for tau in [0.05,0.6,3.0]:
                    temp=0.8
                    phi0=0.27
                    v,g=theory(K,h,m,temp,phi0,tau)
                    a=rot(phi0)@(-J@h/m)
                    if np.linalg.norm(a)>0:
                        e=a/np.linalg.norm(a)
                        ep=J@e
                        gap=e@g@e-ep@g@ep
                        target=(a@a)*(1-math.exp(-2*temp*m*tau))**2/(2*tau)
                        assert math.isclose(gap,target,abs_tol=5e-12,rel_tol=5e-12)
                        exact+=1
                    assert np.min(np.linalg.eigvalsh(g))>0
                    tr_expected=(2*temp*np.trace(K-np.outer(h,h)/m)
                                 +(a@a)*(1-math.exp(-2*temp*m*tau))/tau)
                    assert math.isclose(np.trace(g),tr_expected,rel_tol=3e-13)
                    exact+=1
    from scipy.optimize import brentq
    zr=brentq(lambda z:math.exp(2*z)-1-4*z,0.1,1.0)
    assert abs(zr-0.6282156043130834)<1e-12
    zs=np.linspace(0.04,5,7000)
    f=(1-np.exp(-2*zs))**2/zs
    assert abs(zs[np.argmax(f)]-zr)<0.001
    exact+=2
    K=np.array([[0.05962,0.002094],[0.002094,0.05494]])
    h=np.array([-0.001775,-0.002674]);m=0.02501;temp=4;phi0=0.;tau=0.1
    v,g=theory(K,h,m,temp,phi0,tau)
    v_mc,g_mc=trial(K,h,m,temp,phi0,tau)
    assert np.max(np.abs(v-v_mc))<0.03
    assert np.max(np.abs(g-g_mc))<0.025
    print('Exact matrix/gap/trace checks:',exact)
    print('Universal optimal rotational time:',zr)
    print('Benchmark drift:',v.tolist())
    print('Benchmark covariance growth:',g.tolist())
    print('Monte Carlo drift:',v_mc.tolist())
    print('Monte Carlo covariance growth:',g_mc.tolist())
    print('Monte Carlo samples:',90000)
    print('All checks PASS')

if __name__=='__main__': check()
