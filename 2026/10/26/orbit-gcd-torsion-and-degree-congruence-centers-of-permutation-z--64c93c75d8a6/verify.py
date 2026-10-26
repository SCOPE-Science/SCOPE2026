from itertools import permutations,product
from math import gcd, lcm
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def cycles(p):
 n=len(p); seen=set(); out=[]
 for x in range(n):
  if x in seen:continue
  u=x; a=[]
  while u not in seen:
   seen.add(u);a.append(u);u=p[u]
  out.append(a)
 return out

def relation_matrix(p):
 n=len(p); inv=[0]*n
 for i,j in enumerate(p):inv[j]=i
 rows=[]
 for i in range(n):
  for j in range(n):
   a=[0]*n
   for k,s in [(i,1),(j,1),(p[j],-1),(inv[i],-1)]:a[k]+=s
   rows.append(a)
 return Matrix(rows)

def sm_invariants(p):
 A=smith_normal_form(relation_matrix(p),domain=ZZ)
 return len(p)-sum(A[i,i]!=0 for i in range(min(A.shape))), sorted(abs(int(A[i,i])) for i in range(min(A.shape)) if abs(int(A[i,i]))>1)

def center_pred(p,a):
 m=lcm(*(len(z) for z in cycles(p)))
 return all(a[p[i]]==a[i] for i in range(len(p))) and sum(a)%m==0

def group_product(p,a,b):
 n=len(p);s=sum(a);r=list(range(n))
 for _ in range(s%lcm(*(len(z) for z in cycles(p)))):
  r=[p[k] for k in r]
 z=list(a)
 for i, val in enumerate(b):z[r[i]]+=val
 return tuple(z)

def check():
 total=0
 for n in range(1,7):
  count=0
  for p in permutations(range(n)):
   cc=cycles(p);g=0
   for cyc in cc:g=gcd(g,len(cyc))
   rank,tors=sm_invariants(p)
   assert rank==len(cc) and tors==([] if g==1 else [g]), (p,rank,tors,len(cc),g)
   if n<=4:
    e=[tuple(int(j==i) for j in range(n)) for i in range(n)]
    for a in product((-1,0,1),repeat=n):
     actual=all(group_product(p,a,b)==group_product(p,b,a) for b in e)
     assert actual==center_pred(p,a),(p,a,actual)
   count+=1
  print('n',n,'permutations',count)
  total+=count
 print('VERIFY_OK',total)
if __name__=='__main__':check()
