"""Exact symbolic checks for the dimension-three Higashitani normal-fan calculations.

Requires Python 3 and SymPy. Run: python verify.py
The calculations verify the finite symbolic certificates used in the proof;
very ampleness and the original enumeration of holes are cited from Higashitani.
"""
from itertools import combinations
from math import gcd
from functools import reduce
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
h = S.symbols('h', integer=True, positive=True)
VERTICES = {
 'u1':(0,0,0), 'u2':(0,0,1), 'u3':(0,1,0),
 'u4':(0,h,h), 'u5':(0,h-1,h), 'u6':(0,h,h-1),
 'u7':(1,0,4), 'u8':(1,0,5), 'u9':(1,1,0), 'u10':(1,1,1)
}
RAYS = {
 '0':(-1,0,0), '1':(0,0,-1), '2':(0,-1,0),
 '3':(0,1,-1), '4':(4,-4,-1), '5':(-4,-1,1),
 '6':(1,0,0), '7':(5*h-5,4,1), '8':(h-5,0,1),
 '9':(h-1,1,0)
}
BOUNDS = {'0':0, '1':0, '2':0, '3':1, '4':0,
          '5':1, '6':1, '7':5*h, '8':h, '9':h}
EXPECTED_INC = {
 'u1':'0124','u2':'025','u3':'013','u4':'0789','u5':'058',
 'u6':'039','u7':'246','u8':'25678','u9':'13469','u10':'679'
}
EXPECTED_EDGES = {
 '01':('u1','u3'), '02':('u1','u2'), '03':('u3','u6'),
 '05':('u2','u5'), '08':('u4','u5'), '09':('u4','u6'),
 '13':('u3','u9'), '14':('u1','u9'), '24':('u1','u7'),
 '25':('u2','u8'), '26':('u7','u8'), '39':('u6','u9'),
 '46':('u7','u9'), '58':('u5','u8'), '67':('u8','u10'),
 '69':('u9','u10'), '78':('u4','u8'), '79':('u4','u10')
}

def reduced(expr):
 return S.expand(expr)

def admissible_slack(expr):
 """Every slack is affine with nonnegative slope and nonnegative value at h=2."""
 p=S.Poly(expr,h)
 assert p.degree()<=1, expr
 assert p.eval(2)>=0, expr
 assert reduced(p.diff().as_expr())>=0, expr

def incidence():
 actual={}
 for name,v in VERTICES.items():
  incident=''
  for i,n in RAYS.items():
   slack=reduced(BOUNDS[i]-sum(a*b for a,b in zip(n,v)))
   admissible_slack(slack)
   if slack==0:incident+=i
   else:assert slack.subs(h,2)>0, (name,i,slack)
  actual[name]=incident
 assert actual==EXPECTED_INC,(actual,EXPECTED_INC)
 return actual

def edge_indices():
 edges={}
 for (i,u),(j,v) in combinations(RAYS.items(),2):
  vs=tuple(name for name,inc in EXPECTED_INC.items() if i in inc and j in inc)
  if len(vs)<2:
   continue
  assert len(vs)==2, (i,j,vs)
  name=i+j
  assert name in EXPECTED_EDGES and vs==EXPECTED_EDGES[name], (name,vs)
  cp=[S.expand(z) for z in S.Matrix(u).cross(S.Matrix(v))]
  # Primitive cross-product divisor as an integer function of h. For all
  # ordinary edges a coordinate of the cross product is literally +/-1.
  if name in ('14','78'):
   assert all(S.rem(p,4,h)==0 for p in cp)
   if name=='14':assert cp==[-4,-4,0]
   else:assert cp==[4,-4*h,-4*(h-5)]
   q=[S.expand(z/4) for z in cp]
   assert any(z in (1,-1) for z in q), (name,q)
   index=4
  else:
   assert any(z in (1,-1) for z in cp), (name,cp)
   index=1
  edges[name]=index
 assert set(edges)==set(EXPECTED_EDGES)
 assert len(edges)==18
 assert {k:v for k,v in edges.items() if v!=1}=={'14':4,'78':4}
 return edges

def vertex_cones():
 cl={}
 for v,inc in EXPECTED_INC.items():
  matrix=S.Matrix.hstack(*(S.Matrix(RAYS[i]) for i in inc))
  assert matrix.rank()==3
  # The Smith determinants stay 1: we certify using a fixed triple
  # with determinant +/-1 as a polynomial identity in the parameter.
  dets=[S.factor(S.Matrix.hstack(*(S.Matrix(RAYS[i]) for i in triple)).det())
        for triple in combinations(inc,3)]
  assert any(d in (1,-1) for d in dets), (v,dets)
  rank=len(inc)-3
  if rank==0:
   assert len(dets)==1 and dets[0] in (1,-1)
  cl[v]=rank
 assert cl=={'u1':1,'u2':0,'u3':0,'u4':1,'u5':0,'u6':0,
             'u7':0,'u8':2,'u9':2,'u10':0}
 return cl

def ade_transverse():
 a=S.Matrix(RAYS['1']);b=S.Matrix(RAYS['4'])
 u=a;w=S.Matrix((-1,-1,0))
 # H4 = H1 + 4 * (1,-1,0) (not the preceding tentative vector)
 w=S.Matrix((1,-1,0))
 assert b==u+4*w
 assert any(abs(z)==1 for z in u.cross(w))
 u=S.Matrix(RAYS['8']);w=S.Matrix((h,1,0))
 assert S.Matrix(RAYS['7'])==u+4*w
 assert any(z in (1,-1) for z in list(u.cross(w)))
 # In a saturated basis the cone has rays (1,0), (1,4),
 # with dual semigroup generators (0,1), (1,0), (4,-1).
 # The unique affine relation is X*Y = Z**4.
 assert S.Matrix((0,1))+S.Matrix((4,-1))==4*S.Matrix((1,0))

def line_lengths():
 for a,b in [('u1','u9'),('u4','u8')]:
  diff=[S.expand(x-y) for x,y in zip(VERTICES[a],VERTICES[b])]
  assert any(x in (1,-1) for x in diff), (a,b,diff)

if __name__=='__main__':
 incidence(); edge_indices(); vertex_cones(); ade_transverse(); line_lengths()
 # Independent integer-h checks, not used in place of the symbolic proof.
 from scipy.spatial import ConvexHull
 for H in (2,3,4,5,11,37):
  pts=[tuple(int(S.sympify(x).subs(h,H)) for x in p) for p in VERTICES.values()]
  hull=ConvexHull(pts)
  assert len(hull.vertices)==10, H
 print('VERIFY_OK: symbolic ten-cone and eighteen-edge fan certificate')
