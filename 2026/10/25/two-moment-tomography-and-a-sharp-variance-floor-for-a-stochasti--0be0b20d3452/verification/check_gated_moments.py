"""Numerical verification for a two-state gated diffusion boundary."""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

def h(z):
    w=np.sqrt(z)
    return 1/(w*np.tanh(w))

def log_h_derivative(z):
    w=np.sqrt(z)
    exp_term=np.exp(-2*w)
    return -(1/(2*z))-(2*exp_term)/(w*(1-exp_term*exp_term))

def laplace_boundary(s,alpha,beta):
    M=np.array([[0.,0.,1.,0.],[0.,0.,0.,1.],[s+beta,-beta,0.,0.],[-alpha,s+alpha,0.,0.]])
    E=expm(-M)
    B=E[np.ix_([0,3],[0,1])]
    c=np.linalg.solve(B,[1.,0.])
    p=alpha/(alpha+beta)
    return p*c[0]+(1-p)*c[1]

def laplace_formula(s,alpha,beta):
    lam=alpha+beta
    q=beta/alpha
    return 1/(np.cosh(np.sqrt(s))+q*s*(np.sinh(np.sqrt(s))/np.sqrt(s))*h(lam+s))

def moments(alpha,beta):
    lam=alpha+beta;q=beta/alpha
    m=0.5+q*h(lam)
    v=m*m-1/12-q*(h(lam)/3+2*h(lam)*log_h_derivative(lam))
    return m,v

def recover(m,v):
    e=m-0.5
    R=(m*m-m/3+1/12-v)/(2*e)
    assert R<0
    lam=brentq(lambda z:log_h_derivative(z)-R,1e-10,1e10,xtol=1e-11)
    q=e/h(lam)
    return lam/(1+q),lam*q/(1+q)

for a,b in [(0.1,0.2),(3,0.04),(2,7),(0.2,18),(14,0.3)]:
  for s in [0.03,0.3,1.4]:
    expected=laplace_formula(s,a,b)
    actual=laplace_boundary(s,a,b)
    assert abs(actual-expected)<3e-12,(a,b,s,actual,expected)
  m,v=moments(a,b)
  aa,bb=recover(m,v)
  assert abs(a-aa)/(a+1)<3e-10 and abs(b-bb)/(b+1)<3e-10,(a,b,aa,bb)
  assert v>m*m-m/3+1/12
  print(f'alpha={a:g} beta={b:g} mean={m:.10f} variance={v:.10f} recovered={aa:.10g},{bb:.10g}')
print('ALL_PASS: boundary-matrix Laplace, inversion, and inequality')
