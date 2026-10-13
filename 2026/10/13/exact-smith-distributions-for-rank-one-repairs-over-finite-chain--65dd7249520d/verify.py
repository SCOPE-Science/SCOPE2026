from itertools import product
from collections import Counter
from math import gcd

def val(x,p,t):
 x%=p**t
 for j in range(t):
  if x%p:return j
  x//=p
 return t

def smith(M,p,t):
 q=p**t
 a=[[x%q for x in row] for row in M];n=len(a); seq=[]
 for idx in range(n):
  pos=min(((i,j) for i in range(idx,n) for j in range(idx,n)), key=lambda ij:val(a[ij[0]][ij[1]],p,t))
  i,j=pos
  a[idx],a[i]=a[i],a[idx]
  for row in a:row[idx],row[j]=row[j],row[idx]
  d=val(a[idx][idx],p,t);seq.append(d)
  if d==t:continue
  # canonical pivot by scaling its row
  unit=a[idx][idx]//p**d
  scale=pow(unit,-1,q)
  a[idx]=[(z*scale)%q for z in a[idx]]
  assert a[idx][idx]==p**d
  for i in range(idx+1,n):
   z=(a[i][idx]//p**d)
   assert (a[i][idx]-z*p**d)%q==0
   a[i]=[(aa-z*bb)%q for aa,bb in zip(a[i],a[idx])]
   assert a[i][idx]==0
  for j in range(idx+1,n):
   z=(a[idx][j]//p**d)
   assert (a[idx][j]-z*p**d)%q==0
   for i in range(n):a[i][j]=(a[i][j]-z*a[i][idx])%q
   assert a[idx][j]==0
 assert seq==sorted(seq),(seq,M)
 return tuple(seq)

def weight_triple(p,t,m):
 q=p**t
 pe=[q//(p**j)-q//(p**(j+1)) if j<t else 1 for j in range(t+1)]
 prim=q**m-(q//p)**m
 counts_c=[0]*(t+1)
 for j in range(1,t+1):counts_c[j]=prim*q**(m-1)*pe[j]
 counts_c[0]=q**(2*m)-sum(counts_c)
 assert sum(counts_c)==q**(2*m),(counts_c,q**(2*m))
 counts=Counter()
 for ac,bc,gc in product(range(t+1),repeat=3):
  d1=min(ac,bc,gc);d2=min(t,bc+gc-d1)
  assert d2>=d1
  counts[(0,)*(m-1)+(d1,d2)] += counts_c[ac]*pe[bc]*pe[gc]
 assert sum(counts.values())==q**(2*(m+1))
 return dict(sorted(counts.items()))

def verify(p,t,n):
 q=p**t;m=n-1
 expected=weight_triple(p,t,m)
 if q**(2*n)>1100000:
  print('skipping brute',p,t,n)
  return
 out=Counter()
 for E in product(range(q),repeat=n):
  for F in product(range(q),repeat=n):
   B=[[int(i==j and i<m)+E[i]*F[j] for j in range(n)] for i in range(n)]
   out[smith(B,p,t)]+=1
 print('checked',p,t,n,'target',expected,'observed',dict(sorted(out.items())),'PASS' if out==expected else 'FAIL',flush=True)
 assert out==expected

if __name__=='__main__':
 for p,t,n in [(2,1,2),(2,2,2),(2,2,3),(2,3,2),(2,3,3),(3,2,2),(3,2,3),(3,1,3),(5,1,2)]:
  verify(p,t,n)
