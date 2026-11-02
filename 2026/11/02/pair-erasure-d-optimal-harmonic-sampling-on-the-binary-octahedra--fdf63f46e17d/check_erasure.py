"""Standalone exact checks of two-erasure harmonic Gram determinants on binary octahedral points."""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction
import math
import numpy as np
import sympy as sp


def octahedral_points():
    vectors = []
    for j in range(4):
        for sign in (-1,1):
            x = [0.]*4; x[j] = float(sign); vectors.append(x)
    for signs in product((-1,1), repeat=4):
        vectors.append([s/2 for s in signs])
    for i,j in combinations(range(4),2):
        for a,b in product((-1,1),repeat=2):
            x=[0.]*4; x[i]=a/math.sqrt(2); x[j]=b/math.sqrt(2); vectors.append(x)
    assert len(vectors)==48
    kept=[]
    for v in vectors:
        if not any(np.max(np.abs(np.array(v)+np.array(w)))<1e-12 for w in kept):
            kept.append(v)
    assert len(kept)==24
    return np.asarray(kept)


def quaternion_product(a,b):
    x,y,z=a[1:]; u,v,w=b[1:]
    return np.array([a[0]*b[0]-x*u-y*v-z*w,
                     a[0]*u+x*b[0]+y*w-z*v,
                     a[0]*v-x*w+y*b[0]+z*u,
                     a[0]*w+x*v-y*u+z*b[0]])


def class_of(a,b):
    q = quaternion_product(a*np.array([1,-1,-1,-1]),b)
    r = abs(q[0]); tol=1e-10
    if abs(r-1/math.sqrt(2))<tol:
        return 'four_cycle'
    if abs(r-0.5)<tol:
        return 'three_cycle'
    assert r<tol, q
    nz=sum(abs(v)>tol for v in q[1:])
    return 'double_transposition' if nz==1 else 'transposition' if nz==2 else 'invalid'


def U12(t):
    u,v=np.ones_like(t),2*t
    for _ in range(2,13):
        u,v=v,2*t*v-u
    return v


def verify():
    X=octahedral_points()
    D=X@X.T
    pred=np.rint(U12(D)).astype(int)
    assert np.max(abs(U12(D)-pred))<1e-8
    assert set(np.unique(pred))=={-1,1,13}
    names={}; counts=Counter()
    for i,j in combinations(range(24),2):
        k=class_of(X[i],X[j]); names[(i,j)]=k; counts[k]+=1
    expected_counts={'three_cycle':96,'double_transposition':36,'four_cycle':72,'transposition':72}
    assert dict(counts)==expected_counts,counts
    M=sp.Matrix(pred.tolist())
    assert M==M.T
    # Direct check of an integral adjacency construction, independent of S4 character orthogonality.
    A=sp.zeros(24)
    for (i,j),kind in names.items():
        if kind=='four_cycle': A[i,j]=A[j,i]=1
    assert M==12*sp.eye(24)+sp.ones(24,24)-2*A
    assert all(sum(A.row(i))==6 for i in range(24))
    chpoly=sp.factor(M.charpoly().as_expr())
    lam=M.charpoly().gen
    expect=(lam-24)**2*(lam-12)**4*(lam-8)**9*(lam-16)**9
    assert sp.expand(chpoly-expect)==0,(chpoly,expect)
    inv=M.inv()
    diag=sp.Rational(101,1152)
    assert all(inv[i,i]==diag for i in range(24))
    betas={'three_cycle':sp.Rational(-4,1152),
           'double_transposition':sp.Rational(-7,1152),
           'four_cycle':sp.Rational(9,1152),
           'transposition':sp.Rational(-9,1152)}
    factors={}
    for (i,j),kind in names.items():
        assert inv[i,j]==betas[kind],(i,j,kind,inv[i,j])
        factors[kind]=diag**2-inv[i,j]**2
    numerators={k:int(v*1152**2) for k,v in factors.items()}
    assert numerators=={'three_cycle':10185,'double_transposition':10152,
                        'four_cycle':10120,'transposition':10120},numerators
    det=24**2*12**4*8**9*16**9
    assert M.det()==det
    # Recompute actual 22-by-22 integer determinants in each of four geometrical types.
    for kind in expected_counts:
        i,j=next((a,b) for (a,b),c in names.items() if c==kind)
        remaining=[k for k in range(24) if k not in (i,j)]
        direct=M.extract(remaining,remaining).det(method='domain-ge')
        assert direct==det*factors[kind],(kind,direct)
    assert 10185>10152>10120
    assert sum(expected_counts.values())==276
    print('PASS: exact 24-point Gram, entire rational inverse, all 276 erasure pairs,')
    print('four representative exact 22x22 determinants, integer eigenvalue multiplicities.')
    print('count and determinant multipliers:', expected_counts, numerators)

if __name__=='__main__': verify()
