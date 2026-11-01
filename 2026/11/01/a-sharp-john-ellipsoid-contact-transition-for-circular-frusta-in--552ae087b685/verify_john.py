"""Numerical checks for the John-ellipsoid contact identities of circular frusta.
Only tests finite cases; the all-dimensional theorem follows from its analytic proof.
"""
import math
import random


def coefficients(d, R, r):
    assert isinstance(d, int) and d >= 2 and 0 < r <= R
    A = (R + r)/2
    s = (R-r)/(R+r)
    if s <= 1/d:
        return 0.0, 1.0, R*r
    m = (1-d*s)/(s*(d+1))
    return m, (1+m)**2, R**2*(d-1)/(d+1)


def check(d,R,r):
    A=(R+r)/2
    s=(R-r)/(R+r)
    m,p,q=coefficients(d,R,r)
    tol=1e-8*max(1,R)
    assert m-math.sqrt(p)>=-1-tol and m+math.sqrt(p)<=1+tol
    assert abs(math.sqrt(q+(A*s)**2*p)+A*s*m-A)<tol
    if s<=1/d:
        w=(d-1)/(d*(1-s*s))
        wt=(1-w-w*s)/2
        wb=(1-w+w*s)/2
        assert min(w,wt,wb)>-1e-9
        assert abs(w*s+wt-wb)<1e-9
        assert abs(w*s*s+wt+wb-1/d)<1e-9
        assert abs(w*(1-s*s)/(d-1)-1/d)<1e-9
    else:
        w=d/(d+1)
        xi=s*math.sqrt(p)/(1-s*m)
        assert abs(xi-1/d)<1e-9
        assert abs(w*xi-(1-w))<1e-9
        assert abs(w*xi*xi+(1-w)-1/d)<1e-9
        assert abs(w*(1-xi*xi)/(d-1)-1/d)<1e-9
    return True

if __name__ == '__main__':
    rng=random.Random(68275)
    total=0
    for d in range(2,31):
        for s in [0.,1/(2*d),1/d,min(.9999,2/d),.2,.5,.8,.99]+[rng.uniform(0,.999) for _ in range(8)]:
            s=min(s,.99999999)
            assert check(d,1+s,1-s)
            total+=1
    print('PASS: {} configurations for normalized containment and all contact moments'.format(total))
