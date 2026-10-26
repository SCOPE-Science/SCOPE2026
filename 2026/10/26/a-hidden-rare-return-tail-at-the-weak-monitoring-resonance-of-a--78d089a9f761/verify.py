#!/usr/bin/env python3
"""Checks for two-site weak-detection resonance crossover; finite checks supplement the proof."""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

k=sp.symbols('k',real=True,nonzero=True)
A=sp.Matrix([[-1,0,-2*k],[0,0,2*k],[k,-k,-sp.Rational(1,2)]])
v0=sp.Matrix([1,0,0]); v_int= -A.inv()*v0
assert all(sp.simplify(x-y)==0 for x,y in zip(v_int,sp.Matrix([1,1,0])))
v_t= -A.inv()*v_int
assert all(sp.simplify(x-y)==0 for x,y in zip(v_t,sp.Matrix([2,2+1/(4*k*k),-1/(2*k)])))
print('Exact symbolic integrated density and time-weighted moment identities: PASS')

P=np.array([1+0j,0+0j])
for omega in [0.,.01,.125,.25,.4,1.,2.]:
 G=np.array([[-.5,-1j*omega],[-1j*omega,0]],dtype=complex)
 for t in [0.,.04,.5,1.,3.,8.]:
  delta=np.sqrt(complex(1-16*omega**2))
  if abs(delta)<1e-12:
   F=math.exp(-t/2)*((1-t/4)**2+(t/4)**2)
  else:
   v=delta*t/4
   F=math.exp(-t/2)*(abs(np.cosh(v)-np.sinh(v)/delta)**2+(16*omega**2/abs(delta)**2)*abs(np.sinh(v))**2)
  actual=np.linalg.norm(expm(G*t)@P)**2
  assert abs(F-actual)<5e-11, (omega,t,F,actual)
print('Closed-form survival against direct matrix exponential (42 cases): PASS')

for eps in [.08,.03,.01,.003]:
 q=math.sqrt(1-eps)
 for omega in [.05,.25,.7,1.2]:
  phi=eps*omega
  U=np.array([[math.cos(phi),-1j*math.sin(phi)],[-1j*math.sin(phi),math.cos(phi)]])
  K=np.diag([q,1])@U
  for t in [.3,1.,4.]:
   n=int(t/eps)
   actual=np.linalg.norm(np.linalg.matrix_power(K,n)@P)**2
   G=np.array([[-.5,-1j*omega],[-1j*omega,0]])
   goal=np.linalg.norm(expm(G*t)@P)**2
   assert abs(actual-goal) < 1.7*eps*(1+t)*10, (eps,omega,t,actual,goal)
  # Exact mean via 4x4 discrete Lyapunov resolvent.
  H=np.kron(K.conj(),K)
  vec=np.linalg.solve(np.eye(4)-H, np.outer(P,P.conj()).reshape(4,order='F'))
  X=vec.reshape((2,2),order='F')
  assert abs(np.trace(X).real-2/eps)<2e-7, (eps,omega, X)
print('Finite-step weak-limit checks (48) and exact discrete mean identities (16): PASS')

for eps,kap in [(.03,.05),(.01,.04),(.006,.03)]:
 q=math.sqrt(1-eps); phi=eps*kap
 K=np.diag([q,1])@np.array([[math.cos(phi),-1j*math.sin(phi)],[-1j*math.sin(phi),math.cos(phi)]])
 l,V=np.linalg.eig(K); vinv=np.linalg.inv(V); a=vinv@P
 slow=np.argmax(abs(l))
 ps=V[:,slow]*a[slow]
 assert abs(np.linalg.norm(ps)**2/(4*kap**2)-1)<.17
 for u in [.2,.75,1.5]:
  n=int(u/(eps*kap**2))
  vec=V@(l**n*a)
  ratio=(np.linalg.norm(vec)**2)/(4*kap**2)
  assert abs(ratio-math.exp(-4*u))<.07, (eps,kap,u,ratio)
print('Rare-tail spectral projection and two-time-scale numerical checks (12): PASS')
