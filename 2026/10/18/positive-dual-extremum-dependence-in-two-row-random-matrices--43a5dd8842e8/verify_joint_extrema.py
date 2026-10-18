"""Exact finite rank-permutation verification of simultaneous row/column maxima and minima."""
import itertools
from fractions import Fraction as F
from math import factorial,comb

def rhs(n):
 q=F(factorial(n-1)**2,factorial(2*n))
 cov=F(4*(n*n+4*n+1),n*(n-1)*(n+1)**2*(n+2))-F(2*n*(n+1),n-1)*q
 p=F(n-1,n+1)
 return p,cov

def table(n):
 out={(a,b):0 for a in (1,2) for b in (1,2)}
 for perm in itertools.permutations(range(2*n)):
  kmax=kmin=0
  for r in range(2):
   for c in range(n):
    v=perm[r*n+c]
    row=perm[r*n:(r+1)*n]
    w=perm[(1-r)*n+c]
    kmax+=int(v==max(row) and v>w)
    kmin+=int(v==min(row) and v<w)
  out[(kmax,kmin)]+=1
 return {k:F(v,factorial(2*n)) for k,v in out.items()}

count=0
for n in range(2,5):
 t=table(n)
 p,c=rhs(n)
 want={(2,2):p*p+c,(1,1):(1-p)**2+c,(2,1):p*(1-p)-c,(1,2):p*(1-p)-c}
 assert t==want,(n,t,want)
 assert c>0
 print('exhaustive',n,t,'cov',c)
 count+=4
for n in range(2,150):
 p,c=rhs(n)
 assert 0<c<=p*(1-p),(n,p,c)
 assert (n==2 or c<p*(1-p))
 count+=2
print('PASS',count,'exact checks')
# Independently evaluate the row-sharing/column-sharing/disjoint two-entry integrals
# using finite beta-binomial expansions rather than their simplified formulas.
def pair_integrals(n):
 # P(row shared; 2 rows), direct beta integrals
 sr=F(1,(n-1)*(n+1)*(n+2))+F(1,n*(n+2))
 # P(column shared) from beta integral
 sc=F(1,n*n)-F(factorial(n-1)**2,factorial(2*n))
 # P(disjoint) by integrating (1-y)^(n-2) and (x-y)^2 term by term.
 d=sum(((-1)**j)*comb(n-2,j)*F(2,(j+1)*(j+2)*(j+3)*(n+j+2)) for j in range(n-1))
 return sr,sc,d
for n in range(2,45):
 sr,sc,d=pair_integrals(n)
 p,c=rhs(n)
 e=2*n*((n-1)*sr+sc+(n-1)*d)
 assert e-F(4*n*n,(n+1)**2)==c,(n,e,c)
 count+=1
print('PASS',count,'total exact checks, including independent beta-binomial integrals')
