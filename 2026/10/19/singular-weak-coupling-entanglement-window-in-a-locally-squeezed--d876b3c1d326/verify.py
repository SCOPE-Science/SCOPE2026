"""Reproducible checks for the phase-locked bosonic-dimer optimization theorem.

Run: python verify.py  (dependencies: numpy, scipy, sympy)
Finite numerical checks supplement, but do not replace, the analytical proof.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import solve_continuous_lyapunov

passed = 0

def check(ok, msg='check'):
    global passed
    if not ok:
        raise AssertionError(msg)
    passed += 1

def omega():
    return np.kron(np.eye(2), np.array([[0., 1.], [-1., 0.]]))

def pt_symplectic_min(v):
    p = np.diag([1.,1.,1.,-1.])
    eig = np.linalg.eigvals(1j * omega() @ p @ v @ p)
    return sorted(abs(a) for a in eig)[0]

def dimer(r, coupling, gamma, bath_y):
    K, S = math.cosh(2*r), math.sinh(2*r)
    m = gamma*gamma / (gamma*gamma + 4*coupling*coupling)
    chi = 2*gamma*coupling / (gamma*gamma+4*coupling*coupling)
    anomalous = -bath_y*S/2
    local = bath_y*K/2
    drift = np.array([[-gamma/2,0,0,coupling],
                      [0,-gamma/2,-coupling,0],
                      [0,coupling,-gamma/2,0],
                      [-coupling,0,0,-gamma/2]], float)
    noise = gamma*np.diag([local+anomalous,local-anomalous,
                           local+anomalous,local-anomalous])
    v = solve_continuous_lyapunov(drift, -noise)
    pred = np.array([[local+m*anomalous,0,0,-chi*anomalous],
                     [0,local-m*anomalous,-chi*anomalous,0],
                     [0,-chi*anomalous,local+m*anomalous,0],
                     [-chi*anomalous,0,0,local-m*anomalous]])
    nu = bath_y/2 * (math.sqrt(K*K-m*m*S*S)-chi*S)
    return drift,noise,v,pred,nu,m

m,t = sp.symbols('m t', positive=True)
poly = sp.expand((2*m-1)**2*(1-m*m*t*t)-4*t*t*m**3*(1-m))
check(sp.factor(poly-(((2-t)*m-1)*((2+t)*m-1))) == 0, 'exact derivative sign polynomial')
check(sp.factor(((2-t)**2-t**2)-4*(1-t)) == 0, 'optimum radical identity')
check(sp.factor(((2-t)*m-1).subs(m,1/(2-t)))==0, 'coupling unique root')

for gamma in [0.4,1.,2.3]:
 for r in [0.06,0.25,0.72,1.4]:
  for jratio in [0.07,0.3,0.8,1.7]:
   j = gamma*jratio
   for bath_y in [1.,1.15,1.7]:
    a,d,v,pred,nu,mu = dimer(r,j,gamma,bath_y)
    check(np.max(np.abs(a@v+v@a.T+d)) < 2e-11, 'Lyapunov solution')
    check(np.max(np.abs(v-pred)) < 2e-11, 'independent covariance')
    check(abs(pt_symplectic_min(v)-nu)<2e-11, 'PPT eigenvalue')
    check(nu>0, 'PPT eigenvalue positivity')

for r in [0.0004,0.025,0.1,0.35,0.9,1.8,3.]:
 s=math.sinh(2*r);t=math.tanh(2*r)
 optm=1/(2-t)
 def R(mu): return math.sqrt(1+(1-mu*mu)*s*s)-s*math.sqrt(mu*(1-mu))
 check(abs(R(optm)-1/math.sqrt(1+t))<4e-12, 'exact J optimum')
 for mu in np.linspace(0.0001,0.9999,57):
  check(R(mu)>=R(optm)-3e-11, 'global coupling inequality')
 for j in [0.03,0.23,0.5,3,50]:
  mu=1/(1+j*j)
  ss=math.sqrt(mu/(1-mu*mu))
  rs=math.sqrt(1+(1-mu*mu)*ss*ss)-math.sqrt(mu*(1-mu))*ss
  check(abs(rs-1/math.sqrt(1+mu))<3e-12,'fixed-coupling squeeze optimum')

for r in [3.5,4.,5.]:
 for z in [0.,0.04,0.2,0.70710678118,1.5,2.5,5.]:
  J=1.2*z*math.exp(-2*r)
  _,_,_,_,nu,_=dimer(r,J,1.2,1.)
  check(abs(2*nu-(math.sqrt(1+2*z*z)-z))<4e-5, 'singular scaling profile')

for y in [1.,1.03,1.2,1.4]:
 c=1/y
 if y<math.sqrt(2):
  zlo=c-math.sqrt(2*c*c-1)
  zhi=c+math.sqrt(2*c*c-1)
  f=lambda z: math.sqrt(1+2*z*z)-z
  check(abs(f(zlo)-c)<1e-12,'lower window endpoint')
  check(abs(f(zhi)-c)<1e-12,'upper window endpoint')
  check(f((zlo+zhi)/2)<c,'window interior entangled')
  check(f(zhi+0.1)>c,'window exterior separable')

print('PASS:',passed,'independent algebraic and matrix assertions')
