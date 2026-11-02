#!/usr/bin/env python3
"""Exact level-degeneracy checks and finite-dimensional independent replay for a symmetric V-type quantum battery."""
import math
import itertools
import numpy as np
from scipy.linalg import null_space

def sym_basis(n):
    strings=list(itertools.product(range(3),repeat=n))
    h=np.array([sum(x!=0 for x in word) for word in strings],dtype=int)
    groups={q:[] for q in range(n+1)}
    for j in range(n+1):
      for k in range(j+1):
        inds=[a for a,t in enumerate(strings) if t.count(1)==k and t.count(2)==j-k]
        v=np.zeros(len(strings),complex);v[inds]=1/np.sqrt(len(inds))
        groups[j].append(v)
    return h,groups

def witness(n):
    h,G=sym_basis(n);dim=len(h)
    columns=[];target=[];src=[]
    for q in range(n+1):
      for v in G[q]:src.append(v);target.append(q if q<=1 else q-1)
      if q<=1:
        columns.extend(G[q]);continue
      i=np.where(h==q-1)[0]
      Q=np.column_stack([v[i] for v in G[q-1]])
      B=null_space(Q.conj().T)
      assert B.shape[1]>=q+1
      for k in range(q+1):
        w=np.zeros(dim,complex);w[i]=B[:,k];columns.append(w)
    V=np.column_stack(columns);S=np.column_stack(src)
    assert np.max(abs(V.conj().T@V-np.eye(V.shape[1])))<1e-10
    assert np.max(abs(S.conj().T@S-np.eye(S.shape[1])))<1e-10
    B=V.conj().T@(h[:,None]*V)
    assert np.max(abs(B-np.diag(target)))<1e-10
    assert sum(math.comb(n,q-1)*2**(q-1)-(q) >= q+1 for q in range(2,n+1))==n-1
    rng=np.random.default_rng(100+n)
    for _ in range(16):
      z=rng.standard_normal((S.shape[1],S.shape[1]))+1j*rng.standard_normal((S.shape[1],S.shape[1]))
      r=z@z.conj().T;r/=np.trace(r)
      before=np.trace(r@(S.conj().T@(h[:,None]*S))).real
      after=np.trace(r@B).real
      p=sum(r[j,j].real for j,q in enumerate([q for q in range(n+1) for _ in range(q+1)]) if q>=2)
      assert abs(before-after-p)<1e-9
    return n,dim,S.shape[1],max(abs(B-np.diag(target)).ravel())

def passive_ratio_n2():
   n=2;h,G=sym_basis(n);S=np.column_stack([x for g in G.values() for x in g]);d=S.shape[1]
   rho=S@S.conj().T/d
   ev=np.linalg.eigvalsh(rho)[::-1]
   epass=float(np.dot(ev,np.sort(h)))
   ebefore=float(np.trace(rho@np.diag(h)).real)
   p2=float(np.trace(rho@np.diag(h==2)).real)
   assert abs(ebefore-4/3)<1e-12
   assert abs(epass-1)<1e-12
   assert abs((ebefore-epass)/p2-2/3)<1e-12
   return ebefore,epass,p2,(ebefore-epass)/p2

def passive_incoherent_counterexample():
   """A three-cell symmetric state with passive dephased state but positive ergotropy."""
   h,G=sym_basis(3)
   rho=np.zeros((len(h),len(h)),complex)
   for q,weight in ((0,0.69),(1,0.30),(2,0.01)):
       for v in G[q]: rho+=weight/len(G[q])*np.outer(v,v.conj())
   diag=np.diag(rho).real
   assert abs(diag.sum()-1)<1e-12
   assert min(diag[h==0])>=max(diag[h==1])
   assert min(diag[h==1])>=max(diag[h==2])
   assert min(diag[h==2])>=max(diag[h==3])
   pge2=float(np.sum(diag[h>=2]))
   vals=np.linalg.eigvalsh(rho)[::-1]
   epass=float(vals@np.sort(h))
   current=float(diag@h)
   assert pge2>0 and current-epass >= pge2-1e-12
   return pge2,current,epass,current-epass

def n3_sharpness():
   h,G=sym_basis(3)
   p=0.17
   rho=(1-p)*np.outer(G[0][0],G[0][0].conj())+p*np.outer(G[2][0],G[2][0].conj())
   vals=np.linalg.eigvalsh(rho)[::-1]
   epass=float(vals@np.sort(h))
   current=float(np.trace(rho@np.diag(h)).real)
   assert abs(current-epass-p)<1e-12
   return current,epass,p

if __name__=='__main__':
  for n in (3,4,5): print('fixed_unitary_witness',witness(n))
  print('n2_saturation',passive_ratio_n2())
  print('passive_incoherent_counterexample',passive_incoherent_counterexample())
  print('n3_sharpness',n3_sharpness())
  for n in range(3,30):
    for q in range(2,n+1):
      assert 2**(q-1)*math.comb(n,q-1)-q>=q+1
  print('PASS: finite-dimensional isometries, random mixed-state extraction identities, sharp n=2 witness, integer dimension inequalities')
