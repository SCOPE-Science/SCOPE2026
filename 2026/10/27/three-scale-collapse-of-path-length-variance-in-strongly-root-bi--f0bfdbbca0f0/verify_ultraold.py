from fractions import Fraction
from itertools import product
from math import isfinite
checks=0
for t in (1,2,3):
 n=6
 w=[Fraction(0)]+[Fraction(1,j**t) for j in range(1,n+1)]
 S=[Fraction(0)]*(n+1)
 for j in range(1,n+1): S[j]=S[j-1]+w[j]
 p=[Fraction(0)]+[w[j]/S[j] for j in range(1,n+1)]
 v=[Fraction(0)]*(n+1)
 for j in range(2,n): v[j+1]=(1-p[j]*p[j])*v[j]+p[j]*(1-p[j])
 predicted=sum((1+(n-j)*p[j])**2*v[j] for j in range(2,n+1))
 mass=Fraction(0); m=Fraction(0); m2=Fraction(0)
 for parents in product(*[range(1,j) for j in range(2,n+1)]):
  dep=[0]*(n+1);prob=Fraction(1)
  for j,k in enumerate(parents,2):dep[j]=dep[k]+1;prob*=w[k]/S[j-1]
  X=sum(dep); mass+=prob;m+=prob*X;m2+=prob*X*X
 assert mass==1 and predicted==m2-m*m
 checks+=1
for t in (2,3,4,5,7,9,11):
 alpha=-t;n=500
 p=[0]*(n+1);v=[0.]*(n+1);W=0.
 for j in range(1,n+1): W+=j**alpha;p[j]=j**alpha/W
 for j in range(2,n):v[j+1]=(1-p[j]*p[j])*v[j]+p[j]*(1-p[j])
 s=sum(p[j]**2*v[j] for j in range(3,n+1))
 approximation=18**alpha+32**alpha-4*36**alpha
 assert s>0 and abs(s-approximation)<4*48**alpha
 checks+=1
print(f'PASS {checks} direct tree enumeration and asymptotic numerical assertions; analytical remainder bound required')
