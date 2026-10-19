"""Finite tests for wedge commutator operator in a five-generator exterior algebra."""
from itertools import combinations
import random
N=5; subsets=list(range(1<<N)); odd=[s for s in subsets if s.bit_count()%2]; even=[s for s in subsets if s.bit_count()%2==0]

def coeff(s,t,p):
 if s&t:return 0
 e=0
 for i in range(N):
  if s>>i&1: e+= (t&((1<<i)-1)).bit_count()
 return (-1 if e%2 else 1)%p

def rk(M,p):
 A=[row[:] for row in M];i=0
 for j in range(len(A[0])):
  t=next((k for k in range(i,len(A)) if A[k][j]%p),None)
  if t is None:continue
  A[i],A[t]=A[t],A[i]; a=pow(A[i][j],-1,p)
  A[i]=[(x*a)%p for x in A[i]]
  for k in range(len(A)):
   if k!=i and A[k][j]%p:
    b=A[k][j];A[k]=[(x-b*y)%p for x,y in zip(A[k],A[i])]
  i+=1
  if i==len(A):break
 return i

def adjrank(a,p):
 mat=[]
 for t in even:
  row=[]
  for s in odd:
   x=0
   for h,c in a.items():
    if (h|s)==t:x+=2*c*coeff(h,s,p)
   row.append(x%p)
  mat.append(row)
 return rk(mat,p)

def classify(a,p):
 linear=any(a.get(1<<i,0) for i in range(N))
 if linear:return 8
 triples=[s for s in odd if s.bit_count()==3]
 M=[[a.get(t^s,0)*coeff(t^s,s,p)%p if s&t==s and (t^s).bit_count()==3 else 0 for s in [1<<i for i in range(N)]] for t in even if t.bit_count()==4]
 return rk(M,p)

for p in (3,5,7):
 rng=random.Random(55+p);tot={}
 for t in range(400):
  a={s:rng.randrange(p) for s in odd}
  ar=adjrank(a,p);cr=classify(a,p)
  if ar!=cr:raise AssertionError((p,a,ar,cr))
  tot[ar]=tot.get(ar,0)+1
 print('FIELD',p,'400 random vectors:',tot)
for p in (3,5):
 # exact rank2/4 census for 10 coefficients: q^10 too big; check q=3 is 59049 acceptable
 n3=[s for s in odd if s.bit_count()==3]
 from itertools import product
 freqs={0:0,2:0,4:0}
 for val in product(range(p),repeat=10):
  a=dict(zip(n3,val)); r=classify(a,p);freqs[r]+=1
  if p==5 and sum(freqs.values())>=100000:break
 print('TEST',p,freqs)
 if p==3:
  M2=(p-1)*((p**5-1)*(p**4-1)//((p**2-1)*(p-1)))
  assert freqs=={0:1,2:M2,4:p**10-1-M2},(freqs,M2)
print('VERIFY_OK')
