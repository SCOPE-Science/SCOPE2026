"""Exact coefficient and convex-hull checks for symmetric-base homothetic frusta.

Usage: python verify.py
Only the independent convex-hull diagnostics need NumPy and SciPy.
The rational identities run with the Python standard library.
"""
from fractions import Fraction as F
from math import comb, prod
from itertools import product

CHECKS = 0

def check(condition, label):
    global CHECKS
    assert condition, label
    CHECKS += 1

def integral_slice(n, a, s):
    """Two slice integrals, independently binomial-expanded."""
    m = n - 1
    u = 1 + s
    negative = sum(F(comb(m,k),k+1)*u**(m-k)*(-a)**k*s**(k+1)
                   for k in range(m+1))
    positive = sum(F(comb(m,k),k+1)*u**(m-k)*(-a)**k
                   for k in range(m+1))
    return negative + positive

def polynomial_formula(n, lam, s):
    if lam == 1:
        return (1+s)**n
    return (2*(1+s)**n-(1+lam*s)**n-(lam+s)**n)/F(n)*(1/(1-lam))

def mixed_coefficient(n, j, lam):
    if lam == 1:
        return F(1)
    return F(2-lam**j-lam**(n-j), n*(1-lam))

def identity_checks():
    for n in range(2,16):
        for lam in (F(0),F(1,7),F(2,5),F(9,10),F(1)):
            for s in (F(0),F(1,5),F(1),F(17,6)):
                raw = integral_slice(n,1-lam,s)
                closed = polynomial_formula(n,lam,s)
                expanded = sum(comb(n,j)*mixed_coefficient(n,j,lam)*s**j
                               for j in range(n+1))
                check(raw == closed == expanded, ('Minkowski polynomial',n,lam,s))
            V = mixed_coefficient(n,0,lam)
            check(V == sum(F(comb(n-1,k),k+1)*(-1+lam)**k for k in range(n)),
                  ('original frustum volume',n,lam))
            for j in range(n+1):
                other = mixed_coefficient(n,n-j,lam)
                check(other==mixed_coefficient(n,j,lam),('coefficient symmetry',n,j,lam))
            if lam < 1:
                r = [mixed_coefficient(n,j,lam)/V for j in range(n+1)]
                check(r[0]==r[-1]==1,('endpoint',n,lam))
                for j in range(1,n):
                    check(r[j]>=1,('lower mixed-volume bound',n,j,lam))
                if 0<lam<1:
                    for j in range(1,n):
                        check(r[j+1]-2*r[j]+r[j-1]<0,('strict concavity',n,j,lam))


def geometric_checks():
    import numpy as np
    from scipy.spatial import ConvexHull
    examples=[
        # nonspherical symmetric planar base: six vertices
        np.array([[1,0],[1,1],[0,1],[-1,0],[-1,-1],[0,-1]],float),
        # centrally symmetric cube in three base dimensions
        np.array(list(product([-1.,1.], repeat=3)),float),
    ]
    for B in examples:
        base_volume=ConvexHull(B).volume
        n=B.shape[1]+1
        for lam in (F(0),F(1,4),F(3,5),F(1)):
            v1=np.column_stack((B, np.zeros(len(B))))
            v2=np.column_stack((float(lam)*B, np.ones(len(B))))
            verts=np.concatenate((v1,v2),axis=0)
            for s in (F(1,3),F(1),F(7,4)):
                diffs=(verts[:,None,:]-float(s)*verts[None,:,:]).reshape((-1,n))
                h=ConvexHull(diffs)
                expected=float(polynomial_formula(n,lam,s))*base_volume
                check(abs(h.volume-expected)<5e-8*max(1,expected),
                      ('geometric hull',n,lam,s,h.volume,expected))

if __name__=='__main__':
    identity_checks()
    geometric_checks()
    print('VERIFY_OK',CHECKS,'tests')
