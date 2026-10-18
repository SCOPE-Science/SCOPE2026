#!/usr/bin/env python3
"""Exact-arithmetic checks for the rectangular partial-matching John threshold.

No dependencies beyond the Python standard library. This program checks finite
instances of the identities used in the general mathematical proof; finite
instances are not an exhaustive proof of the infinite family.
"""
from fractions import Fraction as F


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def add(A, B):
    return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]


def scale(s, A):
    return [[s*x for x in row] for row in A]


def outer(u,v):
    return [[x*y for y in v] for x in u]


def dot(u, A, v):
    return sum((u[i]*A[i][j]*v[j] for i in range(len(u)) for j in range(len(v))), F(0))


def formula(a,b):
    t=F(1,b+1)
    S=[[ (F(int(i==j), b*(b+1)) - F(1,b*(b+1)**2))
         for j in range(b)] for i in range(b)]
    Sinv=scale(F(b*(b+1)),add(eye(b), [[F(1) for _ in range(b)] for _ in range(b)]))
    # Inverse above should be b*(b+1)*(I+J) because (b/(b+1))/t^2 = b*(b+1).
    # John's weighted facet normals: -unit coordinates, and row sum.
    w=F(b,b+1)
    N=[[F(0) for _ in range(b)] for _ in range(b)]
    first=[F(0) for _ in range(b)]
    for j in range(b+1):
        n=[-F(int(i==j)) for i in range(b)] if j<b else [F(1)]*b
        N=add(N,scale(w/t**2,outer(n,n)))
        first=[z+w*n0/t for z,n0 in zip(first,n)]
    assert N==Sinv, (a,b,'dual John matrix')
    assert first==[0]*b, (a,b,'dual John first moment')
    assert all(dot([F(int(i==j)) for i in range(b)],S,[F(int(i==j)) for i in range(b)])==t*t for j in range(b))
    allones=[F(1)]*b
    assert dot(allones,S,allones)==t*t
    assert sum((S[i][i] for i in range(b)),F(0))==b*t*t
    # Exact squared comparison for column support a*t+sqrt(a)*t <= 1.
    gap=b+1-a
    feasible= gap>=0 and gap*gap >=a
    classification=b>=a+__import__('math').isqrt(a) -1
    if __import__('math').isqrt(a)**2 != a:
        classification=b>=a+__import__('math').isqrt(a)
    assert feasible==classification, (a,b,'integer cutoff')
    # Two Frobenius shape eigenvalues (parallel, perpendicular to each row's all-ones vector).
    lam_parallel=F(1,b*(b+1)**2)
    lam_perp=F(1,b*(b+1))
    assert all(sum((S[i][j] for j in range(b)),F(0))==lam_parallel for i in range(b))
    assert S[0][0]-S[0][1]==lam_perp
    return feasible, gap*gap-a, lam_parallel,lam_perp


def main():
    total=0; yes=0; no=0; boundary=[]
    for a in range(2,13):
        for b in range(a,a+12):
            feasible,poly,lp,lo=formula(a,b)
            total+=1
            yes+=int(feasible)
            no+=int(not feasible)
            if poly==0: boundary.append((a,b))
    assert (2,3) not in boundary
    assert (4,5) in boundary and (9,11) in boundary
    assert formula(4,5)[0]
    assert not formula(5,6)[0]
    assert formula(5,7)[0]
    print('VERIFY_OK cases=%d stable=%d changed=%d boundary=%s' % (total,yes,no,str(boundary)))

if __name__=='__main__':main()
