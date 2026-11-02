"""Exhaustive small-field check for nilpotent-invariant ordered splittings."""
from itertools import product
from collections import Counter
from math import prod

def matmul(a,b,n,q):
 return tuple(sum(a[i*n+t]*b[t*n+j] for t in range(n))%q for i in range(n) for j in range(n))
def msub(a,b,q):return tuple((x-y)%q for x,y in zip(a,b))
def rank(a,n,q):
 rows=[list(a[i*n:(i+1)*n]) for i in range(n)]
 p=0
 for j in range(n):
  i=next((i for i in range(p,n) if rows[i][j]),None)
  if i is None:continue
  rows[p],rows[i]=rows[i],rows[p]
  inv=pow(rows[p][j],-1,q)
  rows[p]=[(x*inv)%q for x in rows[p]]
  for z in range(n):
   if z!=p:
    t=rows[z][j]
    rows[z]=[(x-t*y)%q for x,y in zip(rows[z],rows[p])]
  p+=1
 return p

def coeff(n,parts,q):
 # exact Gaussian multinomial at reciprocal q as a rational Number
 from fractions import Fraction
 t=Fraction(1,q)
 Q=lambda d:prod(1-t**i for i in range(1,d+1))
 v=Q(n)/prod(Q(d) for d in parts)
 return v

def compositions(n,k):
 if k==1:yield (n,);return
 for x in range(n+1):
  for tail in compositions(n-x,k-1):yield (x,)+tail

def check(n,q,verify_triples=True):
 mats=list(product(range(q),repeat=n*n))
 z=(0,)*(n*n); I=tuple(int(i==j) for i in range(n) for j in range(n))
 nil=[]; ids=[]
 for a in mats:
  power=I
  for k in range(n):power=matmul(power,a,n,q)
  if power==z:nil.append(a)
  if matmul(a,a,n,q)==a:ids.append(a)
 expected_nil=q**(n*n-n)
 assert len(nil)==expected_nil,(n,q,len(nil),expected_nil)
 per_rank=Counter()
 id_r={e:rank(e,n,q) for e in ids}
 for a in nil:
  for e in ids:
   if matmul(a,e,n,q)==matmul(e,a,n,q):per_rank[id_r[e]]+=1
 print('n,q',n,q,'nilpotent',len(nil),'idempotents',len(ids),'rank-pair totals',sorted(per_rank.items()))
 for r in range(n+1):
  assert per_rank[r]==len(nil)*coeff(n,(r,n-r),q),(n,q,r,per_rank[r],coeff(n,(r,n-r),q))
 if not verify_triples:return
 decomps=[]
 for e1 in ids:
  for e2 in ids:
   if matmul(e1,e2,n,q)!=z or matmul(e2,e1,n,q)!=z:continue
   e3=msub(msub(I,e1,q),e2,q)
   if e3 not in id_r:continue
   decomps.append(((id_r[e1],id_r[e2],id_r[e3]),(e1,e2,e3)))
 per=Counter()
 for a in nil:
  for ranks,es in decomps:
   if all(matmul(a,e,n,q)==matmul(e,a,n,q) for e in es):per[ranks]+=1
 print('triple profiles',sorted(per.items()))
 for v in compositions(n,3):assert per[v]==len(nil)*coeff(n,v,q),(n,q,v,per[v],coeff(n,v,q))

if __name__=='__main__':
 for n,q in [(1,2),(2,2),(2,3),(3,2)]:check(n,q)
 print('VERIFY_OK: matrix enumeration, idempotency, commutation, and ordered triples')
