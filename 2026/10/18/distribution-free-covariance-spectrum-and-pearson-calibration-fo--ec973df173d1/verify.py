"""Exact finite checks for weighted bigram-frequency covariance and its four sectors.
Run: python verify.py. Uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import prod

def outer_cov(p,L):
 q=len(p); ij=list(product(range(q), repeat=2)); d=q*q
 V=[[F(0) for _ in ij] for _ in ij]
 for x in product(range(q),repeat=L+1):
  mass=prod(p[u] for u in x)
  ct=[sum((x[t],x[t+1])==k for t in range(L)) for k in ij]
  for i in range(d):
   for j in range(d): V[i][j]+=mass*ct[i]*ct[j]
 mu=[L*p[a]*p[b] for (a,b) in ij]
 return [[V[i][j]-mu[i]*mu[j] for j in range(d)] for i in range(d)]

def explicit(p,L):
 q=len(p); ij=list(product(range(q), repeat=2))
 C=[]
 for a,b in ij:
  row=[]
  for c,d in ij:
   z=(L*((p[a]*p[b] if (a,b)==(c,d) else 0)-p[a]*p[b]*p[c]*p[d])+
    (L-1)*((p[a]*p[b]*p[d] if b==c else 0)+
           (p[c]*p[d]*p[b] if d==a else 0)-2*p[a]*p[b]*p[c]*p[d]))
   row.append(z)
  C.append(row)
 return C

def check_sector(p,L):
 q=len(p);ij=list(product(range(q),repeat=2)); C=explicit(p,L)
 modes=[([F(1)]*len(ij),0,'constant')]
 centered=[]
 for k in range(q-1):
  f=[F(int(i==k),1)-p[k] for i in range(q)]; centered.append(f)
 for f in centered:
  modes.append(([f[a]-f[b] for a,b in ij],1,'endpoint_gradient'))
  modes.append(([f[a]+f[b] for a,b in ij],2*L-1,'symmetric_vertex'))
 for f in centered:
  for g in centered:
   modes.append(([f[a]*g[b] for a,b in ij],L,'doubly_centered'))
 assert len(modes)==q*q
 for A,ev,tag in modes:
  z=[sum(C[k][r]*A[r] for r in range(q*q)) for k in range(q*q)]
  expected=[ev*p[a]*p[b]*A[k] for k,(a,b) in enumerate(ij)]
  assert z==expected,(q,L,p,tag,z,expected)
 return len(modes)

tests=0
for p in [[F(1,2)]*2,[F(1,3),F(2,3)],[F(1,2),F(1,3),F(1,6)], [F(1,4),F(1,4),F(1,2)],[F(1,2),F(1,4),F(1,8),F(1,8)]]:
 for L in range(1,5):
  c=explicit(p,L)
  assert c==outer_cov(p,L),(p,L)
  tests+=len(c)**2
  tests+=check_sector(p,L)
  # Trace of Pearson-normalized covariance is L*(q*q-1).
  q=len(p)
  assert sum(c[k][k]/(p[a]*p[b]) for k,(a,b) in enumerate(product(range(q),repeat=2)))==L*(q*q-1)
  tests+=1
print('VERIFY_OK',tests,'exact rational assertions',flush=True)
