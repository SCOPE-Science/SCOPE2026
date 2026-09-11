"""Honeycomb triangulation certificate: unimodular regular subdivision of 4Delta2.
Heights H(p) = -(i^2+j^2+k^2); subdivision has 16 unit triangles, verified upper-hull.
Also computes vertices/edges of dual tropical curve and genus."""
from fractions import Fraction
import itertools, sympy as sp
from collections import Counter

pts=[(i,j) for i in range(5) for j in range(5-i)]
def Hh(p):
    i,j=p; k=4-i-j
    return Fraction(-(i*i+j*j+k*k))
tris=[t for t in itertools.combinations(pts,3)
      if abs((t[1][0]-t[0][0])*(t[2][1]-t[0][1])-(t[2][0]-t[0][0])*(t[1][1]-t[0][1]))==1]
cells=[]
planes={}
for (a,b,c) in tris:
    M=sp.Matrix([[a[0],a[1],1],[b[0],b[1],1],[c[0],c[1],1]])
    sol=M.LUsolve(sp.Matrix([Hh(a),Hh(b),Hh(c)]))
    if all(sol[0]*p[0]+sol[1]*p[1]+sol[2] >= Hh(p) for p in pts):
        cells.append((a,b,c)); planes[(a,b,c)]=(sol[0],sol[1],sol[2])
assert len(cells)==16, len(cells)
# dual vertices: (u,v) for each triangle
verts={t:(planes[t][0],planes[t][1]) for t in cells}
print("dual vertices:")
for t,v in sorted(verts.items(), key=lambda kv:(kv[1])): print(t, tuple(v))
# interior edges -> bounded edges of tropical curve
ec=Counter(); emap={}
for t in cells:
    a,b,c=t
    for e in [tuple(sorted([a,b])),tuple(sorted([b,c])),tuple(sorted([a,c]))]:
        ec[e]+=1; emap.setdefault(e,[]).append(t)
bounded=[e for e,c in ec.items() if c==2]
print("bounded tropical edges:", len(bounded))
# genus = E - V + 1 of compact part
V=len(cells); E=len(bounded)
print("genus:", E-V+1)
# vertices distinct?
print("distinct vertices:", len(set(verts.values())))
