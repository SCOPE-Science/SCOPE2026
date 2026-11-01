#!/usr/bin/env python3
"""Direct finite-geometry and numeric checks of the stated incidence-metric threshold."""
import itertools, math
import numpy as np
from scipy.optimize import brentq

def projective_points(q):
  pts=[]
  for t in itertools.product(range(q),repeat=4):
    if not any(t): continue
    r=next(a for a in t if a)
    p=tuple((v*pow(r,-1,q))%q for v in t)
    if p not in pts:pts.append(p)
  return sorted(pts)

def symp(x,y,q):
  return (x[0]*y[2]-x[2]*y[0]+x[1]*y[3]-x[3]*y[1])%q

def lines_W(q,pts):
  lines=set()
  for a,x in enumerate(pts):
    for y in pts[a+1:]:
      if symp(x,y,q): continue
      # Exact projective span of two incident isotropic points:
      span=set()
      for h in range(q):
        for k in range(q):
          vec=[(h*x[i]+k*y[i])%q for i in range(4)]
          if not any(vec):continue
          c=next(v for v in vec if v)
          span.add(tuple(v*pow(c,-1,q)%q for v in vec))
      assert len(span)==q+1
      lines.add(frozenset(span))
  return sorted(lines,key=lambda s:tuple(sorted(s)))

def root(q):
  q3=q**3
  f=lambda p:q*(q+1)*2**p+q3*4**p-(q+1)-(q3+q*q)*3**p
  return brentq(f,0,math.log2(1+1/q),xtol=1e-15)

def check(q):
  pts=projective_points(q)
  ls=lines_W(q,pts)
  v=(q+1)*(q*q+1)
  assert len(pts)==len(ls)==v,(q,len(pts),len(ls),v)
  N=np.array([[int(p in l) for l in ls] for p in pts],dtype=int)
  A=N@N.T-(q+1)*np.eye(v,dtype=int)
  assert np.all(np.diag(A)==0)
  assert np.all((A==0)|(A==1))
  assert np.all(N.sum(axis=0)==q+1) and np.all(N.sum(axis=1)==q+1)
  assert np.all(A.sum(axis=1)==q*(q+1))
  P=np.where(A==1,2,4).astype(int);np.fill_diagonal(P,0)
  L=np.where((N.T@N-(q+1)*np.eye(v,dtype=int))==1,2,4).astype(int);np.fill_diagonal(L,0)
  R=np.where(N==1,1,3)
  d=np.block([[P,R],[R.T,L]])
  H=np.eye(2*v)-np.ones((2*v,2*v))/(2*v)
  beta=root(q)
  for p in (0,beta*0.5,beta, beta+min(.05,.1*beta)):
    D=np.where(d==0,0,np.power(d.astype(float),p))
    eig=np.linalg.eigvalsh(H@D@H)
    # For p< beta, exactly one zero eigenvalue, p=beta two, after beta one positive.
    tol=1e-7
    npos=sum(z>tol for z in eig)
    nzero=sum(abs(z)<=tol for z in eig)
    if p < beta-1e-10: assert npos==0 and nzero==1,(q,p,npos,nzero)
    elif abs(p-beta)<1e-10: assert npos==0 and nzero==2,(q,p,npos,nzero)
    else: assert npos>=1,(q,p,npos,nzero)
  return v,beta

if __name__=='__main__':
 for q in (2,3):
  v,beta=check(q)
  print('PASS',q,'v',v,'beta',format(beta,'.14f'))
 for q in (2,3,4,5,7,11,31,101):
  beta=root(q)
  print('ASYM',q,format(q**3*beta,'.12f'))
