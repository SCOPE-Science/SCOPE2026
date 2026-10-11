"""Finite precision checks of a weighted Volterra transfer discriminant.

The all-weight, all-parameter spectral theorem is proved analytically; numeric
experiments in this file verify representative consequences only.
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def exact_identity():
    a,b,A,B,C,D=sp.symbols('a b A B C D',real=True)
    z=a+sp.I*b
    zb=a-sp.I*b
    det=sp.expand((1-z+z*A)*(zb+(1-zb)*D)-z*B*(1-zb)*C)
    assert sp.simplify(det.subs(C,(A*D-1)/B) - (1 + (a*a+b*b)*(A-1) + ((1-a)**2+b*b)*(D-1)))==0
    x=sp.symbols('x',real=True)
    k=1+x
    imbalance=sp.integrate((2*x-1)*k,(x,0,1))
    assert imbalance==sp.Rational(1,6)


def transfer(lam,k):
    def ode(x,v):
        return np.array([k(x)*v[1], -lam*v[0], k(x)*v[3], -lam*v[2]])
    sol=solve_ivp(ode,[0,1],[1.,0.,0.,1.],rtol=2e-11,atol=2e-12)
    A,C,B,D=sol.y[:,-1]
    assert abs(A*D-B*C-1)<3e-9
    return A,B,C,D


def singular(z,w,n=100):
    i=np.arange(n)
    ker=(np.greater(i[:,None],i[None,:]).astype(float)+.5*np.eye(n)-z)
    x=(i+.5)/n
    return np.linalg.svd(ker*np.asarray(w(x))[None,:]/n,compute_uv=False)


def numerical():
    ksym=lambda x: 1+x*(1-x)
    knonsym=lambda x: 1+x
    for lam in (1.,3.,14.,23.):
        A,B,C,D=transfer(lam,ksym)
        assert abs(A-D)<1e-9
        A,B,C,D=transfer(lam,knonsym)
        if lam==1.: assert abs(A-D)>0.015
    w=lambda x: np.sqrt(1+x*(1-x))
    for r in (.1,.37,.74):
        bas=singular(.5+r,w)
        for phi in (0.25,1.12,2.2):
            assert np.max(np.abs(bas-singular(.5+r*np.exp(1j*phi),w)))<2e-12
    w2=lambda x: np.sqrt(1+x)
    a=singular(0,w2)
    b=singular(1,w2)
    assert abs(sum(a*a)-sum(b*b))>0.16
    # exact Hilbert-Schmidt squares: at alpha=0: b=\int(1-t)w²; alpha=1: a=\int t w².
    assert sp.integrate((1-sp.Symbol('t'))*(1+sp.Symbol('t')),(sp.Symbol('t'),0,1))==sp.Rational(2,3)
    assert sp.integrate(sp.Symbol('t')*(1+sp.Symbol('t')),(sp.Symbol('t'),0,1))==sp.Rational(5,6)

if __name__=='__main__':
    exact_identity()
    numerical()
    print('WEIGHTED_VOLTERRA_TRANSFER_OK')
