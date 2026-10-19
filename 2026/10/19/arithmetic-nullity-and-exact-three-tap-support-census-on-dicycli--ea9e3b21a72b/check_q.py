import math,itertools,random
from collections import Counter

def mul(a,b,n):
 i,e=a;j,f=b
 # x^i y^e x^j y^f = x^(i+(-1)^e j + n*e*f) y^(e+f mod2)
 return ((i+((-1)**e)*j+n*e*f)%(2*n),(e+f)%2)

def predicted(S,n):
 cos=Counter(e for i,e in S)
 if len(cos)==1:
  v=[i for i,e in S];N=2*n
  d=math.gcd((v[1]-v[0])%N,(v[2]-v[0])%N,N)
  if (N//d)%3==0 and {((v[1]-v[0])//d)%3,((v[2]-v[0])//d)%3}=={1,2}:return 4*d
  return 0
 else:
  e=max(cos,key=lambda z:cos[z]); pair=[i for i,f in S if f==e]
  d=math.gcd(pair[1]-pair[0],n)
  return 2*d if (n//d)%3==0 else 0

def rank_mod(S,n,p=1000000007):
 G=[(i,e) for e in (0,1) for i in range(2*n)]; lookup={g:i for i,g in enumerate(G)}
 a=[[0]*len(G) for _ in G]
 for col,g in enumerate(G):
  for s in S:a[lookup[mul(s,g,n)]][col]+=1
 rank=0;m=len(G)
 for c in range(m):
  pivot=next((r for r in range(rank,m) if a[r][c]%p),None)
  if pivot is None:continue
  a[rank],a[pivot]=a[pivot],a[rank]
  inv=pow(a[rank][c],p-2,p)
  row=a[rank]
  for r in range(rank+1,m):
   if (f:=a[r][c]%p):
    t=f*inv%p; rr=a[r]
    for k in range(c,m):rr[k]=(rr[k]-t*row[k])%p
  rank+=1
  if rank==m:break
 return m-rank

def census(n):
 G=[(i,e) for e in (0,1) for i in range(2*n)]
 c=Counter();pm=Counter()
 for S in itertools.combinations(G,3):
  p=predicted(S,n);c[p]+=1
  pm[tuple(sorted(Counter(e for i,e in S).values())) ,p]+=1
 return c,pm
if __name__=='__main__':
 random.seed(89)
 checks=0
 for n in range(2,13):
  G=[(i,e) for e in (0,1) for i in range(2*n)]
  sample=list(itertools.combinations(G,3)) if n<=4 else [tuple(random.sample(G,3)) for _ in range(40 if n<=7 else 25)]
  for S in sample:
   expected=predicted(S,n)
   got=rank_mod(S,n)
   if expected!=got:raise AssertionError((n,S,expected,got))
   checks+=1
  print('n',n,'sample_checks',len(sample),flush=True)
 for n in (3,6,9,12):
  c,pm=census(n)
  print('census',n,sorted(c.items()),'mixed vs same',dict(pm),flush=True)
 print('PASS',checks)

def euler_phi(m):
 out=m
 for p in range(2,math.isqrt(m)+1):
  if m%p==0:
   out-=out//p
   while m%p==0:m//=p
 if m>1:out-=out//m
 return out

def predicted_census(n):
 N=2*n
 c=Counter()
 for d in range(1,n+1):
  if n%d==0 and (n//d)%3==0:
   c[2*d]+=8*n*n*euler_phi(n//d)
 for d in range(1,N+1):
  if N%d or (N//d)%3:continue
  M=N//d
  u=M
  while u%3==0:u//=3
  from fractions import Fraction
  f=Fraction(2*N*M*M,27)
  for p in range(2,u+1):
   if u%p==0 and all(p%j for j in range(2,math.isqrt(p)+1)):
    f*=Fraction(p*p-1,p*p)
  assert f.denominator==1, (n,d,f)
  c[4*d]+=int(f)
 c[0]=math.comb(4*n,3)-sum(c.values())
 return c

if __name__=='__main__':
 for n in range(2,25):
  actual,_=census(n)
  formula=predicted_census(n)
  assert actual==formula,(n,actual,formula)
  print('census_formula_ok',n,len(actual),flush=True)
 print('CENSUS_PASS')
