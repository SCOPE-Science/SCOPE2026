"""Reproduce the exact gap--subspace-error identities on an edge and an isolate.

Run with Python 3, NumPy, SymPy, and SciPy. No external data are needed.
Finite checks supplement, rather than replace, the analytic proof.
"""
import math
import random
from fractions import Fraction

import numpy as np
import sympy as sp
from scipy.integrate import quad


def shift(e, t):
    return (math.hypot(1.0, e*t/2.0)-1.0)/e


def residual(e, t):
    return 1.0-1.0/math.hypot(1.0, e*t/2.0)


def conditional_gap(e, t):
    return 0.25+(1.0-t)**2/12.0+shift(e,t)**2


def mean(q):
    return quad(lambda t:2*(1-t)*q(t), 0.0, 1.0, epsabs=2e-13)[0]


def covariance(e):
    f=lambda t:conditional_gap(e,t)
    r=lambda t:residual(e,t)
    return e*(mean(lambda t:f(t)*r(t))-mean(f)*mean(r))


def correlation(e):
    f=lambda t:conditional_gap(e,t)
    r=lambda t:residual(e,t)
    mu_f=mean(f)
    var_f=mean(lambda t:(1+(1-t)**2)/12+shift(e,t)**2)-mu_f**2
    mu_r=mean(r)
    var_r=mean(lambda t:r(t)**2)-mu_r**2
    return (mean(lambda t:f(t)*r(t))-mu_f*mu_r)/math.sqrt(var_f*var_r)


def direct_check():
    rng=random.Random(384019)
    L=np.array([[1.0,-1.0,0.0],[-1.0,1.0,0.0],[0.0,0.0,0.0]])
    A=L/math.sqrt(2.0)
    assert np.allclose(A.T@A,L)
    checks=0
    for e in [0.025,0.1,0.5,1.0,1.999]:
        for _ in range(200):
            u,v,w=(rng.random() for _ in range(3))
            M=(u+v)/2; t=abs(u-v)
            B=L+e*np.diag([u,v,w])
            vals,vecs=np.linalg.eigh(B)
            assert vals[2]>vals[1],(e,vals)
            gap=vals[1]-vals[0]
            expected_gap=e*abs(w-M+shift(e,t))
            assert math.isclose(gap,expected_gap,rel_tol=2e-10,abs_tol=3e-14),(gap,expected_gap)
            V=vecs[:,:2]
            Q=A@V
            observed=float(np.linalg.norm(Q,ord=2)**2)
            assert math.isclose(observed,residual(e,t),rel_tol=2e-8,abs_tol=1e-13),(observed,residual(e,t))
            assert 0<=observed<1
            checks+=4
    return checks


def exact_check():
    t=sp.symbols('t',real=True)
    E=lambda q:sp.integrate(2*(1-t)*q,(t,0,1))
    m=sp.Rational(1,4)+(1-t)**2/12
    assert E(t**2)==sp.Rational(1,6)
    assert E(t**4)==sp.Rational(1,15)
    assert E(m)==sp.Rational(7,24)
    assert E(m*t**2)==sp.Rational(2,45)
    assert sp.simplify(E(t**2*m)-E(t**2)*E(m))==-sp.Rational(1,240)
    assert E(sp.Rational(1,12)+(1-t)**2/12)==sp.Rational(1,8)
    assert sp.simplify(sp.Rational(1,8)-E(m)**2)==sp.Rational(23,576)
    assert sp.simplify(E(t**4)-E(t**2)**2)==sp.Rational(7,180)
    rho=sp.simplify(-sp.Rational(1,240)/sp.sqrt(sp.Rational(23,576)*sp.Rational(7,180)))
    assert rho==-3/sp.sqrt(805)
    assert sp.simplify((sp.Rational(3,1)-2*sp.sqrt(2))/4 < sp.Rational(5,112))==sp.true
    return 9


def integration_check():
    checks=0
    for e in [.01,.05,.1,.5,1.,1.5,1.99]:
        mu=mean(lambda t:conditional_gap(e,t))
        assert conditional_gap(e,0)>mu>conditional_gap(e,1),(e,mu)
        assert covariance(e)<0,(e,covariance(e))
        checks+=2
    assert abs(mean(lambda t:t*t)-1/6)<1e-14
    assert abs(mean(lambda t:conditional_gap(.0001,t))-7/24)<1e-9
    checks+=2
    expected_rho=-3/math.sqrt(805)
    assert abs(correlation(.002)-expected_rho)<2e-5,(correlation(.002),expected_rho)
    checks+=1
    # Directly integrate uniform W and conditional midpoint to verify E[gap|T=t].
    xs, weights=np.polynomial.legendre.leggauss(96)
    xs=(xs+1)/2; weights=weights/2
    for e in [0.3,1.7]:
        for t in [0.0,.1,.35,.7,.95,1.0]:
            m=t/2+(1-t)*xs
            centers=m-shift(e,t)
            avg=sum(wt*(c*c+(1-c)*(1-c))/2 for wt,c in zip(weights,centers))
            assert abs(avg-conditional_gap(e,t))<3e-14,(e,t,avg,conditional_gap(e,t))
            checks+=1
    return checks


if __name__=='__main__':
    n=direct_check()+exact_check()+integration_check()
    print('PASS',n,'assertion groups')
    for e in [0.1,0.5,1.,1.5,1.99]:
        print('epsilon',e,'mean gap',e*mean(lambda t:conditional_gap(e,t)),'mean squared null residual',mean(lambda t:residual(e,t)),'cov',covariance(e))
    print('weak-noise correlation limit',-3/math.sqrt(805))
