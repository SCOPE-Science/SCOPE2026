"""Exact symbolic consistency checks for the two-player lottery-contest return map.

Run: python verify.py (requires sympy; see requirements.txt).
All universal parameter assertions are established analytically in RESULT.md;
this file verifies core polynomial identities and an exact witness.
"""
import sympy as s
c, S = s.symbols('c S', positive=True, real=True)
P = 2*c*S**2 - (1+c)*S + 1
Delta = c**2 - 6*c + 1
assert s.factor(s.discriminant(P,S)-Delta)==0
assert s.simplify(P.subs(S,2/(1+c))+Delta/(1+c)**2)==0
assert s.factor( (-(1-c)**2/(4*c)+1)*4*c - (6*c-c*c-1) )==0
# An exact positive period-two witness in the open interval (4/25,3-2sqrt(2)).
C=s.Rational(1,6)
R=s.sqrt(10)
u=s.Rational(99,160)-9*R/80
v=s.Rational(99,160)+9*R/80
a=s.Rational(21,160)+3*R/80
b=s.Rational(21,160)-3*R/80
assert all(bool(s.N(z,30)>0) for z in (u,v,a,b))
assert bool(s.N(v,30)<1) and bool(s.N(a,s.Integer(30))<s.Rational(1,4))
assert s.simplify((a+u)**2-u)==0
assert s.simplify((b+v)**2-v)==0
assert s.simplify(C*(a+v)**2-a)==0
assert s.simplify(C*(b+u)**2-b)==0
assert s.simplify(a+b+u+v-s.Rational(3,2))==0
D1u=1/(2*(a+u))-1
D1v=1/(2*(b+v))-1
D2a=1/(2*C*(a+v))-1
D2b=1/(2*C*(b+u))-1
mult=s.simplify(D1u*D2a*D1v*D2b)
assert mult==s.Rational(43,243),mult
assert s.simplify(P.subs({c:C,S:s.Rational(3,2)}))==0
print('PASS: polynomial, discriminant, threshold and all four best-response equations')
print('PASS: exact primitive period-two witness at c=1/6; multiplier = 43/243')
print('LIMIT: no finite computation establishes the universal convergence theorem; see analytic proof and Coppel theorem')
