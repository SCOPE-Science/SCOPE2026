"""Exact algebra and independent finite-dimensional checks for unbalanced double-stars.
Run with Python 3 plus sympy and numpy, optionally scipy.
"""
from fractions import Fraction
import sympy as S
import numpy as np

p,q,b=S.symbols('p q b', positive=True)
h=S.symbols('h',positive=True)
K=p*p+p-q
a=(p-q)/K
c=p*(p-q)/(q*K)
b0=(p*(q+1)-q)/K
N=S.expand(p*p*(p-q)**2 - (p*(q+1)-q)**2-p*p*q*q)
identities={
 'first saturation':p*a+b0-1,
 'second saturation':q*c+b0-1,
 'relative spokes':q*c-p*a,
 'eigenvalue equality':(1-a)*(c-a)-q*c*c,
 'P polynomial':N-(p**4-2*p**3*q-p*p*q*q-2*p*p*q-p*p+2*p*q*q+2*p*q-q*q),
 'N shift':S.expand(N.subs(p,q+h))-(h**4+2*q*h**3-(q*q+2*q+1)*h*h-(4*q**3+2*q*q)*h-2*q**4),
 'P at 0':S.factor(N.subs(p,q))+2*q**4,
 'asymptotics':S.limit(N.subs(p,p*q)/q**4,q,S.oo)-(p*p*(p*p-2*p-1)),
}
for n,v in identities.items():
 assert S.simplify(v)==0,(n,S.factor(v))

def l_matrix(pp,qq,aa,cc,bb):
 nn=pp+qq+2
 mat=np.zeros((nn,nn),float)
 def add(i,j,w):
  mat[i,i]+=w;mat[j,j]+=w;mat[i,j]-=w;mat[j,i]-=w
 for i in range(pp):add(0,2+i,aa)
 for j in range(qq):add(1,2+pp+j,cc)
 add(0,1,bb)
 return mat

def fiedler(pp,qq,bb):
 aa=(1-bb)/pp;cc=(1-bb)/qq
 z=np.linalg.eigvalsh(l_matrix(pp,qq,aa,cc,bb))
 return z[1],z[-1],aa,cc

checked=0
for pp in range(3,24):
 for qq in range(2,pp):
  k=pp*pp+pp-qq
  aa=(pp-qq)/k; cc=pp*(pp-qq)/(qq*k);bb=(pp*(qq+1)-qq)/k
  assert 0<aa<1/pp and 0<cc<1/qq and 0<bb<1
  lam,hi,_,_=fiedler(pp,qq,bb)
  assert abs(lam-aa)<1e-9,(pp,qq,lam,aa)
  assert hi-1 <=1-aa+1e-8
  nval=pp*pp*(pp-qq)**2-(pp*(qq+1)-qq)**2-pp*pp*qq*qq
  if nval<0:
   delta=min(0.0001,bb/100)
   lam2,hi2,_,_=fiedler(pp,qq,bb-delta)
   if nval<-20:
    assert lam2>lam+1e-10,(pp,qq,lam,lam2)
  if nval>=0:
   for dt in (-bb/3, -(bb-1)**2/100, (1-bb)/3):
    newb=bb+dt
    if not (0<=newb<=1):continue
    lam2,_,_,_=fiedler(pp,qq,newb)
    assert lam2<lam+1e-8
  checked+=1

# Exact characteristic factorization on quotient block, and its zero multiplicity.
t=S.symbols('t')
# quotient similarity not needed; use 4x4 nonorthogonal coordinate Laplacian [left leaves, left hub, right hub, right leaves]
M=S.Matrix([[a,-a,0,0],[-p*a,1,-b0,0],[0,-b0,1,-q*c],[0,0,-c,c]])
poly=S.factor((t*S.eye(4)-M).det())
assert S.simplify(poly.subs(t,a))==0
assert S.simplify(poly.subs(t,0))==0
print('PASS',len(identities),'symbolic identities,',checked,'full-matrix graph cases')
print('characteristic polynomial',poly)
print('threshold samples', [(qq,next(pp for pp in range(qq+1,80) if (pp*pp*(pp-qq)**2-(pp*(qq+1)-qq)**2-pp*pp*qq*qq)>=0)) for qq in range(2,9)])
