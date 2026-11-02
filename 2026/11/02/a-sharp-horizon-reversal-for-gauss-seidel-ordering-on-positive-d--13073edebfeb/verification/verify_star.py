from fractions import Fraction
from itertools import permutations
import numpy as np
import sympy as S

u,v=S.symbols('u v', real=True);l=S.symbols('l')
A=S.Matrix([[1,u,v],[u,1,0],[v,0,1]])
E=[]
for i in range(3):
 T=S.eye(3)
 for j in range(3): T[i,j]-=A[i,j]
 E.append(T)
P=E[2]*E[0]*E[1]
R=u*u+v*v;w=u*u*v*v
C=S.simplify(A.inv()*P.T*A*P)
assert S.factor(C.charpoly(l).as_expr()-l*(l*l-(R+w)*l+w))==0
assert P.charpoly(l).as_expr().expand()==(l*l*(l-R)).expand()
assert (P**3-R*P**2).applyfunc(S.simplify)==S.zeros(3)
C2=A.inv()*(P**2).T*A*(P**2)
assert S.simplify(S.trace(C2)-(R**3+(1-R)**2*w))==0
assert C2.rank()==1
print('SYMBOLIC POLYNOMIAL IDENTITIES: PASS')

rng=np.random.default_rng(481516)
checks=0
for n in range(3,8):
 for rep in range(20):
  c=rng.uniform(-0.2,0.2,n-1)
  if rep==0:c[0]=0
  R0=float(np.dot(c,c))
  A=np.eye(n);A[0,1:]=c;A[1:,0]=c
  L=np.linalg.cholesky(A)
  B=L.T
  Binv=np.linalg.inv(B)
  Es=[]
  for i in range(n):
   T=np.eye(n);T[i,:]-=A[i,:]
   Es.append(T)
  ps=list(permutations(range(n))) if n<=5 else [tuple(rng.permutation(n)) for _ in range(100)]
  for perm in ps:
   P=np.eye(n)
   for i in perm:P=Es[i]@P
   cutoff=perm.index(0)
   left=perm[:cutoff]
   s=float(sum(c[i-1]**2 for i in left))
   w0=s*(R0-s)
   norm1=(R0+w0+np.sqrt((R0+w0)**2-4*w0))/2
   calc1=np.linalg.norm(B@P@Binv,2)**2
   assert abs(calc1-norm1)<1e-9,(n,perm,calc1,norm1)
   for m in (2,3,4):
    normm=R0**(2*m-4)*(R0**3+(1-R0)**2*w0)
    calcm=np.linalg.norm(B@np.linalg.matrix_power(P,m)@Binv,2)**2
    assert abs(calcm-normm)<1e-9,(n,perm,m,calcm,normm)
   assert abs(max(abs(np.linalg.eigvals(P)))-R0)<1e-9
   checks+=1
print('FULL-MATRIX SWEEP CHECKS:',checks)
