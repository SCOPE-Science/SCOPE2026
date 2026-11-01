"""Symbolic and numerical reproducibility checks for the stated return-map identities.

Requires Python 3 and SymPy (tested with SymPy 1.13+). Finite numerical checks
supplement, and do not establish, the interval-wide phase classification.
"""
from fractions import Fraction
from math import sqrt
import sympy as S

u,k,c,v = S.symbols('u k c v', real=True)
G = 1-2*c*(1-2*k*u**2)**2
P = S.expand(G-u)
C = (1-u)/(2*(1-2*k*u**2)**2)

# Conditional return to the left half, with u=1-2x.
x,a = S.symbols('x a', real=True)
left = 1-(1-a)*(1-2*x)**2
right_at_left = c*(2*left-1)**2
assert S.simplify(1-2*right_at_left-G.subs({k:1-a,u:1-2*x})) == 0

# Exact quotient-derivative, fold locus, and codimension-two cusp.
assert S.simplify(S.diff(C,u) - (-1+8*k*u-6*k*u**2)/(2*(1-2*k*u**2)**3)) == 0
foldk = 1/(2*u*(4-3*u))
foldc = (4-3*u)**2/(32*(1-u))
assert S.simplify(C.subs(k,foldk)-foldc) == 0
assert S.simplify(foldk.subs(u,S.Rational(2,3))-S.Rational(3,8)) == 0
assert S.simplify(foldc.subs(u,S.Rational(2,3))-S.Rational(3,8)) == 0
assert S.simplify(P.subs({k:S.Rational(3,8),c:S.Rational(3,8)}) + (u+2)*(3*u-2)**3/64) == 0
assert S.expand(G.subs({k:S.Rational(3,8),c:S.Rational(3,8),u:S.Rational(2,3)+v})-S.Rational(2,3)) == v-S.Rational(9,8)*v**3-S.Rational(27,64)*v**4
assert S.simplify(foldc.subs(u,S.Rational(8,9))-S.Rational(1,2)) == 0
assert S.simplify(foldk.subs(u,S.Rational(8,9))-S.Rational(27,64)) == 0

# An exact bistable example: three admissible roots, outer multipliers 1/2.
kw,cw = S.Rational(7,16),S.Rational(7,16)
Pw = S.factor(P.subs({k:kw,c:cw}))
assert S.simplify(Pw+(7*u**2+8*u-8)*(49*u**2-56*u+8)/512)==0
rlo=(4-2*S.sqrt(2))/7
rmid=(-4+6*S.sqrt(2))/7
rhi=(4+2*S.sqrt(2))/7
assert all(S.simplify(Pw.subs(u,r))==0 for r in [rlo,rmid,rhi])
assert all(0<float(r)<1 for r in [rlo,rmid,rhi])
assert S.simplify(S.diff(G,u).subs({k:kw,c:cw,u:rlo})-S.Rational(1,2))==0
assert S.simplify(S.diff(G,u).subs({k:kw,c:cw,u:rhi})-S.Rational(1,2))==0
assert float(S.diff(G,u).subs({k:kw,c:cw,u:rmid}))>1

# Exact-root counting across rational sample parameters, avoiding fold equality
# except at the specified cusp. sturm count_roots counts roots in the interval.
count=0
for ka in [S.Rational(j,200) for j in range(5,100,3)]:
    for cc in [S.Rational(j,200) for j in range(3,100,4)]:
        Q=S.Poly(P.subs({k:ka,c:cc}),u,domain='QQ')
        actual=Q.count_roots(S.Rational(0),S.Rational(1))
        if ka<=S.Rational(3,8):
            expected=1
        else:
            delta=S.sqrt(4-S.Rational(3,2)/ka)
            ul=(2-delta)/3
            uh=(2+delta)/3
            cl=(4-3*ul)**2/(32*(1-ul))
            ch=(4-3*uh)**2/(32*(1-uh))
            cc_f=float(cc)
            if abs(cc_f-float(cl))<1e-10 or abs(cc_f-float(ch))<1e-10:
                continue
            expected=3 if float(cl)<cc_f<float(ch) else 1
        assert actual==expected,(ka,cc,actual,expected)
        count+=1

# Numerical diagnostics for the parabolic rate on both sides of the cusp.
for u0 in [0.1,0.9]:
    x0=float(u0)
    for _ in range(250000):
        x0=1-0.75*(1-0.75*x0*x0)**2
    observed=(x0-2/3)*sqrt(250000)
    expected=(-1 if u0<2/3 else 1)*2/3
    assert abs(observed-expected)<0.002,(u0,observed,expected)

print('PASS: return conjugacy, fold, cusp, exact three two-cycle witness,',count,'rational parameter samples, critical-rate diagnostics')
