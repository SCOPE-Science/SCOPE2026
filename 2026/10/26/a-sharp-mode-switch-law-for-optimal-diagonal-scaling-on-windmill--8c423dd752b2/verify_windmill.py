"""Reproduce symbolic identities and finite numerical checks for diagonal scaling
of a weighted windmill correlation matrix. This code provides finite tests,
not a substitute for the mathematical proof for all parameters.
"""
from math import sqrt
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar


def matrix(k, s, t):
    A = np.eye(2*k+1)
    for j in range(k):
        a, b = 2*j+1, 2*j+2
        A[a,b] = A[b,a] = s
        A[0,a] = A[a,0] = t
        A[0,b] = A[b,0] = t
    return A


def qopt(k,s,t):
    a = 1+s
    if k*t*t <= 2*s*s/a:
        return s*(1-s)/(s-k*t*t)
    return a


def kopt(k,s,t):
    a = 1+s
    if k*t*t <= 2*s*s/a:
        q = qopt(k,s,t)
        return (2*s+q)/(1-s)
    rho = sqrt(2*k*t*t/a)
    return (1+rho)/(1-rho)


def condition(A, diag):
    eig = np.linalg.eigvalsh((diag[:,None]*A)*diag[None,:])
    return eig[-1]/eig[0], eig


def main():
    s,t,k,q = sp.symbols('s t k q', positive=True)
    a,nu = 1+s,1-s
    cross_squared=2*k*t*t*q
    discr=(a-q)**2+4*cross_squared
    det=q*(a-2*k*t*t)
    q0=s*(1-s)/(s-k*t*t)
    assert sp.factor((a-nu)*(q0-nu)-2*k*t*t*q0)==0
    assert sp.factor((a+q)**2-4*a*q-(a-q)**2)==0
    assert sp.factor((a+q0)-nu - (2*s+q0)) == 0
    assert sp.factor(q0.subs(t,s/sp.sqrt(k))-1)==0
    assert sp.factor(((q0-a)*(s-k*t*t))) == sp.factor((1+s)*k*t*t-2*s*s)
    print('symbolic polynomial and transition identities: PASS')

    exact = [
        (2, sp.Rational(1,2), sp.Rational(1,10)),
        (3, sp.Rational(1,4), sp.Rational(1,4)),
        (4, sp.Rational(2,5), sp.Rational(1,5)),
        (5, sp.Rational(3,5), sp.Rational(1,10)),
        (6, sp.Rational(1,3), sp.Rational(1,6)),
    ]
    for kk,ss,tt in exact:
        AA=sp.eye(2*kk+1)
        for j in range(kk):
            aidx,bidx=2*j+1,2*j+2
            AA[aidx,bidx]=AA[bidx,aidx]=ss
            for u in (aidx,bidx): AA[0,u]=AA[u,0]=tt
        z=sp.symbols('z')
        chi=sp.factor(AA.charpoly(z).as_expr())
        target=(z-(1-ss))**kk*(z-(1+ss))**(kk-1)*((z-1)*(z-(1+ss))-2*kk*tt**2)
        assert sp.factor(chi-target)==0
        qq=sp.Rational(str(qopt(kk,float(ss),float(tt)))).limit_denominator(10**7)
        # Choose a separate rational positive hub scaling, independently of optimizer.
        qq=sp.Rational(7,5)
        EE=sp.diag(sp.sqrt(qq), *([1]*(2*kk)))
        chi_scaled=sp.factor((EE*AA*EE).charpoly(z).as_expr())
        expected_scaled=(z-(1-ss))**kk*(z-(1+ss))**(kk-1)*((z-qq)*(z-(1+ss))-2*kk*tt**2*qq)
        assert sp.factor(chi_scaled-expected_scaled)==0
    print('five exact-rational full characteristic polynomial certificates: PASS')

    rng=np.random.default_rng(241003)
    sampled=0; one_dim=0; global_samples=0
    for kk in (2,3,4,6,9):
        for ss in (0.13,0.4,0.72):
            bound=sqrt((1+ss)/(2*kk))
            for fraction in (0.1,0.3,0.6,0.83,0.95):
                tt=bound*fraction
                AA=matrix(kk,ss,tt)
                qo=qopt(kk,ss,tt)
                d=np.ones(2*kk+1); d[0]=sqrt(qo)
                best,eig=condition(AA,d)
                assert abs(best/kopt(kk,ss,tt)-1)<5e-10
                assert eig[0]>0
                f=lambda x: condition(AA,np.array([sqrt(np.exp(x))]+[1]*(2*kk)))[0]
                fit=minimize_scalar(f,bounds=(-6,6),method='bounded',options={'xatol':1e-11})
                assert fit.fun>=best*(1-2e-9)
                one_dim+=1
                for _ in range(80):
                    random_diag=np.exp(rng.uniform(-1.3,1.3,size=2*kk+1))
                    val,_=condition(AA,random_diag)
                    assert val >= best*(1-1e-10)
                    global_samples+=1
                sampled+=1
    print(f'{sampled} spectrum/condition identities, {one_dim} independent scalar optimizations, {global_samples} asymmetric random scalings: PASS')
    print('All reproducibility checks passed. Analytical proof is required for unrestricted global optimality.')

if __name__=='__main__':
    main()
