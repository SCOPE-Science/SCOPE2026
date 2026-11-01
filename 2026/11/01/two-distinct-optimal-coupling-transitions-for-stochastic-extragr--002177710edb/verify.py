"""Reproducibility checks for two-oracle stochastic extragradient on a bilinear saddle.

Run with Python 3 and SymPy (see requirements.txt). Finite enumeration is an
independent consistency test, not the proof of the universal assertions.
"""
from fractions import Fraction
from itertools import product
import sympy as s

x,q=s.symbols('x q',real=True)
I=s.eye(2)
J=s.Matrix([[0,1],[-1,0]])
assert J.T==-J and J**2==-I
G={}
checks=0
for u,v in product((1,2),repeat=2):
    M=(1-x*u*v)*I-s.sqrt(x)*v*J
    g=s.expand((1-x*u*v)**2+x*v**2)
    assert s.simplify(M.T*M-g*I)==s.zeros(2)
    G[(u,v)]=g
    checks+=1
assert G[(1,1)]==1-x+x**2
assert G[(2,2)]==1-4*x+16*x**2
assert G[(1,2)]==1+4*x**2
assert G[(2,1)]==1-3*x+4*x**2
checks+=4
rs=s.expand((G[(1,1)]+G[(2,2)])/2)
ra=s.expand((G[(1,2)]+G[(2,1)])/2)
assert rs==1-s.Rational(5,2)*x+s.Rational(17,2)*x*x
assert ra==1-s.Rational(3,2)*x+4*x*x
assert s.simplify((rs-ra)-x*(s.Rational(9,2)*x-1))==0
assert s.factor((G[(1,1)]*G[(2,2)])-(G[(1,2)]*G[(2,1)]))==-x*(8*x*x-13*x+2)
checks+=4
assert s.solve(s.Eq(rs,1),x)==[0,s.Rational(5,17)]
assert s.solve(s.Eq(ra,1),x)==[0,s.Rational(3,8)]
assert s.solve(s.Eq((rs+ra)/2,1),x)==[0,s.Rational(8,25)]
r1=(13-s.sqrt(105))/16
r2=(13+s.sqrt(105))/16
assert 0<r1<s.Rational(1,5)<s.Rational(2,9)<s.Rational(5,17)<s.Rational(8,25)<s.Rational(3,8)<r2
assert rs.subs(x,s.Rational(1,5))==s.Rational(21,25)
assert ra.subs(x,s.Rational(1,5))==s.Rational(43,50)
assert (G[(1,1)]*G[(2,2)]).subs(x,s.Rational(1,5))==s.Rational(441,625)
assert (G[(1,2)]*G[(2,1)]).subs(x,s.Rational(1,5))==s.Rational(406,625)
checks+=8
# Enumerate exact finite-horizon law for three marginal-preserving couplings.
for val in (Fraction(1,50),Fraction(1,5),Fraction(7,20),Fraction(1,2)):
  gains={key:Fraction(str(g.subs(x,s.Rational(val.numerator,val.denominator)))) for key,g in G.items()}
  for prob in (Fraction(0),Fraction(1,3),Fraction(1,2),Fraction(1)):
    atom_probs={(1,1):prob/2,(2,2):prob/2,(1,2):(1-prob)/2,(2,1):(1-prob)/2}
    r=sum((p*gains[key] for key,p in atom_probs.items()),Fraction())
    for n in range(1,5):
      enum=sum((Fraction(1)*s.prod([atom_probs[a] for a in path])*s.prod([gains[a] for a in path])
               for path in product(atom_probs,repeat=n)),Fraction())
      assert enum==r**n
      checks+=1
print('PASS:',checks,'exact symbolic/rational assertions, including finite-horizon enumeration')
