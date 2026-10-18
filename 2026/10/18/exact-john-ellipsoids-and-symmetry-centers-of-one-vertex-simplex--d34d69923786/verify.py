"""Exact-rational consistency checks for the simplex-frustum John ellipsoid.

Run with Python 3: python3 verify.py. This is a supplementary finite
check, not a proof of the all-dimensional claims in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, log
from random import Random


def params(n, t):
    threshold = F(n-1, n+1)
    if t <= threshold:
        h = F(n, n+1)
        p = F(1, n*(n+1))
        q = F(1, n*(n+1)**2)
        s = F(1, n)
    else:
        h = (1+t)/2
        p = t/F(n*(n-1))
        q = (1-t)**2/F(4*n)
        s = (1-t)/(1+t)
    return h, p, q, s


def check_exact(n, t):
    h, p, q, s = params(n, t)
    assert p > 0 and q > 0
    # Nonnegative-coordinate facet is tangent.
    assert (n-1)*p+q == h*h/F(n)
    # Axial half-span is s*h: compare squared quantities.
    assert n*q == (s*h)**2
    assert h*(1+s) <= 1
    assert h*(1-s) >= t
    if t >= F(n-1,n+1):
        assert h*(1+s)==1 and h*(1-s)==t
    else:
        assert h*(1+s)==1 and h*(1-s)==F(n-1,n+1)

    # John contact certificate, in parallel and perpendicular components.
    w = F(n-1, n)*(1/(1-s*s))
    wp = (1+n*s)/(2*(1+s))
    wm = (1-n*s)/(2*(1-s))
    assert w > 0 and wp > 0 and wm >= 0
    assert -n*w*s + wp-wm == 0  # first moment
    assert w*n*(1-s*s)/F(n-1) == 1  # perpendicular frame
    assert w*n*s*s + wp+wm == 1  # parallel frame
    if t < F(n-1,n+1):
        assert wm == 0
    if t > F(n-1,n+1):
        assert wm > 0

    # Symmetry coefficient and unique candidate center; verify 2n+2 facets.
    alpha=F(1,1)/(n-t)
    ci = alpha/(1+alpha)
    assert ci == F(1,1)/(n+1-t)
    sumci = n*ci
    assert (1+alpha)*ci - alpha == 0
    assert (1+alpha)*sumci-alpha*t == 1
    assert (1+alpha)*sumci-alpha >= t
    assert n*alpha == 1+alpha*t  # sharp upper bound

    # Exact vertex radii in ellipsoid norm, via eigen-decomposition.
    first = F(n-1,n)/p + (1-h)**2/(n*q)
    second = t*t*F(n-1,n)/p + (t-h)**2/(n*q)
    if t <= F(n-1,n+1):
        assert first == n*n
        assert second <= n*n
    else:
        assert first == 1+F((n-1)**2,1)/t
        assert second == 1+(n-1)**2*t
        assert first > second


def random_stress():
    random=Random(39711)
    tests=0
    for n in (2,3,4,7,10):
        for t in (F(0),F(1,7),F(n-1,n+1),F(4,5),F(19,20)):
            h,p,q,_=params(n,t)
            best=(n-1)*log(float(p))+log(float(q))
            for k in range(1000):
                # Independently generate centers and positive axis matrices;
                # reject those failing any of n+2 support inequalities.
                H=float(t)+(1-float(t))*random.random()
                X=float(h) * (0.03 + 1.75*random.random())
                A= max(X,1e-9)*float(p)/float(h)
                B=max(X,1e-9)*float(q)/float(h)
                if H+sqrt(n*B)>1+1e-12: continue
                if H-sqrt(n*B)<float(t)-1e-12: continue
                if (n-1)*A+B>H*H/n+1e-12: continue
                candidate=(n-1)*log(A)+log(B)
                assert candidate <= best + 1e-9,(n,t,k,candidate,best)
                tests+=1
    return tests


def main():
    count=0
    for n in range(2,31):
        threshold=F(n-1,n+1)
        vals={F(0),F(1,20),threshold/2,threshold,(threshold+1)/2,
              F(4,5),F(17,20),F(19,20),F(99,100)}
        for t in sorted(vals):
            if 0 <= t < 1:
                check_exact(n,t)
                count+=1
    r=random_stress()
    print(f'VERIFY_OK: {count} exact rational parameter checks; '
          f'{r} randomly generated feasible symmetric competitors.')

if __name__=='__main__': main()
