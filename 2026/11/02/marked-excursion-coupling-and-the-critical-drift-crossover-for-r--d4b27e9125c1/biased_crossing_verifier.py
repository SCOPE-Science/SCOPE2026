"""Exact rational checks for biased Bernoulli-walk return and crossing identities."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
from math import comb
import sympy as sp
x=sp.symbols('x')
checks=0
for p in (F(1,3),F(2,5),F(3,4),F(1,2)):
    q=1-p
    # Coefficients of claimed joint pgf via truncated formal series
    for m in range(0,6):
        n=2*m+1
        by_abs=defaultdict(lambda: defaultdict(F))
        joint=defaultdict(F)
        for bits in product((-1,1),repeat=n):
            s=[0]
            for z in bits: s.append(s[-1]+z)
            k=sum(s[t]==0 for t in range(2,n,2))
            c=sum(s[t-1]*s[t+1]<0 for t in range(1,n))
            weight=p**sum(z==1 for z in bits)*q**sum(z==-1 for z in bits)
            by_abs[tuple(abs(a) for a in s)][c]+=weight
            joint[k,c]+=weight
        assert sum(joint.values())==1
        checks+=1
        for profile,vals in by_abs.items():
            k=sum(profile[t]==0 for t in range(2,n,2))
            mass=sum(vals.values())
            for c in range(k+1):
                assert vals[c]==mass*F(comb(k,c),2**k),(p,m,profile,c,vals[c],mass)
                checks+=1
        # independent recurrence of joint laws from explicit first-return distribution
        # F_p(x) = 1 - sqrt(1-4pqx), Q=(1-F)/(1-x)
        xx=sp.symbols('xx')
        fp=1-sp.sqrt(1-4*sp.Rational(p.numerator,p.denominator)*sp.Rational(q.numerator,q.denominator)*xx)
        qp=(1-fp)/(1-xx)
        for k in range(m+1):
            pgk=sp.expand(sp.series(fp**k*qp,xx,0,m+1).removeO()).coeff(xx,m)
            exact=F(int(sp.numer(pgk)),int(sp.denom(pgk)))
            assert sum(joint[k,c] for c in range(k+1))==exact,(p,m,k)
            checks+=1
            for c in range(k+1):
                assert joint[k,c]==exact*F(comb(k,c),2**k)
                checks+=1
print('PASS biased exact arithmetic assertions:',checks)
