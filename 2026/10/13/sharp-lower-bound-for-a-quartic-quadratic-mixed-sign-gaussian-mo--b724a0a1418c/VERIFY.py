"""Exact-rational checks for a sharp mixed-sign Gaussian moment bound.
Run: python3 VERIFY.py. Requires Python standard library only.
The accompanying analytic proof covers the continuous parameter interval.
"""
from fractions import Fraction as F
from math import comb


def double_factorial_even(e):
    if e % 2:
        return 0
    out = 1
    for j in range(1, e, 2):
        out *= j
    return out


def x_moment(e, t):
    if e % 2:
        return F(0)
    ans = F(1)
    for j in range(0, e, 2):
        ans *= t + j
    return ans


def direct_moment(t, a, v, k, ell, m):
    # Independent normalized weighted X, W, V; Y=aX+vW, Z=kX+ell W+mV.
    from math import factorial
    ans = F(0)
    for iy in range(5):
        for ik in range(3):
            for il in range(3 - ik):
                im = 2 - ik - il
                multinomial = factorial(2) // (factorial(ik)*factorial(il)*factorial(im))
                coef = comb(4, iy)*multinomial*a**iy*v**(4-iy)*k**ik*ell**il*m**im
                ans += (coef * x_moment(iy+ik,t)
                        * double_factorial_even(4-iy+il)
                        * double_factorial_even(im))
    return ans


def matrix(t, a, v):
    r = a*a
    aa = r*r*t*(t+2)+6*r*(1-r)*t+3*(1-r)**2
    xx = r*r*t*(t+2)*(t+4)+6*r*(1-r)*t*(t+2)+3*(1-r)**2*t
    ww = r*r*t*(t+2)+18*r*(1-r)*t+15*(1-r)**2
    xw = 4*a**3*v*t*(t+2)+12*a*v**3*t
    return aa, xx, ww, xw


def bernstein_k(r,t):
    return ((3-t)*(1-r)**3 + 2*(t+12)*r*(1-r)**2
            + (t+2)*(t+9)*r*r*(1-r) + 2*t*(t+2)*r**3)


count = 0
for j in range(1, 10):
    t = F(j, 10)
    for i in range(0, 11):
        r = F(i, 10)
        a0 = r*r*t*(t+2)+6*r*(1-r)*t+3*(1-r)**2
        xx = r*r*t*(t+2)*(t+4)+6*r*(1-r)*t*(t+2)+3*(1-r)**2*t
        ww = r*r*t*(t+2)+18*r*(1-r)*t+15*(1-r)**2
        cross_sq = r*(1-r)*(4*r*t*(t+2)+12*(1-r)*t)**2
        floor = t*(t+2)
        assert a0-floor == (1-r)*(1-t)*(3+t-r*(3-t))
        assert xx-floor == t*(1-t+6*r*(t+1)+r*r*(t*t-1))
        assert ((xx-floor)*(ww-floor)-cross_sq
                == t*(1-r)*(1-t)*(t+5)*bernstein_k(r,t))
        assert xx-floor > 0 and a0-floor >= 0
        assert bernstein_k(r,t)>0
        assert (xx-floor)*(ww-floor)-cross_sq >= 0
        count += 1

pairs = [(F(0),F(1)),(F(3,5),F(4,5)),(F(-3,5),F(4,5)),
         (F(4,5),F(3,5)),(F(1),F(0)),(F(-1),F(0))]
triples = [(F(0),F(0),F(1)),(F(1),F(0),F(0)),
           (F(3,5),F(4,5),F(0)),(F(0),F(3,5),F(4,5)),
           (F(4,5),F(0),F(3,5)),(F(-3,5),F(4,5),F(0))]
for t in [F(1,5), F(1,2), F(4,5)]:
    for a,v in pairs:
        aa,xx,ww,xw = matrix(t,a,v)
        for k,ell,m in triples:
            assert k*k+ell*ell+m*m==1
            via_matrix=k*k*xx+ell*ell*ww+2*k*ell*xw+m*m*aa
            via_expansion=direct_moment(t,a,v,k,ell,m)
            assert via_expansion==via_matrix, (t,a,v,k,ell,m)
            assert via_expansion>=t*(t+2)
            count += 1
            if a*a==1 and k==0:
                assert via_expansion==t*(t+2)
print('VERIFY_OK: %d exact-rational identities, moments and inequalities'%count)
