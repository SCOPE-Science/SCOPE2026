"""Direct finite-extension check of two annihilating 2-by-2 matrices.
Represent F4 as F2[z]/(z*z+z+1), with coefficients 0..3.
"""
from collections import Counter
from itertools import product
from check import formula

def add(a,b):return a^b

def mul(a,b):
 p=0
 for i in range(2):
  if (b>>i)&1:p^=a<<i
 if p&8:p^=0b1110
 if p&4:p^=0b111
 return p

def rk(A,rows,cols):
 x=[list(A[i*cols:(i+1)*cols]) for i in range(rows)];r=0
 for c in range(cols):
  z=next((i for i in range(r,rows) if x[i][c]),None)
  if z is None:continue
  x[z],x[r]=x[r],x[z]
  inv=mul(x[r][c],x[r][c])
  x[r]=[mul(a,inv) for a in x[r]]
  for i in range(rows):
   if i!=r and x[i][c]:
    factor=x[i][c];x[i]=[add(a,mul(factor,b)) for a,b in zip(x[i],x[r])]
  r+=1
  if r==rows:break
 return r

def mm(A,B):return tuple(add(mul(A[2*i],B[j]),mul(A[2*i+1],B[2+j])) for i in range(2) for j in range(2))

zero=(0,)*4
S=[(A,rk(A,2,2)) for A in product(range(4),repeat=4) if mm(A,A)==zero]
obs=Counter()
for (A,r),(B,s) in product(S,repeat=2):
 if mm(A,B)!=zero or mm(B,A)!=zero:continue
 H=tuple(M[2*i+j] for i in range(2) for M in (A,B) for j in range(2))
 V=tuple(M[2*i+j] for M in (A,B) for i in range(2) for j in range(2))
 t=rk(H,2,4);k=2-rk(V,4,2)
 obs[((r,s),t,k)]+=1
for rs in product(range(2),repeat=2):
 for t in range(3):
  for k in range(t,3):
   assert obs[(rs,t,k)]==formula(2,4,rs,t,k),(rs,t,k,obs[(rs,t,k)],formula(2,4,rs,t,k))
assert sum(obs.values())==76, sum(obs.values())
print('DOUBLE_FLAG_F4_EXTENSION_OK total',sum(obs.values()),'nonzero_strata',len(obs))
