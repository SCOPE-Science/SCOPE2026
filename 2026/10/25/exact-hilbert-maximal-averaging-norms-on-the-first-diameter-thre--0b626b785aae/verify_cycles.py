#!/usr/bin/env python3
"""Exact integer certificates for sharp cycle maximal-averaging norms."""
from fractions import Fraction
from itertools import combinations, product
DATA=(dict(n=6,denom=30,rep=(0,1,0,1,2,3),split=(1517,1000),lower=(1520400,1000000),upper=(1520401,1000000),f=(699001,181094,1000000,204881,204881,101856),char=[1,-2730,2294900,-629760000,54297000000,-1166400000000,0]),dict(n=7,denom=105,rep=(0,1,2,3,3,2,1),split=(1531,1000),lower=(1532672,1000000),upper=(1532673,1000000),f=(1000000,201666,201666,144076,144076,201666,201666),char=[1,-25935,176610896,-420178361400,275404544100000,0,0,0]))
def determinant(m):
 a=[list(row) for row in m];n=len(a)
 if not n:return 1
 sign,denominator=1,1
 for k in range(n-1):
  if not a[k][k]:
   swap=next((i for i in range(k+1,n) if a[i][k]),None)
   if swap is None:return 0
   a[k],a[swap]=a[swap],a[k];sign=-sign
  pivot=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    numerator=a[i][j]*pivot-a[i][k]*a[k][j]
    assert numerator%denominator==0
    a[i][j]=numerator//denominator
  for i in range(k+1,n):a[i][k]=0
  denominator=pivot
 return sign*a[-1][-1]
def integer_averaging_matrix(n,denom,selector):
 return [[denom//min(2*r+1,n) if min((i-j)%n,(j-i)%n)<=r else 0 for j in range(n)] for i,r in enumerate(selector)]
def gram(matrix):
 n=len(matrix);return [[sum(matrix[k][i]*matrix[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def below(B,denom,numerator,divisor):
 n=len(B);q=[[(denom**2*numerator if i==j else 0)-divisor*B[i][j] for j in range(n)] for i in range(n)]
 return all(determinant([row[:k] for row in q[:k]])>0 for k in range(1,n+1))
def orbit(selector):
 n=len(selector);return {tuple(selector[(direction*i+shift)%n] for i in range(n)) for direction in (-1,1) for shift in range(n)}
def characteristic(B):
 n=len(B);return [1]+[(-1)**k*sum(determinant([[B[i][j] for j in subset] for i in subset]) for subset in combinations(range(n),k)) for k in range(1,n+1)]
def run(d):
 n,denom,rep=d['n'],d['denom'],d['rep'];chosen=orbit(rep)
 assert len(chosen)==(12 if n==6 else 7)
 rejected=0
 for selector in product(range(4),repeat=n):
  if selector in chosen:continue
  B=gram(integer_averaging_matrix(n,denom,selector))
  assert below(B,denom,*d['split']),(n,selector)
  rejected+=1
 assert rejected==4**n-len(chosen)
 U=integer_averaging_matrix(n,denom,rep);B=gram(U)
 assert characteristic(B)==d['char']
 F=d['f'];f2=sum(z*z for z in F);Af2=sum(sum(row[j]*F[j] for j in range(n))**2 for row in U)
 for num,div in (d['split'],d['lower']):assert Af2*div>num*denom**2*f2
 assert below(B,denom,*d['upper'])
 assert all(z>0 for row in B for z in row)
 print('n',n,'CERTIFICATE_OK','selectors',4**n,'winning',len(chosen),'losing',rejected)
 print('characteristic_coefficients',d['char'])
 print('rational_Rayleigh_lower_bound',Fraction(Af2,denom**2*f2))
if __name__=='__main__':
 for d in DATA:run(d)
 print('ALL_CERTIFICATES_OK')
