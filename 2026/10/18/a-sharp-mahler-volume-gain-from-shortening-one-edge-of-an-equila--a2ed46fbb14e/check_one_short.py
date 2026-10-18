"""Finite rational polytope checks for a one-short-pair Lipschitz-free family.

Requires Python 3, NumPy and SciPy. All input coordinates, vertex solves,
facet-simplex determinants and accumulated volume values are exact Fractions;
Qhull is used only to triangulate the hull boundaries combinatorially.
This checks finite examples; the general theorem is proved separately.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
import numpy as np
from scipy.spatial import ConvexHull


def determinant(matrix):
    A = [list(row) for row in matrix]
    n = len(A)
    det = F(1)
    for k in range(n):
        p = next((i for i in range(k,n) if A[i][k]), None)
        if p is None: return F(0)
        if p != k:
            A[k],A[p] = A[p],A[k]
            det = -det
        pivot = A[k][k]
        det *= pivot
        for i in range(k+1,n):
            scale = A[i][k]/pivot
            for j in range(k+1,n): A[i][j] -= scale*A[k][j]
            A[i][k] = F(0)
    return det


def solve(A,b):
    n=len(b)
    C=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        p=next((i for i in range(k,n) if C[i][k]),None)
        if p is None:return None
        C[k],C[p]=C[p],C[k]
        v=C[k][k]
        for j in range(k,n+1):C[k][j]/=v
        for i in range(n):
            if i==k:continue
            v=C[i][k]
            for j in range(k,n+1):C[i][j]-=v*C[k][j]
    return tuple(row[n] for row in C)


def make_vertices(N,t):
    d=N-1
    pairs=[]
    for a,b in combinations(range(N),2):
        v=[F(0)]*d
        if a>0:v[a-1]+=1
        if b>0:v[b-1]-=1
        w=t if (a,b)==(0,1) else F(1)
        pairs.append((tuple(v),w))
    P=set()
    inequalities=[]
    for v,w in pairs:
        P.add(tuple(x/w for x in v))
        P.add(tuple(-x/w for x in v))
        inequalities.extend([(v,w),(tuple(-x for x in v),w)])
    Q=set()
    for idx in combinations(range(len(inequalities)),d):
        rows=[inequalities[i][0] for i in idx]
        vals=[inequalities[i][1] for i in idx]
        x=solve(rows,vals)
        if x is None:continue
        if all(sum(v[j]*x[j] for j in range(d))<=w for v,w in inequalities):
            Q.add(x)
    return sorted(P),sorted(Q)


def volume(points):
    d=len(points[0])
    hull=ConvexHull(np.array([[float(x) for x in v] for v in points]))
    total=F(0)
    for simplex in hull.simplices:
        matrix=[points[int(i)] for i in simplex]
        total+=abs(determinant(matrix))
    # All origin-coned boundary simplices form a disjoint volume partition.
    return total/factorial(d)


def expected(N,t):
    d=N-1
    A=F(comb(2*d,d),factorial(d))
    pv=A*(d-1+d/t)/F(2*d-1)
    qv=2*d*t-(d-1)*t*t
    return pv,qv


def run():
    examples=0
    for N in range(3,6):
        for t in (F(1,2),F(2,3),F(3,4),F(1)):
            P,Q=make_vertices(N,t)
            vp,vq=volume(P),volume(Q)
            ep,eq=expected(N,t)
            assert (vp,vq)==(ep,eq),(N,t,vp,vq,ep,eq)
            examples+=1
            print(f'N={N}, t={t}, |P|={vp}, |Q|={vq}, Mahler={vp*vq}, dual_vertices={len(Q)}')
    for N in range(4,25):
        d=N-1
        t=F(d,2*(d-1))
        def product(z):return expected(N,z)[0]*expected(N,z)[1]
        assert product(t)>product(F(1))
        assert product(t)>product(F(1,1000))
        assert product(t)>product(F(99,100))
    print(f'ALL {examples} EXACT RATIONAL POLYTOPE-VOLUME TESTS PASSED')

if __name__=='__main__':run()
