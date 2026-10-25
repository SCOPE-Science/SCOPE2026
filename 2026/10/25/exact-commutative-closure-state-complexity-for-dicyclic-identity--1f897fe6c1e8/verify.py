"""Reproducibility checks for an exact dicyclic group-language state count.
No external packages; finite tests are supplemental to the written proof.
"""
from itertools import product
from collections import deque

def product_group(m,x,y):
 k,e=x; l,f=y
 return ((k+(-1)**e*l+(m if e==f==1 else 0))%(2*m), (e+f)%2)

def feasible_direct(m,r,s):
 vals={(0,0)}
 # Enumerate all distinct outcomes via number-of-letters DP, not all words.
 dp={(0,0):{(0,0)}}
 for i in range(r+1):
  for j in range(s+1):
   if (i,j)==(0,0):continue
   x=set()
   if i>0:
    for h in dp[i-1,j]:x.add(product_group(m,h,(1,0)))
   if j>0:
    for h in dp[i,j-1]:x.add(product_group(m,h,(0,1)))
   dp[i,j]=x
 return (0,0) in dp[r,s]

def predicate(m,r,s):
 if s%2:return False
 if s==0:return r%(2*m)==0
 if s%4==0:return r%2==0
 return r>=m and (r-m)%2==0

def canonical(m,r,s):
 if s==0:
  return ('A-low',r) if r<m-1 else ('A-residue',r%(2*m))
 if r<m-1:return ('B-low',r,s%4)
 return ('B-stable',s%2,(r+(m%2)*((s+1)//2))%2)

def check(m):
 for r in range(0,min(16,2*m+6)):
  for s in range(0,14):
   assert feasible_direct(m,r,s)==predicate(m,r,s),(m,r,s)
 witness={}
 for r in range(0,4*m+5):
  for s in range(0,9):
   t=canonical(m,r,s)
   if t in witness:
    rr,ss=witness[t]
    for u in range(0,4*m+4):
     for v in range(0,12):
      assert predicate(m,rr+u,ss+v)==predicate(m,r+u,s+v),(m,(rr,ss),(r,s),(u,v))
   else:witness[t]=(r,s)
 assert len(witness)==7*m-1,(m,len(witness))
 for t,(r,s) in witness.items():
  for a in ((1,0),(0,1)):
   assert canonical(m,r+a[0],s+a[1]) in witness
 for t,(r,s) in witness.items():
  for j,(t2,(rr,ss)) in enumerate(witness.items()):
   if t2==t:continue
   assert any(predicate(m,r+u,s+v)!=predicate(m,rr+u,ss+v) for u in range(0,4*m+4) for v in range(0,7)),(m,t,t2)
 return len(witness)

if __name__=='__main__':
 for m in range(2,11):print('m=',m,'states=',check(m),'expected=',7*m-1)
 print('VERIFY_OK')
