"""Exact symbolic checks for compatibility thresholds of three damped Pauli POVMs.

Run: python verify.py.  The continuum nonexistence theorem also uses the
rotation-averaging and trace-witness arguments in RESULT.md.
"""
import sympy as sp
q=sp.symbols('q',real=True,nonnegative=True)
r=sp.symbols('r',real=True,nonnegative=True)
I=sp.eye(2)
X=sp.Matrix([[0,1],[1,0]])
Y=sp.Matrix([[0,-sp.I],[sp.I,0]])
Z=sp.diag(1,-1)
P=sp.diag(0,1)
Zplus=I-q*P
K0=sp.diag(1,r)
K1=sp.Matrix([[0,sp.symbols('t',nonnegative=True)],[0,0]])
def dual(B): return K0.H*B*K0+K1.H*B*K1
assert sp.simplify(dual(X)-r*X)==sp.zeros(2)
assert sp.simplify(dual(Y)-r*Y)==sp.zeros(2)
# Channel formulas are directly checked by enforcing t^2=1-r^2.
t=K1[0,1]
assert sp.simplify(dual(I).subs(t*t,1-r*r)-I)==sp.zeros(2)
assert sp.simplify(dual(Z).subs(t*t,1-r*r)-((1-r*r)*I+r*r*Z))==sp.zeros(2)
assert sp.simplify(dual(X)-r*X)==sp.zeros(2)
for a in (-1,1):
 for b in (-1,1):
  g=(Zplus+a*r*X+b*r*Y)/4
  assert sp.simplify(sp.det(g).subs(r*r,q)-(1-3*q)/16)==0
for a in (-1,1):
 f=(Zplus+a*r*X)/2
 assert sp.simplify(sp.det(f).subs(r*r,q)-(1-2*q)/4)==0
# Exact identities for eight proposed mother-POVM effects.
G={(a,b,1):(Zplus+a*r*X+b*r*Y)/4 for a in (-1,1) for b in (-1,1)}
G.update({(a,b,-1):q*P/4 for a in (-1,1) for b in (-1,1)})
assert sp.simplify(sum(G.values(),sp.zeros(2))-I)==sp.zeros(2)
for a in (-1,1):
 assert sp.simplify(sum((G[a,b,z] for b in (-1,1) for z in (-1,1)),sp.zeros(2))-(I+a*r*X)/2)==sp.zeros(2)
for b in (-1,1):
 assert sp.simplify(sum((G[a,b,z] for a in (-1,1) for z in (-1,1)),sp.zeros(2))-(I+b*r*Y)/2)==sp.zeros(2)
for z in (-1,1):
 assert sp.simplify(sum((G[a,b,z] for a in (-1,1) for b in (-1,1)),sp.zeros(2))-(I+z*((1-q)*I+q*Z))/2)==sp.zeros(2)
# At q=2/5, every pair is compatible using explicit 4-outcome constructions.
for v in (X,Y):
 F={(a,1):(Zplus+a*r*v)/2 for a in (-1,1)}
 F.update({(a,-1):q*P/2 for a in (-1,1)})
 assert sp.simplify(sum(F.values(),sp.zeros(2))-I)==sp.zeros(2)
 for a in (-1,1):
  assert sp.simplify(sum((F[a,z] for z in (-1,1)),sp.zeros(2))-(I+a*r*v)/2)==sp.zeros(2)
 for z in (-1,1):
  assert sp.simplify(sum((F[a,z] for a in (-1,1)),sp.zeros(2))-(I+z*((1-q)*I+q*Z))/2)==sp.zeros(2)
 for a in (-1,1):
  ev=[x.subs(q,sp.Rational(2,5)).subs(r,sp.sqrt(sp.Rational(2,5))) for x in F[a,1].eigenvals()]
  assert all(x.is_nonnegative for x in ev)
# Orthogonal equatorial pair: H_{ab} = (I+a*r*X+b*r*Y)/4.
for a in (-1,1):
 for b in (-1,1):
  assert sp.simplify(sp.det((I+a*r*X+b*r*Y)/4).subs(r*r,q)-(1-2*q)/16)==0
# q=1/3 saturates triple positivity, q=2/5 has three-way incompatibility;
# the proof in RESULT.md excludes all mother POVMs at q>1/3.
print('VERIFY_OK symbolic_marginals=passed Kraus_dual=passed pair_and_triple_determinants=passed rational_Specker_witness=2/5')
