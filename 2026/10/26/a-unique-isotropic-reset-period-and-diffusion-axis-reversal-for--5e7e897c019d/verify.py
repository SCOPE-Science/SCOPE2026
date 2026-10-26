#!/usr/bin/env python3
"""Numerical and symbolic checks for the planar coupled-colloid transport identities."""
import numpy as np
import sympy as sp

def theory(beta,m,S,c,tau):
    S=np.asarray(S,float);c=np.asarray(c,float);u=beta*m*tau
    J=np.array([[0.,-1.],[1.,0.]])
    f=-J@c/m
    k=np.exp(-u);q=np.exp(-4*u)
    h=-np.expm1(-4*u)/(4*u)
    z=0.5*np.trace(S)*np.eye(2)+h*(S-0.5*np.trace(S)*np.eye(2))
    C=2*beta*z+(1-q)*np.dot(f,f)/(2*tau)*np.eye(2)+(q-k*k)/tau*np.outer(f,f)
    V=(k-1)*f/tau
    return V,C

def simulate(beta,m,S,c,tau,n=24000,steps=400,seed=341):
    rng=np.random.default_rng(seed)
    S=np.asarray(S,float);c=np.asarray(c,float)
    sroot=np.linalg.cholesky(S)
    dt=tau/steps
    th=np.zeros(n)
    X=np.zeros((n,2),dtype=float)
    for _ in range(steps):
        dW0=rng.normal(0,np.sqrt(dt),size=n)
        dW=rng.normal(0,np.sqrt(dt),size=(n,2))
        cs=np.cos(th);sn=np.sin(th)
        Rb=np.column_stack((c[0]*cs-c[1]*sn,c[0]*sn+c[1]*cs))
        # Ito drift beta*R(theta)*J*c.
        Jc=np.array([-c[1],c[0]])
        drift=np.column_stack((Jc[0]*cs-Jc[1]*sn,Jc[0]*sn+Jc[1]*cs))
        perp=dW@sroot.T
        noise=perp+c[None,:]/np.sqrt(m)*dW0[:,None]
        rot_noise=np.column_stack((noise[:,0]*cs-noise[:,1]*sn,noise[:,0]*sn+noise[:,1]*cs))
        X+=beta*drift*dt+np.sqrt(2*beta)*rot_noise
        th+=np.sqrt(2*beta*m)*dW0
    return X.mean(axis=0)/tau,np.cov(X.T,bias=True)/tau

def main():
    checks=0
    u=sp.symbols('u',positive=True)
    # Nontrivial conditional-covariance cancellation and trace simplification.
    q=sp.exp(-u)
    var_parallel=(1+q**4)/2-q**2
    var_perp=(1-q**4)/2
    assert sp.simplify(var_parallel-(1-q**2)**2/2)==0; checks+=1
    assert sp.simplify(var_parallel+var_perp-(1-q**2))==0;checks+=1
    assert sp.simplify((1-q**2)-(1-q)*(1+q))==0;checks+=1
    # Schur-complement positivity and boundary checks.
    cases=[(1.3,0.75,np.array([[1.3,0.14],[0.14,0.9]]),np.array([0.6,-0.32]),1.1),
           (0.8,1.7,np.array([[0.73,-0.21],[-0.21,1.4]]),np.array([-0.22,0.65]),0.65),
           (1.,0.8,np.array([[0.9,0.25],[0.25,0.9]]),np.array([0.0,0.0]),0.9)]
    for ix,(beta,m,S,c,tau) in enumerate(cases):
        V,C=theory(beta,m,S,c,tau)
        A=S+np.outer(c,c)/m
        assert np.linalg.eigvalsh(S).min()>0;checks+=1
        assert np.linalg.eigvalsh(C).min()>0;checks+=1
        exp_trace=2*beta*np.trace(S)+(c@c/m**2)*(-np.expm1(-2*beta*m*tau))/tau
        assert np.allclose(np.trace(C),exp_trace,rtol=2e-14,atol=1e-14);checks+=1
        fmag=np.linalg.norm(c)/m
        assert np.isclose(np.trace(C)-2*beta*np.trace(S),fmag*(1+np.exp(-beta*m*tau))*np.linalg.norm(V),atol=1e-14);checks+=1
        for T in [1e-5,0.04,0.21,0.8,1.3,4.0,11.]:
            _,cur=theory(beta,m,S,c,T)
            assert np.linalg.eigvalsh(cur).min()>0;checks+=1
            assert np.trace(cur)<=2*beta*np.trace(A)+1e-8;checks+=1
            assert np.trace(cur)>=2*beta*np.trace(S)-1e-8;checks+=1
        near=theory(beta,m,S,c,1e-6)[1]
        far=theory(beta,m,S,c,10000)[1]
        assert np.allclose(near,2*beta*A,rtol=1e-5);checks+=1
        assert np.allclose(far,beta*np.trace(S)*np.eye(2),rtol=1e-3,atol=1e-4);checks+=1
        Vm,Cm=simulate(beta,m,S,c,tau,seed=840+ix)
        # Sampling tolerances scale by the predicted finite-sample cycle dispersion.
        se=np.sqrt(np.diag(C)*tau/24000)/tau
        assert np.all(np.abs(Vm-V)<5.5*se+0.016),('mean',ix,Vm,V,se);checks+=1
        assert np.allclose(Cm,C,atol=.065,rtol=.075),('cov',ix,Cm,C);checks+=1
        print('case',ix,'velocity theory/simulation',V,Vm,'cov theory/simulation',C.ravel(),Cm.ravel())
    # A genuine finite-period isotropization with a 90-degree principal-axis reversal.
    beta,m=1.2,0.9
    c=np.array([.65,-.2]);J=np.array([[0.,-1.],[1.,0.]])
    f=-J@c/m
    alpha=m/2
    H=np.outer(f,f)-.5*(f@f)*np.eye(2)
    S=1.2*np.eye(2)+alpha*H
    Tstar=np.log(2*m/alpha-1)/(2*beta*m)
    v0,C0=theory(beta,m,S,c,Tstar)
    assert np.allclose(C0, np.trace(C0)/2*np.eye(2),rtol=1e-12,atol=1e-12);checks+=1
    e=f/np.linalg.norm(f);e_perp=J@e
    Tbefore,Tafter=Tstar*.6,Tstar*1.8
    _,Cbefore=theory(beta,m,S,c,Tbefore)
    _,Cafter=theory(beta,m,S,c,Tafter)
    assert e@Cbefore@e < e_perp@Cbefore@e_perp;checks+=1
    assert e@Cafter@e > e_perp@Cafter@e_perp;checks+=1
    for T in [Tbefore,Tstar,Tafter]:
        _,CT=theory(beta,m,S,c,T)
        u=beta*m*T
        h=-np.expm1(-4*u)/(4*u)
        Gamma=2*m/(np.exp(2*u)+1)
        dev=CT-.5*np.trace(CT)*np.eye(2)
        assert np.allclose(dev,2*beta*h*(alpha-Gamma)*H,atol=1e-12);checks+=1
    print('isotropy threshold',Tstar, 'before/at/after longitudinal diffusion',
          e@Cbefore@e,e@C0@e,e@Cafter@e)
    print(f'PASS: {checks} algebraic, domain, limit, principal-axis, and independently sampled Ito-SDE checks')

if __name__=='__main__':main()
