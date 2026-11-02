from math import gcd

def v2(x):
 if x==0:return 999
 a=0
 while x%2==0:x//=2;a+=1
 return a

def odd_period(c,M):
 odd=M//(2**v2(M))
 return odd//gcd(odd,abs(c))

def target(c,M):
 if c==0:return (0,1)
 a=v2(M);d=odd_period(c,M)
 if c%2:
  return (4*a-2 if a else 0,d)
 if a==0:return(0,d)
 t=v2(c)
 if a<=t:q=1
 elif t==1:q=2**max(2,a-1)
 else:q=2**(a-t+1)
 return 0,d*q

def sequence(c,M,L):
 A=[1,1]
 for n in range(2,L):A.append((A[n-1]+c*(n-1)*A[n-2])%M)
 return A

checks=0
for M in range(2,261):
 for c in range(-24,25):
  s,d=target(c,M)
  maxn=s+3*d+30
  A=sequence(c,M,maxn)
  if any(A[n]!=A[n+d] for n in range(s,s+2*d+25)):
   i=next(n for n in range(s,s+2*d+25) if A[n]!=A[n+d]);raise AssertionError((c,M,s,d,'nonperiod',i,A[i],A[i+d]))
  if s:
   # A non-zero at s-1 mod 2^a, so minimal preperiod
   a=v2(M)
   assert A[s-1]%(2**a) !=0,(c,M,s,'preperiod')
  # shortest period, check proper divisors at fixed preperiod
  for h in range(1,d):
   if d%h==0 and all(A[n]==A[n+h] for n in range(s,s+2*d+20)):
    raise AssertionError((c,M,s,d,h,'short'))
  checks+=1
print('GENERAL_GRID_OK',checks,'c -24..24','moduli 2..260')
# Valuation phase check for t>=2 and for t==1
for t in [1,2,3,4,5]:
 for u in [-7,-5,-3,-1,1,3,5,7]:
  c=(2**t)*u
  for r in range(1,10):
   h=2**r;mod=2**(r+t+4)
   A=sequence(c,mod,h+81)
   for n in range(0,80):
    delta=(A[n+h]-A[n])%mod
    if t>=2: assert v2(delta)==r+t-1,(t,u,r,n,v2(delta),r+t-1)
    elif r>=2: assert delta%(2**(r+1))==0,(t,u,r,n,delta)
print('SHIFT_PHASE_OK',5*8*9*80,'checks, exceptions handled')

for a in range(1,13):
 for t in [0,1,2,3,4,5,6]:
  for u in [1,3,5]:
   c=2**t*u
   M=2**a;s,d=target(c,M)
   A=sequence(c,M,s+3*d+12)
   assert all(A[n]==A[n+d] for n in range(s,s+2*d+8)),(a,c,d,'period')
   for h in [d//2,d//4]:
    if h>=1:assert any(A[n]!=A[n+h] for n in range(s,s+2*d+8)),(a,c,h,'minimum')
print('DYADIC_LAYERS_OK',12*7*3,'cases up to 4096')
