from itertools import product
from math import prod
from collections import Counter

def rref_rank(rows,q):
 a=[list(x) for x in rows];rank=0
 if not a:return 0
 n=len(a[0]);m=len(a)
 for j in range(n):
  k=next((i for i in range(rank,m) if a[i][j]%q),None)
  if k is None:continue
  a[rank],a[k]=a[k],a[rank]
  u=pow(a[rank][j],-1,q);a[rank]=[v*u%q for v in a[rank]]
  for i in range(m):
   if i!=rank:
    c=a[i][j]%q
    a[i]=[(x-c*y)%q for x,y in zip(a[i],a[rank])]
  rank+=1
  if rank==m:break
 return rank

def gauss(n,k,q):
 if k<0 or k>n:return 0
 v=1
 for j in range(k):v=v*(q**(n-j)-1)//(q**(k-j)-1) if False else v
 return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def factor(m,q,s):
 k=3;acc=0
 for r in range(s,min(k,m)+1):
  acc+=gauss(k-s,r-s,q)*prod(q**m-q**i for i in range(r))*q**(k*(m-r))
 return acc

def pred(m,q):
 f0= factor(m,q,0);f2=factor(m,q,2);f3=factor(m,q,3)
 a2=q**3-1 if q%2==0 else q**3-1-(q-1)**3
 a3=0 if q%2==0 else (q-1)**3
 return f0+a2*f2+a3*f3

def brute(m,q):
 vectors=list(product(range(q),repeat=m));Arows=list(product(vectors,repeat=3));c=0
 for A in Arows:
  for B in Arows:
   if all(sum(A[i][t]*B[i][t] for t in range(m))%q==0 for i in range(3)) and all((sum(A[i][t]*B[j][t]-A[j][t]*B[i][t] for t in range(m))%q)==0 for i in range(3) for j in range(i+1,3)):
    c+=1
 return c

if __name__=='__main__':
 for m,q in [(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)]:
  b=brute(m,q);p=pred(m,q)
  print('m,q',m,q,'brute',b,'pred',p,'triples with central',q**3*b,'PASS',b==p)
  assert b==p
