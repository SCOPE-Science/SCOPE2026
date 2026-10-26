from collections import Counter
from math import gcd, lcm,prod
from sympy import primerange

def period(k,a,b):
 d=gcd(a,b); a//=d
 ans=1
 for p in primerange(2,k+1):
  if a%p==0: continue
  pp=p; e=1
  while pp*p<=k: pp*=p;e+=1
  if (k+1)%pp: ans*=pp
 return ans

def frequency_model(k,a,b):
 d=gcd(a,b);a//=d
 local=[]
 for p in primerange(2,k+1):
  if a%p==0: continue
  E=0;pp=1;C=0
  while pp*p<=k:
   pp*=p;E+=1;C+=(k+1)//pp-1
  digits=[];N=k+1
  for _ in range(E):digits.append(N%p); N//=p
  D={(0,0):1}
  for digit in digits:
   V={}
   for (carry,t),num in D.items():
    for nextcarry,choices in ((0,p-digit-carry),(1,digit+carry)):
     if choices>0:
      key=(nextcarry,t+nextcarry)
      V[key]=V.get(key,0)+num*choices
   D=V
  hist=Counter()
  for (c,t),num in D.items():hist[C+t]+=num
  assert sum(hist.values())==pp
  local.append((p,pp,hist))
 P=period(k,a*d,b)
 dist={d**k:1}
 # local hist: each period pgf probability; multiply counts and divide exceptional (constant) local period factor
 active=[(p,pp,h) for p,pp,h in local if len(h)>1]
 assert prod(pp for p,pp,h in active)==P,(P,active)
 for p,pp,hist in active:
  new={}
  for v,freq in dist.items():
   for exp,count in hist.items(): new[v*p**exp]=new.get(v*p**exp,0)+freq*count
  dist=new
 for p,pp,hist in local:
  if len(hist)==1:
   exp=next(iter(hist))
   dist={v*p**exp:freq for v,freq in dist.items()}
 return dist, P

def direct(k,a,b,n):
 seq=[a*(n+i)+b for i in range(k+1)]
 x=1;L=1
 for y in seq: x*=y;L=lcm(L,y)
 return x//L

for k in range(0,16):
 for a in range(1,9):
  for b in range(0,8):
   P=period(k,a,b)
   if P>10000:continue
   hist,C=frequency_model(k,a,b)
   assert sum(hist.values())==P
   actual=Counter(direct(k,a,b,n) for n in range(1,P+1))
   assert actual==hist, (k,a,b,P,actual,hist)
print('VERIFY_OK tested k=0..15, a=1..8, b=0..7, cases 1024')
for t in [(6,1,0),(10,1,0),(12,2,1),(9,6,2)]:
 k,a,b=t;f,P=frequency_model(*t);print(t,'period',P,'distribution',sorted(f.items()))
