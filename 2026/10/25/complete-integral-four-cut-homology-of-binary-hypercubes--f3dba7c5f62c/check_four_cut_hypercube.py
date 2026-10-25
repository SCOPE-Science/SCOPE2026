#!/usr/bin/env python3
"""Reproduce the finite integral base calculation and small-cube rank checks.
Requires Python 3.10+ and SymPy 1.12+; all graphs and boundary matrices are generated here.
"""
from itertools import combinations
from math import comb
from collections import defaultdict
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def connected_four_sets(d):
    n=1<<d
    def connected(q):
        seen={q[0]}; queue=[q[0]]
        for x in queue:
            for y in q:
                if y not in seen and (x^y).bit_count()==1:
                    seen.add(y);queue.append(y)
        return len(seen)==4
    return [q for q in combinations(range(n),4) if connected(q)]

def signed_boundary(rows, cols):
    r={f:i for i,f in enumerate(rows)}
    b=Matrix.zeros(len(rows),len(cols))
    for j,face in enumerate(cols):
        for i in range(len(face)):
            b[r[face[:i]+face[i+1:]],j]=(-1)**i
    return b

def binary_rank_boundary(d,quadruples):
    n=1<<d
    t={a:i for i,a in enumerate(combinations(range(n),3))}
    piv={}
    for q in quadruples:
        v=0
        for f in combinations(q,3):v^=1<<t[f]
        while v:
            i=v.bit_length()-1
            if i not in piv:
                piv[i]=v;break
            v^=piv[i]
    return len(piv)

quads=connected_four_sets(3)
assert len(quads)==38
tri=list(combinations(range(8),3))
assert set(tri)==set(t for q in quads for t in combinations(q,3))
B=signed_boundary(tri,quads)
D=smith_normal_form(B,domain=ZZ)
diag=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols))]
assert diag.count(1)==35 and diag.count(0)==3 and set(diag)=={0,1}
assert signed_boundary(list(combinations(range(8),2)),tri).rank()==21
print('LOCAL_Q3: (vertices,edges,triangles,tetrahedra)=(8,28,56,38); SNF(d3): 35 ones, 3 zeros; rank(d2)=21')
for d in range(3,7):
    quads=connected_four_sets(d)
    n=1<<d
    f0=n;f1=d*(1<<(d-1));f2=comb(d,2)*(1<<(d-2));f3=comb(d,3)*(1<<(d-3))
    assert len(quads)==32*f3+f2
    beta3=4*f3-f2+f1-f0+1
    beta2=comb(n,3)-comb(n,2)-28*f3-2*f2+f1
    rank_mod2=binary_rank_boundary(d,quads)
    assert len(quads)-rank_mod2==beta3
    print('Q%d: N=%d, connected-four=%d, mod2-boundary-rank=%d, beta_dual_3=%d, beta_dual_2=%d'%(d,n,len(quads),rank_mod2,beta3,beta2))
print('FINITE_CHECKS_OK')
