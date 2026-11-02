"""Finite-field verification for split diagonal metabelian commuting tuples."""
from itertools import product
from math import comb

CASES = [
 (2, [[1]], [1,2,3]),
 (2, [[1],[1]], [1,2,3]),
 (2, [[1],[1],[1]], [1,2]),
 (2, [[1,0],[0,1]], [1,2]),
 (2, [[1,0],[0,1],[1,1]], [1,2,3]),
 (2, [[1,0,0],[0,1,0],[0,0,1],[1,1,1]], [1,2]),
 (3, [[1,0],[0,1],[1,1]], [1,2]),
 (3, [[1,0],[0,1],[1,1],[1,2]], [1,2]),
]

def rank(rows,q):
 if not rows: return 0
 M=[list(r) for r in rows]; k=0
 for c in range(len(M[0])):
  i=next((i for i in range(k,len(M)) if M[i][c]%q),None)
  if i is None:continue
  M[k],M[i]=M[i],M[k]
  z=pow(M[k][c],-1,q)
  M[k]=[x*z%q for x in M[k]]
  for j in range(len(M)):
   if j!=k and M[j][c]%q:
    z=M[j][c];M[j]=[(x-z*y)%q for x,y in zip(M[j],M[k])]
  k+=1
  if k==len(M):break
 return k

def predicted(q,weights,arity):
 d=len(weights[0]);m=len(weights)
 # Uniform matroid formula for rank=min(s,d)
 return q**m*sum(comb(m,s)*(q**(arity-1)-1)**s*q**(arity*(d-min(s,d))) for s in range(m+1))

def brute(q,weights,arity):
 d=len(weights[0]); m=len(weights)
 count=0
 # Enumerate H coordinates, count all possible compatible radical rows by actual minors.
 # Enumerates radical rows only to independently verify the line-or-free rule,
 # then multiplies their counts (all constraints separate by weight).
 rows=list(product(range(q), repeat=arity))
 for Hflat in product(range(q),repeat=d*arity):
  H=[Hflat[t*d:(t+1)*d] for t in range(arity)]
  ways=1
  for alpha in weights:
   t=tuple(sum(a*h for a,h in zip(alpha,H[j]))%q for j in range(arity))
   num=0
   for u in rows:
    if all((t[i]*u[j]-t[j]*u[i])%q==0 for i in range(arity) for j in range(i+1,arity)):
     num+=1
   ways*=num
  count+=ways
 return count

def check():
 count=0
 for q,weights,arities in CASES:
  d=len(weights[0]);m=len(weights)
  for r in range(1,min(d,m)+1):
   # The row configuration is uniform in all the selected tests.
   from itertools import combinations
   assert all(rank([weights[i] for i in I],q)==r for I in combinations(range(m),r))
  for arity in arities:
   a=predicted(q,weights,arity); b=brute(q,weights,arity)
   assert a==b, (q,d,m,arity,a,b)
   count+=1
  print('OK',q,d,m,tuple(arities))
 print('UNIFORM_METABELIAN_COMMUTING_OK',count)

if __name__=='__main__':check()
