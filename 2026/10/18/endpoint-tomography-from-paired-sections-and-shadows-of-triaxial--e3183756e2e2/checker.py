"""Reproducibility checks for the triaxial ellipsoid paired section--projection tail theorem.
Only exact algebraic identities and independently integrated finite examples are tested.
The all-triaxial statement is established by the mathematical proof, not by this code.
"""
from fractions import Fraction as F
from math import pi, asin, sqrt, isclose
import numpy as np
from scipy.integrate import quad


def invariants(a,b,c):
    assert 0<a<b<c
    A=(b-a)**2/(a*b)
    B=(c-a)**2/(a*c)
    C=(c-b)**2/(b*c)
    delta=B-A-C
    assert delta>0
    K=1+B/4
    gamma=sqrt(2/(B*delta))
    return A,B,C,delta,K,gamma


def conditional_tail(t, eta, A,B,C):
    x=t*t
    h2=B*(1-x)**2/4
    h1=x*(1-x)*(A-C)/2
    h0=h2+x*(1-x)*(A+C)/2
    target=B/4-eta
    if h2 <= 0:
        return 0.
    disc=h1*h1+4*h2*(h0-target)
    if disc<=0:
        return 0.
    lo=(h1-sqrt(disc))/(2*h2)
    hi=(h1+sqrt(disc))/(2*h2)
    lo=max(-1.,lo); hi=min(1.,hi)
    if hi<=lo:
        return 0.
    return (asin(hi)-asin(lo))/pi


def deterministic_upper_tail(a,b,c,eta):
    A,B,C,D,K,gamma=invariants(a,b,c)
    # By (a+c-(b-a)(c-b)t^2/b)^2/(4ac), there is no
    # contribution beyond |u_2|>sqrt(2eta / D).
    tmax=min(1.,sqrt(2*eta/D))
    val,err=quad(lambda t:conditional_tail(t,eta,A,B,C),0.,tmax,
                 epsabs=1.e-11,epsrel=1.e-10,limit=700)
    return val,err


def test():
    samples=[(F(1),F(2),F(3)),(F(2),F(3),F(7)),
             (F(3),F(5),F(8)),(F(1),F(4),F(25))]
    for a,b,c in samples:
        A,B,C,D,K,gamma=invariants(a,b,c)
        assert D == (b-a)*(a+c)*(c-b)/(a*b*c)
        assert gamma*gamma>0
        k=c/a; t=b/a
        recovered_h = (k+1) - (k/(k+1))*D
        assert abs(float(recovered_h-t-k/t))<1e-12
        # The two solutions to z^2 - recovered_h*z + k are t and k/t.
        assert abs(float(t*t-recovered_h*t+k))<1e-12
        # Inversion + rescaling produces the same distribution and slope.
        dual=(F(1),a*c/b/a,c/a) if False else (a,a*c/b,c)
        A2,B2,C2,D2,K2,gamma2=invariants(*dual)
        assert K==K2
        assert D==D2
        assert abs(float(gamma-gamma2))<1e-12
        # Exact pairwise identity for squared same-normal area ratio.
        w=(F(1,5),F(1,3),F(7,15))
        assert sum(w)==1
        lam=(a,b,c)
        X=sum(lam[i]*w[i] for i in range(3))
        Y=sum(w[i]/lam[i] for i in range(3))
        assert X*Y-1 == A*w[0]*w[1]+B*w[0]*w[2]+C*w[1]*w[2]
    assert isclose(float(invariants(F(1),F(2),F(3))[4]), 4./3.,abs_tol=1e-14)
    assert isclose(invariants(1.,2.,3.)[5],1.5,rel_tol=1.e-13)
    rng=np.random.default_rng(31415926)
    for (a,b,c) in ((1,2,3),(2,3,7),(1,4,25)):
        A,B,C,D,K,gamma=invariants(a,b,c)
        x=rng.normal(size=(20000,3));x=x/np.linalg.norm(x,axis=1)[:,None]
        X=np.sum((x*x)*np.array([a,b,c]),axis=1)
        Y=np.sum((x*x)/np.array([a,b,c]),axis=1)
        w=x*x
        poly=1+A*w[:,0]*w[:,1]+B*w[:,0]*w[:,2]+C*w[:,1]*w[:,2]
        assert np.max(np.abs(X*Y-poly))<1e-12
        assert np.min(poly)>=1-1e-12 and np.max(poly)<=K+1e-12
        vals=[]
        for eta in (0.012,0.003,0.00075):
            area,error=deterministic_upper_tail(a,b,c,eta)
            ratio=area/(gamma*eta)
            vals.append((eta,area,ratio,error))
        print('axes_sq=',(a,b,c),'K=',K,'gamma=',gamma,'tail_data=',vals)
        assert abs(vals[-1][2]-1)<0.016, 'tail slope coefficient disagreement'
        assert abs(vals[-1][2]-1)<abs(vals[0][2]-1), 'tail ratio not converging'
    print('All exact, spectral-bound and independent spherical cap integration checks passed.')

if __name__=='__main__':
    test()
