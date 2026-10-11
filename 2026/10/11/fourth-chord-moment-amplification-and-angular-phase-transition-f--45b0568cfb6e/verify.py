"""Exact symbolic checks for fourth-power independent-point chord moments.

Run: python verify.py
Dependency: SymPy 1.13 or later (2.x compatible).
The universal inequality follows from positive polynomial identities, not sampling.
"""
import sympy as sp

A, B, Z, t = sp.symbols('A B Z t', real=True)
# A=length(a), B=length(b), Z=dot(a,b).
# X=U a+V b has area-uniform law, U,V independent uniform[-1,1].
mi2 = (A**2+B**2)/3
mi4 = (A**4+B**4)/5+(2*A**2*B**2+4*Z**2)/9
tr_ci_sq = (A**4+B**4+2*Z**2)/9
M_I = sp.factor(2*mi4+2*mi2**2+4*tr_ci_sq)

# The boundary is a length-weighted union of the four sides.
p, q = A/(A+B), B/(A+B)
mb2 = p*(B**2+A**2/3)+q*(A**2+B**2/3)
mb4 = p*(B**4+(2*A**2*B**2+4*Z**2)/3+A**4/5) + q*(A**4+(2*A**2*B**2+4*Z**2)/3+B**4/5)
ca, cb = (A/3+B)/(A+B), (A+B/3)/(A+B)
tr_cb_sq = ca**2*A**4+cb**2*B**4+2*ca*cb*Z**2
M_B = sp.factor(2*mb4+2*mb2**2+4*tr_cb_sq)

assert sp.simplify(M_I-8*(6*A**4+5*A**2*B**2+6*B**4+10*Z**2)/45)==0
assert sp.simplify(mb2-(A+B)**2/3)==0
assert sp.simplify(M_B-M_I-8*(24*A**5*B+49*A**4*B**2+30*A**3*B**3+49*A**2*B**4+24*A*B**5+20*A**2*Z**2+60*A*B*Z**2+20*B**2*Z**2)/(45*(A+B)**2))==0

D = sp.factor(sp.Rational(61,17)*M_I-M_B)
D0 = sp.factor(D.subs(Z,0).subs(A,1+t).subs(B,1))
D1 = sp.factor(D.subs(Z,A*B).subs(A,1+t).subs(B,1))
P0 = 264*t**4+1704*t**3+4211*t**2+5014*t+2507
P1 = 88*t**4+216*t**3+221*t**2+10*t+5
assert sp.simplify(D0-8*t**2*P0/(765*(t+2)**2))==0
assert sp.simplify(D1-8*P1/255)==0
assert all(c>0 for c in sp.Poly(P0,t).all_coeffs())
assert all(c>0 for c in sp.Poly(P1,t).all_coeffs())
assert sp.simplify(D.subs({A:1,B:1})-8*Z**2/51)==0
assert sp.simplify(M_I.subs({A:1,B:1,Z:0})-sp.Rational(136,45))==0
assert sp.simplify(M_B.subs({A:1,B:1,Z:0})-sp.Rational(488,45))==0
assert sp.simplify((M_B/M_I).subs({A:1,B:1,Z:0})-sp.Rational(61,17))==0
assert sp.simplify((2*mb2)/(2*mi2)-(A+B)**2/(A**2+B**2))==0
assert sp.limit(sp.factor((M_B/M_I).subs({A:1+t,B:1,Z:0})),t,sp.oo)==1
print('PARALLELOGRAM_FOURTH_CHORD_EXACT_OK')
G = 4*A**6+4*A**5*B-9*A**4*B**2-9*A**2*B**4+4*A*B**5+4*B**6
angular_numerator = sp.diff(M_B,Z)*M_I-sp.diff(M_I,Z)*M_B
assert sp.simplify(angular_numerator-256*Z*G/(135*(A+B)**2))==0
r, v = sp.symbols('r v', real=True)
F = 4*v**3+4*v**2-21*v-8
assert sp.simplify(G.subs(A,r*B)/B**6 - r**3*F.subs(v,r+1/r))==0
assert F.subs(v,2)==-2
assert sp.diff(F,v).subs(v,2)>0
print('PARALLELOGRAM_ANGULAR_PHASE_EXACT_OK')
