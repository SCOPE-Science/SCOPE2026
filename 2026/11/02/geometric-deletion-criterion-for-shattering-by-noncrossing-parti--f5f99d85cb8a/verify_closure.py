from itertools import combinations
from functools import lru_cache
from math import comb
import time,sys

def generate(n):
 E=list(combinations(range(n),2)); m=len(E)
 cross={}
 for A in range(1,1<<n):
  for B in range(1,1<<n):
   if A&B or A>=B:continue
   AA=[i for i in range(n) if A>>i&1]
   BB=[j for j in range(n) if B>>j&1]
   flag=0
   for a,c in combinations(AA,2):
    if flag:break
    for b,d in combinations(BB,2):
     if a<b<c<d or b<a<d<c:
      flag=1;break
   if flag:cross[A,B]=True
 def crosses(A,B):
  return cross.get((A,B) if A<B else (B,A),False)
 @lru_cache(maxsize=500000)
 def cl(m):
  comps=[1<<i for i in range(n)]
  for k,(a,b) in enumerate(E):
   if (m>>k)&1:
    ia=next(i for i,v in enumerate(comps) if v>>a&1)
    ib=next(i for i,v in enumerate(comps) if v>>b&1)
    if ia!=ib:
     if ia>ib:ia,ib=ib,ia
     comps[ia]|=comps.pop(ib)
  while True:
   c=0
   for i in range(len(comps)):
    for j in range(i+1,len(comps)):
     if crosses(comps[i],comps[j]):
      comps[i]|=comps.pop(j);c=1;break
    if c:break
   if not c:break
  labels=[0]*n
  for a,x in enumerate(comps):
   for i in range(n):
    if (x>>i)&1:labels[i]=a
  return tuple(labels)
 def shattered(S):
  for k in range(m):
   if (S>>k)&1:
    p=cl(S^(1<<k));a,b=E[k]
    if p[a]==p[b]:return False
  return True
 t=time.monotonic()
 counts=[];examples={};ne=0
 for k in range(n):
  ct=0
  for ix in combinations(range(m),k):
   z=sum(1<<i for i in ix)
   if shattered(z):ct+=1
  counts.append(ct)
  print('n',n,'k',k,'shattered',ct,'elapsed',round(time.monotonic()-t,2),'cache',cl.cache_info().currsize,flush=True)
 return counts

if __name__=='__main__':
 for n in (list(map(int,sys.argv[1:])) if len(sys.argv)>1 else [4,5,6]):
  got=generate(n)
  assert got=={4:[1,6,15,12],5:[1,10,45,90,55],6:[1,15,105,375,588,273]}[n], (n,got)
  print("CROSSING_BLOCK_CLOSURE_PASS",n,got,flush=True)
 print("ALL_CLOSURE_CHECKS_PASS")
