"""Reproducibility checks for a harmonically confined run--pause--reverse particle.

Dependencies: Python 3, sympy, scipy, numpy.
Run: python verify_run_pause_reverse.py
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

alpha,beta,kappa,v,t = sp.symbols('alpha beta kappa v t', positive=True, real=True)
z=sp.symbols('z', real=True)
B=sp.Matrix([[-alpha, alpha],[-beta,-beta]])
D=lambda x: (x+alpha)*(x+beta)+alpha*beta
checks=0
assert sp.factor((z*sp.eye(2)-B).det()-D(z))==0;checks+=1
assert sp.factor((z*sp.eye(2)-B).inv()[0,0]-(z+beta)/D(z))==0;checks+=1
P=sp.simplify((beta+kappa)/D(kappa))
assert sp.factor(((kappa*sp.eye(2)-B).inv())[0,0]-P)==0;checks+=1
R=sp.factor(((beta-kappa)/D(-kappa)+(beta+kappa)/D(kappa))/2/kappa)
Bco=alpha*(2*beta**2-kappa**2)/(kappa*D(-kappa)*D(kappa))
assert sp.factor(R-Bco)==0;checks+=1
r=sp.symbols('r',positive=True, real=True)
critical=sp.factor((r+1)**2*(3*r*r+14*r+3)-r*(8-(r+1)**2)**2)
assert sp.factor(critical+(r+3)*(r*r-6*r+1)*(r*r+4*r-1))==0;checks+=1

# The stationary velocity covariance is A*(exp(B*t))[0,0],
# where A=v^2 beta/(alpha+beta). The stationary position process
# is its exponential linear filter, and the following computes
# its autocovariance by an independent three-dimensional ODE.
def covariance_ode(a,b,k,velocity,time):
    A=velocity**2*b/(a+b)
    T=np.array([[-a,a],[-b,-b]],dtype=float)
    y0=np.linalg.solve(k*np.eye(2)-T,np.array([1.,0.]))
    x0=A*y0[0]/k
    E=np.zeros((3,3));E[0,0]=-k;E[0,1]=A;E[1:,1:]=T
    return float((expm(E*time)@np.array([x0,*y0]))[0])

def covariance_formula(a,b,k,velocity,time):
    disc=(a-b)**2-4*a*b
    if not disc<0: raise ValueError('Require complex velocity poles')
    m=(a+b)/2
    w=math.sqrt(-disc)/2
    delta=(a-b)/2
    complex_amplitude=(1+1j*delta/w)/(k*k-(-m+1j*w)**2)
    Dp=(k+a)*(k+b)+a*b
    Dm=(-k+a)*(-k+b)+a*b
    A=velocity**2*b/(a+b)
    real_amplitude=a*(2*b*b-k*k)/(k*Dp*Dm)
    return A*((complex_amplitude*complex(math.cos(w*time),math.sin(w*time))).real*math.exp(-m*time)+real_amplitude*math.exp(-k*time))

examples=[(3.,1.,math.sqrt(2),1.2),(3.,1.,1.1,1.2),(3.,1.,2.,1.2),
          (3.,1.,3.2,1.2),(1.,1.,1.,2.),(.2,1.,.6,1.2),(.3,1.,.65,1.2),
          (5.,1.,2.5,.7)]
for a,b,k,velocity in examples:
    for time in (0.,.01,.25,1.,2.,4.,10.,20.):
        x=covariance_formula(a,b,k,velocity,time)
        y=covariance_ode(a,b,k,velocity,time)
        assert abs(x-y)<1.e-10*(1+abs(y)),(a,b,k,time,x,y)
        checks+=1
# At tuned cancellation, the non-oscillatory exponential vanishes identically.
a,b,k=3.,1.,math.sqrt(2)
assert abs(a*(2*b*b-k*k))<1.e-12;checks+=1
for j in range(12):
    time=(j+.25)*math.pi/math.sqrt(2)
    x=covariance_formula(a,b,k,1,time)
    assert abs(x)*math.exp((a+b)*time/2)>1e-6; checks+=1

print(f'{checks} symbolic and independently computed covariance checks passed')
