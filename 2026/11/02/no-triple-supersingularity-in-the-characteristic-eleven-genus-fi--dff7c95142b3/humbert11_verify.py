"""Exact finite-field certificate for the p=11 Humbert supersingularity arrangement.
No nonstandard Python dependencies. All loops are exhaustive in GF(11^2)."""
from math import comb
from collections import Counter
P=11
ZERO=(0,0);ONE=(1,0)
def add(x,y):return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def neg(x):return ((-x[0])%P,(-x[1])%P)
def sub(x,y):return add(x,neg(y))
def mul(x,y):return ((x[0]*y[0]+2*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def power(x,n):
 r=ONE
 while n:
  if n&1:r=mul(r,x)
  x=mul(x,x);n>>=1
 return r
def inv(x):
 assert x!=ZERO
 v=power(x,119)
 assert mul(x,v)==ONE
 return v
def div(x,y):return mul(x,inv(y))
coefs=[comb(5,k)**2%P for k in range(6)]
assert coefs==[1,3,1,1,3,1]
def poly_mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,ai in enumerate(a):
  for j,bj in enumerate(b):c[i+j]=(c[i+j]+ai*bj)%P
 return c
f=[1]
for factor in [[-2,1],[1,1],[5,1],[1,-1,1]]:f=poly_mul(f,factor)
assert f==coefs
assert pow(2,5,P)==-1%P # GF(11^2)=F_11[z]/(z^2-2)
assert all(power((a,b),121)==(a,b) for a in range(P) for b in range(P))
def hasse(x):
 val=ZERO
 for c in reversed(coefs):val=add(mul(val,x),(c,0))
 return val
ALL=[(a,b) for a in range(P) for b in range(P)]
ROOTS=[x for x in ALL if hasse(x)==ZERO]
assert len(ROOTS)==5
assert set(ROOTS)=={(2,0),(6,0),(10,0),(6,1),(6,10)}
# Verify the standard S_3 action preserves supersingularity.
for t in ALL:
 if t in (ZERO,ONE):continue
 assert (hasse(t)==ZERO)==(hasse(sub(ONE,t))==ZERO)
 assert (hasse(t)==ZERO)==(hasse(inv(t))==ZERO)
def five(t,u):
 # Five elliptic quotient cross-ratios; last is S_3-equivalent
 # to v(1-u)/(v-u) in Carvacho--Hidalgo--Quispe (2015), Thm 5.1.
 return [t,u,div(u,t),div(sub(u,ONE),sub(t,ONE)),div(mul(t,sub(u,ONE)),mul(u,sub(t,ONE)))]
def ss_count(u,v):return sum(hasse(r)==ZERO for r in five(u,v))
for u in ROOTS:
 for v in ROOTS:
  if u!=v:assert ss_count(u,v)==2
print('HASSE_POLYNOMIAL_FACTOR_AND_SIMPLE_ROOTS=PASS',coefs)
print('GF121_HASSE_ROOTS',ROOTS)
print('ALL_20_ROOT_PAIRS_HAVE_EXACTLY_TWO_SUPERSINGULAR_QUOTIENTS=PASS')
for ff in [[(i,0) for i in range(P)],ALL]:
 q=len(ff)
 counts=Counter(ss_count(u,v) for u in ff if u not in (ZERO,ONE) for v in ff if v not in (ZERO,ONE,u))
 r=3 if q==11 else 5
 predicted={2:10*r*(r-1),1:5*r*(q-3)-20*r*(r-1),0:(q-2)*(q-3)-5*r*(q-3)+10*r*(r-1)}
 assert all(counts[i]==predicted[i] for i in (0,1,2))
 assert not any(k>=3 for k in counts)
 assert sum(counts.values())==(q-2)*(q-3)
 print('Q',q,'PARAMETER_RANK5_4_3_COUNTS',counts[0],counts[1],counts[2])
print('VERIFY_OK')
