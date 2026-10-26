"""Independent reproducibility tests for planar Taylor--Aris fixed-flux/fixed-dissipation optimization.

Scientific, deterministic; scipy and numpy required.  Run with python verify_taylor.py.
"""
import math
import numpy as np
from numpy.polynomial import Polynomial, Legendre
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.linalg import eigh


def integrate(fn, n=256):
    t, w = leggauss(n)
    y = (t+1)/2
    return float(np.dot(w/2, fn(y)))

alpha = brentq(lambda z: math.cos(z)*math.cosh(z)-1, 4.7, 4.8, xtol=1.e-14)
a = alpha/2
Delta = math.sin(a)*math.cosh(a)-math.cos(a)*math.sinh(a)
lam = alpha**4


def F0(y):
    return 3*y**2-2*y**3-y

def F0_d(y):
    return 6*y-6*y**2-1

def F0_dd(y):
    return 6-12*y

def H(y):
    t=y-.5
    return (math.sinh(a)*np.sin(alpha*t)-math.sin(a)*np.sinh(alpha*t))/(alpha*Delta)

def H_d(y):
    t=y-.5
    return (math.sinh(a)*np.cos(alpha*t)-math.sin(a)*np.cosh(alpha*t))/Delta

def H_dd(y):
    t=y-.5
    return -alpha*(math.sinh(a)*np.sin(alpha*t)+math.sin(a)*np.sinh(alpha*t))/Delta

def Fcrit(y): return H(y)-F0(y)
def Fc_d(y): return H_d(y)-F0_d(y)
def Fc_dd(y): return H_dd(y)-F0_dd(y)

def e1raw(y):
    t=y-.5
    return np.cosh(alpha*t)/math.cosh(a)-np.cos(alpha*t)/math.cos(a)
def e1raw_dd(y):
    t=y-.5
    return alpha**2*(np.cosh(alpha*t)/math.cosh(a)+np.cos(alpha*t)/math.cos(a))

norm_e=math.sqrt(integrate(lambda y:e1raw_dd(y)**2))
def e1(y):return e1raw(y)/norm_e
def e1dd(y):return e1raw_dd(y)/norm_e
rcrit2=integrate(lambda y:Fc_dd(y)**2)
qcrit=integrate(lambda y:H(y)**2)


def close(x,y,tol=2e-9):
    if abs(x-y)>tol*max(1,abs(x),abs(y)):
        raise AssertionError((x,y))

assert 4.73<alpha<4.731
close(lam,500.56390174038)
close(rcrit2,0.37020566946831)
close(qcrit,0.00614437965871598)
close(integrate(lambda y:F0(y)**2),1/210)
close(integrate(lambda y:(6-12*y)**2),12)
for y in [0, .12, .5, .73, 1]:
    close(Fcrit(y),-Fcrit(1-y)); close(e1(y),e1(1-y))
    close(lam*H(y), lam*(Fcrit(y)+F0(y)))
for y in [0, 1]:
    close(Fcrit(y),0);close(Fc_d(y),0)
    close(e1(y),0)
close(integrate(lambda y:e1dd(y)**2),1)
close(integrate(lambda y:e1(y)**2),1/lam)
close(integrate(lambda y:Fcrit(y)*e1(y)),0)

for E in [12+rcrit2, 12.6,13,20,100]:
    radius=math.sqrt(max(0,E-12-rcrit2))
    for sign in [-1,1]:
        ff=lambda y:Fcrit(y)+sign*radius*e1(y)
        dd=lambda y:Fc_dd(y)+sign*radius*e1dd(y)
        close(integrate(lambda y:dd(y)**2),E-12)
        close(integrate(lambda y:(F0(y)+ff(y))**2),qcrit+(E-12-rcrit2)/lam)

