from functools import lru_cache
from math import comb,factorial
from collections import Counter

def poly_predict(n):
 out=Counter()
 for k in range(n//2+1):
  m=factorial(n)//(2**k*factorial(k)*factorial(n-2*k))
  r=n-2*k
  for c in range(r+1):
   u=r-c
   # ((1+z)^u-1)^c, powers 1..u
   dp={0:1}
   for _ in range(c):
    nd=Counter()
    for a,t in dp.items():
     for j in range(1,u+1):nd[a+j]+=t*comb(u,j)
    dp=nd
   for a,t in dp.items():out[2*k+a]+=m*comb(r,c)*t
 return out

def brute(n):
 pairs=[(a,b) for a in range(n) for b in range(a+1,n)]
 vertices=[(a,e) for e,(i,j) in enumerate(pairs) for a in (i,j)]
 def is_adj(x,y):
  u,e=vertices[x];v,f=vertices[y]
  return e==f and u!=v
 def conflicts(x,y):
  for a in range(2):
   A=vertices[x] if a==0 else vertices[y]
   B=vertices[y] if a==0 else vertices[x]
   # selected incidences x=(u,e), y=(v,f) ; graph endpoints original u,v and subdivision e,f
   # a third incidence linking original of first to subdivision of second
   if A[0] in pairs[B[1]] and (A[0],B[1])!=A and (A[0],B[1])!=B:return True
  return False
 N=len(vertices);mask=[0]*N
 for i in range(N):
  for j in range(i+1,N):
   if conflicts(i,j):mask[i]|=1<<j;mask[j]|=1<<i
 c=Counter()
 for subset in range(1<<N):
  good=True
  x=subset
  while x:
   bit=x&-x;v=bit.bit_length()-1
   if mask[v]&subset:good=False;break
   x-=bit
  if good:c[subset.bit_count()]+=1
 return c
for n in range(2,6):
 p=poly_predict(n);b=brute(n)
 print('n',n,'edges',n*(n-1),'formula',sorted(p.items()),'brute',sorted(b.items()),'MATCH',p==b)
