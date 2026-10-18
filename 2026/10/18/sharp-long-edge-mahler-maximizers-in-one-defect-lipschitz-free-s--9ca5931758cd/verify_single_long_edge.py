"""Finite cross-checks for a one-exceptional-distance Lipschitz-free ball.

Usage: python verify_single_long_edge.py

Requires NumPy and SciPy for combinatorial hull detection. All volumes
are reconstructed from exact rational determinants of vertex coordinates.
This is corroborative finite-dimensional evidence, not a general proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from scipy.spatial import ConvexHull, HalfspaceIntersection
import numpy as np


def determinant(A):
    """Exact determinant by elimination over fractions."""
    m = len(A)
    b = [list(row) for row in A]
    sign = 1
    out = F(1)
    for k in range(m):
        pivot = next((i for i in range(k, m) if b[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            sign = -sign
        p = b[k][k]
        out *= p
        for i in range(k+1, m):
            if b[i][k]:
                c = b[i][k]/p
                for j in range(k+1, m):
                    b[i][j] -= c*b[k][j]
                b[i][k] = F(0)
    return sign*out


def hull_volume(vertices):
    d=len(vertices[0]); arr=np.array([[float(y) for y in row] for row in vertices])
    # The origin is strictly inside these symmetric full-dimensional polytopes.
    hull=ConvexHull(arr)
    total=F(0)
    for simp in hull.simplices:
        rows=[vertices[int(i)] for i in simp]
        total += abs(determinant(rows))/factorial(d)
    return total


def trial(d, t):
    n=d+1
    def e(i):
        return [F(int(j==i)) for j in range(1,n)]
    vs=[]; hs=[]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            dist=t if {i,j}=={1,2} else F(1)
            diff=[x-y for x,y in zip(e(i),e(j))]
            vs.append([x/dist for x in diff])
            hs.append([float(x) for x in diff]+[-float(dist)])
    primal=hull_volume(vs)
    # Get all dual-ball vertices from the bounding difference inequalities.
    # TU incidence matrices imply coordinates lie in the denominator-t lattice.
    corners=HalfspaceIntersection(np.array(hs),np.zeros(d)).intersections
    q=t.denominator
    dual_vertices=[];seen=set()
    for row in corners:
        v=tuple(F(int(round(float(z)*q)),q) for z in row)
        if v in seen: continue
        for i in range(n):
            for j in range(n):
                if i==j:continue
                dist=t if {i,j}=={1,2} else F(1)
                assert (F(0) if i==0 else v[i-1])-(F(0) if j==0 else v[j-1]) <= dist
        seen.add(v);dual_vertices.append(v)
    dual=hull_volume(dual_vertices)
    C=comb(2*d,d)
    expected_primal=F(C, factorial(d))-F(2**d, factorial(d))*(1-F(1)/t)
    expected_dual=F(d+1)+F(2,d)*(1-(F(2)-t)**d)
    assert primal==expected_primal,(d,t,'primal',primal,expected_primal)
    assert dual==expected_dual,(d,t,'dual',dual,expected_dual)
    assert primal*dual==expected_primal*expected_dual
    return len(dual_vertices),primal,dual

if __name__=='__main__':
    count=0
    for d in [2,3,4,5]:
        for t in [F(1),F(5,4),F(3,2),F(2)]:
            nv,p,q=trial(d,t)
            print(f'd={d} t={t} dual_vertices={nv} primal={p} polar={q}')
            count+=1
    print('EXACT_ONE_DEFECT_VOLUME_CHECKS_PASS',count,'cases')
