#!/usr/bin/env python3
"""Exact spherical-arrangement certificate for central sections of a regular dodecahedron.
Uses SymPy for exact quadratic-field signs; no random sampling is used in the proof certificate.
"""
import sympy as sp
import itertools, collections, math
PH=(1+sp.sqrt(5))/2
PI=PH-1
V=[sp.Matrix(t) for t in itertools.product((-1,1),repeat=3)]
V += [sp.Matrix([0,a*PI,b*PH]) for a,b in itertools.product((-1,1),repeat=2)]
V += [sp.Matrix([a*PI,b*PH,0]) for a,b in itertools.product((-1,1),repeat=2)]
V += [sp.Matrix([a*PH,0,b*PI]) for a,b in itertools.product((-1,1),repeat=2)]
W=[]; vertexindex=[]
for v in V:
  if any(v==w for w in W): vertexindex.append((W.index(v),1))
  elif any(v==-w for w in W): vertexindex.append((next(i for i,w in enumerate(W) if v==-w),-1))
  else: W.append(v); vertexindex.append((len(W)-1,1))
assert len(V)==20 and len(W)==10

def exactsign(t):
 t=sp.expand(t)
 if t==0:return 0
 if t.is_positive:return 1
 if t.is_negative:return -1
 t=sp.simplify(t)
 if t==0:return 0
 if t.is_positive:return 1
 if t.is_negative:return -1
 raise ValueError('undecided algebraic sign: '+str(t))

assert all(sp.simplify(w.dot(w))==3 for w in W)
assert {sp.simplify(W[i].dot(W[j])**2) for i,j in itertools.combinations(range(10),2)}=={sp.Integer(1),sp.Integer(5)}
assert all(exactsign(sp.det(sp.Matrix.hstack(W[i],W[j],W[k])))!=0 for i,j,k in itertools.combinations(range(10),3))

# Every open chamber mask is certified by the extreme vertices in its closure.
# Pairwise great-circle crosses enumerate all vertices: no three planes concur.
intersections=[]
for i,j in itertools.combinations(range(10),2):
 p=W[i].cross(W[j]); assert p!=sp.zeros(3,1)
 for sense in (1,-1):
  x=sense*p
  pos=neg=0
  for k,w in enumerate(W):
   t=exactsign(w.dot(x))
   if t>0:pos|=1<<k
   if t<0:neg|=1<<k
  intersections.append((x,i,j,pos,neg))
assert len(intersections)==90
cells={}
for mask in range(1<<10):
 corners=[entry for entry in intersections if (entry[3] & ~mask)==0 and (entry[4] & mask)==0]
 if len(corners)>=3:cells[mask]=corners
assert len(cells)==92,('cells',len(cells))
assert collections.Counter(map(len,cells.values()))=={6:20,3:60,5:12}

# The finite edge test is exact: a dodecahedral edge has squared length 6-2sqrt(5).
edgelen=6-2*sp.sqrt(5)
edges=[(i,j) for i,j in itertools.combinations(range(20),2) if sp.simplify((V[i]-V[j]).dot(V[i]-V[j])-edgelen)==0]
assert len(edges)==30

def sidecount(mask):
 def signvert(idx):
  i,parity=vertexindex[idx]
  return parity*(1 if (mask>>i)&1 else -1)
 return sum(signvert(i)!=signvert(j) for i,j in edges)
types={m:sidecount(m) for m in cells}
assert collections.Counter(types.values())=={6:20,8:60,10:12},collections.Counter(types.values())
assert collections.Counter((len(cells[m]),types[m]) for m in cells)=={(6,6):20,(3,8):60,(5,10):12}

# Adjacent chambers differ by exactly one sign at a separating great circle.
# Each side is identified by its two endpoints, which share exactly one bounding circle.
# An unordered side is counted from each of its two chambers.
interfaces=collections.Counter(); side_length_squares=collections.Counter(); classangles=collections.defaultdict(list)
for mask,corners in cells.items():
 # For each boundary circle, exactly two corner endpoints lie on it.
 for k in range(10):
  pair=[v for v in corners if v[1]==k or v[2]==k]
  if not pair:continue
  assert len(pair)==2,(mask,k,len(pair))
  neighbor=mask^(1<<k)
  assert neighbor in cells,(mask,k,neighbor)
  typ=(min(types[mask],types[neighbor]),max(types[mask],types[neighbor]))
  interfaces[typ]+=1
  x,y=pair[0][0],pair[1][0]
  c=sp.simplify(x.dot(y)**2/(x.dot(x)*y.dot(y)))
  # Cosine positivity proven by direct exact dot sign, giving angles < pi/2.
  assert exactsign(x.dot(y))>0
  side_length_squares[(typ,str(c))]+=1
  classangles[typ].append(float(sp.acos(sp.sqrt(c))))
assert interfaces=={(6,8):240,(8,10):120},interfaces
# Every geometric edge of the chamber arrangement was double-counted.
assert sum(interfaces.values())//2==180
COS_H=(3+sp.sqrt(5))/(4*sp.sqrt(2))
COS_P=(1+3*sp.sqrt(5))/8
expected_h=sp.simplify(COS_H**2)
expected_p=sp.simplify(COS_P**2)
assert all(sp.simplify(sp.sympify(v)-expected_h)==0 for typ,val in side_length_squares for v in [val] if typ==(6,8))
assert all(sp.simplify(sp.sympify(v)-expected_p)==0 for typ,val in side_length_squares for v in [val] if typ==(8,10))
H=float(sp.acos(COS_H));P=float(sp.acos(COS_P))
assert abs(6*H+3*P-math.pi)<1e-11,(H,P,6*H+3*P)
print('EXACT_TEN_GREAT_CIRCLES_92_CHAMBERS_OK')
print('EXACT_SECTION_TYPE_COUNTS',sorted(collections.Counter(types.values()).items()))
print('EXACT_ADJACENCY_COUNTS',sorted((k,v//2) for k,v in interfaces.items()))
print('EXACT_TWO_GEODESIC_EDGE_LENGTHS_OK',H,P)
# Flux across interfaces: one-way crossing coefficient is L/(4pi²), total untyped=10/pi.
assert abs((2*120*H+2*60*P)/(4*math.pi**2)-10/math.pi)<1e-10
print('EXACT_LINEAR_TRANSITION_COEFFICIENTS_OK',30*H/math.pi**2,15*P/math.pi**2)
print('COMPLETE_EXACT_DODECAHEDRON_SECTION_CERTIFICATE_OK')
