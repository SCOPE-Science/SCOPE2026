#!/usr/bin/env python3
"""Exact wheel edge-polytope facet and fixed-point tests.
Run: python wheel_checker.py. Requires Python 3, sympy, scipy, numpy.
Tests are finite corroboration of a separate all-n proof.
"""
from itertools import combinations
from math import gcd
import numpy as np
import sympy as sp
from scipy.spatial import ConvexHull


def maximal_independent_sets(n):
    result=[]
    for mask in range(1,1<<n):
        S={i for i in range(n) if mask>>i&1}
        if any((i+1)%n in S for i in S):
            continue
        if all((i in S or (i+1)%n in S or (i-1)%n in S) for i in range(n)):
            result.append(frozenset(S))
    return result


def comps(n):
    if n<0:return 0
    if n==0:return 1
    return comps(n-2)+comps(n-3)


def data(n):
    P=np.array([[int(j==i) for j in range(n)] for i in range(n)]+[[int(j==i)+int(j==(i+1)%n) for j in range(n)] for i in range(n)],dtype=int)
    ones=tuple([1]*n)
    E=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    H=[(tuple(-v for v in E[j]),0,'coord'+str(j)) for j in range(n)]
    H.append((tuple(-v for v in ones),1,'hub'))
    if n%2: H.append((ones,-2,'rim'))
    sets=maximal_independent_sets(n)
    for S in sets:
        H.append((tuple(int(i in S) for i in range(n)),-1,'set'+str(sorted(S))))
    return P,H,sets

for n in range(4,12):
    P,H,sets=data(n)
    aa=comps(n)
    assert len([S for S in sets if 0 in S])==aa
    assert len([S for S in sets if 1 in S])==aa
    assert all(np.max(P@np.array(a)+b)==0 for a,b,_ in H)
    for a,b,label in H:
        supp=[list(map(int,p)) for p in P if sum(x*y for x,y in zip(a,p))+b==0]
        assert sp.Matrix([list(sp.Matrix(p)-sp.Matrix(supp[0])) for p in supp[1:]]).rank()==n-1,(n,label)
    h=ConvexHull(P.astype(float),qhull_options='Qx')
    for simplex in h.simplices:
        found=any(all(sum(a[j]*P[i,j] for j in range(n))+b==0 for i in simplex) for a,b,_ in H)
        assert found,(n,tuple(simplex))
    for name,vertex in [('spoke',0),('rim',n)]:
        active=[list(a) for a,b,_ in H if int(np.dot(P[vertex],a))+b==0]
        M=sp.Matrix(active)
        assert M.rank()==n
        Qsol=sp.linsolve((M,sp.ones(M.rows,1)))
        actual=bool(Qsol!=sp.EmptySet)
        expected=(n==4) if name=='spoke' else (n in (4,5,7))
        assert actual==expected,(n,name,actual,expected)
        expected_rank=aa if name=='spoke' else 2*aa-2+int(n%2==1)
        assert len(active)-n==expected_rank
        if actual:
            assert len(tuple(Qsol)[0])==n
            assert all(v.is_Integer for v in tuple(Qsol)[0])
        if name=='spoke':
            candidate=[next(a for a,b,label in H if label=='coord'+str(i)) for i in range(1,n)]
            candidate+=[next(a for a,b,label in H if label=='hub')]
        else:
            candidate=[next(a for a,b,label in H if label=='coord'+str(i)) for i in range(2,n)]
            left=next(S for S in sets if 0 in S)
            right=next(S for S in sets if 1 in S)
            candidate.append([int(i in left) for i in range(n)])
            candidate.append([int(i in right) for i in range(n)])
        assert abs(int(sp.det(sp.Matrix(candidate))))==1,(n,name)
        print('n',n,name,'ray_count',len(active),'class_rank',expected_rank,'Gorenstein',actual)
    print(' n',n,'max_stable_sets',len(sets),'a_n',aa,'facets',len(H),'qhull_simplices',len(h.simplices))
print('ALL EXACT FACET, LATTICE AND Q-GORENSTEIN TESTS PASSED')
