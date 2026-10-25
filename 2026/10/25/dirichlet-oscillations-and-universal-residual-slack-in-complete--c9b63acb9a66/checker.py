"""Independent geometry and distribution checks for the complete-bipartite Lipschitz body.

Usage: python checker.py
Requires numpy and scipy. Finite numerical checks do not prove the general theorem.
"""
import math
import itertools
from fractions import Fraction
import numpy as np
from scipy.spatial import HalfspaceIntersection, ConvexHull
from scipy.stats import beta, kstest


def exact_coordinate_volume(p, q):
    n = p + q
    return 2**(n-1) * math.factorial(p) * math.factorial(q) / math.factorial(n-1)


def independent_hull_volume(p, q):
    """Compute the volume in the anchored chart from all defining halfspaces."""
    d = p + q - 1
    rows = []
    for i in range(p):
        for j in range(q):
            a = np.zeros(d)
            if i:
                a[i-1] = 1
            a[p-1+j] = -1
            rows.append(np.r_[a,-1.0])
            rows.append(np.r_[-a,-1.0])
    h = HalfspaceIntersection(np.array(rows), np.zeros(d))
    return ConvexHull(h.intersections).volume


def independent_rejection_samples(p, q, N, seed):
    """Sample an anchored box and reject using *all* original graph-edge inequalities."""
    rng=np.random.default_rng(seed)
    # All other A coordinates and all B coordinates lie in [-2,2] when A_0=0.
    # Bound is loose but honest, and the accepted points are uniform.
    a=rng.uniform(-2,2,size=(N,p-1))
    b=rng.uniform(-2,2,size=(N,q))
    all_a=np.concatenate([np.zeros((N,1)),a],axis=1)
    lo=all_a.min(axis=1)
    hi=all_a.max(axis=1)
    ok=(b.min(axis=1)>=hi-1) & (b.max(axis=1)<=lo+1)
    a=all_a[ok];b=b[ok]
    ra=a.max(axis=1)-a.min(axis=1)
    rb=b.max(axis=1)-b.min(axis=1)
    return np.c_[ra/2,rb/2,1-(ra+rb)/2],ok.sum()


def ehrhart_leading_coefficient(p, q):
    """Independent integer lattice enumeration and finite differences."""
    d=p+q-1
    values=[]
    for t in range(d+1):
        v=0
        for tail in itertools.product(range(-2*t,2*t+1),repeat=p-1):
            coords=(0,)+tail
            r=max(coords)-min(coords)
            if r<=2*t:
                v+=(2*t-r+1)**q
        values.append(v)
    for _ in range(d):
        values=[values[i+1]-values[i] for i in range(len(values)-1)]
    return Fraction(values[0],math.factorial(d))


def run():
    tested=0
    for p,q in [(1,2),(1,3),(2,2),(2,3),(3,2),(2,4),(3,3),(4,2)]:
        volume=independent_hull_volume(p,q)
        expected=exact_coordinate_volume(p,q)
        assert math.isclose(volume,expected,rel_tol=2e-9,abs_tol=2e-9),(p,q,volume,expected)
        # Verify the Euclidean/anchored Jacobian directly.
        n=p+q; gram=np.eye(n-1)-np.ones((n-1,n-1))/n
        assert math.isclose(np.linalg.det(gram),1/n,rel_tol=1e-11)
        assert math.isclose(volume/math.sqrt(n),2**(n-1)*math.sqrt(n)/math.comb(n,p),rel_tol=2e-9)
        tested+=1
    lattice_cases=0
    for p,q in [(1,2),(2,2),(2,3),(3,2),(3,3),(2,4),(3,4),(4,3)]:
        exact=Fraction(2**(p+q-1)*math.factorial(p)*math.factorial(q),math.factorial(p+q-1))
        got=ehrhart_leading_coefficient(p,q)
        assert got==exact,(p,q,got,exact)
        lattice_cases+=1
    moments=0
    for p,q in [(2,2),(2,3),(3,2),(3,3)]:
        draws,accepted=independent_rejection_samples(p,q,450000,20+p*100+q)
        assert accepted>250,(p,q,accepted)
        expected=np.array([p-1,q-1,2])/(p+q)
        empirical=draws.mean(axis=0)
        # Use a normal standard-error tolerance for bounded variables.
        var=expected*(1-expected)/(p+q+1)
        err=6*np.sqrt(var/accepted)+0.003
        assert np.all(abs(empirical-expected)<err),(p,q,accepted,empirical,expected,err)
        stat,pvalue=kstest(draws[:,0],lambda z:beta.cdf(z,p-1,q+1))
        assert pvalue>0.00001,(p,q,stat,pvalue)
        gap_stat,gap_p=kstest(draws[:,2],lambda z:beta.cdf(z,2,p+q-2))
        assert gap_p>0.00001,(p,q,gap_stat,gap_p)
        assert np.max(np.abs(draws.sum(axis=1)-1))<1e-12
        moments+=1
    print('VERIFY_OK geometry_hull_cases=',tested,'ehrhart_enumerations=',lattice_cases,'independent_sampling_cases=',moments)


if __name__=='__main__':
    run()
