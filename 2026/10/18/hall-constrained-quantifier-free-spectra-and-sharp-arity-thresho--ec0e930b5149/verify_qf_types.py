#!/usr/bin/env python3
"""Independent tuple-atomic-diagram enumeration versus Hall-constrained EGF.
The algebra is a finite idempotent unary function. No external dependencies.
"""
from fractions import Fraction
from itertools import product
from math import factorial

def add(a,b):
 out=dict(a)
 for j,c in b.items():out[j]=out.get(j,Fraction())+c
 return {j:c for j,c in out.items() if c}
def mul(a,b):
 out={}
 for j,c in a.items():
  for k,d in b.items():out[j+k]=out.get(j+k,Fraction())+c*d
 return {j:c for j,c in out.items() if c}
def scale(a,c):return {j:x*c for j,x in a.items() if x*c}

def formula(cap):
 cap=sorted(cap,reverse=True)
 r=len(cap); top=cap[0]; B=[{1:Fraction(1)}]
 # y^(b) (1+y)/b! where b>=1
 for b in range(1,top+1): B.append({b:Fraction(1,factorial(b)),b+1:Fraction(1,factorial(b))})
 ans={0:Fraction(1)}
 def recur(counts,remain,highest):
  nonlocal ans
  t=sum(counts)
  if t:
   demands=[]
   for b,num in enumerate(counts): demands.extend([b]*num)
   demands.sort(reverse=True)
   if any(demands[i]>cap[i] for i in range(t)):return
   q={0:Fraction(1)}
   for b,num in enumerate(counts):
    for _ in range(num):q=mul(q,B[b])
    q=scale(q,Fraction(1,factorial(num)))
   ans=add(ans,q)
  if t==r:return
  for b in range(highest,-1,-1):
   # unique multiset enumeration by nonincreasing b
   counts[b]+=1; recur(counts,remain-1,b); counts[b]-=1
 recur([0]*(top+1),r,top)
 return ans

def stirling(k,d):
 if d>k:return 0
 a=[0]*(d+1);a[0]=1
 for i in range(1,k+1):
  b=[0]*(d+1)
  for j in range(1,min(d,i)+1):b[j]=a[j-1]+j*a[j]
  a=b
 return a[d]

def predicted(poly,k):return sum(c*factorial(d)*stirling(k,d) for d,c in poly.items())

def construct(cap):
 f=[]
 for c in cap:
  root=len(f);f.append(root);f.extend([root]*c)
 return f

def qf_types(f,k):
 seen=set();n=len(f)
 for row in product(range(n),repeat=k):
  terms=row+tuple(f[x] for x in row)
  # canonical atom equality classes; all QF diagrams are exactly this
  nums={}; canon=[]
  for v in terms:
   if v not in nums:nums[v]=len(nums)
   canon.append(nums[v])
  seen.add(tuple(canon))
 return len(seen)

def run():
 tested=0;total_tuples=0
 for n in range(1,8):
  for r in range(1,n+1):
   def partitions_of_sum(s,hi):
    if s==0: yield []
    else:
     for j in range(min(s,hi),1-1,-1):
      for tail in partitions_of_sum(s-j,j):yield [j]+tail
   for pos in partitions_of_sum(n-r,n-r):
    if len(pos)>r:continue
    cap=pos+[0]*(r-len(pos))
    poly=formula(cap); f=construct(cap)
    for k in range(0,5 if n<=4 else 4 if n<=6 else 3):
     a=qf_types(f,k); p=predicted(poly,k)
     assert p.denominator==1 and a==p,(cap,k,a,p,poly)
     tested+=1;total_tuples+=n**k
 # known stress representative unequal capacities
 for cap in [(3,1,0),(2,2,0),(1,1,1),(4,2),(2,1,1)]:
  poly=formula(cap); f=construct(cap)
  for k in range(0,5):
   a=qf_types(f,k); p=predicted(poly,k)
   assert a==p,(cap,k,a,p)
   tested+=1; total_tuples+=len(f)**k
 print('VERIFY_OK instances=',tested,'evaluated_tuple_assignments=',total_tuples)
 for cap in [(0,0),(1,1),(2,1,0),(3,1,0),(2,2)]:
  pol=formula(cap); print('profile',cap,'P(y)=',str(sorted(pol.items())),'T0..5=',[int(predicted(pol,k)) for k in range(6)])
if __name__=='__main__':run()

def compare_thresholds():
 from itertools import combinations_with_replacement
 count=0
 for r in range(1,5):
  caps=list(combinations_with_replacement(range(0,5),r))
  for c0 in caps:
   c=sorted(c0,reverse=True)
   for d0 in caps:
    d=sorted(d0,reverse=True)
    if c==d or not all(x<=y for x,y in zip(c,d)):continue
    kstar=min((j+1)*(c[j]+1) for j in range(r) if c[j]<d[j])
    pc=formula(c);pd=formula(d)
    for k in range(kstar+1):
     a=predicted(pc,k);b=predicted(pd,k)
     assert ((a==b) if k<kstar else (a<b)), (c,d,k,kstar,a,b)
    count+=1
 print('SHARP_THRESHOLD_OK pairs=',count)
if __name__=='__main__':compare_thresholds()
