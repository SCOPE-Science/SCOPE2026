#!/usr/bin/env python3
"""Reproduce exact pentagon and independent odd-cycle Pauli witness checks."""
import itertools, numpy as np, sympy as sp
from scipy.optimize import linprog
I=sp.eye(2);X=sp.Matrix([[0,1],[1,0]]);Y=sp.Matrix([[0,-sp.I],[sp.I,0]]);Z=sp.diag(1,-1)
pa={'I':I,'X':X,'Y':Y,'Z':Z}
names=['IX','IY','YX','XI','ZY']
M=[sp.kronecker_product(*(pa[c] for c in n)) for n in names]
for i in range(5):
 for j in range(i+1,5):
  r=M[i]*M[j]-(-1 if (j-i)%5 in (1,4) else 1)*M[j]*M[i]
  assert r==sp.zeros(4)
Q=[M[i]*M[(i+2)%5] for i in range(5)]
for i in range(5):
 for j in range(i+1,5):assert Q[i]*Q[j]+Q[j]*Q[i]==sp.zeros(4)
assert sum(Q,sp.zeros(4))**2 ==5*sp.eye(4)
for s in itertools.product((-1,1), repeat=5):
 H=sum((s[i]*M[i] for i in range(5)),sp.zeros(4))
 assert sp.factor(H.charpoly().as_expr())== (sp.Symbol('lambda')**4-10*sp.Symbol('lambda')**2+5)
 assert (H**4-10*H**2+5*sp.eye(4)).applyfunc(sp.simplify)==sp.zeros(4)
print('EXACT_ALL_32_SIGNED_CHARACTERISTIC_POLYNOMIALS_OK')
Ms=np.array([np.array(m.tolist(),dtype=complex) for m in M]); V=[]
for i in range(5):
 j=(i+2)%5
 for a,b in itertools.product((-1,1), repeat=2):
  v=np.zeros(5);v[i]=a;v[j]=b;V.append(v)
V=np.asarray(V).T
Aeq=np.concatenate([V,-V],axis=1);Aeq=np.vstack([Aeq,np.concatenate([np.ones(20),-np.ones(20)])]);c=np.ones(40)
rng=np.random.default_rng(3204)
for _ in range(256):
 z=rng.normal(size=4)+1j*rng.normal(size=4);z=z/np.linalg.norm(z)
 b=np.real(np.einsum('i,kij,j->k',z.conj(),Ms,z))
 lp=linprog(c,A_eq=Aeq,b_eq=np.r_[b,1],bounds=(0,None),method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
 assert lp.success,lp.message
 expected=max([1,np.sum(np.abs(b))/2]+[abs(b[i])+abs(b[(i+1)%5]) for i in range(5)])
 assert abs(lp.fun-expected)<2e-7,(lp.fun,expected)
print('256_EXACT_POLYTOPE_LP_CHECKS_OK')
H=np.sum(Ms,axis=0);eig,U=np.linalg.eigh(H);v=U[:,-1];b=np.real(np.einsum('i,kij,j->k',v.conj(),Ms,v));lam=np.sqrt(5+2*np.sqrt(5));print('TOP_EIG',eig[-1], 'B',b.tolist(),'ROM',max(1,max(abs(b[i])+abs(b[(i+1)%5]) for i in range(5)),sum(abs(b))/2),'TARGET',lam/2); assert np.max(np.abs(b-lam/5))<1e-12
print('C5_CHECKS_OK')

import numpy as np
from functools import reduce
from operator import matmul
I=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]],complex);Z=np.diag([1.,-1.]).astype(complex)
def kron(v):
 m=np.array([[1]],dtype=complex)
 for a in v:m=np.kron(m,a)
 return m
for k in range(2,9):
 n=2*k+1
 gamma=[]
 for j in range(k):
  gamma += [kron([Z]*j+[X]+[I]*(k-j-1)), kron([Z]*j+[Y]+[I]*(k-j-1))]
 gamma += [kron([Z]*k)]
 P=[1j*gamma[j]@gamma[(j+1)%n] for j in range(n)]
 for i in range(n):
  for j in range(i+1,n):
   E=np.max(np.abs(P[i]@P[j]-(-1 if (j-i)%n in [1,n-1] else 1)*P[j]@P[i])); assert E<1e-12,(n,i,j,E)
 for trial in range(3):
  signs=np.ones(n) if trial==0 else np.random.default_rng(trial+k).choice([-1,1],size=n)
  H=sum(s*p for s,p in zip(signs,P))
  eig=np.linalg.eigvalsh(H)
  target=1/np.tan(np.pi/(2*n))
  err=max(abs(eig[0]+target),abs(eig[-1]-target))
  assert err <1e-10,(n,eig[0],eig[-1],target)
 print(n,'dim',2**k,'norm',target,'capacity',max(np.sqrt(2),target/k),'odd facet dominant',target/k>np.sqrt(2))
print('VERIFY_OK')
