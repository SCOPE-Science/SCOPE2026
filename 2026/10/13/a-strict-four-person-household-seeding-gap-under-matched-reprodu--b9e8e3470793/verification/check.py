#!/usr/bin/env python3
"""Exact symbolic checks for matched one-day household transmission models."""
from functools import lru_cache
from math import comb
import sympy as S

p,g,q = S.symbols('p g q', real=True)

def totals(mode, x, household_size=4):
    @lru_cache(None)
    def e(s, i):
        if i == 0:
            return S.Integer(0)
        if s == 0:
            return S.Integer(i)
        hazard = 1-(1-x)**i if mode == 'standard' else x
        return S.expand(i + sum(S.binomial(s,j) * hazard**j
                              * (1-hazard)**(s-j) * e(s-j,j)
                              for j in range(1,s+1)))
    return [S.factor(e(household_size-k,k)) for k in range(household_size+1)]

E_S = totals('standard',p)
E_G = totals('greenwood',g)
assert E_S[0]==E_G[0]==0 and E_S[4]==E_G[4]==4
assert S.simplify(E_S[1]-E_G[1].subs(g,p)-3*p**3*(1-p)**2)==0
assert S.simplify(E_S[2]-E_G[2].subs(g,p)-2*p*(1-p)**2*(1+2*p-p**2))==0
assert S.simplify(E_S[3]-(3+1-(1-p)**3))==0
assert S.simplify(E_G[3]-(3+g))==0

A = E_G[1]
B = E_G[2]
Q4 = 12*g**4-18*g**3+2*g**2+5*g+1
P5 = 12*g**5-30*g**4-4*g**3+18*g**2+8*g+1
P8 = 2*p**8-18*p**7+66*p**6-126*p**5+131*p**4-67*p**3+5*p**2+8*p+1
assert S.simplify(S.diff(A,g)-3*(1-g)*Q4)==0
assert S.simplify(S.diff(B,g)-2*(1-g)*(3*g+1))==0
assert S.simplify((2*(1+2*g-g**2)/(3*g**2)
                   - 2*(3*g+1)/(3*Q4))
                  - 2*(1-g)*P5/(3*g**2*Q4))==0
u=2*p-p**2
assert S.simplify(E_G[1].subs(g,u)-E_S[1]-3*p*(1-p)**3*P8)==0

def bernstein_coeffs(poly,variable):
    poly=S.Poly(poly,variable)
    n=poly.degree()
    cs=[poly.nth(i) for i in range(n+1)]
    return [S.cancel(sum(cs[j]*S.binomial(k,j)/S.binomial(n,j)
                         for j in range(k+1))) for k in range(n+1)]

assert bernstein_coeffs(Q4,g)==[1,S.Rational(9,4),S.Rational(23,6),S.Rational(5,4),2]
assert bernstein_coeffs(P5,g)==[1,S.Rational(13,5),6,S.Rational(54,5),S.Rational(53,5),5]
assert bernstein_coeffs(P8,p)==[1,2,S.Rational(89,28),S.Rational(187,56),S.Rational(221,70),S.Rational(41,14),S.Rational(75,28),S.Rational(19,8),2]

# The total response equals a binomial mixture over k simultaneous seeds.
F_S=S.expand(sum(S.binomial(4,k)*q**k*(1-q)**(4-k)*E_S[k]
                 for k in range(5))/4)
F_G=S.expand(sum(S.binomial(4,k)*q**k*(1-q)**(4-k)*E_G[k]
                 for k in range(5))/4)
assert S.simplify((F_S-F_G)-(S.Rational(3,2)*q**2*(1-q)**2*(E_S[2]-E_G[2])
                                    +q**3*(1-q)*(E_S[3]-E_G[3])
                                    +q*(1-q)**3*(E_S[1]-E_G[1])))==0

# Exact enclosing rationals for the matching Greenwood parameter at p=1/2.
p0=S.Rational(1,2)
lo=S.Rational(525741,1000000)
hi=S.Rational(525742,1000000)
assert E_G[1].subs(g,lo)<E_S[1].subs(p,p0)<E_G[1].subs(g,hi)
assert lo>p0 and hi<2*p0-p0**2
for gg in [lo,hi]:
    ds2=S.simplify(E_S[2].subs(p,p0)-E_G[2].subs(g,gg))
    ds3=S.simplify(E_S[3].subs(p,p0)-E_G[3].subs(g,gg))
    assert ds2>0 and ds3>0
print('VERIFY_OK')
