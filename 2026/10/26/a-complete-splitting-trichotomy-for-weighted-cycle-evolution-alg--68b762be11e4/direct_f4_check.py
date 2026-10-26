#!/usr/bin/env python3
"""Independent direct F4 multiplication check for monomial cycle maps."""
from itertools import product

def mul(a,b):
 x=0
 for j in range(2):
  for k in range(2):
   if ((a>>j)&1) and ((b>>k)&1):x ^= 1<<(j+k)
 if x&4:x ^= 7  # t^2 = t+1 over F2
 return x

assert [mul(2,x) for x in [1,2,3]]==[2,3,1]
pows=[1,2,3]
def check(A,k,U):
 n=len(A)
 for i in range(n):
  # phi(e_i^2) = a_i zeta^{u_{i+1}} e_{i+k+1}
  # phi(e_i)^2 = zeta^{2u_i} a_{i+k} e_{i+k+1}
  if mul(pows[A[i]],pows[U[(i+1)%n]]) != mul(pows[(2*U[i])%3],pows[A[(i+k)%n]]):return False
 return True

def allmaps(A):
 n=len(A)
 return {(k,U) for k in range(n) for U in product(range(3),repeat=n) if check(A,k,U)}

for n in (2,4,6):
 for A in ((0,)*n,(1,)+(0,)*(n-1)):
  G=allmaps(A)
  expected=n if n%2 else (3*n if A[0]==0 else 3*n//2)
  assert len(G)==expected,(n,A,len(G))
  if A[0]==1 and n==6:
   # The lifts of the even rotation all have order nine.
   def compose(x,y):
    k,U=x;l,V=y
    return ((k+l)%n,tuple((V[i]+U[(i+l)%n])%3 for i in range(n)))
   e=(0,(0,)*n)
   for g in G:
    if g[0]==2:
     t=e
     for j in range(1,10):
      t=compose(g,t)
      if t==e:break
     assert j==9,(g,j)
  print('DIRECT_F4',n,'twisted',bool(A[0]),'automorphisms',len(G))
print('DIRECT_F4_OK')
