#!/usr/bin/env python3
import math


def eigvals_theta(c1, c2, s):
    tr = c1 + c2
    det = c1*c2*(1-s*s)
    disc = max(0.0, tr*tr - 4.0*det)
    root = math.sqrt(disc)
    return 0.5*(tr+root), 0.5*(tr-root)


def schatten_distance(c1, c2, s, p):
    lp, lm = eigvals_theta(c1,c2,s)
    a, b = abs(lp-1.0), abs(lm-1.0)
    if math.isinf(p):
        return max(a,b)
    return (a**p+b**p)**(1.0/p)


def closed(s,p):
    if p == 1:
        c=1.0/(1.0+s)
        d=2.0*s/(1.0+s)
    elif math.isinf(p):
        c=1.0
        d=s
    else:
        q=p/(p-1.0)
        a,b=1.0+s,1.0-s
        c=(a**(q-1.0)+b**(q-1.0))/(a**q+b**q)
        d=2.0*s/(a**q+b**q)**(1.0/q)
    return c,d


def check_case(s,p):
    c,d=closed(s,p)
    got=schatten_distance(c,c,s,p)
    assert abs(got-d) < 2e-11, (s,p,c,d,got)
    # Dense local/global grid in logarithmic coefficient scale.
    best=float('inf')
    best_pair=None
    # 181 points from exp(-3) to exp(3) in each coordinate.
    vals=[math.exp(-3.0+6.0*i/180.0) for i in range(181)]
    for c1 in vals:
        for c2 in vals:
            val=schatten_distance(c1,c2,s,p)
            if val < best:
                best,best_pair=val,(c1,c2)
    # Grid cannot generally hit the exact optimum; formula must be no worse.
    assert d <= best + 3e-11, (s,p,d,best,best_pair)
    # Perturb each coefficient separately around the exact optimizer.
    for factor in (0.8,0.95,1.05,1.2):
        assert schatten_distance(c*factor,c,s,p) > d - 1e-12
        assert schatten_distance(c,c*factor,s,p) > d - 1e-12


def main():
    for s in (0.0,0.2,0.7,0.95):
        for p in (1.0,1.5,2.0,3.0,10.0,float('inf')):
            check_case(s,p)
        # Published Hilbert-Schmidt specialization.
        c2,d2=closed(s,2.0)
        assert abs(c2-1.0/(1.0+s*s)) < 2e-15
        assert abs(d2-math.sqrt(2.0)*s/math.sqrt(1.0+s*s)) < 2e-15
    # Analytic monotonicity numerator is positive for representative q,r.
    for q in (1.05,1.2,2.0,5.0,20.0):
        for r in (1e-6,0.1,0.5,0.9,0.999):
            num=(1+r)**(q-1)+(1-r)**(q-1)
            assert num > 0.0
    print('VERIFY_OK')

if __name__=='__main__':
    main()
