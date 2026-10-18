"""Exact symbolic checks for the threefold-axis octahedral overlap and chord law.
Requires Python 3 and SymPy; no external data or private files.
"""
import itertools, sympy as S
from fractions import Fraction as F
T=S.symbols('t')
signs=list(itertools.product([-1,1],repeat=3))
rhs={sig:1-S.Rational(abs(sum(sig)),2)*T for sig in signs}
expected={tuple(q) for v in [(1-T,-T/2,0),(-1+T,T/2,0)] for q in itertools.permutations(v)}
# Sympy canonical
expected={tuple(S.expand(x) for x in v) for v in expected}
valid=set(); incidences=[]
for tri in itertools.combinations(signs,3):
 A=S.Matrix(tri)
 if A.det()==0:continue
 xyz=tuple(S.expand(v) for v in A.inv()*S.Matrix([rhs[s] for s in tri]))
 low=S.Rational(0);high=S.Rational(2,3)
 for sg in signs:
  ex=S.expand(rhs[sg]-sum(sg[i]*xyz[i] for i in range(3)))
  b=ex.coeff(T);a=ex.subs(T,0)
  if b>0:low=max(low,-a/b)
  elif b<0:high=min(high,-a/b)
  elif a<0:high=-1
 if low<high:
  valid.add(xyz)
  incidences.append((tri,xyz,low,high))
  assert xyz in expected,(xyz,low,high)
assert valid==expected,(len(valid),expected-valid)
for sg in signs:
    contacts=sum(1 for y in valid if S.expand(rhs[sg]-sum(sg[i]*y[i] for i in range(3)))==0)
    assert contacts==(6 if abs(sum(sg))==3 else 4),(sg,contacts)
assert all(lo==0 and hi==S.Rational(2,3) for _,_,lo,hi in incidences)
print('56 triples, interior affine vertices',len(valid),'full-domain incidence triple count',len(incidences))

# Independent symbolic shoelace checks on explicit ordered face vertices.
a=1-T
b=-T/2
hex_face=[(b,a,0),(b,0,a),(0,b,a),(a,b,0),(a,0,b),(0,a,b)]
quad_face=[(0,a,b),(a,0,b),(-b,0,-a),(0,-b,-a)]
def signed_xy(poly):
    return S.factor(sum(poly[i][0]*poly[(i+1)%len(poly)][1] - poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly)))/2)
assert S.simplify(signed_xy(hex_face)**2 - (4-3*T**2)**2/64)==0
assert S.simplify(signed_xy(quad_face)**2 - ((2-T)*(2-3*T))**2/64)==0
print('FACETS_OK 2 hexagons and 6 quadrilaterals, shoelace exact')

# exact facet formula: two hexagons and six quadrilaterals
H=S.sqrt(3)*(4-3*T**2)/8
Q=S.sqrt(3)*(2-T)*(2-3*T)/8
A=1-S.Rational(3,2)*T;B=1-T/2
v=S.factor((2*A*H+6*B*Q)/(3*S.sqrt(3)))
assert S.factor(v-(S.Rational(4,3)-3*T+S.Rational(3,2)*T**2))==0
print('volume',v)
R=S.symbols('r',nonnegative=True)
g=S.expand(v.subs(T,R/S.sqrt(3)))
assert S.simplify(g-(S.Rational(4,3)-S.sqrt(3)*R+R**2/2))==0
area=-S.diff(g,R).subs(R,0)
L=2/S.sqrt(3)
atom=-S.diff(g,R).subs(R,L)
assert S.simplify(area-S.sqrt(3))==0
assert S.simplify(atom/area-S.Rational(1,3))==0
assert S.simplify((L*1)/area-S.Rational(2,3))==0
print('CHORD_OK atom_fraction',atom/area,'continuous_fraction',L/area,'mean',S.factor(v.subs(T,0)/area))
