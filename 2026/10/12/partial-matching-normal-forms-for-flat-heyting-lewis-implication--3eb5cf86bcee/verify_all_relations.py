"""Finite checks for all binary relations (no upward closure assumed), n<=4."""
from itertools import product
from math import comb, factorial

def op(rows):
 n=len(rows); mask=(1<<n)-1
 ups=[mask ^ ((1<<p)-1) for p in range(n+1)]
 values=[]
 for A in ups:
  for B in ups:
   good=[]
   for w in range(n):
    if all(((r & ~A)!=0) or ((r & ~B)==0) for r in rows[w:]):
     good.append(w)
   values.append(good[0] if good else n)
 return tuple(values)

def minimal_from_op(F,n):
 # Use adjacent-input responses to recover last rows of each threshold.
 e=[]
 for p in range(n):
  pos=F[p*(n+1)+(p+1)]-1
  if pos>=0:e.append((pos,p))
 assert len(set(x for x,y in e))==len(e)
 return tuple(sum(1<<y for x,y in e if x==j) for j in range(n))

for n in range(1,5):
 groups={}; multiplicity={}
 for rows in product(range(1<<n),repeat=n):
  F=op(rows)
  multiplicity[F]=multiplicity.get(F,0)+1
  edges=sum(r.bit_count() for r in rows)
  if F not in groups:groups[F]=[edges,1,rows]
  elif edges<groups[F][0]:groups[F]=[edges,1,rows]
  elif edges==groups[F][0]:groups[F][1]+=1
 assert len(groups)==sum(comb(n,k)**2*factorial(k) for k in range(n+1))
 for F,(ed,num,rows) in groups.items():
  assert num==1,(n,ed,num,rows)
  assert rows==minimal_from_op(F,n),(n,rows,minimal_from_op(F,n))
  assert ed==sum(v>0 for v in rows)
  edges_list=[(i,v.bit_length()-1) for i,v in enumerate(rows) if v]
  ends={i for i,p in edges_list}
  w=lambda p:2**(n-p-1)
  pred=1
  for i,p in edges_list:pred*=w(p)
  for i in range(n):
   if i not in ends:
    pred*=1+sum(w(p) for j,p in edges_list if j>i)
  assert multiplicity[F]==pred,(n,rows,pred,multiplicity[F])
 print('raw_n',n,'relations',2**(n*n),'operators',len(groups),'all_unique_minimizer',True,'fibre_total',sum(multiplicity.values()))
print('RAW_VERIFY_OK')
