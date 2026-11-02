"""Exact-algebra consistency checks for the B3 symmetry-fiber theorem.

Run with Python 3.10+ and sympy. These checks supplement the proof;
they do not replace the interval-sign arguments in RESULT.md.
"""
from math import comb, cos, pi, sqrt
import sympy as S

x,y,t=S.symbols('x y t',real=True)
check=0

def same(a,b):
    global check
    assert S.simplify(a-b)==0,(a,b)
    check+=1

# Centered order-three B spline: pair samples for x_fiber=1/2.
a=(3-x*x)/4
b=(3-3*x)**2/8
c=(3-5*x)**2/8
d=(3-7*x)**2/8
P=S.expand(a+b*(4*y-3)+c*(16*y*y-20*y+5)+d*(64*y**3-112*y*y+56*y-7))
Q=S.expand(a+b*(4*y-3)+c*(16*y*y-20*y+5))
L=S.expand(a+b*(4*y-3))
for i,value in enumerate([-(247*x*x-198*x+39)/8,
                           3*(95*x*x-76*x+15),
                           -12*(53*x*x-44*x+9),
                           8*(7*x-3)**2]):
    same(P.coeff(y,i),value)
same(S.factor(S.discriminant(P,y)),81*(3*x-1)**4*(48621*x**4-95084*x**3+67662*x*x-20844*x+2349))
same(P.subs(y,1),3*(27*x*x-30*x+11)/8)
same(P.subs(y,S.Rational(1,4)),3*(3*x-1)**2/4)
same(P.subs(x,S.Rational(1,3)),(4*y-1)**3/18)
crit=(99-2*S.sqrt(42))/247
same(P.subs({x:crit,y:0}),0)
same(S.diff(P,y).subs({x:crit,y:0}),(594-12*S.sqrt(42))/3211)
assert S.Rational(1,3)<crit<S.Rational(3,7);check+=1

# A polynomial negative throughout a segment if all its Bernstein
# coefficients in that segment are negative.
def bernstein_coeffs(expr,low,high):
    f=S.Poly(S.expand(expr.subs(x,low+(high-low)*t)),t)
    n=f.degree()
    cc=[f.nth(i) for i in range(n+1)]
    return [S.factor(sum(cc[j]*S.Rational(comb(k,j),comb(n,j))
                         for j in range(k+1))) for k in range(n+1)]

D4=48621*x**4-95084*x**3+67662*x*x-20844*x+2349
b4=bernstein_coeffs(D4,S.Rational(1,3),S.Rational(3,7))
assert b4==[-S.Rational(64,27),-S.Rational(1472,189),-S.Rational(832,147),-S.Rational(864,343),-S.Rational(2160,2401)]
assert all(z<0 for z in b4);check+=2
same(Q.coeff(y,0),3*(2*x-1)**2)
same(Q.coeff(y,1),-2*(29*x*x-33*x+9))
same(Q.coeff(y,2),2*(5*x-3)**2)
same(S.discriminant(Q,y),4*(241*x**4-594*x**3+525*x*x-198*x+27))
D2=241*x**4-594*x**3+525*x*x-198*x+27
b2=bernstein_coeffs(D2,S.Rational(3,7),S.Rational(23,50))
assert b2==[-S.Rational(135,2401),-S.Rational(1773,34300),-S.Rational(10469,245000),-S.Rational(53811,1750000),-S.Rational(105719,6250000)]
assert all(z<0 for z in b2);check+=2
# On 23/50 <= x <= 3/5, the Q-linear coefficient is positive:
# 29x^2 - 33x +9 <0 throughout, as convex quadratic with negative endpoints.
assert (29*x*x-33*x+9).subs(x,S.Rational(23,50))<0
assert (29*x*x-33*x+9).subs(x,S.Rational(3,5))<0
check+=2
same(L.coeff(y,0),(-29*x*x+54*x-21)/8)
same(L.coeff(y,1),4*b)
assert ((-29*x*x+54*x-21)/8).subs(x,S.Rational(3,5))>0
assert ((-29*x*x+54*x-21)/8).subs(x,S.Integer(1))>0
check+=2

# Supplemental sampled verification of zero counts for 1/3 < lambda < 1:
import numpy as np

def bthree(v):
    v=abs(v)
    if v<=.5:return .75-v*v
    if v<1.5:return .5*(1.5-v)**2
    return 0.

def zeros_by_trig(lam):
    coeff=[bthree(lam*(j+.5)) for j in range(4)]
    ff=lambda nu:sum(coeff[j]*cos((2*j+1)*pi*nu) for j in range(4))
    grid=np.linspace(1e-5,.49999,801)
    return sum(ff(u)*ff(v)<0 for u,v in zip(grid[:-1],grid[1:]))
for lam in [0.334,0.337,0.34,0.345,0.348,0.349,0.355,0.36,0.4,0.43,0.48,0.5,0.55,0.6,0.75,0.99]:
    observed=zeros_by_trig(lam)
    expected=int(lam<float(crit))
    assert observed==expected,(lam,observed,expected)
    check+=1
print('CHECK_OK',check)
