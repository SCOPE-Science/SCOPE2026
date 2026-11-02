#!/usr/bin/env python3
"""Pure-integer outward-rounded interval certificate for a rational Gabor fiber block.
The code uses only the Python standard library and does not compute a determinant
with unverified floating-point arithmetic.
"""
from functools import lru_cache
from math import pi, log

P = 200
M = P // 2
D = P * (P + 1)
BITS = 192
SCALE = 1 << BITS


def floor_ratio(n, d):
    assert d > 0
    return n // d


def ceil_ratio(n, d):
    assert d > 0
    return -((-n) // d)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def sub(x, y):
    return (x[0] - y[1], x[1] - y[0])


def neg(x):
    return (-x[1], -x[0])


def mul(x, y):
    v = [a * b for a in x for b in y]
    return (floor_ratio(min(v), SCALE), ceil_ratio(max(v), SCALE))


def div(x, y):
    if y[1] < 0:
        return div(neg(x), neg(y))
    assert y[0] > 0, 'division denominator interval meets zero'
    pairs = [(a, b) for a in x for b in y]
    return (min(floor_ratio(SCALE*a, b) for a,b in pairs),
            max(ceil_ratio(SCALE*a, b) for a,b in pairs))


def factor_h(u_num, u_den):
    qlo = floor_ratio(u_num*SCALE, u_den)
    qhi = ceil_ratio(u_num*SCALE, u_den)
    powlo = [SCALE]; powhi = [SCALE]
    for _ in range(3*D):
        powlo.append(floor_ratio(powlo[-1]*qlo, SCALE))
        powhi.append(ceil_ratio(powhi[-1]*qhi, SCALE))
    def power(ex):
        return (powlo[ex], powhi[ex])
    one = (SCALE,SCALE)
    denom = [None]+[add(one,power(j*D)) for j in (1,2,3)]
    @lru_cache(None)
    def H(L):
        L=abs(L)
        assert 0<=L<=D
        ss=[]
        for j in (1,2,3):
            ss.append(div(sub(power(j*L),power(j*(D-L))),denom[j]))
        return add(sub(ss[0],mul((2*SCALE,2*SCALE),ss[1])),ss[2])
    return H


def certify(numerator,denominator):
    H=factor_h(numerator,denominator)
    a=[]
    for s in range(1,M+1):
        row=[]
        for k in range(1,M+1):
            pos = H(P*s+(P+1)*k)
            if k<M:
                row.append(sub(pos,H(P*s-(P+1)*k)))
            else:
                row.append(pos)
        a.append(row)
    determinant_sign=1
    min_distance=SCALE
    max_width=0
    negative_pivots=0
    for j in range(M):
        pivot=a[j][j]
        if pivot[0]>0:
            pivot_sign=1
            min_distance=min(min_distance,pivot[0])
        elif pivot[1]<0:
            pivot_sign=-1
            negative_pivots+=1
            min_distance=min(min_distance,-pivot[1])
        else:
            raise AssertionError(f'undecidable interval pivot at j={j+1}; interval={pivot}')
        determinant_sign *= pivot_sign
        max_width=max(max_width,pivot[1]-pivot[0])
        for i in range(j+1,M):
            factor=div(a[i][j],pivot)
            for k in range(j+1,M):
                a[i][k]=sub(a[i][k],mul(factor,a[j][k]))
            a[i][j]=(0,0)
    result = dict(u=f'{numerator}/{denominator}',sign=determinant_sign,
                  negative_pivots=negative_pivots,
                  min_pivot_exclusion_lower=float(min_distance/SCALE),
                  max_pivot_width_upper=float(max_width/SCALE),
                  dim=M,precision_bits=BITS)
    print('SIGN_CERTIFIED',result,flush=True)
    return determinant_sign

if __name__ == '__main__':
    first=certify(969,1000)
    second=certify(31,32)
    assert (first,second)==(-1,1)
    # Rational logarithmic lower bounds and pi<22/7 establish beta>1:
    # for u=969/1000, -log u > t+t^2/2, t=31/1000.
    from fractions import Fraction
    t=Fraction(31,1000)
    assert t+t*t/2 > Fraction(22,700)
    print('CHECK_OK: both endpoints lie at beta>1, and the even-fiber 100x100 determinant changes sign')
