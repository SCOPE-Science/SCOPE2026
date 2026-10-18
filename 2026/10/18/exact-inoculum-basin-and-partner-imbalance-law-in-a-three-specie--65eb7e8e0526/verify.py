"""Independent numerical and symbolic checks for a three-taxon ecological-fitting threshold.

Run: python verify.py
Uses scipy, numpy, sympy; analytical proof is in RESULT.md.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import beta as beta_fn
import sympy as sp

def integral(a,c,r):
    q=.5-c/a
    assert 0<=r<1 and q>0
    return quad(lambda t: t**(q-1)/np.sqrt(1-r+r*t),0,1,epsabs=2e-11,epsrel=2e-11,limit=200)[0]/a

def threshold(a,c,d,r):
    return 1/(1+(-d)*integral(a,c,r))

def ode(a,c,d,mu):
    J=np.array([[0,a,d],[a,0,d],[c,c,0]],dtype=float)
    def fun(t,N):
        total=sum(N)
        return N*((J@N)/total-mu*total)
    return fun

def classify(a,c,d,mu,r,mode):
    # r=resident relative squared imbalance; resident total exactly 2.
    y=math.sqrt(r)
    resident=np.array([1+y,1-y],dtype=float)
    zc=threshold(a,c,d,r)
    # fraction initial is z=I/(I+2).
    z0=zc*mode
    invader=2*z0/(1-z0)
    sol=solve_ivp(ode(a,c,d,mu),[0,1200],[*resident,invader],method='DOP853',rtol=1e-10,atol=1e-12)
    X=sol.y[:,-1]
    if mode<1:
        assert np.allclose(X[:2],a/(4*mu),rtol=.002,atol=.002),(r,mode,X)
        assert X[2]<1e-4,(r,mode,X)
    elif mode>1:
        assert sum(X)<0.1,(r,mode,X)
        assert X[2]/sum(X)>.999,(r,mode,X)
        assert abs(mu*1200*sum(X)-1)<.1,(r,mode,X)
    return X

def exact_check():
    # With N=(N1,N2,N3), x_i=N_i/sum N, y=(x1-x2)/(x1+x2), r=y**2,
    # z=x3, w=(1-z)/z, s'=1-z, verify s-system by rational polynomials.
    a,c,d,p,z,y=sp.symbols('a c d p z y',real=True)
    x1=p*(1+y)/2; x2=p*(1-y)/2
    f1=a*x2+d*z; f2=a*x1+d*z; f3=c*p
    mean=(x1*f1+x2*f2)/p
    yp=sp.factor((1-y*y)*(f1-f2)/2)
    zp=sp.factor(z*p*(f3-mean))
    A=c-a*sp.Rational(1,2)*(1-y*y)
    assert sp.simplify(yp + a*p*y*(1-y*y)/2)==0
    assert sp.simplify(zp-z*p*(A*p-d*z))==0
    wp=sp.factor(mean-f3)
    assert sp.simplify(wp+ A*p-d*z)==0
    q=sp.symbols('q',positive=True)
    assert sp.simplify(sp.diff((a*(1-y*y))/2,y)+a*y)==0
    print('symbolic frequency identities: pass')

def main():
    exact_check()
    a,c,d,mu=2.,.5,-1.,.01
    assert abs(integral(a,c,0)-2)<1e-9
    assert abs(threshold(a,c,d,0)-1/3)<1e-9
    rr=[0,.04,.25,.64,.81,.96]
    vals=[threshold(a,c,d,r) for r in rr]
    assert all(x>y for x,y in zip(vals,vals[1:])),vals
    print('strict threshold decline: pass',list(zip(rr,vals)))
    q=.5-c/a
    B=beta_fn(q,c/a)
    for r in [.999, .9999, .99999]:
        zc=threshold(a,c,d,r)
        prediction=a/(-d*B)*(1-r)**(c/a)
        assert abs(zc/prediction-1)<.2,(r,zc,prediction)
    print('imbalanced-resident beta scaling: pass')
    for r in [0,.25,.64]:
        for mode in [.5,1.6]:
            result=classify(a,c,d,mu,r,mode)
            print('ODE basin',r,mode,result)
    print('ALL VERIFICATION CHECKS PASSED')
if __name__=='__main__': main()
