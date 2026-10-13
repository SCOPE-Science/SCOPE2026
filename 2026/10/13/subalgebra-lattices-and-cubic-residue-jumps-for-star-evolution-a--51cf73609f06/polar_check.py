from checker import Field,iso_counts
from math import prod

def gauss(q,n,k):
 if k<0 or k>n:return 0
 return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def orth(q,n,delta):
 def chi(a):
  a%=q
  if a==0:return 0
  return 1 if pow(a,(q-1)//2,q)==1 else -1
 def Z(n,d):
  if n==0:return 1
  if n%2:return q**(n-1)
  return q**(n-1)+(q-1)*q**(n//2-1)*chi(((-1)**(n//2))*d)
 result=[]
 for r in range(n+1):
  a=prod(q**j*(Z(n-2*j,delta*((-1)**j))-1) for j in range(r)) if 2*r<=n else 0
  b=prod(q**r-q**j for j in range(r))
  assert a%b==0
  result.append(a//b)
 return result

def sympl(q,n):
 assert n%2==0
 return [prod(q**(n-j)-q**j for j in range(r))//prod(q**r-q**j for j in range(r)) for r in range(n//2+1)]

for q,m in [(3,1),(3,2),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2)]:
 f=Field(q)
 I=iso_counts(f,m)
 J=[]
 for d in range(m):
  n=0
  from checker import rrefs
  for B in rrefs(q,m,d):
   if all(f.sum(v)==0 for v in B) and all(f.dot(v,w)==0 for i,v in enumerate(B) for w in B[i:]):n+=1
  J.append(n)
 assert I==orth(q,m,1),(q,m,I,orth(q,m,1))
 assert J==orth(q,m-1,pow(m,-1,q)),(q,m,J,orth(q,m-1,pow(m,-1,q)))
 print('ORTH_OK',q,m,I,J)
for q,m in [(2,1),(2,3),(2,5),(4,1),(4,3)]:
 f=Field(q)
 I=iso_counts(f,m)
 sym=sympl(q,m-1)
 assert I==sym+[0]*(m-len(sym)+1),(q,m,I,sym)
 print('SYMP_OK',q,m,I)
print('POLAR_OK')
