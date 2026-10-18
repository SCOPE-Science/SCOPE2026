"""Exact finite checks for leaf-count dependence in correlated uniform-attachment trees.

Run with Python 3.9 or later; only the standard library is required.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict, Counter

checks = 0

def assert_equal(a, b, context):
    global checks
    checks += 1
    assert a == b, (context, a, b)

def exact_leaf_dist(n):
    """Exhaustively list all uniform recursive trees and count graph-degree-one vertices."""
    if n == 2:
        return {2: F(1)}
    hist = Counter()
    total = 0
    for ps in product(*(range(m) for m in range(2, n))):
        deg = [0]*n
        deg[0], deg[1] = 1, 1
        for v, p in enumerate(ps, start=2):
            deg[p] += 1
            deg[v] += 1
        leaves = sum(x == 1 for x in deg)
        hist[leaves] += 1
        total += 1
    return {k: F(v,total) for k,v in hist.items()}

def next_leaf_dist(p, m):
    """One step of the exact leaf-count transition for an m-vertex uniform-attachment tree."""
    out = defaultdict(F)
    for k, mass in p.items():
        out[k] += mass*F(k,m)
        out[k+1] += mass*(1-F(k,m))
    return {k:v for k,v in out.items() if v}

def leaf_dist(n):
    x = {2:F(1)}
    for m in range(2,n):
        x = next_leaf_dist(x,m)
    return x

def moment(p,j=1):
    return sum((F(k)**j)*v for k,v in p.items())

def cov_joint(n,t):
    """Exact bivariate distribution with a common t-vertex ancestor."""
    shared = leaf_dist(t)
    joint = defaultdict(F)
    for ell,w in shared.items():
        d={ell:F(1)}
        for m in range(t,n):
            d=next_leaf_dist(d,m)
        for a,pa in d.items():
            for b,pb in d.items():
                joint[a,b]+=w*pa*pb
    return joint

def joint_cov(joint):
    ex=sum(F(a)*v for (a,b),v in joint.items())
    ey=sum(F(b)*v for (a,b),v in joint.items())
    return sum(F(a*b)*v for (a,b),v in joint.items())-ex*ey

def run():
    global checks
    # Independent enumeration of (n-1)! labeled uniform-attachment trees.
    for n in range(2,9):
        actual = exact_leaf_dist(n)
        expected = leaf_dist(n)
        assert_equal(actual,expected,('distribution',n))
        assert_equal(sum(actual.values()),F(1),('mass',n))
        assert_equal(moment(actual),F(n,2)+F(1,n-1),('mean',n))
        if n>=3:
            assert_equal(moment(actual,2)-moment(actual)**2,
                         F(n,12)-F(1,(n-1)**2),('variance',n))
    for n in range(4,17):
        d=leaf_dist(n)
        v=F(n,12)-F(1,(n-1)**2)
        assert_equal(moment(d,2)-moment(d)**2,v,('variance-dp',n))
        for t in range(2,n+1):
            joint=cov_joint(n,t)
            assert_equal(sum(joint.values()),F(1),('joint-mass',n,t))
            assert_equal({a:sum(w for (aa,b),w in joint.items() if aa==a) for a in d},d,
                         ('joint-marginal',n,t))
            covariance=joint_cov(joint)
            expected=F(0) if t<=3 else F(t*(t-1)**2-12,12*(n-1)**2)
            assert_equal(covariance,expected,('joint-cov',n,t))
            if t<=3:
                for a in d:
                    for b in d:
                        assert_equal(joint.get((a,b),F(0)),d[a]*d[b],('independence',n,t,a,b))
            else:
                assert expected > 0
            # Positive quadrant dependence: tail-event covariances are nonnegative.
            for a in range(2,n+1):
                pa=sum(w for k,w in d.items() if k>=a)
                for b in range(2,n+1):
                    pb=sum(w for k,w in d.items() if k>=b)
                    pab=sum(w for (x,y),w in joint.items() if x>=a and y>=b)
                    assert pab>=pa*pb, ('quadrant-dependence',n,t,a,b,pab,pa*pb)
                    checks+=1
            corr=(covariance/v)
            want= F(0) if t<=3 else F(t*(t-1)**2-12,n*(n-1)**2-12)
            assert_equal(corr,want,('correlation',n,t))
    # Exact deterministic checks on the asymptotic covariance scale.
    for numerator,denominator in ((0,1),(1,4),(1,2),(3,4),(1,1)):
        target=F(numerator,denominator)**3
        n=100000
        t=max(3,n*numerator//denominator)
        c=F(0) if t<=3 else F(t*(t-1)**2-12,n*(n-1)**2-12)
        assert abs(c-target)<F(1,2000), (numerator,denominator,c,target)
        checks += 1
    print(f'PASS: {checks} exact assertions; recursive trees exhaustively listed to n=8; all bivariate leaf-count distributions checked through n=16')

if __name__=='__main__':
    run()
