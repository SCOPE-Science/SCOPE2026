#!/usr/bin/env python3
"""Exact checks for three-leader split-network coherence thresholds."""
from fractions import Fraction
from itertools import combinations
import sympy as S

p,q,a,P,Q=S.symbols('p q a P Q', integer=True, positive=True)
F=(p-a-1)/(p+q)+(q-4+a)/p+(p+q+a)/(3*p+a*(q-3)+a*a)

def diff(i,j): return S.factor(F.subs(a,i)-F.subs(a,j))

def check_identity(lhs,rhs):
    assert S.cancel(lhs-rhs)==0

check_identity(diff(2,3), (p-6)*(q-1)/(3*p*(3*p+2*q-2)))
check_identity(diff(3,0), -(p*q-3*p+q*q-9*q)/(3*p*(p+q)))
N02=p*p*q-4*p*p+2*p*q*q-14*p*q+q**3-7*q*q+6*q
N12=p**3*q-3*p**3+2*p*p*q*q-12*p*p*q+2*p*p+p*q**3-9*p*q*q+14*p*q-2*q**3+6*q*q-4*q
check_identity(diff(0,2),2*N02/(3*p*(p+q)*(3*p+2*q-2)))
check_identity(diff(1,2),N12/(p*(p+q)*(3*p+q-2)*(3*p+2*q-2)))
check_identity(S.expand(N02.subs({p:P+4,q:Q+7})),P**2*(Q+3)+P*(2*Q**2+22*Q+24)+Q**3+22*Q**2+127*Q+90)
check_identity(S.expand(N12.subs({p:P+4,q:Q+7})),P**3*(Q+4)+P**2*(2*Q**2+28*Q+64)+P*(Q**3+28*Q**2+211*Q+320)+2*Q**3+44*Q**2+246*Q+92)

cases={
3:{1:2*(p+15)/(3*(p+3)*(3*p+1)),2:2*(p*p+24*p+18)/(3*p*(p+3)*(3*p+4)),3:6/(p*(p+3))},
4:{1:(p*p+32*p-8)/(3*p*(p+4)*(3*p+2)),2:16*(p+1)/(3*p*(p+2)*(p+4)),3:-(p-20)/(3*p*(p+4))},
5:{1:10*(p-1)/(3*p*(p+1)*(p+5)),2:-2*(p*p-20*p-20)/(3*p*(p+5)*(3*p+8)),3:-2*(p-10)/(3*p*(p+5))},
6:{1:-(p*p-24*p+72)/(3*p*(p+6)*(3*p+4)),2:-4*(p-6)/(3*(p+6)*(3*p+10)),3:-(p-6)/(p*(p+6))}}
for v,terms in cases.items():
 for i,rhs in terms.items(): check_identity(diff(i,0).subs(q,v),rhs)
for v,terms in ({
4:{1:2*(p-8)*(2*p+3)/(3*p*(p+4)*(3*p+2)),2:(p-6)/(3*p*(p+2))},
5:{1:2*(p*p-4*p-15)/(3*p*(p+1)*(p+5)),2:4*(p-6)/(3*p*(3*p+8))},
6:{1:2*(4*p*p-9*p-72)/(3*p*(p+6)*(3*p+4)),2:5*(p-6)/(3*p*(3*p+10))}}
 ).items():
 for i,rhs in terms.items(): check_identity(diff(i,3).subs(q,v),rhs)


def fraction_f(r,s,k):
 u=r-k; v=s-3+k
 if v==0: return Fraction(u-1,r+s)+Fraction(1,s+k)
 return Fraction(u-1,r+s)+Fraction(v-1,r)+Fraction(r+s+k,3*r+k*(s-3)+k*k)

def optimizers(r,s):
 if s==3:return [0]
 if s==4:return [0] if r<20 else ([0,3] if r==20 else [3])
 if s==5:return [0] if r<10 else ([0,3] if r==10 else [3])
 if s==6:return [0] if r<6 else ([0,2,3] if r==6 else [3])
 return [2] if r<6 else ([2,3] if r==6 else [3])
count=0
for r in range(4,261):
 for s in range(3,181):
  vals=[fraction_f(r,s,k) for k in range(4)]
  actual=[k for k,v in enumerate(vals) if v==min(vals)]
  assert actual==optimizers(r,s), (r,s,actual,optimizers(r,s))
  count+=1

# Independent exact Laplacian inverses for small graphs and *all* leader allocations.
matrices=0
for r in range(4,9):
 for s in range(3,10):
  n=r+s
  L=S.zeros(n,n)
  for i in range(n):
   for j in range(i+1,n):
    if i<r or j<r:
     L[i,i]+=1; L[j,j]+=1; L[i,j]-=1; L[j,i]-=1
  for k in range(4):
   leaders=set(range(k))|set(range(r,r+3-k))
   followers=[i for i in range(n) if i not in leaders]
   M=L.extract(followers,followers)
   exact=S.trace(M.inv())
   assert exact==fraction_f(r,s,k),(r,s,k,exact,fraction_f(r,s,k))
   matrices+=1
print('VERIFY_OK symbolic_identities=24 parameter_pairs=%d independent_laplacian_inverses=%d'%(count,matrices))
