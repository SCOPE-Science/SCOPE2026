#!/usr/bin/env python3
"""Exact checks for two-component simultaneous descent-ascent finite-epoch risk.

Requires Python 3 and SymPy. This script does not substitute for the
universal algebraic proof given in RESULT.md.
"""
from fractions import Fraction as F
import itertools
import sympy as s

a, b, c, h = s.symbols('a b c h', real=True)
E = s.eye(2)
A = s.diag(a, b)
B = s.Matrix([[a, c], [-c, b]])
P, Q = E-h*A, E-h*B
RR = ((P*Q).T*(P*Q) + (Q*P).T*(Q*P))/2
IID = sum(((X*Y).T*(X*Y) for X,Y in itertools.product([P,Q], repeat=2)), s.zeros(2))/4
D = s.simplify(IID-RR)
delta = b-a
Dstar = s.diag(c*c*h**3*((2*a*delta+c*c)*h-2*delta)/4,
               c*c*h**3*(2*delta*(1-b*h)+c*c*h)/4)
assert all(s.factor((D-Dstar)[i,j]) == 0 for i in range(2) for j in range(2))
assert D[0,1] == 0 and D[1,0] == 0

# Independent rational matrix multiplication, no symbolic substitutions
# and no floating-point estimates for the four sampling outcomes.
def mat_mul(X, Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def transpose(X): return tuple(tuple(X[j][i] for j in range(2)) for i in range(2))
def msq(X): return mat_mul(transpose(X), X)
def add(X,Y): return tuple(tuple(X[i][j]+Y[i][j] for j in range(2)) for i in range(2))
def scale(x,X): return tuple(tuple(x*X[i][j] for j in range(2)) for i in range(2))

checks = 0
for aa,bb,cc,hh in itertools.product([F(1),F(2),F(3,2)], [F(2),F(3)], [F(1),F(2),F(3)], [F(1,10),F(1,5),F(1,4)]):
    if bb<=aa: continue
    X=((1-hh*aa,F(0)),(F(0),1-hh*bb))
    Y=((1-hh*aa,-hh*cc),(hh*cc,1-hh*bb))
    rr=scale(F(1,2),add(msq(mat_mul(X,Y)),msq(mat_mul(Y,X))))
    iid=scale(F(1,4),sum_mats := add(add(msq(mat_mul(X,X)),msq(mat_mul(Y,Y))), add(msq(mat_mul(X,Y)),msq(mat_mul(Y,X)))))
    diff=add(iid,scale(-1,rr))
    want1=cc*cc*hh**3*((2*aa*(bb-aa)+cc*cc)*hh-2*(bb-aa))/4
    want2=cc*cc*hh**3*(2*(bb-aa)*(1-bb*hh)+cc*cc*hh)/4
    assert diff==((want1,F(0)),(F(0),want2))
    checks+=4

# A concrete problem having a sharp crossover inside the conventional
# component Lipschitz stepsize range.
AA=F(1);BB=F(3,2);CC=F(2)
for hh, expected in [
    (F(1,10),(F(-1,2000),F(1,800))),
    (F(1,5),(F(0),F(3,250))),
    (F(1,4),(F(1,256),F(13,512)))]:
    got=[s.cancel(Dstar[i,i].subs({a:s.Rational(AA.numerator,AA.denominator),b:s.Rational(BB.numerator,BB.denominator),c:s.Rational(CC.numerator,CC.denominator),h:s.Rational(hh.numerator,hh.denominator)})) for i in range(2)]
    assert all(got[i]==s.Rational(expected[i].numerator,expected[i].denominator) for i in range(2))
    checks+=2
# At h=1/4, both component update maps are strict Euclidean contractions.
q=s.Matrix([[s.Rational(3,4),-s.Rational(1,2)],[s.Rational(1,2),s.Rational(5,8)]])
p=s.diag(s.Rational(3,4),s.Rational(5,8))
for T in [p,q]:
    defect=s.eye(2)-T.T*T
    assert defect[0,0]>0 and defect.det()>0
    checks+=2
# A safe sufficient bound for h=1/4 < 1/max ||A||_2,||B||_2.
assert s.Rational(1,4)**2*(AA*AA+BB*BB+2*CC*CC)<1
checks+=1
print('PASS: symbolic identity and',checks,'independent exact rational assertions')
