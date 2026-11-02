"""Reproducible checks for finite-path boundary absorption theorem.
Requires Python 3, numpy, scipy, and sympy. Execute: python verify.py.
Checks are supplementary to the analytic proof in RESULT.md.
"""
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov

checks=0

def green(n,kappa,omega):
    out=np.zeros((n,n),dtype=complex)
    for j in range(1,n+1):
        for k in range(j,n+1):
            if (k-j)%2==0:
                v=(n+1-k)*(j/kappa + kappa*(j-1)/omega**2)
            else:
                v=-1j*(n+1-k)/omega
            out[j-1,k-1]=v
            out[k-1,j-1]=v.conjugate()
    return out

def generator(n,kappa,omega):
    T=np.diag(np.ones(n-1),1)+np.diag(np.ones(n-1),-1)
    G=1j*omega*T/2
    G[0,0]-=kappa/2
    return G

for n in range(2,16):
    for kappa,omega in [(0.2,1.),(1.,1.),(2.7,0.75),(4.1,2.3)]:
        G=generator(n,kappa,omega)
        X=green(n,kappa,omega)
        residual=G.conj().T@X+X@G+np.eye(n)
        assert np.max(np.abs(residual))<2e-10, (n,kappa,omega,np.max(np.abs(residual)))
        checks+=1
        assert np.max(np.abs(X - solve_continuous_lyapunov(G.conj().T,-np.eye(n))))<2e-8
        checks+=1
        assert np.min(np.linalg.eigvalsh(X))>0
        checks+=1
        for j in range(1,n+1):
            exact=(n+1-j)*(j/kappa+kappa*(j-1)/omega**2)
            assert abs(X[j-1,j-1]-exact)<1e-10
            checks+=1
            if j>1:
                optimal=omega*np.sqrt(j/(j-1))
                m=(n+1-j)*2*np.sqrt(j*(j-1))/omega
                assert abs(green(n,optimal,omega)[j-1,j-1]-m)<1e-9
                checks+=1
# Symbolic checks for each dimensional size. Generic proof of all N in RESULT.md.
kappa,omega=sp.symbols('kappa omega', positive=True)
for n in range(2,9):
    x=sp.zeros(n)
    for j in range(1,n+1):
        for k in range(j,n+1):
            val=(n+1-k)*(sp.Integer(j)/kappa+kappa*(j-1)/omega**2) if (k-j)%2==0 else -sp.I*(n+1-k)/omega
            x[j-1,k-1]=val
            x[k-1,j-1]=sp.conjugate(val)
    t=sp.zeros(n)
    for j in range(n-1):
        t[j,j+1]=t[j+1,j]=1
    e=sp.zeros(n); e[0,0]=1
    res=sp.I*omega*(x*t-t*x)/2-kappa*(e*x+x*e)/2+sp.eye(n)
    for a in range(n):
        for b in range(n):
            assert sp.simplify(res[a,b])==0,(n,a,b,res[a,b])
            checks+=1
print(f'PASS: {checks} deterministic numerical and finite-size symbolic consistency checks')
