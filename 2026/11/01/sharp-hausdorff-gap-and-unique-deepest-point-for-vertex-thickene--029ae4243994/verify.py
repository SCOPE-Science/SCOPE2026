"""Exact-arithmetic diagnostics for the simplex vertex-convexification gap.

Coordinates are barycentric. Regular-simplex squared Euclidean lengths
are (ell**2/2) times squared zero-sum coefficient lengths; ell=1 here.
This program is finite corroboration, not a proof of the continuum theorem.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def projection_simplex(q, mass):
    """Squared-Euclidean projection of a rational vector to a nonnegative simplex."""
    if mass == 0:
        return tuple(F(0) for _ in q)
    arr = sorted(q, reverse=True)
    for k in range(1,len(arr)+1):
        tau = (sum(arr[:k],F(0))-mass)/k
        if arr[k-1] > tau and (k==len(arr) or arr[k] <= tau):
            y=tuple(max(F(0),t-tau) for t in q)
            assert sum(y)==mass
            return y
    raise AssertionError('projection active-set failure')


def exact_dist2(x, lam):
    s=1+lam
    assert all(t>=0 for t in x) and sum(x)==s
    if any(t>=1 for t in x):
        return F(0)
    vals=[]
    for i in range(len(x)):
        other=[x[j] for j in range(len(x)) if j!=i]
        yy=projection_simplex(other,lam)
        dist=(1-x[i])**2+sum((a-b)**2 for a,b in zip(other,yy))
        vals.append(dist/2)
    return min(vals)


def expected_max_dist2(n,lam):
    # edge length one; dimension d=n-1
    d=n-1
    return F(max(d-lam,0)**2,2*d*n)


def directional_bound2(x,lam):
    s=1+lam; m=max(x)
    if m>=1: return F(0)
    return s*(1-m)**2/(2*(s-m))


def run():
    count=0
    cases=[F(0),F(1,5),F(1,2),F(2,3),F(1),F(5,4),F(2),F(11,4),F(4)]
    for n in range(3,8):
        for lam in cases:
            s=1+lam
            if lam>=n-1:
                # all points of the s-simplex meet some cap
                assert expected_max_dist2(n,lam)==0
            xcent=tuple(s/n for _ in range(n))
            assert exact_dist2(xcent,lam)==expected_max_dist2(n,lam)
            count+=1
            # enumerate all rational points on a fixed partitioned simplex
            grid=5
            def comps(total,parts):
                if parts==1:
                    yield (total,)
                else:
                    for k in range(total+1):
                        for rest in comps(total-k,parts-1):
                            yield (k,)+rest
            for c in comps(grid,n):
                x=tuple(s*z/grid for z in c)
                d2=exact_dist2(x,lam)
                assert d2<=expected_max_dist2(n,lam),(n,lam,x,d2)
                assert d2<=directional_bound2(x,lam),(n,lam,x,d2)
                if lam<n-1 and len(set(x))>1:
                    assert d2<expected_max_dist2(n,lam)
                count+=1
            # random rational coordinates to probe off-grid points
            rand=Random(811*n+19*lam.numerator+23*lam.denominator)
            for it in range(190):
                zs=[rand.randrange(1,100) for _ in range(n)]
                x=tuple(s*z/sum(zs) for z in zs)
                d2=exact_dist2(x,lam)
                assert d2<=expected_max_dist2(n,lam)
                assert d2<=directional_bound2(x,lam)
                if lam<n-1 and len(set(x))>1:
                    assert d2<expected_max_dist2(n,lam)
                count+=1
    print('PASS',count,'exact rational checks of projection/bound/rigidity')
    print('PASS exact formula at every centroid and all tested boundary regimes')

if __name__=='__main__':
    run()
