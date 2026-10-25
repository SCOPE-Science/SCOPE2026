"""Exact reproducibility checks for split-graph stable-set polytope inertia.
Only finite instances are tested; the general theorem uses the accompanying proof.
"""
from fractions import Fraction
from math import factorial, prod
from itertools import product
from scipy.spatial import ConvexHull
import numpy as np


def rising(a, k):
    return prod(range(a, a+k))


def beta_moment(p, q, k, l):
    # For the volume-weighted slice parameter T ~ Beta(p,q+1).
    return Fraction(rising(p,k)*rising(q+1,l), rising(p+q+1,k+l))


def direct_moments(p, q):
    """Construct full covariance from raw polynomial slice integrals."""
    n = p+q
    if p == 0:
        return [[Fraction(int(i==j),12) for j in range(n)] for i in range(n)]
    mt = lambda k,l: beta_moment(p,q,k,l)
    mean = [mt(1,0)/p]*p + [mt(0,1)/2]*q
    def raw(i,j):
        if i<p and j<p:
            coeff = Fraction(2 if i==j else 1, p*(p+1))
            return coeff*mt(2,0)
        if i>=p and j>=p:
            return Fraction(1 if i==j else 1,3 if i==j else 4)*mt(0,2)
        return mt(1,1)/Fraction(2*p,1)
    return [[raw(i,j)-mean[i]*mean[j] for j in range(n)] for i in range(n)]


def theoretical_moments(p,q):
    n=p+q
    u=Fraction(1,(n+1)*(n+2))
    v=Fraction(1,(n+1)**2*(n+2))
    lam=Fraction((q+1)*(q+2),12*(n+1)*(n+2))
    return [[(u*(i==j)-v) if i<p and j<p else
             (-Fraction(q+1,2)*v) if (i<p)!=(j<p) else
             (lam*(i==j)+Fraction(p*(q+1),4)*v)
             for j in range(n)] for i in range(n)]


def split_vertices(p,q):
    n=p+q
    result=[]
    for ss in product([0.,1.], repeat=q): result.append([0.]*p+list(ss))
    for j in range(p):
        v=[0.]*n;v[j]=1.;result.append(v)
    return np.array(result)


def det_frac(a):
    n=len(a)
    b=[list(row) for row in a]
    d=Fraction(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if b[i][k]),None)
        if pivot is None:return Fraction(0)
        if pivot!=k:
            b[k],b[pivot]=b[pivot],b[k]
            d=-d
        c=b[k][k];d*=c
        for i in range(k+1,n):
            t=b[i][k]/c
            for j in range(k+1,n):b[i][j]-=t*b[k][j]
            b[i][k]=0
    return d


def claimed_det(p,q):
    n=p+q
    return Fraction((q+1)**(q+1)*(q+2)**q,
                    12**q*(n+1)**(n+1)*(n+2)**n)

count=0
for p in range(0,6):
    for q in range(1,6):
        n=p+q
        if n>9: continue
        actual=direct_moments(p,q)
        expected=theoretical_moments(p,q)
        assert actual == expected,(p,q,'covariance')
        assert det_frac(actual) == claimed_det(p,q),(p,q,'determinant')
        if p and q:
            # Shear: Z_j = Y_j + (sum_i X_i)/2, independently check zero covariances.
            for i in range(p):
                for j in range(q):
                    cross=actual[i][p+j]+sum(actual[i][k] for k in range(p))/2
                    assert cross==0,(p,q,'shear cross')
            for j in range(q):
                for k in range(q):
                    var=actual[p+j][p+k]
                    var += Fraction(1,2)*sum(actual[i][p+j]+actual[i][p+k] for i in range(p))
                    var += Fraction(1,4)*sum(actual[i][h] for i in range(p) for h in range(p))
                    assert var == (Fraction((q+1)*(q+2),12*(n+1)*(n+2)) if j==k else 0)
        count+=1

hulls=0
for p in range(0,4):
    for q in range(1,5):
        n=p+q
        if n>6:continue
        vv=split_vertices(p,q)
        if n==1:volume=np.ptp(vv[:,0])
        else:volume=ConvexHull(vv).volume
        goal=factorial(q)/factorial(n)
        assert abs(volume-goal)<1e-9,(p,q,volume,goal)
        hulls+=1

ratios=0
for q in range(2,500):
    r=((q+1)/q)**2*(1+2/q)**q/12
    assert r<1,(q,r)
    ratios+=1

print(f'VERIFY_OK exact_covariance_determinants={count} convex_hull_volumes={hulls} strict_ratio_cases={ratios}')
