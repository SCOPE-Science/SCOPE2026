"""Exact finite dual certificate for at least 41 distinct semiprime reciprocals summing to 1."""
from math import isqrt
from fractions import Fraction

M=2000
K=40
T=10**12
LAM=Fraction(29,4000)
MU=(LAM-Fraction(1,M+1))/2
assert LAM>Fraction(1,M+1)

def sieve(n):
 a=bytearray(b'\x01')*(n+1)
 a[:2]=b'\0\0'
 for p in range(2,isqrt(n)+1):
  if a[p]:a[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
 return [p for p in range(2,n+1) if a[p]]

def iceil_div(a,b):
 return -(-a//b)

pr=sieve(M)
byprime={p:[] for p in pr}
D=[]
for i,p in enumerate(pr):
 for q in pr[i+1:]:
  d=p*q
  if d>M:break
  D.append(d)
  byprime[p].append((q,d))
  byprime[q].append((p,d))
assert len(D)==563
penalty=(MU.numerator*T)//MU.denominator
sum_ceil=0
positive=[]
max_dp_states=0
for p,neighbors in byprime.items():
 if not neighbors:continue
 dp=[None]*p
 dp[0]=0
 for q,d in neighbors:
  # w(p,q)= 1/(2pq)-LAM/2 = (1/d-LAM)/2.
  numerator=(LAM.denominator-LAM.numerator*d)*T
  denominator=2*d*LAM.denominator
  wup=iceil_div(numerator,denominator)
  a=pow(q,-1,p)
  new=dp[:]
  for r,v in enumerate(dp):
   if v is None:continue
   j=(r+a)%p
   candidate=v+wup
   if new[j] is None or new[j]<candidate:new[j]=candidate
  dp=new
 good=dp[0]
 bad=max((v for r,v in enumerate(dp) if r and v is not None),default=None)
 Cp=max(good, bad-penalty if bad is not None else good)
 assert Cp>=0
 if Cp>0:positive.append((p,Cp))
 sum_ceil+=Cp
 max_dp_states+=sum(v is not None for v in dp)

# LAM*K + sum(C_p) < 1, verified without floating point.
left= LAM.numerator*K*T + LAM.denominator*sum_ceil
right=LAM.denominator*T
assert left<right,(left,right)
print('VERIFY_OK min_terms_ge_41=yes M=2000 head_denominators=%d primes=%d checked_residue_states=%d lambda=%s mu=%s C_scaled=%d bound_below_one_margin_scaled=%d positive_primes=%d' %
      (len(D),len([p for p,arr in byprime.items() if arr]),max_dp_states,str(LAM),str(MU),sum_ceil,right-left,len(positive)))
print('exact_certified_upper=',Fraction(left,right))
print('positive_prime_contributions=',positive)
