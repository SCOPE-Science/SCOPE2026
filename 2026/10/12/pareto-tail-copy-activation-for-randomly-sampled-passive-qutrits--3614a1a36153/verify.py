"""Finite consistency checks for equal-gap qutrit activation-volume analysis."""
from itertools import product
from fractions import Fraction
from math import log
from scipy.integrate import quad

def enumerated_passivity(p,N):
    # Exhaust all product computational basis populations for this finite N.
    min_weight_by_E = {}
    max_weight_by_E = {}
    for w in product(range(3),repeat=N):
        E=sum(w)
        v=Fraction(1)
        for i in w: v*=p[i]
        min_weight_by_E[E]=min(v,min_weight_by_E.get(E,v))
        max_weight_by_E[E]=max(v,max_weight_by_E.get(E,v))
    return all(min_weight_by_E[k]>=max_weight_by_E[k+1] for k in range(2*N))

def wedge(p,N):
    a=log(float(p[0]/p[1])); b=log(float(p[1]/p[2]))
    return (a+b)+1e-13>=N*abs(a-b) if N%2 else (a+b)+1e-13 >= (N-1)*abs(a-b)

cases=0
for N in range(1,9):
 for x in range(2,10):
  for y in range(2,8):
   p=(Fraction(x*x*y, x*x*y+x*y+1),Fraction(x*y,x*x*y+x*y+1),Fraction(1,x*x*y+x*y+1))
   got=enumerated_passivity(p,N)
   a=log(float(p[0]/p[1])); b=log(float(p[1]/p[2]))
   M=N if N%2 else N-1
   # tolerance away from exact boundary only
   if abs(a+b-M*abs(a-b))>1e-10:
    assert got==wedge(p,N),(p,N,got)
   cases+=1

def tail(m):
    return 6*quad(lambda u: (1+u+u**(2+1/m))**-2-(1+u+u**(2-1/(m+1)))**-2,0,1,epsabs=1e-12)[0]
C=24*quad(lambda u: -u*u*log(u)/(1+u+u*u)**3,0,1,epsabs=1e-12)[0]
assert 0.52<C<0.53
assert tail(10000)*10000/C>0.999
print('VERIFY_OK finite_tensor_cases='+str(cases)+' tail_at_3='+str(tail(1))+' tail_at_5='+str(tail(2))+' constant='+repr(C)+' 10000_scaled='+repr(tail(10000)*10000))
