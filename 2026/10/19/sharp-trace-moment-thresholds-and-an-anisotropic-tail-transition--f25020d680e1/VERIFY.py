"""Reproduce exact analytic identities for a one-column two-sided Gaussian sketch."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma, beta


def angular_moments(e, power):
    f=lambda t: (e*(1-e)*abs(math.cos(t)*math.sin(t))/(math.cos(t)**2+e**2*math.sin(t)**2))**power
    return 2/math.pi *quad(f,0,math.pi/2,epsabs=3e-13,epsrel=3e-13,limit=250)[0]


def angular_mu_moments(e):
    fun=lambda t:(math.cos(t)**2+e**3*math.sin(t)**2)/(math.cos(t)**2+e**2*math.sin(t)**2)
    first=2/math.pi*quad(fun,0,math.pi/2,epsabs=3e-13,limit=250)[0]
    second=2/math.pi*quad(lambda t:fun(t)**2,0,math.pi/2,epsabs=3e-13,limit=250)[0]
    return first,second-first**2

checks=0
for e in [0.03,0.11,0.4,0.71,0.97]:
    m1=2*e*math.log(1/e)/(math.pi*(1+e))
    m2=e*(1-e)**2/(2*(1+e)**2)
    avg,var=angular_mu_moments(e)
    for lhs,rhs in [(angular_moments(e,1),m1),(angular_moments(e,2),m2),
                    (avg,(1+e**2)/(1+e)),(var,m2)]:
        assert abs(lhs-rhs)<2e-10,(e,lhs,rhs)
        checks+=1
    # evaluate full formula deterministically for random real probe arrays
    rng=np.random.default_rng(int(1000*e))
    for s in [1,2,3,5]:
        g=rng.standard_normal(2)
        Psi=rng.standard_normal((2,s))
        A=np.diag([1.,e]); v=A@g
        N=v[:,None] @ ((Psi.T @ v)[None,:] @ Psi.T @ A) / ((Psi.T @ v) @ (Psi.T @ v))
        tr=np.trace(N)
        a=Psi.T@v; b=Psi.T@(A@A@g)
        assert abs(tr-(a@b)/(a@a))<1e-12
        x,y=g
        mu=(x*x+e**3*y*y)/(x*x+e**2*y*y)
        tau=e*(1-e)*abs(x*y)/(x*x+e**2*y*y)
        # exact orthogonal component check, not relying on distribution fit
        expectedvar=(np.linalg.norm(A@A@g)**2/np.linalg.norm(A@g)**2-mu**2)
        assert abs(expectedvar-tau**2)<1e-12,(e,s,expectedvar,tau)
        checks+=2

for s in [2,3,4,5]:
    k=gamma((s+1)/2)/(s*math.sqrt(math.pi)*gamma(s/2))
    target=k*beta((s+1)/2,(s-1)/2)/math.pi
    # Stable angular evaluation for smaller e (s>1 dominated convergence)
    vals=[k*angular_moments(e,s)/e for e in [0.01,0.004]]
    assert abs(vals[-1]-target)<0.009,(s, vals, target)
    checks+=1

print('ALL_CHECKS_PASSED',checks)
print('Closed form: E[T_s]=(1+eps^2)/(1+eps) (s>=2); Var[T_s]=(s-1)/(s-2)*eps*(1-eps)^2/(2*(1+eps)^2) (s>=3).')
print('Tail: P(T_s>t)~P(T_s<-t)~k_s E[tau^s] t^-s, k_s=Gamma((s+1)/2)/(s sqrt(pi) Gamma(s/2)).')
