"""Independent facet-hyperplane rank check for low-dimensional examples."""
from itertools import combinations
import numpy as np
from scipy.spatial import ConvexHull
from verify_skeleton import labels, edges, adjacency_formula

def check(parts):
 p=labels(parts); n=len(p); e=edges(p)
 roots=e+[(j,i) for i,j in e]
 X=np.zeros((len(roots),n-1),dtype=float)
 for k,(u,v) in enumerate(roots):
  if u<n-1:X[k,u]+=1
  if v<n-1:X[k,v]-=1
 hull=ConvexHull(X)
 eq=hull.equations
 errs=[]; ct=0
 for i,j in combinations(range(len(X)),2):
  tight=(np.abs(eq[:,:-1]@X[i]+eq[:,-1])<1e-8) & (np.abs(eq[:,:-1]@X[j]+eq[:,-1])<1e-8)
  exposed_rank=np.linalg.matrix_rank(eq[tight,:-1],tol=1e-8) if np.any(tight) else 0
  found=exposed_rank==n-2
  expected=adjacency_formula(roots[i],roots[j],p)
  if found!=expected:errs.append((roots[i],roots[j],found,expected,exposed_rank))
  ct+=found
 if errs:raise AssertionError((parts,errs[:5]))
 print('HULL PASS',parts,'edges',ct,'simplicial hyperplanes',len(eq),flush=True)
for parts in ((1,1,1),(2,1,1),(2,2,1),(3,2,1),(2,2,2)):
 check(parts)
print('ALL HULL ADJACENCIES PASSED')
