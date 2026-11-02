#!/usr/bin/env python3
"""Independent finite exact boundary checks for weighted-tree p-heat Lipschitz criteria.
Only Python standard library is required. Tests do not substitute for universal proofs.
"""
from fractions import Fraction as Q
from itertools import product
import math

def phi(x,p):
    return (abs(x)**(p-2))*x if x else 0.

def tree_data(edges, masses, conductances, lengths):
    n=len(masses)
    assert len(edges)==n-1==len(conductances)==len(lengths)
    # Check acyclic connectivity by simple union-find.
    parent=list(range(n))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for a,b in edges:
        ra,rb=root(a),root(b)
        assert ra!=rb
        parent[ra]=rb
    assert len({root(i) for i in range(n)})==1
    return n

def rates(edges,masses,c):
    return [ (Q(1,masses[u])+Q(1,masses[v]))*c[e] for e,(u,v) in enumerate(edges)]

def predicted(edges,masses,c,ell,p):
    out=[]
    for i,(u,v) in enumerate(edges):
        left=c[i]*(ell[i]**(p-1))*(1/masses[u]+1/masses[v])
        right=sum(c[j]*(ell[j]**(p-1))/masses[w]
                  for j,(a,b) in enumerate(edges) if j!=i
                  for w in (u,v) if w==a or w==b)
        out.append((left,right))
    return out

def edge_flow(edges,masses,c,g,p):
    n=len(masses); v=[0]*n
    for (a,b),w,z in zip(edges,c,g):
        flow=w*phi(z,p)
        v[a]+=flow/masses[a];v[b]-=flow/masses[b]
    return [v[b]-v[a] for a,b in edges]

def boundary_exhaustive(edges,masses,c,ell,p):
    n=len(edges); expected=predicted(edges,masses,c,ell,p)
    for i in range(n):
        best=-1e100
        for signs in product([-1,1],repeat=n):
            g=[signs[j]*ell[j] for j in range(n)]
            derivative=edge_flow(edges,masses,c,g,p)[i]*signs[i]/ell[i]
            best=max(best,derivative)
        exact=(expected[i][1]-expected[i][0])/ell[i]
        assert abs(best-exact)<1e-9,(i,best,exact)
    return n*(2**n)

def check_star(q,m0,mi):
    # Existence iff sum_i 1/(2 + m0/mi) <= 1.
    beta=[Q(2)+Q(m0,m) for m in mi]
    lhs=sum((1/b for b in beta),Q(0))
    x=[1/b for b in beta]
    if lhs<Q(1):
        # Distribute the slack as extra x_e while maintaining sum x = 1.
        x=[v+(1-lhs)/q for v in x]
    if lhs<=1:
        S=sum(x)
        assert all(beta[i]*x[i]>=S for i in range(q))
    else:
        assert lhs>1
    return lhs

checks=0
cases=[
 ([(0,1)], [Q(3),Q(4)],[Q(2)],[Q(5)]),
 ([(0,1),(1,2)],[Q(1),Q(1),Q(1)],[Q(1),Q(1)],[Q(1),Q(1)]),
 ([(0,1),(0,2),(0,3)],[Q(1)]*4,[Q(1)]*3,[Q(1)]*3),
 ([(0,1),(0,2),(0,3),(0,4)],[Q(2)]+[Q(1)]*4,[Q(1)]*4,[Q(1)]*4),
 ([(0,1),(0,2),(0,3),(0,4)],[Q(1)]*5,[Q(1)]*4,[Q(1)]*4),
 ([(0,1),(1,2),(1,3),(3,4)],[Q(1),Q(2),Q(3),Q(4),Q(2)],[Q(1),Q(3),Q(2),Q(4)],[Q(1),Q(2),Q(1),Q(3)]),
]
for E,m,c,ell in cases:
    tree_data(E,m,c,ell)
    for p in (2,3,4):
        checks+=boundary_exhaustive(E,m,c,ell,p)
print('BOUNDARY_EXACT_OK cases=',len(cases)*3,'signed_faces=',checks)
assert check_star(4,2,[1]*4)==1
assert check_star(4,1,[1]*4)==Q(4,3)
assert check_star(3,1,[1]*3)==1
assert check_star(5,8,[1]*5)==Q(1,2)
assert check_star(5,3,[1]*5)==1
print('STAR_MASS_THRESHOLD_EXACT_OK q=3,4,5')
# Independent explicit two-solution expansion witnesses on the 3-vertex path.
E=[(0,1),(1,2)];m=[1.,1.,1.];c=[1.,1.]
for p in (1.2,1.5,2.5,3,4,5):
    y=4**(1/(p-2))
    base=[1.,y]
    delta=[1.,1.]
    # Derived directional derivative of first edge-flow component.
    expected=2*(p-1)
    h=1e-6*min(1,y)
    plus=[base[i]+h*delta[i] for i in range(2)]
    diff=[(a-b)/h for a,b in zip(edge_flow(E,m,c,plus,p),edge_flow(E,m,c,base,p))]
    assert abs(diff[0]-expected)<max(1e-3*expected,1e-5),(p,diff,expected)
    assert diff[0]>0
    print('TWO_INPUT_WITNESS_OK p=',p,'d_dt_first_gradient=',round(diff[0],7))
print('ALL_TREE_P_HEAT_LIPSCHITZ_CHECKS_OK')
