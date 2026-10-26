"""Reproduce finite-dimensional spectral and arithmetic identities for a two-row circulant Gaussian sketch."""
from math import gcd, cos, pi, gamma, isclose
import numpy as np
count=0
for m in range(2,31):
 for r in range(1,m):
  d=gcd(m,r); L=m//d; k=m-d
  S=np.zeros((m,m))
  for i in range(m):S[i,(i+r)%m]=1
  C=(S+S.T)/2
  vals_p=np.linalg.eigvalsh(np.eye(m)-C)
  vals_n=np.linalg.eigvalsh(np.eye(m)+C)
  assert sum(abs(v)<1e-8 for v in vals_p)==d
  assert sum(abs(v)<1e-8 for v in vals_n)==(d if L%2==0 else 0)
  prod=1.
  for v in vals_p:
   if v>1e-8:prod*=v
  theory=(L*L/(2**(L-1)))**d
  assert isclose(prod,theory,rel_tol=1e-7,abs_tol=1e-9),(m,r,prod,theory)
  for j in range(m):
   g=np.sin(np.arange(m)*(j+1)+0.437)
   T=np.stack([g,S@g]); sv=np.linalg.svd(T,compute_uv=False)
   q=min(g@(np.eye(m)-C)@g,g@(np.eye(m)+C)@g)
   assert isclose(sv[-1]**2,q,rel_tol=5e-7,abs_tol=1e-8)
   count+=1
  coeff=(1+(L%2==0))/(L**d*gamma(k/2+1))
  assert coeff>0
print('VERIFY_OK spectral zero counts, pseudodeterminant product, Gram identity and coefficient;',count,'vectors')
