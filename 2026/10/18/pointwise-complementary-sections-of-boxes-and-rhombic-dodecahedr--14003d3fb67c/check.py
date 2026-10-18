#!/usr/bin/env python3
"""Standalone exact incidence and numerical distribution checks for two affine polytopes.
Requires Python, NumPy, and SymPy. All random checks are supplementary.
"""
import itertools as it
import math
import numpy as np
import sympy as sp

# Vertices and edges of a unit cube and its rhombic-dodecahedral companion.
C=list(it.product((-1,1),repeat=3))
R=[tuple(2*q if i==j else 0 for j in range(3)) for i in range(3) for q in (-1,1)]+C
EC=[(i,j) for i,j in it.combinations(range(8),2) if sum((C[i][k]-C[j][k])**2 for k in range(3))==4]
ER=[(i,j) for i,j in it.combinations(range(14),2) if sum((R[i][k]-R[j][k])**2 for k in range(3))==3]
assert len(C)==8 and len(R)==14 and len(EC)==12 and len(ER)==24
assert sorted(sum(i in edge for edge in ER) for i in range(14))==[3]*8+[4]*6
# Twelve exact rhombic facet inequalities show the full edge graph.
for i,j in it.combinations(range(3),2):
    for si,sj in it.product((-1,1),repeat=2):
        lhs=[si*w[i]+sj*w[j] for w in R]
        assert all(z<=2 for z in lhs) and lhs.count(2)==4
# Every cube edge has two partner dodecahedral edges, one incident to
# each endpoint. If u_i>0 and the low/high endpoint scalar products are
# L<H, then the two partner-crossing indicators and the cube-edge crossing
# indicator sum to 1 for each of three possible strict sign pairs.
for low,high in ((-1,-1),(-1,1),(1,1)):
    cube=int(low!=high)
    rhombic=int(low==1)+int(high==-1)
    assert cube+rhombic==1
# Test exact identities on rational normals and positive rational affine scales.
for a in ((1,1,1),(1,2,5),(2,3,7),(3,8,10)):
    for u in it.product((-5,-2,-1,1,2,5),repeat=3):
        sv=[sum(u[k]*a[k]*v[k] for k in range(3)) for v in R]
        sc=[sum(u[k]*a[k]*v[k] for k in range(3)) for v in C]
        if 0 in sv or 0 in sc:continue
        nr=sum(sv[i]*sv[j]<0 for i,j in ER)
        nc=sum(sc[i]*sc[j]<0 for i,j in EC)
        assert nr+nc==12 and nr in (6,8) and nc in (4,6)
# For a general affine map, the replacement normal is T^t u;
# the incidence identity above therefore transfers verbatim.

# Numeric verification of exact Haar law at multiple anisotropies.
rng=np.random.default_rng(194819)
u=rng.normal(size=(150000,3));u/=np.linalg.norm(u,axis=1,keepdims=True)
for a in ((1,1,1),(2,3,5),(1,1,10),(.1,3,10)):
    a=np.array(a,dtype=float); r=np.linalg.norm(a)
    p6=4/math.pi*sum(math.asin(float(t/r)) for t in a)-2
    assert 0<p6<1
    vv=np.array(R,float)*a
    ss=np.sign(u@vv.T)
    nr=sum((ss[:,i]*ss[:,j]<0) for i,j in ER)
    assert np.all((nr==6)|(nr==8))
    p6sample=float(np.mean(nr==6))
    assert abs(p6sample-p6)<.008,(a,p6,p6sample)
    print('GEOMETRY_CHECK',a.tolist(),'exact_P6',repr(p6),'sample_P6',repr(p6sample))

# Symbolic second-order expansion on the mean-zero logarithmic slice:
# take (t1,t2,t3)=(h,-h,0), then the exact coefficient is -2/(pi*sqrt(2)).
h=sp.symbols('h',real=True)
# For total S=3+4h^2+O(h^4), x_i=e^ti/sqrt(S).
base=sp.asin(1/sp.sqrt(3))
S=sp.exp(2*h)+sp.exp(-2*h)+1
f=4/sp.pi*(sp.asin(sp.exp(h)/sp.sqrt(S))+sp.asin(sp.exp(-h)/sp.sqrt(S))+sp.asin(1/sp.sqrt(S)))-2
assert sp.simplify(sp.diff(f,h).subs(h,0))==0
assert sp.simplify(sp.diff(f,h,2).subs(h,0)+2*sp.sqrt(2)/sp.pi)==0
pmax=12/sp.pi*base-2
assert abs(float(pmax)-0.3509593121836443)<1e-13
print('CHECK_OK','cube_edges',len(EC),'rhombic_edges',len(ER),'pointwise_sum',12,'P6_cubic',float(pmax))
