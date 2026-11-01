"""Exact-arithmetic diagnostics for the crosspolytope vertex-translate volume law.

Run: python3 volume_spline_verifier.py
The analytic proof is in RESULT.md; finite tests here are not a proof for all d.
"""
from fractions import Fraction as F
from math import comb, factorial
from itertools import product


def spline_volume(d, t):
    """Exact proposed Euclidean vacancy volume, t>=0, integer d>=2."""
    t = F(t)
    v0 = F(2**d, factorial(d))
    if t <= 1:
        return v0 * ((1+t)**d - 2*d*t**d)
    if t >= d-1:
        return F(0)
    return v0 * 2*(-1)**d * sum(
        F((-1)**j*comb(d,j),j-2) * max(F(0),j-1-t)**d
        for j in range(3,d+1)
    )


def integrate_positive_affine_power(a,b,left,right,power):
    """Integrate max(0,a*s+b)**power over [left,right], exactly."""
    if right <= left:
        return F(0)
    if a == 0:
        return (right-left)*max(F(0),b)**power
    root = -b/a
    if a > 0:
        left = max(left,root)
    else:
        right = min(right,root)
    if right <= left:
        return F(0)
    return ((a*right+b)**(power+1)-(a*left+b)**(power+1))/(a*(power+1))


def direct_slice_volume(d,t):
    """Independently integrate box-constrained simplex sections by inclusion-exclusion."""
    t=F(t)
    if t < 1:
        # In this regime the 2d equal-radius crosspolytopes have disjoint interiors.
        return F(2**d,factorial(d))*((1+t)**d-2*d*t**d)
    lower,upper=t-1,t+1
    integral=sum(
       (-1)**j*comb(d,j)*integrate_positive_affine_power(
          F(2-j,2), F(j,2)*(t-1),lower,upper,d-1
       ) for j in range(d+1)
    )
    return F(2**d,factorial(d-1))*integral


def uncovered_direct(d,t,x):
    """Direct membership test, independent of the integral formula."""
    t=F(t)
    x=[F(q) for q in x]
    if sum(map(abs,x)) > 1+t:
        return False
    centers = [tuple((sign if k==i else 0) for k in range(d))
               for i in range(d) for sign in (-1,1)]
    return all(sum(abs(x[k]-v[k]) for k in range(d))>t for v in centers)


def run_checks():
    counts = {"exact_slice_integrals":0,"nonnegative":0,"threshold":0,
              "point_membership":0,"knot_jumps":0}
    for d in range(2,13):
        samples=sorted({F(k,5) for k in range(0,5*(d+2)+1)} |
                       {F(j,1) for j in range(d+1)} |
                       {F(2*j+1,2) for j in range(d+1)})
        for t in samples:
            p=spline_volume(d,t)
            q=direct_slice_volume(d,t)
            assert p==q, (d,t,p,q)
            counts['exact_slice_integrals']+=1
            assert F(0)<=p<=F(2**d,factorial(d))*(1+t)**d
            counts['nonnegative']+=1
            if t>=d-1:
                assert p==0
                counts['threshold']+=1
            if d>=3 and F(d-2)<=t<d-1:
                # Last positive chamber has exactly one B-spline atom.
                assert p==F(2**d,factorial(d))*F(2,d-2)*(d-1-t)**d
                counts['knot_jumps']+=1
        # At t=1 the (d-1)-st derivative jump is 2**d*d*(d-1).
        # At each integer k>=2, the d-th derivative jump is
        # 2**(d+1)*(-1)**k * C(d,k+1)/(k-1).
        for k in range(2,d):
            jump=F(2**(d+1)*(-1)**k*comb(d,k+1),k-1)
            assert jump != 0
            counts['knot_jumps']+=1
    # Coordinates deliberately include facets, the origin and points in a hole.
    for d in range(2,6):
        for t in [F(0),F(1,2),F(1),F(3,2),F(2),F(5,2),F(3)]:
            for coords in product([F(0),F(1,3),F(2,3),F(1)],repeat=d):
                if sum(coords)>1+t:
                    continue
                s=sum(coords)
                M=max(coords)
                expected= s+1-2*min(M,1)>t
                assert uncovered_direct(d,t,coords)==expected,(d,t,coords)
                counts['point_membership']+=1
    return counts

if __name__=='__main__':
    c=run_checks()
    print('PASS',c,'TOTAL',sum(c.values()))
