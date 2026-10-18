"""Exact checks for coupon absence under independently uniform subset batches."""
from fractions import Fraction as Q
from math import comb
from itertools import product
import sympy as S
cases=0
roots=0
for n in range(2,8):
  options=sorted(set([0,1,2,n//2,n-1,n]) & set(range(n+1)))
  for k in range(1,4):
    for sizes in product(options,repeat=k):
      law={n:Q(1)}
      for s in sizes:
        q=n-s
        out={}
        for x,px in law.items():
          for y in range(max(0,q-(n-x)),min(x,q)+1):
            out[y]=out.get(y,Q(0))+px*Q(comb(x,y)*comb(n-x,q-y),comb(n,q))
        law=out
      assert sum(law.values())==1
      for j in range(n+1):
        lhs=sum(p*comb(x,j) for x,p in law.items() if x>=j)
        rhs=Q(comb(n,j))*Q(1)
        for s in sizes: rhs*=Q(comb(n-j,s),comb(n,s)) if s<=n-j else Q(0)
        assert lhs==rhs,(n,sizes,j,lhs,rhs)
      cases+=1
      if n<=6 and k<=2:
        pol=S.Poly(sum(S.Rational(p.numerator,p.denominator)*S.Symbol('z')**x for x,p in law.items()),S.Symbol('z'))
        if pol.degree()>=1:
          intervals=pol.intervals(eps=S.Rational(1,1000000))
          assert sum(mult for _,mult in intervals)==pol.degree(),(n,sizes,pol)
          assert all(interval[1]<=0 for interval,mult in intervals),(n,sizes,pol)
          roots+=1
print('PASS exact laws and factorial moments:',cases,'; certified real nonpositive-root polynomials:',roots)
