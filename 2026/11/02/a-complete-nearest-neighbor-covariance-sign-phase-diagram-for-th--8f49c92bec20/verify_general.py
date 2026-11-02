#!/usr/bin/env python3
"""Standard-library multivariate polynomial certificate for the all-(p,q,t) claim.

Checks an identity in Q[p,q,t] after explicit positive-denominator clearing.
No random tests, interpolation, numerical tolerance, or external CAS required.
Run: python3 verify_general.py
"""
from fractions import Fraction

class Poly:
    def __init__(self, coeff=None):
        if isinstance(coeff, Poly):
            self.c = dict(coeff.c)
        elif isinstance(coeff, dict):
            self.c = {k: Fraction(v) for k, v in coeff.items() if v}
        else:
            self.c = {} if not coeff else {(0,0,0):Fraction(coeff)}
    def __add__(self, other):
        other = Poly(other)
        z = dict(self.c)
        for key,val in other.c.items():
            z[key] = z.get(key,Fraction(0))+val
        return Poly(z)
    __radd__ = __add__
    def __neg__(self):
        return Poly({k:-v for k,v in self.c.items()})
    def __sub__(self, other):
        return self + -Poly(other)
    def __rsub__(self, other):
        return Poly(other)-self
    def __mul__(self, other):
        other=Poly(other)
        out={}
        for x,a in self.c.items():
            for y,b in other.c.items():
                z=tuple(x[i]+y[i] for i in range(3))
                out[z]=out.get(z,Fraction(0))+a*b
        return Poly(out)
    __rmul__=__mul__
    def __pow__(self, n):
        assert type(n) is int and n>=0
        acc=Poly(1)
        for _ in range(n): acc=acc*self
        return acc
    def __eq__(self,other):
        return self.c==Poly(other).c

p=Poly({(1,0,0):1})
q=Poly({(0,1,0):1})
t=Poly({(0,0,1):1})
Z=1+p+p*q
Na=t+1
Da=(1+p)*((1+p)*t+1)
Nb=q*(q*t+1)
Db=(1+q)*((1+q)*t+1)
D=Da*Db-Na*Nb
Un=Na*((Z-2*p*q)*Db+Nb*(Z-2))
Wn=Nb*((Z-2)*Da+Na*(Z-2*p*q))
A=p**2*q*(q+1)-p*(q**2+4*q+2)-3*q-2

# From generator moments: U=Un/(ZD), W=Wn/(ZD),
# V = ((m2-W)/(1+p)+q(m0-U)/(1+q))/2.
# Multiply Cov(X0,X1) by common positive 2 Z^2 D (1+p)(1+q).
lhs=(-2*Z*(1+p)*(1+q)*Un
     +2*D*(1+p)*(1+q)*(1+p*q)
     -Z*(1+q)*(p*q*D-Wn)
     -Z*q*(1+p)*(D-Un))
rhs=p*(A*t-2*Z)*(1+p)*(1+q)
assert lhs==rhs, {'difference':(lhs-rhs).c}
print('PASS: exact coefficient-by-coefficient identity in Q[p,q,t]')
print('monomials checked:', len(lhs.c | rhs.c),'; numerator coefficient support:',len(rhs.c))
print('denominator positivity follows analytically from D=Da*Db*(1-a*b)>0')
