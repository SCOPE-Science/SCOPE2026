"""Finite reproducibility checks for stretched complete-bipartite metric transportation inballs.

Run with Python 3.10+; exhaustive independent vertex intersection check uses NumPy/SciPy.
All stated general-dimension identities follow analytically, not from these finite tests.
"""
from fractions import Fraction
from itertools import product
from math import comb
import numpy as np
from scipy.spatial import HalfspaceIntersection


def metric(m, t):
    n = 2*m
    return [[0 if i == j else t if (i < m) == (j < m) else Fraction(1)
             for j in range(n)] for i in range(n)]


def centered(f):
    mean = sum(f) / len(f)
    return tuple(v - mean for v in f)


def norm_sq(f):
    u = centered(f)
    return sum(z*z for z in u)


def predicted_normals(m, t):
    vectors = set()
    for split in (0,1):
        for bits in product((0,1), repeat=m):
            if not (any(bits) and not all(bits)):
                continue
            for other in product((0,1), repeat=m):
                inner = tuple(t*b for b in bits)
                outer = tuple(t-1+(2-t)*b for b in other)
                f = inner+outer if split == 0 else outer+inner
                vectors.add(tuple(z-f[0] for z in f))
    for first in (0,1):
        f = (Fraction(first),)*m+(Fraction(1-first),)*m
        vectors.add(tuple(z-f[0] for z in f))
    return vectors


def tight_connected(f,d):
    n=len(f)
    found={0}
    while True:
        new=set(found)
        for i in found:
            for j in range(n):
                if abs(f[i]-f[j])==d[i][j]:new.add(j)
        if new == found: break
        found=new
    return len(found)==n


def delta(m,t):
    values = [(abs(a*t+b*(2-t)-m),a,b)
              for a in range(1,m) for b in range(m+1)]
    small=min(z[0] for z in values)
    return small,[(a,b) for v,a,b in values if v==small]


def closed(m,t):
    dv,pairs=delta(m,t)
    maximum=Fraction(m,2)*(1+(t-1)**2)-dv**2/(2*m)
    contacts=2*sum(comb(m,a)*comb(m,b) for a,b in pairs)
    dim=0 if (m%2 or any(a != m//2 for a,b in pairs)) else 1
    return maximum,contacts,dim


def rank(vectors, atol=1e-8):
    arr=np.array([[float(x) for x in v] for v in vectors])
    return np.linalg.matrix_rank(arr, tol=atol)


def qhull_normals(m,t):
    n=2*m;d=metric(m,t)
    A=[];right=[]
    for i in range(n):
        for j in range(i+1,n):
            row=[0.0]*(n-1)
            if i:row[i-1]+=1
            if j:row[j-1]-=1
            A.append(row);right.append(float(d[i][j]))
            A.append([-x for x in row]);right.append(float(d[i][j]))
    halfspaces=np.hstack((np.array(A),-np.array(right)[:,None]))
    pts=HalfspaceIntersection(halfspaces,np.zeros(n-1)).intersections
    return {tuple(round(float(x),8) for x in p) for p in pts}


def check_case(m,t,independent=False):
    d=metric(m,t)
    verts=predicted_normals(m,t)
    assert len(verts)==2*(2**m-1)**2
    assert all(all(abs(f[i]-f[j])<=d[i][j] for i in range(2*m)
                       for j in range(2*m)) and tight_connected(f,d) for f in verts)
    if independent:
        brute=qhull_normals(m,t)
        expected={tuple(round(float(z),8) for z in f[1:]) for f in verts}
        assert brute==expected,(m,t,len(brute),len(expected),len(brute^expected))
    expected,contact_count,expected_dim=closed(m,t)
    actual=max(norm_sq(v) for v in verts)
    touching={v for v in verts if norm_sq(v)==expected}
    assert actual==expected
    assert len(touching)==contact_count,(len(touching),contact_count,m,t)
    affine_centers=(2*m-1)-rank([centered(v) for v in touching])
    assert affine_centers==expected_dim,(m,t,affine_centers,expected_dim)
    print(f'PASS m={m}, t={t}, vertices={len(verts)}, contact={contact_count}, '
          f'inv-radius-squared={expected}, center-locus-dim={affine_centers}, '
          f'independent-intersection={independent}')


if __name__=='__main__':
    for m in (2,3):
        for t in (Fraction(4,3),Fraction(3,2),Fraction(7,4)):
            check_case(m,t,True)
    for m in (4,5,6):
        for t in (Fraction(4,3),Fraction(3,2),Fraction(7,5)):
            check_case(m,t,False)
    print('ALL EXACT METRIC AND EUCLIDEAN-INBALL CHECKS PASSED')
