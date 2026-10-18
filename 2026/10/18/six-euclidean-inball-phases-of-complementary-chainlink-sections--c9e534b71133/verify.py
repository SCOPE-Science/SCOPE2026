"""Exact algebraic feasibility/duality verification for chainlink section radii.
Requires SymPy >= 1.12; all comparisons are exact algebraic, not sampled.
"""
import itertools
import sympy as s
T=s.symbols('t',real=True)
X,Y,R=s.symbols('x y r',real=True)
u=s.sqrt(s.Rational(2,3));v=s.sqrt(2)
coords=[X,Y,T-X-Y];a=(4,5,6);ell=2
facet={}
for i in range(3):
 facet[('L',i)]=-coords[i]+u*R
 facet[('U',i)]=coords[i]+u*R-a[i]
 facet[('D',i)]=coords[i]-coords[(i+1)%3]+v*R-(a[i]-ell)
triples=[ [('L',0),('L',1),('L',2)], [('L',0),('D',0),('L',2)],
 [('L',0),('D',0),('D',1)], [('D',0),('D',1),('D',2)],
 [('U',0),('U',1),('D',2)], [('U',0),('U',1),('U',2)] ]
breaks=[s.Integer(0),2*s.sqrt(3),(1+5*s.sqrt(3))/2,2+3*s.sqrt(3),14-3*s.sqrt(3),15-2*s.sqrt(3),s.Integer(15)]
# Explicit upper bounds inferred by nonnegative dual facet combinations.
c1=(s.sqrt(6)-s.sqrt(2))/4
c2=(3*s.sqrt(2)-s.sqrt(6))/12
F=[T/s.sqrt(6), c1*(T+2), c2*(T+7), 3*s.sqrt(2)/2, c1*(17-T), (15-T)/s.sqrt(6)]
# Weights in order of facet triples. Each list has nonnegative entries.
weights=[[1/s.sqrt(6)]*3,[2*c1,c1,c1],[3*c2,2*c2,c2], [1/(3*s.sqrt(2))]*3,[2*c1,c1,c1],[1/s.sqrt(6)]*3]

def nonnegative(expr):
 v=s.simplify(s.radsimp(expr))
 z=s.sign(v)
 if z not in (s.S.Zero,s.S.One):
  raise AssertionError('inconclusive exact sign: '+str(v)+' sign='+str(z))
 return True

for j,triple in enumerate(triples):
 sol=s.solve([facet[z] for z in triple],(X,Y,R),dict=True)[0]
 assert s.simplify(sol[R]-F[j])==0,(j,sol)
 # Exact dual certificate: all weighted shifted-normal equations cancel x,y.
 dual=s.expand(sum(weights[j][k]*facet[z] for k,z in enumerate(triple)))
 assert s.simplify(s.diff(dual,X))==0 and s.simplify(s.diff(dual,Y))==0
 assert s.simplify(s.diff(dual,R)-1)==0
 assert s.simplify(dual.subs(R,0)+F[j])==0
 for w in weights[j]:nonnegative(w)
 # Exact endpoint verification of every constraint. Affine slacks give all t.
 for endpoint in (breaks[j],breaks[j+1]):
  for name,f in facet.items():
   slack=s.simplify((-f).subs(sol).subs(T,endpoint))
   nonnegative(slack)
  for k in range(6):nonnegative(s.simplify((F[k]-F[j]).subs(T,endpoint)))
 print('phase',j+1,'exact dual and 9 facet checks PASS at both endpoints')
# Exact two-section difference
r6=s.simplify(F[2].subs(T,6));r9=s.simplify(F[4].subs(T,9))
assert s.simplify(r6-13*(3*s.sqrt(2)-s.sqrt(6))/12)==0
assert s.simplify(r9-2*(s.sqrt(6)-s.sqrt(2)))==0
nonnegative(r9-r6)
print('exact r(6)=',r6,'r(9)=',r9,'difference=',s.simplify(r9-r6))

# Independently enumerate planar vertices exactly and compute perimeter/area.
x,y=s.symbols('x y');
def polygon(t):
 xyz=[x,y,s.Integer(t)-x-y]
 inequalities=[]
 for i in range(3):
  inequalities.extend([-xyz[i],xyz[i]-a[i],xyz[i]-xyz[(i+1)%3]-(a[i]-ell)])
 vertices=set()
 for f,g in itertools.combinations(inequalities,2):
  sol=s.solve((f,g),(x,y),dict=True)
  if len(sol)!=1 or x not in sol[0] or y not in sol[0]:continue
  xx,yy=s.simplify(sol[0][x]),s.simplify(sol[0][y])
  if all(s.sign(s.simplify(h.subs({x:xx,y:yy}))) in (s.S.NegativeOne,s.S.Zero) for h in inequalities):
   vertices.add((xx,yy))
 # Order in the Euclidean plane (orientation-preserving linear chart).
 import math
 vs=list(vertices);cx=sum(z[0] for z in vs)/len(vs);cy=sum(z[1] for z in vs)/len(vs)
 vs.sort(key=lambda z:math.atan2(float(z[1]-cy),float(z[0]-cx)))
 P=s.Integer(0);twice_area=s.Integer(0)
 for i in range(len(vs)):
  xx,yy=vs[i];xx2,yy2=vs[(i+1)%len(vs)];dx=xx2-xx;dy=yy2-yy
  P+=s.sqrt(2*(dx*dx+dx*dy+dy*dy))
  twice_area+=xx*yy2-xx2*yy
 return len(vs),s.simplify(P),s.simplify(s.sqrt(3)*abs(twice_area)/2)
p6=polygon(6);p9=polygon(9)
assert p6==p9,(p6,p9)
assert p6==(6,s.Rational(9,2)*(s.sqrt(2)+s.sqrt(6)),s.Rational(43,4)*s.sqrt(3)),p6
print('exact polygon geometry PASS: vertices, intrinsic perimeter, intrinsic area',p6)
print('ALL EXACT CHECKS PASSED')