# Independent closed-form subcritical stationary branches and their energies.
for k in [0.2, 1, 2, 3.5, 4.5]:
    a0=k/2
    d0=math.sin(a0)*math.cosh(a0)-math.cos(a0)*math.sinh(a0)
    def h0(y):
        t=y-.5
        return (math.sinh(a0)*np.sin(k*t)-math.sin(a0)*np.sinh(k*t))/(k*d0)
    def h0_d(y):
        t=y-.5
        return (math.sinh(a0)*np.cos(k*t)-math.sin(a0)*np.cosh(k*t))/d0
    def h0_dd(y):
        t=y-.5
        return -k*(math.sinh(a0)*np.sin(k*t)+math.sin(a0)*np.sinh(k*t))/d0
    def fsubdd(y): return h0_dd(y)-F0_dd(y)
    for y in [0, .17, .5, .83, 1]:
        close(h0(y),-h0(1-y))
    for y in [0,1]:
        close(h0(y),0,tol=2e-8)
        close(h0_d(y),-1,tol=2e-8)
    assert 0 < integrate(lambda y:fsubdd(y)**2) < rcrit2

# Independent finite-element-like polynomial Galerkin computations, with the physical
# dispersion computed from the same primitive but independent coordinates.
def gal(N):
    x=Polynomial([0,1]); base=x*x*(1-x)*(1-x)
    pol=[base*Legendre.basis(j).convert(kind=Polynomial)(2*x-1) for j in range(N)]
    d2=[p.deriv(2) for p in pol]
    S=np.array([[integrate(lambda y,p=p,t=t:p(y)*t(y)) for t in pol] for p in pol]);
    K=np.array([[integrate(lambda y,p=p,t=t:p(y)*t(y)) for t in d2] for p in d2]);
    b=np.array([integrate(lambda y,p=p:F0(y)*p(y)) for p in pol]);
    s,V=eigh(S,K)
    ix=np.argsort(s)[::-1];s=s[ix];V=V[:,ix];bb=V.T@b
    # Largest numerical spectral direction is reflection-even F.
    ys=np.array([0,.21,.5,.79,1]); lead=sum(V[j,0]*pol[j](ys) for j in range(N))
    close(lead[0],0,tol=2e-8)
    close(lead[1],lead[3],tol=2e-7)
    assert abs(bb[0])<1e-9
    rcrit_n=math.sqrt(sum((bb[1:]/(s[0]-s[1:]))**2))
    return pol,S,K,b,s,V,bb,rcrit_n

for N in [8,12]:
    pol,S,K,b,s,V,bb,rn=gal(N)
    if N==12:
        assert abs(s[0]-1/lam)<1e-10
        assert abs(rn**2-rcrit2)<1e-7
    for E in [12.05, 12.25, 12+rcrit2+.05,13,16]:
        r=math.sqrt(E-12)
        if r<=rn:
            fun=lambda mu:np.linalg.norm(bb/(mu-s))-r
            mu=brentq(fun, s[0]+1e-8, max(10,s[0]+2*np.linalg.norm(bb)/r))
            z=bb/(mu-s)
        else:
            mu=s[0]
            z=np.zeros(N)
            z[1:]=bb[1:]/(mu-s[1:])
            z[0]=math.sqrt(max(0,r*r-np.dot(z[1:],z[1:])))
        f=V@z
        close(float(f@K@f),r*r,1e-7)
        value=1/210+2*(b@f)+f@S@f
        assert value>1/210
        if E>=12+rcrit2:
            sharp=qcrit+(E-12-rcrit2)/lam
            assert value<=sharp+2e-7 and sharp-value <3e-6,(N,E,value,sharp)
        # Randomly chosen competitors with identical energy cannot beat computed optimum
        rng=np.random.default_rng(N*1000+round(E*100))
        for _ in range(100):
            d=rng.normal(size=N);d=d/math.sqrt(d@K@d)*r
            other=1/210+2*b@d+d@S@d
            assert other<=value+1e-8,(N,E,other,value)
print('PASS: analytic clamped identities, threshold, reflection pair, dispersion; Galerkin N=8,12 and 1000 random feasible competitors.')
print('alpha=',alpha,'threshold_E_over_12=',(12+rcrit2)/12,'rcrit2=',rcrit2,'Tcrit=',qcrit)
