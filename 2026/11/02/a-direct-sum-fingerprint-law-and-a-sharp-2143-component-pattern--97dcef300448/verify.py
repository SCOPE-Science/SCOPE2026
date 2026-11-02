from fractions import Fraction
from math import comb,factorial
from itertools import permutations,combinations

def cuts(t):
 m=len(t); return {j for j in range(1,m) if set(t[:j])==set(range(1,j+1))}

def formula(n,t):
 m=len(t); D=cuts(t); s=Fraction()
 for k in range(1,n):
  cross=sum(Fraction(comb(k,j)*comb(n-k,m-j),comb(n,k))*(Fraction(1,factorial(j)*factorial(m-j))*(j in D)-Fraction(1,factorial(m))) for j in range(1,m) if j<=k and m-j<=n-k)
  s+=cross
 return s

def brute(n,t):
 m=len(t); s=0; sx=0; sk=0
 for p in permutations(range(1,n+1)):
  x=0
  for inds in combinations(range(n),m):
   seq=[p[i] for i in inds]; pattern=tuple(1+sum(w<z for w in seq) for z in seq)
   x+=(pattern==t)
  k=1+sum(set(p[:j])==set(range(1,j+1)) for j in range(1,n))
  s+=k*x;sx+=x;sk+=k
 den=factorial(n)
 return Fraction(s,den)-Fraction(sx*sk,den*den)

if __name__=='__main__':
 t=(2,1,4,3); tests=0
 for n in range(4,40):
  z=formula(n,t)
  if n<=7:assert z>0,(n,z)
  else:assert z<0,(n,z)
  if n in (4,5,6,7,8,9,10,15,20,39):print('2143',n,z)
  tests+=1
 for m in (2,3,4):
  for t in permutations(range(1,m+1)):
   for n in range(m,min(7,m+3)+1):
    z=formula(n,t); a=brute(n,t)
    assert z==a,(n,t,z,a)
    tests+=1
 print('PASSED',tests,'independent checks')
