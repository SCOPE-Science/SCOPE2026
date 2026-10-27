"""Exact verification of the six-state circulant leader-placement transition.
Run: python verify.py (requires SymPy 1.14.0)."""
import sympy as sp

c = sp.symbols('c', positive=True)
a, b = sp.Integer(10), sp.Integer(1)
u, v, w = 1/(13+2*c), sp.Rational(1,33), 1/(40+2*c)
D = [(u+3*v+2*w)/6,(u+v)/2,(2*u+w)/3]
E = [(u*u+3*v*v+2*w*w)/6,(u*u+v*v)/2,(2*u*u+w*w)/3]
Q = [sp.factor(E[j]/D[j]+3*D[j]) for j in range(3)]
P = 10*c**4+419*c**3+4920*c**2+4685*c-146357
Rdiff = (2*c**2+20*c-103)/(66*(c+20)*(2*c+13))
Qdiff = -P/(33*(c+20)*(c+23)*(2*c+13)*(2*c+31))
assert sp.simplify(D[1]-D[2]-Rdiff)==0
assert sp.simplify(Q[2]-Q[1]-Qdiff)==0
up,vp,wp = sp.symbols('up vp wp', positive=True)
DD=[(up+3*vp+2*wp)/6,(up+vp)/2,(2*up+wp)/3]
EE=[(up**2+3*vp**2+2*wp**2)/6,(up**2+vp**2)/2,(2*up**2+wp**2)/3]
QQ=[EE[j]/DD[j]+3*DD[j] for j in range(3)]
assert sp.simplify(QQ[1]-QQ[0] - (up-wp)*(up**2+6*up*vp+4*up*wp+vp**2+4*vp*wp)/((up+vp)*(up+3*vp+2*wp)))==0
assert sp.simplify(QQ[2]-QQ[0] - 3*(up-vp)*(2*up**2+10*up*vp+7*up*wp+5*vp*wp)/(2*(2*up+wp)*(up+3*vp+2*wp)))==0
assert P.subs(c,4)<0<P.subs(c,5)
assert (2*c**2+20*c-103).subs(c,3)<0<(2*c**2+20*c-103).subs(c,4)
assert sp.factor(sp.diff(P,c))==40*c**3+1257*c**2+9840*c+4685

# Direct six-by-six matrix inversion, independent of the Fourier formula.
for cv in [sp.Rational(1),sp.Rational(3),sp.Rational(4),sp.Rational(17,4),sp.Rational(5),sp.Rational(10)]:
 L=sp.zeros(6)
 for i in range(6):
  for j in range(i+1,6):
   r=min(j-i,6-j+i)
   conductance={1:sp.Rational(10),2:sp.Rational(1),3:cv}[r]
   L[i,i]+=conductance; L[j,j]+=conductance
   L[i,j]-=conductance;L[j,i]-=conductance
 J=sp.ones(6,6)/6
 G=(L+J).inv()-J
 for r in (1,2,3):
  f=[k for k in range(6) if k not in (0,r)]
  actual=sp.trace(L.extract(f,f).inv())
  d=(G[0,0]+G[r,r]-2*G[0,r])/2
  e=((G*G)[0,0]+(G*G)[r,r]-2*(G*G)[0,r])/2
  prediction=sp.trace(G)+6*G[0,0]-(e/d+3*d)
  assert sp.simplify(actual-prediction)==0
  assert sp.simplify(d-D[r-1].subs(c,cv))==0
  assert sp.simplify(e-E[r-1].subs(c,cv))==0
  assert sp.simplify(actual - (sp.trace(G)+6*G[0,0]-Q[r-1].subs(c,cv)))==0
  if cv==4:
   vals={1:sp.Rational(5912,25641),2:sp.Rational(3253,16632),3:sp.Rational(584,3003)}
   assert actual==vals[r]

assert sp.simplify((D[1]-D[2]).subs(c,4)-sp.Rational(1,3696))==0
assert sp.simplify((Q[2]-Q[1]).subs(c,4)-sp.Rational(241,216216))==0
print('VERIFY_OK: symbolic spectral and gap identities; monotonic threshold signs; 6 exact parameter values; 18 grounded inverses; 18 resistance and biharmonic checks; strict c=4 reversal')
