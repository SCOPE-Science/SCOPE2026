"""Standalone symbolic and numerical diagnostics for the capacity-normalized GAL flip theorem.
Run: python verify.py . Requires sympy; optional: standard Python math.
These checks supplement, but do not replace, the analytic proof in RESULT.md.
"""
import math
import sympy as sp

x, A, m, r = sp.symbols('x A m r')
f = r*x*(1-x)*(A+m*x)
q = (1-x)*(A+m*x)
g = x*q
assert sp.expand(sp.diff(f,x,2)+2*r*(A+3*m*x-m)) == 0
assert sp.expand(sp.diff(f,x,3)+6*r*m) == 0
assert sp.cancel((1+x*sp.diff(q,x)/q+1)*q - (2*q+x*sp.diff(q,x))) == 0
assert sp.expand(2*q+x*sp.diff(q,x) - (A*(2-3*x)+m*x*(3-4*x))) == 0
assert sp.expand(sp.diff(g,x) - (A*(1-2*x)+m*x*(2-3*x))) == 0

u,c,v = sp.symbols('u c v',real=True)
sc=(2*c-1)/(4*c-3*c*c-1)
su=(3*u-2)/(2*(2*u-1)*(1-u))
T=u*u*(2*u-1)/(3*u*u-3*u+1)
Q=12*u**4-24*u**3+22*u**2-12*u+3
expected=u*Q/(2*(2*u-1)*(2*u**2-2*u+1)*(6*u**3-6*u**2+3*u-1))
assert sp.factor(su-sc.subs(c,T)-expected)==0
assert sp.factor(Q.subs(u,sp.Rational(2,3)+v) -
    (12*v**4+8*v**3+6*v**2-sp.Rational(4,9)*v+sp.Rational(1,27))) == 0
up=sp.factor(1/sp.diff(su,u))
assert sp.factor(up-2*(1-u)**2*(2*u-1)**2/(6*u**2-8*u+3))==0
Kc=1-su+su*c;Ku=1-su+su*u
Dlog=sp.factor((c-u)/(Kc*Ku)+2*up/u)
Dcomp=-4*(u-1)*(2*u-1)**2*(-3*c*u*u+3*c*u-c+2*u**3-u*u)/(
    u*(6*u*u-8*u+3)*(-3*c*u+2*c+4*u*u-3*u))
assert sp.factor(Dlog-Dcomp)==0

# Exact rational tests of transformed curve identity and endpoint ratios.
for S in [sp.Rational(1,10),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(9,10)]:
 a=1-S;b=S
 cf=((b-a)+sp.sqrt((b-a)**2+3*b*a))/(3*b)
 uf=(3*(b-a)+sp.sqrt(9*(b-a)**2+32*b*a))/(8*b)
 assert abs(float(sp.N(sc.subs(c,cf)-S,40))) < 1e-30
 assert abs(float(sp.N(su.subs(u,uf)-S,40))) < 1e-30
 assert float(cf)>float(T.subs(u,uf))
 ratio=float(sp.N((cf*(1-cf)*(a+b*cf))/((1-uf)*(a+b*uf)),40))
 assert .75<ratio<64/81
 assert abs(float(sp.N((2-3*uf)*a+b*uf*(3-4*uf),40)))<1e-30

assert sp.Rational(1,4)/sp.Rational(1,3)==sp.Rational(3,4)
assert sp.Rational(4,27)/sp.Rational(3,16)==sp.Rational(64,81)

# Optional numerical diagnostic: shape monotonicity, distinguished maxima, negative flip slope.
previous=.75
for i in range(1,1000):
 S=i/1000;a=1-S;b=S
 cf=((b-a)+math.sqrt((b-a)**2+3*b*a))/(3*b)
 uf=(3*(b-a)+math.sqrt(9*(b-a)**2+32*b*a))/(8*b)
 ratio=cf*(1-cf)*(a+b*cf)/((1-uf)*(a+b*uf))
 assert .5<cf<2/3 and 2/3<uf<.75
 assert ratio>previous-2e-12 and ratio<64/81
 previous=ratio
print('PASS: polynomial identities, analytic monotonicity reduction, endpoints, 5 exact algebraic samples, 999 numerical diagnostics')
