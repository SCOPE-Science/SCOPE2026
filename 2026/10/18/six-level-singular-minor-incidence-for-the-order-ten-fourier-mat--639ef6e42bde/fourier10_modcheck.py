"""Independent finite-field recheck of all 4x4 cyclic-order-ten Fourier minors."""
from itertools import combinations
from collections import Counter
from hashlib import sha256

def primitive10(p):
 for z in range(2,p):
  if pow(z,10,p)==1 and pow(z,5,p)!=1 and pow(z,2,p)!=1:
   return z
 raise ValueError(p)

def singular_mod(M,p):
 a=[list(x) for x in M]
 for j in range(4):
  k=next((i for i in range(j,4) if a[i][j]%p),None)
  if k is None:return True
  a[j],a[k]=a[k],a[j]
  piv=pow(a[j][j],-1,p)
  for i in range(j+1,4):
   v=a[i][j]*piv%p
   for t in range(j,4):a[i][t]=(a[i][t]-v*a[j][t])%p
 return False

def signatures(p):
 z=primitive10(p); tab=[[pow(z,(r*c)%10,p) for c in range(10)] for r in range(10)]
 sub=list(combinations(range(10),4)); counts=Counter(); classes=Counter(); bits=bytearray()
 for R in sub:
  d=0
  for C in sub:
   s=singular_mod([[tab[r][c] for c in C] for r in R],p)
   bits.append(s); d+=s
  counts[d]+=1
 return z, counts,sha256(bytes(bits)).hexdigest(),sum(bits)
if __name__=='__main__':
 for p in (101,181,241):
  z,classes,digest,total=signatures(p)
  print(p,z,total,sorted(classes.items()),digest)
  assert total==5000
  assert classes=={0:20,10:100,20:50,30:20,110:10,130:10}
 print('OK modular crosschecks')
