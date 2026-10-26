"""Exact census of smooth tangent-filling binary plane-cubic nets.

All calculations are over the two-element field. Coefficient-mask bit order is
X^3, X^2Y, X^2Z, XY^2, XYZ, XZ^2, Y^3, Y^2Z, YZ^2, Z^3.
Run: python verify_exhaustive.py
"""
from collections import Counter
from itertools import combinations, product
import json
from sympy import symbols, groebner

x,y,z=symbols('x y z'); variables=(x,y,z)
exps=[(a,b,3-a-b) for a in range(3,-1,-1) for b in range(3-a,-1,-1)]
monomials=[x**a*y**b*z**c for a,b,c in exps]
positions={p:i for i,p in enumerate(exps)}
points=range(1,8)

def coordinates(p):return tuple((p>>j)&1 for j in range(3))
def expr(mask):return sum(monomials[j] for j in range(10) if mask>>j&1)
point_values=[sum((int(m.subs(dict(zip(variables, coordinates(p))))%2)<<j) for j,m in enumerate(monomials)) for p in points]
partial_values=[]
for p in points:
 partial_values.append([sum((int(m.diff(v).subs(dict(zip(variables,coordinates(p))))%2)<<j) for j,m in enumerate(monomials)) for v in variables])

def parity(value):return value.bit_count()%2
def point_set(mask):return {p for p in points if not parity(mask & point_values[p-1])}
def tangent(mask,p):return sum(parity(mask & partial_values[p-1][j])<<j for j in range(3))
def tangent_cover(mask):
 cover=set()
 for p in point_set(mask):
  l=tangent(mask,p)
  if l:cover.update(q for q in points if not parity(q&l))
 return cover

def smooth(mask):
 F=expr(mask)
 # The affine Jacobian ideals on the three standard charts have empty varieties
 # over the algebraic closure precisely if each Gröbner basis is (1).
 derivatives=[F.diff(v) for v in variables]
 for k in range(3):
  uv=[v for j,v in enumerate(variables) if j!=k]
  equations=[e.subs(variables[k],1) for e in [F]+derivatives]
  basis=groebner(equations,*uv,modulus=2)
  if len(basis.polys)!=1 or not basis.polys[0].is_one:return False
 return True

smooth_set={m for m in range(1,1024) if smooth(m)}
tangent_set={m for m in smooth_set if len(tangent_cover(m))==7}
assert len(smooth_set)==336 and len(tangent_set)==154
# Every binary 2-plane is its three-element nonzero set. A 3-plane can be
# extended from one 2-plane by adjoining c; deduplication is by frozenset.
pencils={frozenset((a,b,a^b)) for a,b in combinations(sorted(tangent_set),2) if a^b in tangent_set}
nets=set()
for pencil in pencils:
 for c in tangent_set:
  if c in pencil: continue
  new=frozenset(pencil | {c} | {c^u for u in pencil})
  if len(new)==7 and new.issubset(tangent_set):nets.add(new)
assert len(pencils)==392 and len(nets)==8

# An all-tangent-filling 4-space would have 15 distinct dimension-three
# subspaces. There are only eight nets in the entire coefficient space.
no_four_dimensional_space=len(nets)<15

def rank3(matrix):
 rows=[list(row) for row in matrix]; rank=0
 for col in range(3):
  pivot=next((k for k in range(rank,3) if rows[k][col]),None)
  if pivot is None:continue
  rows[pivot],rows[rank]=rows[rank],rows[pivot]
  for k in range(3):
   if k!=rank and rows[k][col]:rows[k]=[a^b for a,b in zip(rows[k],rows[rank])]
  rank+=1
 return rank==3

def poly_product(a,b):
 out=set()
 for e in a:
  for f in b:
   g=tuple(e[k]+f[k] for k in range(3))
   if g in out:out.remove(g)
   else:out.add(g)
 return out

def transformation_basis(rows):
 linear=[{tuple(int(j==k) for j in range(3)) for k in range(3) if rows[i][k]} for i in range(3)]
 out=[]
 for powers in exps:
  terms={(0,0,0)}
  for k,degree in enumerate(powers):
   for _ in range(degree):terms=poly_product(terms,linear[k])
  out.append(sum(1<<positions[e] for e in terms))
 return out

def translate(mask,rep):
 out=0
 for j in range(10):
  if mask>>j&1:out^=rep[j]
 return out

actions=[]
for rows_as_bits in product(range(8),repeat=3):
 rows=[tuple((row>>j)&1 for j in range(3)) for row in rows_as_bits]
 if rank3(rows):actions.append(transformation_basis(rows))
assert len(actions)==168
example=min(nets,key=lambda v:sorted(v))
net_orbit={frozenset(translate(m,action) for m in example) for action in actions}
assert len(net_orbit)==8 and net_orbit==nets
assert all(len({p for p in points if not parity(p&l)})==3 for l in points)

def is_rational_line(point_subset):
 return any(point_subset=={p for p in points if not parity(p&l)} for l in points)

support_sets=[]
for net in nets:
 supports=[point_set(m) for m in net]
 assert all(len(P)==3 and is_rational_line(P) for P in supports)
 assert len({frozenset(P) for P in supports})==7
 support_sets.append(supports)

# Inflection at a rational point is intersection multiplicity at least 3:
# the coefficient of t^2 in F(P+tQ) must vanish on its tangent line.
def flex_points(mask):
 from sympy import Poly
 T=symbols('t');F=expr(mask)
 out=[]
 for p in point_set(mask):
  tangent_line=tangent(mask,p)
  q=next(q for q in points if q!=p and not parity(q&tangent_line))
  P=coordinates(p);Q=coordinates(q)
  restrict=F.subs({variables[j]:P[j]+T*Q[j] for j in range(3)},simultaneous=True)
  if Poly(restrict,T,modulus=2).nth(2)==0:out.append(p)
 return out
assert all(len(flex_points(m))==3 for net in nets for m in net)

result={
 'all_nonzero_cubics':1023,'geometrically_smooth':len(smooth_set),
 'smooth_tangent_filling':len(tangent_set),
 'all_tangent_filling_pencils':len(pencils),
 'all_tangent_filling_nets':len(nets),
 'four_dimensional_exists':not no_four_dimensional_space,
 'projective_group_order':len(actions),'net_orbit_size':len(net_orbit),
 'net_stabilizer_order':len(actions)//len(net_orbit),
 'every_net_member_has_three_rational_flexes':True,
 'all_seven_rational_lines_occur_as_net_member_point_sets':True,
 'canonical_net_masks':sorted(example),
 'all_net_mask_sets':sorted([sorted(net) for net in nets])
}
print(json.dumps(result,sort_keys=True,indent=2))
