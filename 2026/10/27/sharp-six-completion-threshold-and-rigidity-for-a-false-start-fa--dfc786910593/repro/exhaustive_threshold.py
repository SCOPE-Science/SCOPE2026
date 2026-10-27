from math import comb
from itertools import product
from collections import Counter
K=6
O=[0]*(K+1); ONE=[1]+[0]*K

def mul(a,b):
 c=[0]*(K+1)
 for i,v in enumerate(a):
  if not v:continue
  for j,w in enumerate(b[:K+1-i]):
   if w:c[i+j]+=v*w
 return c

def add(a,b,mulb=1):return [x+mulb*y for x,y in zip(a,b)]

def pow1(k): return [((-1)**j)*comb(k,j) if j<=k else 0 for j in range(K+1)]

def geometric_sum(r,n):
 # pair power/sum exponentiation, with (p,s)*(r,t) = (p*r,s+p*t)
 p=list(ONE);s=list(O)
 basep=list(r); bases=list(ONE)
 while n:
  if n&1:
   s=add(s,mul(p,bases));p=mul(p,basep)
  bases=add(bases,mul(basep,bases));basep=mul(basep,basep);n>>=1
 return s

FT=[];v=[-1]+[0]*K
for i in range(K+1):
 FT.append(v)
 q=1<<i
 term=add(ONE,pow1(q),-1)
 v=mul(v,term)

def reach(s):
 L=len(s);c=[(-1)**j*sum(z*comb(k,j) for k,z in enumerate(s) if k>=j) for j in range(K+1)]
 for i in range(K+1):
  den=1<<(i*(i-1)//2)
  if c[i]%den:return i-1
  b=c[i]//den
  if b:
   S=geometric_sum(pow1(1<<i),abs(b))
   delta=mul(mul(pow1(L),FT[i]),S)
   c=add(c,delta,1 if b>0 else -1)
   L+=abs(b)*(1<<i)
   assert all(x==0 for x in c[:i+1]),(s,i,b,c[:i+1])
 return K


if __name__=="__main__":
 TM=tuple(-1 if j.bit_count()%2==0 else 1 for j in range(17))
 counts={}
 witnesses={}
 for n in range(2,18):
  count=[0]*7
  full=[]
  for tail in product((-1,1),repeat=n-1):
   s=(-1,)+tail
   if s==TM[:n]: continue
   highest=reach(s)
   for j in range(highest+1): count[j]+=1
   if highest>=6: full.append(s)
  counts[n]=count
  if full:witnesses[n]=full
 assert all(counts[n][6]==0 for n in range(2,17))
 assert counts[17][6]==1
 expected=TM[:16]+(-1,)
 assert witnesses[17]==[expected],witnesses[17]
 assert counts[17][5]==7
 print("checked all nonexceptional words with first sign -1 of lengths 2 through 17")
 print("number of 6-completable normalized words by length:", [(n,counts[n][6]) for n in range(2,18)])
 print("5-completable normalized words at n=17:", counts[17][5])
 print("unique normalized maximizer:", expected)
 print("global extremizers: maximizer and its sign complement")
