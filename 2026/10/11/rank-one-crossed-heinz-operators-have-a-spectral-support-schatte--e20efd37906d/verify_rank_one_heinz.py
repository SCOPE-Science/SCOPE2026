#!/usr/bin/env python3
"""Exact-rational checks of a crossed/ordinary Heinz rank-one witness.

This checks selected finite identities; the operator theorem requires the
separate spectral-measure and exterior-power arguments in RESULT.md.
"""
from fractions import Fraction as F
from math import isqrt


def dot(x, y):
    return sum((a*b for a,b in zip(x,y)), F(0))


def moments(weights, f, g):
    assert sum(weights, F(0)) == 1
    mf=dot(weights,f)
    mg=dot(weights,g)
    vf=sum((w*(x-mf)**2 for w,x in zip(weights,f)),F(0))
    vg=sum((w*(y-mg)**2 for w,y in zip(weights,g)),F(0))
    cov=sum((w*(x-mf)*(y-mg) for w,x,y in zip(weights,f,g)),F(0))
    return vf,vg,cov


def frobenius_sq(mat):
    return sum((x*x for row in mat for x in row), F(0))


def rank2_singular_product_sq(C):
    # Product of nonzero singular values squared equals sum of squared 2x2 minors.
    n=len(C)
    ans=F(0)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                for l in range(k+1,n):
                    d=C[i][k]*C[j][l]-C[i][l]*C[j][k]
                    ans+=d*d
    return ans


def test_witness():
    # A=diag(1,16,81), B=uu*, u=(1,1,1)/sqrt(3), t=1/4.
    f=(F(1),F(2),F(3))  # eigenvalues of A^(1/4)
    g=(F(1),F(8),F(27)) # eigenvalues of A^(3/4)
    p=(F(1,3),)*3
    vf,vg,cov=moments(p,f,g)
    assert (vf,vg,cov)==(F(2,3),F(362,3),F(26,3))
    C=[[F(f[i]+g[j],3) for j in range(3)] for i in range(3)]
    H=[[F(f[i]+g[i],3) for j in range(3)] for i in range(3)]
    assert frobenius_sq(C)==F(952,3)
    assert frobenius_sq(H)==F(1004,3)
    assert frobenius_sq(H)-frobenius_sq(C)==2*cov==F(52,3)
    assert rank2_singular_product_sq(C)==vf*vg==F(724,9)
    # Exact squared trace gap is 4(sqrt(181)-13)/3 > 0.
    assert 181 > 13*13
    assert vf*vg>cov*cov
    # H has rank one; the two positive singular values of C have
    # squares summing 952/3 and product 2*sqrt(181)/3.
    print('RANK_ONE_CROSSED_HEINZ_EXACT_WITNESS_OK')


def test_boundary_cases():
    for lambdas in ((1,16),(1,81),(16,81)):
        f=tuple(F(isqrt(isqrt(k))) for k in lambdas)
        g=tuple(x**3 for x in f)
        assert tuple(x**4 for x in f)==lambdas
        vf,vg,cov=moments((F(1,2),F(1,2)),f,g)
        assert vf*vg==cov*cov and cov>0
    # Equal powers at t=1/2 yield zero trace defect for three spectral points.
    vf,vg,cov=moments((F(1,3),)*3,(F(1),F(2),F(3)),(F(1),F(2),F(3)))
    assert vf==vg==cov==F(2,3)
    print('RANK_ONE_CROSSED_HEINZ_BOUNDARY_IDENTITIES_OK')

if __name__=='__main__':
    test_witness()
    test_boundary_cases()
