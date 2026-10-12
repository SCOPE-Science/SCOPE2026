#!/usr/bin/env python3
"""Exact-arithmetic checks for a two-worker coupled-compression gradient-memory model.

Requires Python 3 and SymPy. Running this program checks algebraic identities and
finite histories. The infinite-horizon proof is given separately in RESULT.md.
"""
from fractions import Fraction
import sympy as sp

q,t,z=sp.symbols('q t z')
half=sp.Rational(1,2)
M={}
for a,b in [(0,0),(0,1),(1,0),(1,1)]:
    M[a,b]=sp.Matrix([[1-a-b,sp.Rational(a,1)-half,sp.Rational(b,1)-half],
                        [a,1-a,0],[b,0,1-b]])
weights={(0,0):q,(0,1):half-q,(1,0):half-q,(1,1):q}
X,U,H,V=sp.symbols('X U H V')
S=sp.Matrix([[X,U,U],[U,H,V],[U,V,H]])
Snew=sp.zeros(3)
for key in M:
    Snew += weights[key]*M[key]*S*M[key].T
coords=[(0,0),(0,1),(1,1),(1,2)]
T=sp.Matrix([[sp.expand(Snew[i,j]).coeff(var) for var in (X,U,H,V)] for (i,j) in coords])
T_expected=sp.Matrix([[2*q,-4*q,half,2*q-half],
                      [-q,2*q,-sp.Rational(1,4),sp.Rational(1,4)-q],
                      [half,0,half,0],
                      [q,1-2*q,0,q]])
assert T==T_expected
assert sp.simplify((sp.eye(4)-T).det()-(1-10*q)/8)==0
char_expected=z*(8*z**3-(40*q+4)*z**2+(36*q-4)*z+1-6*q)/8
assert sp.expand(T.charpoly(z).as_expr()-char_expected)==0
F=sp.factor((sp.eye(4)-t*T).inv()[0,0])
F_expected=(t-2)**2*((6*q-1)*t-2)/((6*q-1)*t**3+(4-36*q)*t**2+(4+40*q)*t-8)
assert sp.cancel(F-F_expected)==0
assert sp.factor(((1-t)*F).subs(q,sp.Rational(1,10)).limit(t,1))==sp.Rational(6,19)
# Exact Schur reduction: the nonzero eigenvalues solve z^3+a*z^2+b*z+c.
a=-5*q-half
b=sp.Rational(9,2)*q-half
c=(1-6*q)/8
A=1-c*c
B=a-c*b
C=b-c*a
assert sp.simplify(A+B+C-(6*q+7)*(1-10*q)/64)==0
assert sp.simplify(A-B+C-3*(3-2*q)*(82*q+7)/64)==0
assert sp.simplify(A-C-(204*q*q-292*q+91)/64)==0
assert sp.simplify(A+C-(-276*q*q+316*q+35)/64)==0
# Full independent enumeration of exact finite histories (as opposed to only
# iterating the covariance recurrence).
checked=0
for qq in [Fraction(0),Fraction(1,20),Fraction(1,10),Fraction(1,4),Fraction(1,2)]:
    histories={(Fraction(1),Fraction(0),Fraction(0)):Fraction(1)}
    vec=sp.Matrix([1,0,0,0])
    for k in range(7):
        exx=sum(prob*state[0]**2 for state,prob in histories.items())
        assert sp.Rational(exx.numerator,exx.denominator)==vec[0], (qq,k)
        checked+=1
        nxt={}
        for (x,h1,h2),prob in histories.items():
            for a1,a2,w in [(0,0,qq),(0,1,Fraction(1,2)-qq),
                            (1,0,Fraction(1,2)-qq),(1,1,qq)]:
                if w==0:continue
                gh=(h1+h2)/2 + a1*(x-h1)+a2*(x-h2)
                st=(x-gh, a1*x+(1-a1)*h1, a2*x+(1-a2)*h2)
                nxt[st]=nxt.get(st,Fraction(0))+prob*w
        histories=nxt
        vec=T.subs(q,sp.Rational(qq.numerator,qq.denominator))*vec
print('PASS: four update matrices; exact moment transfer; characteristic polynomial;')
print('      resolvent, critical residue, Schur inequalities, and', checked, 'independent finite-history checks')
