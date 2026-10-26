"""Reproducible algebra for the sharp quadratic Bergman fourth moment.

Requires Python 3 and sympy; numpy is optional for numerical sampling.
Every limiting claim rests on the analytical derivation in RESULT.md.
"""
import math
import random
import sympy as S

s, r, k = S.symbols('s r k', real=True)
U = 1 + s**2/S.Integer(3)
B = 2 + 4*s/S.Integer(3) + s**2
C = 1 + 4*s**2/S.Integer(3) + s**4/S.Integer(5)
J = (r**2/S.Integer(3) + B*r + C)/(U + r/S.Integer(2))**2
rs = 2*(6*s**4+20*s**3+15*s**2+60*s+45)/(5*(5*s**2+12*s+6))
F = 9*(11*s**4+40*s**3+60*s**2+80*s+40)/(43*s**4+120*s**3+150*s**2+360*s+225)
p = 4*s**3+5*s**2-35*s-30
assert S.simplify(S.diff(J,r)*(U+r/S.Integer(2))**3 - ((S.Rational(2,3)*U-B/S.Integer(2))*r+B*U-C)) == 0
assert S.simplify(S.diff(J,r).subs(r,rs)) == 0
assert S.simplify(J.subs(r,rs)-F)==0
assert S.simplify(S.diff(F,s) - (-180*(s+1)*(5*s**2+12*s+6)*p/(43*s**4+120*s**3+150*s**2+360*s+225)**2)) == 0
assert S.simplify(rs-s-3-3*s*p/(5*(5*s**2+12*s+6)))==0
assert S.simplify(S.resultant(p,k*(43*s**4+120*s**3+150*s**2+360*s+225)-9*(11*s**4+40*s**3+60*s**2+80*s+40),s) - (-2293875*(19070*k**3-110975*k**2+206145*k-122472))) == 0
assert S.limit(F,s,S.oo)==S.Rational(99,43)
assert F.subs(s,0)==S.Rational(8,5)

ss = 2.81133480627639311155
kk = 2.67977554220761442903
assert abs(float(p.subs(s,ss)))<2e-13
assert abs(float(F.subs(s,ss))-kk)<2e-13
assert abs(float(rs.subs(s,ss))-(ss+3))<1e-12
assert abs(19070*kk**3-110975*kk**2+206145*kk-122472)<1e-7

rng=random.Random(20261023)
def ratio(a,b,c):
    f2=[a*a,2*a*b,b*b+2*a*c,2*b*c,c*c]
    n4=sum(abs(t)**2/(j+1) for j,t in enumerate(f2))
    n2=abs(a)**2+abs(b)**2/2+abs(c)**2/3
    return n4/(n2*n2)
for j in range(2500):
    a=complex(rng.gauss(0,1),rng.gauss(0,1))
    b=complex(rng.gauss(0,1),rng.gauss(0,1))
    c=complex(rng.gauss(0,1),rng.gauss(0,1))
    assert ratio(a,b,c)<=kk+1e-12
assert abs(ratio(1, math.sqrt(3+ss), ss)-kk)<1e-13
print('PASS 8 exact symbolic checks, 4 numerical critical checks, 2500 deterministic complex trials.')
print('s* =',repr(ss),'K =',repr(kk),'fourth-root =',repr(kk**.25))
