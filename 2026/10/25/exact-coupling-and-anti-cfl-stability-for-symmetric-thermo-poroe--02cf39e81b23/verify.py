"""Symbolic identities and numerical witnesses for a scalar symmetric time-splitting model."""
import sympy as sp
import numpy as np
z,c,d,t=sp.symbols('z c d t')
# One-step map on (u_n,p_n,theta_n,p_{n-1},theta_{n-1}), with a=1, C=Ce=1, B=Be=b.
# Matrix formulation: u'=d(p+theta); (1+t)p'=d(u-u')+p+c(theta-theta_old)
# (1+t)theta'=d(u-u')+theta+c(p-p_old)
J=sp.Matrix([
  [0,d,d,0,0],
  [d/(1+t),(1-d**2)/(1+t),(c-d**2)/(1+t),0,-c/(1+t)],
  [d/(1+t),(c-d**2)/(1+t),(1-d**2)/(1+t),-c/(1+t),0],
  [0,1,0,0,0],[0,0,1,0,0]
])
p=sp.factor(J.charpoly(z).as_expr())
ps=(1+t)*z**2-(1+c-2*d**2)*z-(2*d**2-c)
pq=(1+t)*z**2-(1-c)*z-c

assert sp.factor(p-z*ps*pq/(1+t)**2)==0
print('CHARACTERISTIC_FACTORIZATION_OK')
for cv,dv,tv in [(.5,.6**.5,.005),(.5,1,0.25),(.5,1,1),(.5,1,2),(.3,.5,.001),(.9,.99**.5,.01)]:
 mat=np.array(J.subs({c:cv,d:dv,t:tv}),dtype=float)
 ev=np.linalg.eigvals(mat)
 s=max(abs(ev))
 predicted=(4*dv**2<2+tv+2*cv)
 assert (s<1-1e-9)==predicted or abs(4*dv**2-2-tv-2*cv)<1e-8
 print('WITNESS',cv,dv,tv,'radius',round(s,9),'pred_stable',predicted)
# Initial constant history s_{-1}=s_0=1, same θ,p=1, u0=2d.
def symmetric_trajectory(c_,d2,t_,N):
 K=2*d2-c_
 sm=1.; s0=1.
 for j in range(N):
  sn=((1-K)*s0+K*sm)/(1+t_)
  sm,s0=s0,sn
 return s0
for d2 in [.60,.75,1.0]:
 for n in [50,100,200,400]:
  h=1/n; T=1.; b=1.; s=symmetric_trajectory(.5,d2,h*b,n)
  exact=np.exp(-T/(1+2*d2-.5))
  print('TIME',d2,n,s,exact,'err',abs(s-exact))

# Reproducible randomized consistency check of the strict Schur inequality.
rng=np.random.default_rng(123456)
for i in range(300):
 cv=float(rng.uniform(.0001,.9999)); dv=float(rng.uniform(0,2)); tv=float(rng.uniform(.0001,6))
 mat=np.array(J.subs({c:cv,d:dv,t:tv}),dtype=float)
 radius=max(abs(np.linalg.eigvals(mat)))
 pred=(4*dv*dv<2+tv+2*cv)
 if pred: assert radius < 1+1e-9
 else: assert radius>1-1e-9
print('RANDOM_SCHUR_CHECKS_OK',300)
