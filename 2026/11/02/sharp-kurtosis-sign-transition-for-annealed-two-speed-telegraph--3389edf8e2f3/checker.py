"""Finite-generator and moment-equation cross-checks for annealed two-speed reversal kinetics.
Uses a finite-state tilted generator and moment ODE. Requires sympy, scipy, numpy.
"""
import sympy as sp
import numpy as np
from scipy.linalg import expm

a,b,k,z,L=sp.symbols('a b k z L',positive=True)
# Forward jump rates: state (+a,+b,-a,-b), each reversal redraw uniform speed.
Q=sp.Matrix([[-L,0,L/2,L/2],[0,-L,L/2,L/2],[L/2,L/2,-L,0],[L/2,L/2,0,-L]])
V=sp.diag(a,b,-a,-b)
poly=sp.factor((z*sp.eye(4)-Q-k*V).det())
print('CHARACTERISTIC:',poly)
# Compare series numerically for three contrasting regimes and rate values.
q_threshold=(7+2*sp.sqrt(10))/3
print('MAX_RATIO:',q_threshold,'=',float(q_threshold))
def predicted(a,b,L):
  mu1=(a+b)/2
  mu2=(a*a+b*b)/2
  mu3=(a**3+b**3)/2
  mu4=(a**4+b**4)/2
  A=2*mu2-mu1**2
  B=2*mu4-2*mu1*mu3+mu2**2
  return A/L,3*(4*B-5*A*A)/L**3

def compute(a,b,rate,t):
  q=np.array([[-rate,0,rate/2,rate/2],[0,-rate,rate/2,rate/2],[rate/2,rate/2,-rate,0],[rate/2,rate/2,0,-rate]],float)
  vv=np.array([a,b,-a,-b]);n=4
  mat=np.zeros((20,20))
  for h in range(5):
     mat[4*h:4*h+4,4*h:4*h+4]=q.T
     if h>0:mat[4*h:4*h+4,4*(h-1):4*h]=h*np.diag(vv)
  start=np.zeros(20);start[:4]=.25
  out=expm(t*mat)@start
  moments=[np.sum(out[4*h:4*h+4]) for h in range(5)]
  K4=moments[4]-3*moments[2]**2
  return moments[2],K4,K4/(moments[2]**2)

cases=[(1,1,1),(1,1.5,2),(1,2,1),(1,3,1),(1,float(q_threshold),1),(1,8,.7)]
for aa,bb,rr in cases:
  pred2,pred4=predicted(aa,bb,rr)
  vals=[(t,)+compute(aa,bb,rr,t) for t in (30,60,120)]
  measured2=(vals[2][1]-vals[1][1])/60
  measured4=(vals[2][2]-vals[1][2])/60
  assert abs(measured2/pred2-1)<1e-8,(aa,bb,measured2,pred2)
  assert abs(measured4-pred4)<max(.001,abs(pred4)*.0001),(aa,bb,measured4,pred4)
  print(f'a={aa},b={bb}, rate={rr}: predicted rates var={pred2:.8f}, k4={pred4:.8f}; verified={measured2:.8f}, {measured4:.8f}; kurtosis at t120={vals[-1][3]:.8f}')
print('ALL CHECKS PASS')
