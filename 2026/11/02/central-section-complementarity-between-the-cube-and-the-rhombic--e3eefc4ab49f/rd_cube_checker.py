"""Reproduce central-section complementarity for the cube and rhombic dodecahedron.

Python 3, numpy. Rational vertex/facet/edge checks and independent Haar sampling.
"""
import itertools
import math
from collections import Counter
from fractions import Fraction
import numpy as np

X = (-1, 1)
D = tuple(tuple(2*s if j == i else 0 for j in range(3))
          for i in range(3) for s in X) + tuple(itertools.product(X, repeat=3))
C = tuple(itertools.product(X, repeat=3))
# Every facet is a halfspace (s*x_i+t*x_j <= 2) with i < j.
FACETS = tuple((i,j,s,t) for i in range(3) for j in range(i+1,3)
               for s in X for t in X)
assert len(D) == 14 and len(set(D)) == 14 and len(FACETS) == 12
assert all(s*v[i]+t*v[j] <= 2 for v in D for i,j,s,t in FACETS)
# Exhaustively solve all triples of independent active halfspaces in exact
# arithmetic; this independently certifies that there are NO hidden vertices.
def determinant(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
planes=[]
for i,j,s,t in FACETS:
    a=[0,0,0];a[i]=s;a[j]=t
    planes.append(tuple(a))
all_vertices=set()
for rows in itertools.combinations(planes,3):
    det=determinant(rows)
    if not det:continue
    sol=[]
    for k in range(3):
        mat=[[2 if j==k else rows[i][j] for j in range(3)] for i in range(3)]
        sol.append(Fraction(determinant(mat),det))
    if all(sum(row[j]*sol[j] for j in range(3))<=2 for row in planes):
        all_vertices.add(tuple(sol))
assert all_vertices==set(D),(len(all_vertices),all_vertices.symmetric_difference(set(D)))
print('EXACT_EXHAUSTIVE_HALFSPACE_VERTEX_ENUMERATION_PASSED')
facet_vertices=[]
for i,j,s,t in FACETS:
    f=frozenset(v for v in D if s*v[i]+t*v[j]==2)
    assert len(f)==4
    facet_vertices.append(f)
# The 24 edges are precisely two-vertex intersections of distinct facet pairs.
d_edges=set()
for a,b in itertools.combinations(facet_vertices,2):
    common=a & b
    if len(common)==2: d_edges.add(frozenset(common))
assert len(d_edges)==24
# Analytically anticipated axial-cubic incidence, checked against facet construction.
expected_d_edges={frozenset((v,w)) for v in D[:6] for w in C
                  if sum(p*q for p,q in zip(v,w))==2}
assert d_edges==expected_d_edges
c_edges={frozenset((v,w)) for v,w in itertools.combinations(C,2)
         if sum(abs(v[i]-w[i]) for i in range(3))==2}
assert len(c_edges)==12
print('EXACT_POLYTOPE_12_FACETS_24_EDGES_PASSED')

def counts(u):
    def dot(v):return sum(x*y for x,y in zip(u,v))
    assert all(dot(v) != 0 for v in D)
    n_d=sum(dot(v)*dot(w)<0 for v,w in (tuple(e) for e in d_edges))
    n_c=sum(dot(v)*dot(w)<0 for v,w in (tuple(e) for e in c_edges))
    return n_c,n_d

for rep,expected in [((3,3,3),(6,6)), ((5,2,1),(4,8))]:
    seen=set()
    for permutation in itertools.permutations(rep):
        for signs in itertools.product(X,repeat=3):
            u=tuple(a*b for a,b in zip(permutation,signs))
            if u in seen:continue
            seen.add(u)
            assert counts(u)==expected,(u,counts(u))
    assert len(seen)>=8
print('EXHAUSTIVE_SIGNED_COORDINATE_CHAMBERS_AND_POINTWISE_COMPLEMENT_PASSED')

ang=math.acos(1/3)
area=3*ang-math.pi
p_hex=8*area/(4*math.pi)
assert abs(p_hex-(1-6*math.asin(1/3)/math.pi))<1e-14
assert abs(p_hex-0.3509593121836436)<1e-14
print('EXACT_SPHERICAL_GIRARD_IDENTITY_PASSED',p_hex)

rng=np.random.default_rng(20261029)
ns=150000
z=rng.standard_normal((ns,3))
# Distinct independently evaluated sign-change counts against direct condition.
res=Counter()
for k in range(0,ns,1000):
    batch=z[k:k+1000]
    cv=np.array(C,dtype=np.int64)
    dv=np.array(D,dtype=np.int64)
    cprods=batch@cv.T
    dprods=batch@dv.T
    ci={v:i for i,v in enumerate(C)};di={v:i for i,v in enumerate(D)}
    csum=np.zeros(len(batch),dtype=np.int64)
    dsum=np.zeros(len(batch),dtype=np.int64)
    for e in c_edges:
        v,w=tuple(e)
        csum+=(cprods[:,ci[v]]*cprods[:,ci[w]]<0)
    for e in d_edges:
        v,w=tuple(e)
        dsum+=(dprods[:,di[v]]*dprods[:,di[w]]<0)
    assert np.all(csum+dsum==12)
    res.update(zip(csum.tolist(),dsum.tolist()))
assert set(res)=={(4,8),(6,6)}
emp=res[(6,6)]/ns
assert abs(emp-p_hex)<5*math.sqrt(p_hex*(1-p_hex)/ns)
print('INDEPENDENT_GAUSSIAN_ORIENTATION_SAMPLING_PASSED',ns,res,'p_hex',emp)
print('ALL_CHECKS_PASSED')
