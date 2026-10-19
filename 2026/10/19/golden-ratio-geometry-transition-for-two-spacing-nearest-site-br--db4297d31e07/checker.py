"""Independent reproducibility checks for a two-spacing nearest-site Brownian-reset model.

Only standard numerical libraries NumPy, SciPy, and mpmath are required.
The program does not substitute finite tests for the exact proof.
"""
import numpy as np
from math import sinh,cosh,sqrt,acosh,pi
from scipy.integrate import quad


def quantities(a,b,D,r):
    k=sqrt(r/D); L=a+b
    R=sinh(k*b)*cosh(k*a/2)
    Q=sinh(k*a)*cosh(k*b/2)
    S=R+Q
    p=R/S
    tau=(sinh(k*L)-sinh(k*a)-sinh(k*b))/(r*S)
    deff=L*L*p*(1-p)/(2*tau)
    deff2=r*L*L*cosh(k*a/2)*cosh(k*b/2)/(4*(sinh(k*a/2)+sinh(k*b/2))*sinh(k*L/2))
    return p,tau,deff,deff2

def resolvent(a,b,D,r):
    k=sqrt(r/D); L=a+b
    def g(y):
        if y < 0:
            return sinh(k*(b+y))*sinh(k*a)/(D*k*sinh(k*L))
        return sinh(k*b)*sinh(k*(a-y))/(D*k*sinh(k*L))
    p_right=(sinh(k*b)/sinh(k*L))+r*quad(g,a/2,a,epsabs=1e-12)[0]
    p_left=(sinh(k*a)/sinh(k*L))+r*quad(g,-b,-b/2,epsabs=1e-12)[0]
    duration=quad(g,-b,0,epsabs=1e-12)[0]+quad(g,0,a,epsabs=1e-12)[0]
    return p_right,p_left,duration

def close(x,y,tol=3e-10):
    assert abs(x-y)<tol*max(1.,abs(x),abs(y)),(x,y)

n=0
for a,b,D,r in [(0.45,0.55,1,0.05),(.1,.9,1,1),(.48,.52,1,20),(.3,.7,2,3),(.8,.2,1.7,.4),(.25,.75,.8,12),(.5,.5,1,2),(.99,.01,.5,3)]:
    p,tau,Deff,Deff2=quantities(a,b,D,r)
    right,left,one_duration=resolvent(a,b,D,r)
    close(p,right/(right+left))
    close(tau,one_duration/(right+left))
    close(Deff,Deff2)
    close(Deff,(a+b)**2*p*(1-p)/(2*tau))
    assert Deff>0 and 0<p<1 and tau>0
    n+=5

phi=(1+sqrt(5))/2
qc=acosh(phi)
close(cosh(qc),phi)
# Formula for the homogeneous lattice, with spacing l, is (kl/2)^2 coth(kl/2)csch(kl/2).
def homogeneous(k,l):
    x=k*l/2
    return x*x*cosh(x)/(sinh(x)*sinh(x))
for s in [.15,.7,1.5,2.0,2.125,2.6,4.0]:
    k=2*s;L=1;D=1;r=k*k
    equal=quantities(.5,.5,D,r)[2]/D
    nearly_dimer=quantities(1e-8,1-1e-8,D,r)[2]/D
    close(equal,homogeneous(k,L/2))
    close(nearly_dimer,homogeneous(k,L),5e-7)
    predicted_sign=np.sign(phi-cosh(s/2))
    actual_sign=np.sign(nearly_dimer-equal)
    assert actual_sign==predicted_sign,(s,predicted_sign,actual_sign)
    n+=3
# Independently verify global endpoint bounds of strictly convex hyperbolic profile.
for s in [0.25,1,1.75,2.,2.2,3,5]:
    c=cosh(s/2)
    f=lambda w: 2*w+(cosh(s)-1)/w
    endpoint=max(f(1.),f(c))
    for w in np.linspace(1,c,301):
        assert f(w)<=endpoint+5e-12
        n+=1
# Backtracking correction is strictly positive at non-uniform spacing and nonzero rate.
for a,b in [(.3,.7),(.1,.9),(.49,.51)]:
    p,tau,Deff,_=quantities(a,b,1.,3.)
    m=a*p-b*(1-p)
    q=a*a*p+b*b*(1-p)
    close(q-m*m,(a+b)**2*p*(1-p))
    assert abs(m)>1e-7
    assert q/(2*tau)>Deff
    n+=3
print('PASS',n,'numerical/quadrature/phase assertions')
print('golden-ratio switching: sqrt(r/D)*L =',4*qc)
print('crossover r L^2/D =',16*qc*qc)
