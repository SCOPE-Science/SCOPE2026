from fractions import Fraction
from math import comb
from itertools import combinations_with_replacement

def hist(d):
 n=len(d); e=[0]*(n+1);e[0]=1
 for v in d:
  for k in range(n,0,-1):e[k]+=v*e[k-1]
 p=[Fraction(0)]*(n+1)
 for k in range(n+1):
  a=Fraction(e[k],__import__('math').factorial(n)//__import__('math').factorial(n-k))
  for j in range(k+1):p[j]+=a*(-1)**(k-j)*comb(k,j)
 assert sum(p)==1 and sum(i*p[i] for i in range(n+1))==1
 return p
for n in range(2,11):
 rows=[]
 for d in combinations_with_replacement(range(n+1),n):
  if sum(d)!=n:continue
  dd=tuple(sorted(d,reverse=True));p=hist(dd)
  stop=[sum(p[j]*(j-k) for j in range(k+1,n+1)) for k in range(n)]
  rows.append((dd,stop))
 comps=0
 for d,t in rows:
  for e,s in rows:
   if d==e:continue
   if all(sum(d[:i]) >= sum(e[:i]) for i in range(1,n+1)):
    comps+=1
    # d more concentrated => F_d <=cx F_e
    if not all(t[k]<=s[k] for k in range(n)):
     print('COUNTER',n,d,e,t,s);exit()
 print('CONVEX_PASS n',n,'profiles',len(rows),'majorized_pairs',comps)
