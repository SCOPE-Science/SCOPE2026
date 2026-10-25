#!/usr/bin/env python3
"""Exact finite certificates for the characteristic classification at index 11.

Python 3 standard library only. No external data; prints certificate and checks.
"""
from math import comb, factorial, gcd

CANDIDATES = (23, 67, 89, 199)
EXPECTED = {
 67: {9: (27, 34), 15: (50, 57), 25: (19,), 59: (65,)},
 89: {2: (43,), 45: (65,)},
 199: {61: (69, 180), 62: (48, 159), 63: (), 139: ()},
}

def bareiss_determinant(M):
 A=[r[:] for r in M]; n=len(A); prev=1; sign=1
 for i in range(n-1):
  if A[i][i]==0:
   j=next((j for j in range(i+1,n) if A[j][i]), None)
   if j is None: return 0
   A[i],A[j]=A[j],A[i];sign=-sign
  pivot=A[i][i]
  for j in range(i+1,n):
   for k in range(i+1,n):
    numerator=A[j][k]*pivot-A[j][i]*A[i][k]
    assert numerator%prev==0
    A[j][k]=numerator//prev
   A[j][i]=0
  prev=pivot
 return sign*A[-1][-1]

def wendt11():
 f=[1]+[0]*10+[-1] # descending for X^11-1
 g=[comb(11,j) for j in range(12)]
 g[-1]-=1 # (X+1)^11 -1
 n=11
 rows=[]
 for i in range(n): rows.append([0]*i+f+[0]*(n-1-i))
 for i in range(n): rows.append([0]*i+g+[0]*(n-1-i))
 return bareiss_determinant(rows)

def p_formula(p,k,x,z):
 """(k-1)!(z-1)^k [w^(k-1)] (1+w)^(x-1)/(z(1+w)^(-1/11)-1) mod p"""
 n=k-1
 T=(-pow(11,-1,p))%p
 A=[1]; B=[1]
 for j in range(1,n+1):
  inv=pow(j,-1,p)
  A.append(A[-1]*(x-j)*inv%p)
  B.append(B[-1]*(T-j+1)*inv%p)
 D=[(z*b-(j==0))%p for j,b in enumerate(B)]
 assert D[0]!=0
 C=[]; inv0=pow(D[0],-1,p)
 for j in range(n+1):
  C.append((A[j]-sum(D[h]*C[j-h] for h in range(1,j+1)))*inv0%p)
 return factorial(n)*pow(z-1,k,p)*C[n]%p

def p_recurrence(p,k,x,z):
 """Independent evaluation of the polynomial recurrence P_k(T,X,Y) at Y=z."""
 T=(-pow(11,-1,p))%p
 pol=[1]
 for h in range(1,k):
  new=[0]*(len(pol)+1)
  A=x-h
  for j,c in enumerate(pol):
   new[j]=(new[j]+(-A-T*j)*c)%p
   new[j+1]=(new[j+1]+(A-h*T+T*j)*c)%p
  pol=new
 return sum(c*pow(z,j,p) for j,c in enumerate(pol))%p

def verify():
 W=wendt11()
 expected=23**5*67**2*89*199**2
 assert W==expected,(W,expected)
 for p in CANDIDATES:
  assert all(p%d for d in range(2,int(p**.5)+1))
 assert expected==W
 print('WENDT_11',W,'=23^5*67^2*89*199^2')
 total=0
 for p in (67,89,199):
  assert (p-1)%11==0
  zvals=tuple(z for z in range(p) if z!=1 and pow(z,11,p)==1 and pow(z-1,11,p) in (1,p-1))
  assert tuple(sorted(zvals))==tuple(sorted(EXPECTED[p]))
  t=(-pow(11,-1,p))%p
  for z in zvals:
   xs=tuple(x for x in range(p) if p_formula(p,11,x,z)==0)
   assert xs==EXPECTED[p][z],(p,z,xs)
   xs_recurrence=tuple(x for x in range(p) if p_recurrence(p,11,x,z)==0)
   assert xs_recurrence==xs,(p,z,xs_recurrence,xs)
   # Independent polynomial-recurrence checks for every potential root.
   for x in xs:
    assert p_recurrence(p,11,x,z)==0
    residues=[]
    for c in (0,1):
     y=(2*x-c*t)%p
     v=p_formula(p,22,y,z)
     assert p_recurrence(p,22,y,z)==v
     assert v!=0,(p,z,x,c)
     residues.append(v)
     total+=1
    print('EXCLUSION',p,z,x,'second_sums',residues)
   if not xs: print('FIRST_SUM_EXCLUSION',p,z)
 print('CERTIFICATE_OK',total,'nonzero second-sum residues')
 assert len({(x*(pow(x,11,23)+2))%23 for x in range(23)})==23
 print('WITNESS_OK x^12+2x permutes F_23')

if __name__=='__main__':verify()
