"""Exact-rational enclosure for one explicit reduced planar body's area.

The infinite-dimensional maximizing theorem is proved analytically in RESULT.md;
this standard-library checker independently certifies its displayed numerical witness.
"""
from fractions import Fraction as F


def _alt_interval(x, sin=True, terms=24):
    assert F(0) <= x <= F(2)
    s = F(0)
    term = x if sin else F(1)
    for j in range(terms):
        s += (-1)**j * term
        if sin:
            term *= x*x / F((2*j+2)*(2*j+3))
        else:
            term *= x*x / F((2*j+1)*(2*j+2))
    remainder = (-1)**terms * term
    return (min(s, s+remainder), max(s, s+remainder))


def sin_int(x): return _alt_interval(x, True)
def cos_int(x): return _alt_interval(x, False)


def certificate():
    m = F(15, 16)
    assert m > F(11, 14) and m < F(3, 2)  # 3 < pi < 22/7
    # t = -cos(2m)/sin(m), strictly between 0 and sin(m).
    s0,s1 = sin_int(m)
    c0,c1 = cos_int(2*m)
    assert c1 < 0 and s0 > 0
    t0,t1 = -c1/s1, -c0/s0
    assert F(0) < t0 < t1 < s0
    # Rational bisection, comparing strict, rigorous Taylor enclosures.
    lo,hi = F(0),m
    for j in range(85):
        mid=(lo+hi)/2
        a0,a1=sin_int(mid)
        if a1 < t0:
            lo=mid
        elif a0 > t1:
            hi=mid
        else:
            raise AssertionError('insufficient precision in root interval')
    assert hi-lo < F(1,10**23)
    # L=m-a. Use monotonicity of sine on [0,1] and cosine on [0,1].
    Llo,Lhi = m-hi,m-lo
    assert F(0)<lo<hi<m and F(0)<Llo<Lhi<F(1)
    s2lo,s2hi=sin_int(2*m)
    sinLlo,_=sin_int(Llo)
    _,sinLhi=sin_int(Lhi)
    cosAlo,_=cos_int(hi)
    _,cosAhi=cos_int(lo)
    cosMlo,cosMhi=cos_int(m)
    # area = m/2 + sin(2m)/4 + 1/2 * [L - sin L
    #     +(cos a - cos m)(sin m - sin a)].
    b0,b1=cosAlo-cosMhi,cosAhi-cosMlo
    d0,d1=s0-t1,s1-t0
    assert b0>0 and d0>0
    low=m/2+s2lo/4+(Llo-sinLhi+b0*d0)/2
    high=m/2+s2hi/4+(Lhi-sinLlo+b1*d1)/2
    assert F(79455604,10**8) < low < high < F(79455605,10**8)
    assert low > F(788844,10**6) # larger than previous 0.78884379...
    print('VERIFY_OK')
    print('a in', '(',float(lo),',',float(hi),')')
    print('area in', '(',float(low),',',float(high),')')


if __name__=='__main__': certificate()
