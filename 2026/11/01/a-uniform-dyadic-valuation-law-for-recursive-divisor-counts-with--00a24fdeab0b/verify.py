from functools import lru_cache
from itertools import product
from math import factorial,comb
@lru_cache(None)
def kap(e):
  if not any(e):return 1
  ranges=[range(a+1) for a in e]
  return 1+sum(kap(d) for d in product(*ranges) if d!=e)
# Direct divisor recurrence on exponent vectors (prime labels irrelevant).
def v2(x):return (x&-x).bit_length()-1
checked=0
for r in range(1,13):
 for k in range(7):
  exp=(r,)+(1,)*k
  value=kap(exp)
  expected=r if k==0 or r%2 else r+v2(r+2) if k==1 else r+1
  assert v2(value)==expected,(r,k,value,v2(value),expected)
  checked+=1
print('direct_divisor_recurrence_verified',checked,'max',max(kap((r,)+(1,)*k) for r in range(1,13) for k in range(7)))
# Symbolic Stirling expansion independent of divisor recursion.
S=[[1]]
for k in range(1,15):
 z=S[-1];S.append([0]+[(z[j-1] if j-1<len(z) else 0)+(j*z[j] if j<len(z) else 0) for j in range(1,k+1)])
for r in range(1,13):
 for k in range(7):
  m=2**r*sum((comb(r+j,j)+(comb(r+j-1,j-1) if j else 0))*factorial(j)*S[k][j] for j in range(k+1))
  assert m==kap((r,)+(1,)*k)
print('stirling_formula_verified',84)
print('VERIFY_OK')
