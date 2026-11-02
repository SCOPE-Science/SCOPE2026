"""Numerical cross-checks for optical-branch group-velocity theorem.
Requires Python 3, NumPy, SciPy. Units: spring=cell length=1.
Finite checks are not proofs of the all-parameter theorem.
"""
import math
import numpy as np
from numpy.linalg import eigvalsh
from scipy.optimize import brentq, minimize_scalar


def exact(c):
    assert 0 < c < 1
    f = lambda u: u**3+c*c*u-2*c*c
    u = brentq(f,c,1,xtol=2e-15)
    q = 2*math.asin(math.sqrt((1-u*u)/(1-c*c)))
    v = math.sqrt((1-u)*(1-c*c/(u*u)))/4
    return u,q,v


def raw(c,q):
    mu=1-c*c
    u=math.sqrt(1-mu*math.sin(q/2)**2)
    return mu*math.sin(q)/(8*u*math.sqrt(1+u))


def dispersion(c,q):
    m1=(1-c)/2; m2=(1+c)/2
    # two-atom Bloch matrix with nearest springs (each=1); phases for unit cell
    # normalized Bloch dynamical matrix for frequency squared
    dm=np.array([[2/m1,-(1+np.exp(-1j*q))/math.sqrt(m1*m2)],
                 [-(1+np.exp(1j*q))/math.sqrt(m1*m2),2/m2]])
    ww=eigvalsh(dm)
    return math.sqrt(ww[1])

checks=0
for c in np.linspace(0.001,0.999,101):
    u,q,v=exact(float(c))
    # In this mass normalization Omega^2 = 4/(1-c^2).
    Om=2/math.sqrt(1-c*c)
    opt=minimize_scalar(lambda x:-raw(c,x),bounds=(0,math.pi),method='bounded',options={'xatol':1e-12})
    assert abs(-opt.fun-v)<2e-10,(c,opt.fun,v)
    checks+=1
    assert abs(raw(c,q)-v)<1e-12,(c,raw(c,q),v)
    checks+=1
    # dispersion derivative with mass convention, should equal Omega*raw(c,q)
    h=1e-5
    num=(dispersion(c,q+h)-dispersion(c,q-h))/(2*h)
    assert abs(num+Om*v)<5e-6, (c,num,Om*v)
    checks+=1
    # unique sign change of F'(u) on (c,1)
    grid=np.linspace(c,1,1001)
    fs=2*c*c -grid**3-c*c*grid
    assert np.sum(fs[:-1]*fs[1:]<0)<=1
    checks+=1
    # acoustic sound speed and universal sharp optical bound
    vsound=Om*math.sqrt(1-c*c)/(2*math.sqrt(2))
    assert Om*v/vsound<1/math.sqrt(2)
    checks+=1
for c in [1e-3,1e-4,1e-5,1e-6,1e-7,1e-8]:
    u,q,v=exact(c)
    print('small contrast',c,'u/c^(2/3)',u/c**(2/3),'(pi-q)/c^(2/3)',(math.pi-q)/c**(2/3),
          '(1-4v)/c^(2/3)',(1-4*v)/c**(2/3))
    assert abs(u/(c**(2/3))-2**(1/3))<0.03
    assert abs((math.pi-q)/(c**(2/3))-2**(4/3))<0.04
    assert abs((1-4*v)/(c**(2/3))-3/(2**(5/3)))<0.05
    checks+=3
print('CHECKS PASSED',checks)
