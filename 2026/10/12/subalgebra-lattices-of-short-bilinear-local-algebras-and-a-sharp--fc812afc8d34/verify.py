from itertools import combinations,product
from fractions import Fraction
from math import prod

class Field:
 def __init__(self,q):
  assert q in (2,3,4,5,7);self.q=q
 def add(self,a,b):return (a^b) if self.q==4 else (a+b)%self.q
 def neg(self,a):return a if self.q==4 else (-a)%self.q
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):
  if self.q!=4:return a*b%self.q
  x=0
  for i in range(2):
   for j in range(2):
    if (a>>i)&1 and (b>>j)&1:x^=1<<(i+j)
  if x&8:x^=0b1100
  if x&4:x^=0b111
  return x
 def inv(self,a):
  for b in range(1,self.q):
   if self.mul(a,b)==1:return b
  raise ValueError(a)

def rref_spaces(f,n,d):
 for ps in combinations(range(n),d):
  spots=[(i,j) for i,p in enumerate(ps) for j in range(p+1,n) if j not in ps]
  for vals in product(range(f.q),repeat=len(spots)):
   rows=[[0]*n for _ in range(d)]
   for i,p in enumerate(ps):rows[i][p]=1
   for (i,j),a in zip(spots,vals):rows[i][j]=a
   yield rows

def in_span(f,rows,v):
  v=list(v)
  for row in rows:
   p=next((i for i,z in enumerate(row) if z),None)
   if p is None:continue
   a=v[p]
   for j in range(p,len(v)):
    v[j]=f.sub(v[j],f.mul(a,row[j]))
  return not any(v)

def bil(f,B,v,w):
 r=0
 for i in range(len(B)):
  for j in range(len(B)):
   r=f.add(r,f.mul(f.mul(v[i],B[i][j]),w[j]))
 return r

def count(f,B):
 n=len(B);stat={}
 for d in range(n+2):
  valid=0
  for rows in rref_spaces(f,n+1,d):
   yes=True
   for v in rows:
    for w in rows:
     z=bil(f,B,v[:n],w[:n]);out=[0]*n+[z]
     if not in_span(f,rows,out):yes=False;break
    if not yes:break
   valid+=yes
  stat[d]=valid
 return stat

def gaussian(n,k,q):
 if k<0 or k>n:return 0
 return prod((q**(n-i)-1) for i in range(k))//prod((q**(k-i)-1) for i in range(k))

def S(h,k,q):
 if k<0 or k>h:return 0
 return int(prod(Fraction(q**(2*(h-i))-1,q**(k-i)-1) for i in range(k)))

def iso(q,n,kind,k):
 if k<0:return 0
 h=n//2
 if q%2:
  if n%2:return S(h,k,q)
  if kind=='split':
   if k>h:return 0
   return int(prod(Fraction((q**(h-i)-1)*(q**(h-i-1)+1),q**(k-i)-1) for i in range(k)))
  else:
   if k>h-1:return 0
   return int(prod(Fraction((q**(h-i)+1)*(q**(h-i-1)-1),q**(k-i)-1) for i in range(k)))
 if n%2:return S(h,k,q)
 if kind=='alternating':return S(h,k,q)
 return q**k*S(h-1,k,q)+S(h-1,k-1,q)

def matrix_B(f,n,kind):
 q=f.q;B=[[0]*n for _ in range(n)]
 if q%2:
  if n%2:
   B[0][0]=1;j0=1
  elif kind=='split':j0=0
  else:
   
   d=next(a for a in range(2,q) if a not in {f.mul(x,x) for x in range(q)})
   B[0][0]=1;B[1][1]=f.neg(d);j0=2
  for j in range(j0,n,2):B[j][j+1]=B[j+1][j]=1
 else:
  if kind=='nonalternating':
   for j in range(n):B[j][j]=1
  else:
   for j in range(0,n,2):B[j][j+1]=B[j+1][j]=1
 return B

if __name__=='__main__':
 tests=[(2,2,'alternating'),(2,2,'nonalternating'),(2,3,'nonalternating'),(2,4,'alternating'),(2,4,'nonalternating'),(3,2,'split'),(3,2,'nonsplit'),(3,3,'parabolic'),(3,4,'split'),(3,4,'nonsplit'),(4,2,'alternating'),(4,2,'nonalternating'),(4,3,'nonalternating'),(5,2,'split'),(5,2,'nonsplit'),(5,3,'parabolic'),(7,2,'split'),(7,2,'nonsplit')]
 for q,n,t in tests:
  f=Field(q);B=matrix_B(f,n,t);observed=count(f,B)
  expected={d:gaussian(n,d-1,q)+q**d*iso(q,n,t,d) for d in range(n+2)}
  if observed!=expected:print('FAIL',q,n,t,observed,expected);raise AssertionError('wrong')
  print('PASS',q,n,t,observed)
 print('VERIFY_OK')

def general_iso(q,n,r,kind,k):
 s=n-r
 return sum(gaussian(s,a,q)*q**((k-a)*(s-a))*iso(q,r,kind,k-a) for a in range(max(0,k-r),min(k,s)+1))

def matrix_deg(f,n,r,kind):
 b=matrix_B(f,r,kind)
 return [[b[i][j] if i<r and j<r else 0 for j in range(n)] for i in range(n)]

if __name__=='__main__':
 tests=[]
 for q,n in ((2,3),(2,4),(3,3),(3,4),(4,3)):
  for r in range(1,n+1):
   if q%2:
    kinds=['parabolic'] if r%2 else ['split','nonsplit']
   else:
    kinds=['nonalternating'] if r%2 else ['nonalternating','alternating']
   for kind in kinds:tests.append((q,n,r,kind))
 fingerprints={}
 for q,n,r,kind in tests:
  f=Field(q);B=matrix_deg(f,n,r,kind);actual=count(f,B)
  expected={d:gaussian(n,d-1,q)+q**d*general_iso(q,n,r,kind,d) for d in range(n+2)}
  assert actual==expected,(q,n,r,kind,actual,expected)
  fingerprints[(q,n,r,kind)]=tuple(actual.values())
  print('PASS_GENERAL',q,n,r,kind,tuple(actual.values()))
 for q,n in {(q,n) for q,n,r,t in tests}:
  group=[(r,t,fingerprints[q,n,r,t]) for qq,nn,r,t in tests if (qq,nn)==(q,n)]
  for i,(r,t,fp) in enumerate(group):
   for rr,tt,ff in group[i+1:]:
    if q%2:assert fp!=ff,('odd-field collision',q,n,r,t,rr,tt)
    elif fp==ff:assert t==tt=='nonalternating' and {r,rr}=={2*((max(r,rr)+1)//2)-1,2*((max(r,rr)+1)//2)},('extra collision',q,n,r,t,rr,tt)
 print('VERIFY_GENERAL_OK')
