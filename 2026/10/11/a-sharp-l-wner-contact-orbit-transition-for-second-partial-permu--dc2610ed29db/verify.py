#!/usr/bin/env python3
"""Exact checks for circumscribed ellipsoids of partial permutohedra P(m,2).

All arithmetic in this program is rational. These are finite tests of
the theorem's formulas, not an all-dimensional proof.
"""
from fractions import Fraction as F

def formula(m):
    assert isinstance(m, int) and m >= 2
    M = F(m)
    if m <= 5:
        t = F(4, m+3)
        u = 16*M/(M+3)**2
        v = 16*M/(3*(M+3))
        pA = 2*M*(5-M)/(M+3)**2
        pB = 8*M*(M-1)/(3*(M+3)**2)
        p0 = (M*M-4*M+27)/(3*(M+3)**2)
    else:
        t = F(3,m+1)
        u = 9*M/(M+1)**2
        v = M*(5*M-9)/((M-1)*(M+1))
        p0, pA, pB = F(1,m+1), F(0), F(m,m+1)
    return t,u,v,p0,pA,pB

def orbit_points(m):
    Z = tuple([0]*m)
    A = []
    B = []
    for i in range(m):
        ai = [0]*m
        ai[i] = 2
        A.append(tuple(ai))
        for j in range(m):
            if i != j:
                bij = ai.copy()
                bij[j] = 1
                B.append(tuple(bij))
    assert len(set([Z]+A+B)) == 1+m+m*(m-1)
    return Z,A,B

def radius_squared(point,m,t,u,v):
    sm = sum(point)
    nm = sum(q*q for q in point)
    return (F(sm)-m*t)**2/(m*u) + (F(nm)-F(sm*sm,m))/v

def check_analytic(m):
    t,u,v,p0,pA,pB = formula(m)
    assert t>0 and u>0 and v>0
    assert min(p0,pA,pB)>=0 and p0+pA+pB==1
    assert m*t == 2*pA+3*pB
    # The eigenvalue u of m times the orbit-mixture covariance:
    assert u == (4*pA+9*pB-(2*pA+3*pB)**2)
    # The eigenvalue v on the coordinate-sum-zero subspace:
    assert v == 4*pA + F(5*m-9,m-1)*pB
    q0 = radius_squared([0]*m,m,t,u,v)
    qA = radius_squared([2]+[0]*(m-1),m,t,u,v)
    qB = radius_squared([2,1]+[0]*(m-2),m,t,u,v)
    assert q0==1 and qB==1
    assert (qA==1) == (m<=5)
    if m>=6:
        assert 1-qA == F(4*(m-5)*(m+1),9*m*(5*m-9))
    return qA

def check_matrix(m):
    """Enumerate the complete finite vertex set and moment certificate."""
    t,u,v,p0,pA,pB = formula(m)
    Z,A,B = orbit_points(m)
    items = [(Z,p0)] + [(a,pA/m) for a in A] + [(b,pB/(m*(m-1))) for b in B]
    assert sum((p for _,p in items), F(0))==1
    for i in range(m):
        assert sum((p*point[i] for point,p in items), F(0)) == t
    # Reconstruct Q=m*Cov from actual integer-coordinate vertices.
    for i in range(m):
        for j in range(m):
            covariance = m*sum((p*(point[i]-t)*(point[j]-t) for point,p in items), F(0))
            expected = (v if i==j else F(0))+(u-v)/m
            assert covariance==expected, (m,i,j,covariance,expected)
    allpts = [Z]+A+B
    ds = [radius_squared(pt,m,t,u,v) for pt in allpts]
    assert max(ds)==1
    assert len([q for q in ds if q==1])==(1+m*m if m<=5 else 1+m*(m-1))
    return len(allpts), len([q for q in ds if q==1])

def main():
    for m in range(2,101):
        check_analytic(m)
    for m in range(2,16):
        n,c = check_matrix(m)
        print("m=%d vertices=%d contacts=%d rational_moment_certificate=OK"%(m,n,c))
    print("PASS: 99 exact dimension formulas and 14 independent full-matrix/contact enumerations.")

if __name__ == "__main__":
    main()
