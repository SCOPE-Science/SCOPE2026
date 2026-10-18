"""Exact Ehrhart moment verification for centered uniform graph-Lipschitz balls.

Only Python standard library and SymPy are required. This is an independent
lattice-point calculation, not a replacement for the infinite-dimensional
algebraic argument in the accompanying proof.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial
from sympy import Matrix, Rational, ones, eye


def slice_variance(n):
    """Variance on a central n-cube slice, along any zero-sum edge direction."""
    k = n - 1
    a0 = Fraction(0)
    a2 = Fraction(0)
    for j in range(k + 1):
        a = k - 2 * j
        lo, hi = max(0, a - 1), max(0, a + 1)
        c = (-1) ** j * comb(k, j)
        a0 += c * Fraction(hi**k - lo**k, k)
        a2 += c * (
            Fraction(hi ** (k + 2) - lo ** (k + 2), k + 2)
            - Fraction(2 * a * (hi ** (k + 1) - lo ** (k + 1)), k + 1)
            + Fraction(a * a * (hi**k - lo**k), k)
        )
    return Fraction(n, n - 1) * a2 / a0


def weighted_laplacian(n, edges, cycles):
    edge_cycle = {}
    for C in cycles:
        for e in C:
            a,b=sorted(e)
            if (a,b) in edge_cycle:
                raise ValueError('cycle overlap')
            edge_cycle[a,b] = len(C)
    L = Matrix.zeros(n)
    for a,b in edges:
        w = 1 / slice_variance(edge_cycle[tuple(sorted((a,b)))]) if tuple(sorted((a,b))) in edge_cycle else Fraction(3,1)
        w = Rational(w.numerator, w.denominator)
        L[a,a]+=w; L[b,b]+=w; L[a,b]-=w; L[b,a]-=w
    return L


def lattice_counts(n, edges, q):
    E={tuple(sorted(e)) for e in edges}
    parents=[]
    for v in range(1,n):
        p=next((u for u in range(v) if tuple(sorted((v,u))) in E),None)
        if p is None:raise ValueError('list vertices in rooted connected order')
        parents.append(p)
    x=[0]*n
    total=0
    raw=[[0]*n for _ in range(n)]
    def recur(v):
        nonlocal total
        if v==n:
            total+=1
            S=sum(x)
            z=[n*t-S for t in x]
            for a in range(n):
                for b in range(a,n):raw[a][b]+=z[a]*z[b]
            return
        p=parents[v-1]
        for delta in range(-q,q+1):
            val=x[p]+delta
            if any(tuple(sorted((v,u))) in E and abs(val-x[u])>q for u in range(v) if u!=p):
                continue
            x[v]=val
            recur(v+1)
    recur(1)
    return total,raw


def leading(vals):
    d=len(vals)-1
    for k in range(d):
        vals=[b-a for a,b in zip(vals,vals[1:])]
    return Fraction(vals[0],factorial(d))


def exact_covariance(n, edges):
    dim=n-1
    scans=[lattice_counts(n,edges,q) for q in range(dim+3)]
    volume=leading([s[0] for s in scans[:dim+1]])
    cov=Matrix.zeros(n)
    for a in range(n):
        for b in range(a,n):
            numerator=leading([s[1][a][b] for s in scans])
            frac=numerator/(n*n*volume)
            cov[a,b]=cov[b,a]=Rational(frac.numerator,frac.denominator)
    return volume,cov


def check(label,n,edges,cycles):
    vol,C=exact_covariance(n,edges)
    L=weighted_laplacian(n,edges,cycles)
    J=ones(n,n)/n
    expected=(L+J).inv()-J
    assert C==expected, (label,C-expected)
    assert C*ones(n,1)==Matrix.zeros(n,1)
    # Independent determinant identity on an orthonormal basis of the zero-sum space.
    bridge_count=len(edges)-sum(len(C) for C in cycles)
    det_formula=Fraction(1,n*3**bridge_count)
    for cyc in cycles:
        det_formula*=slice_variance(len(cyc))**(len(cyc)-1)/len(cyc)
    # The pseudodeterminant of C is n times any principal cofactor of C.
    assert n*C[:n-1,:n-1].det() == Rational(det_formula.numerator,det_formula.denominator)
    assert all(L[a,b]<0 if tuple(sorted((a,b))) in {tuple(sorted(e)) for e in edges} else L[a,b]==0
               for a in range(n) for b in range(a+1,n))
    print(f'PASS {label} n={n} edges={len(edges)} cycles={len(cycles)} lattice_volume={vol} all {n*n} covariance entries exact')

if __name__=='__main__':
    assert slice_variance(3)==Fraction(5,12)
    assert slice_variance(4)==Fraction(2,5)
    tests=[
        ('three-cycle',3,[(0,1),(1,2),(2,0)],[[(0,1),(1,2),(2,0)]]),
        ('four-cycle',4,[(0,1),(1,2),(2,3),(3,0)],[[(0,1),(1,2),(2,3),(3,0)]]),
        ('triangle-bridge',4,[(0,1),(1,2),(2,0),(2,3)],[[(0,1),(1,2),(2,0)]]),
        ('square-bridge',5,[(0,1),(1,2),(2,3),(3,0),(3,4)],[[(0,1),(1,2),(2,3),(3,0)]]),
        ('two-triangles-share-vertex',5,[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],[[(0,1),(1,2),(2,0)],[(0,3),(3,4),(4,0)]]),
        ('four-path',4,[(0,1),(1,2),(2,3)],[]),
        ('two-triangles-bridge',6,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)],[[(0,1),(1,2),(2,0)],[(3,4),(4,5),(5,3)]]),
    ]
    for args in tests:check(*args)
    # Contrasting non-cactus K_{2,3}; the two hubs 0,2 form a nonedge.
    edges=[(u,v) for u in (0,2) for v in (1,3,4)]
    volume,cov=exact_covariance(5,edges)
    J=ones(5,5)/5
    precision=(cov+J).inv()-J
    assert volume == 8
    assert precision[0,2] == Rational(-3,8)
    assert precision == Matrix([
        [Rational(57,8),Rational(-9,4),Rational(-3,8),Rational(-9,4),Rational(-9,4)],
        [Rational(-9,4),Rational(9,2),Rational(-9,4),0,0],
        [Rational(-3,8),Rational(-9,4),Rational(57,8),Rational(-9,4),Rational(-9,4)],
        [Rational(-9,4),0,Rational(-9,4),Rational(9,2),0],
        [Rational(-9,4),0,Rational(-9,4),0,Rational(9,2)],
    ])
    print('NONCACTUS_K23_EXACT_BOUNDARY_OK',volume,precision[0,2])
    print('CHECKS_PASSED',len(tests),'NONCACTUS_BOUNDARIES',1)
