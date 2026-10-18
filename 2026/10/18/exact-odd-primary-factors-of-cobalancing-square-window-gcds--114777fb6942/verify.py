from math import gcd

def pell_pair_mul(x,y,p):return ((x[0]*y[0]+2*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def pell_pair_pow(k,p):
 ans=(1,0);a=(3%p,2%p)
 while k:
  if k&1:ans=pell_pair_mul(ans,a,p)
  a=pell_pair_mul(a,a,p);k//=2
 return ans

def factors(n):
 d=2
 while d*d<=n:
  if n%d==0:
   a=0
   while n%d==0:n//=d;a+=1
   yield d,a
  d+=1
 if n>1:yield n,1

N=750
u=[0,0]
for _ in range(2,N+10):u.append(6*u[-1]-u[-2]+1)
prefix=[0]
for x in u:prefix.append(prefix[-1]+x*x)
for k in range(1,N+1):
 g=0
 for n in range(5):g=gcd(g,prefix[n+k+2]-prefix[n+2]) # window i 1..k when n=0
 odd=g
 while odd%2==0:odd//=2
 expected=1
 for p,a in factors(k):
  if p==2:continue
  if p==5:continue
  if pell_pair_pow(k,p)==(1,0):expected*=p**a
 if k%6==0:
  a=0;t=k
  while t%5==0:a+=1;t//=5
  expected*=5**(a+1)
 if odd!=expected:
  print('FAIL',k,'got',odd,'expected',expected,'G',g)
  break
else:print('PASS oddpart for',N,'lengths. Selected: ',[(k,(lambda g:g//(g&-g))(gcd(*[prefix[i+k+2]-prefix[i+2] for i in range(5)]))) for k in (6,12,21,42,60,84,120,147,205,300,420,600)])
