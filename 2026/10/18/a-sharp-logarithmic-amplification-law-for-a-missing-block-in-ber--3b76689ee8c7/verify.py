#!/usr/bin/env python3
"""Independent finite arithmetic checks for deleted-block Berrut interpolation.
Run: python3 verify.py   (Python standard library only).
The tests do not establish an asymptotic theorem.
"""
from fractions import Fraction as F
from math import log

def nodes(N, k, h):
    return list(range(0, h + 1)) + list(range(h + k + 1, N + 1))

def rational_parts(ns, x):
    terms = [F(1, 1)/(x - v) for v in ns]
    signed = sum(((-1)**j * t for j, t in enumerate(terms)), F(0))
    a = sum((abs(t) for t in terms), F(0))
    return a, abs(signed)

def gap_parts(N, k, h, x):
    L = k + 1
    a = F(L, 2)
    s = x - (h + a)
    p = h + 1
    q = N - h - L + 1
    left = [F((-1)**r, 1)/(a+s+r) for r in range(p)]
    right = [F((-1)**r, 1)/(a-s+r) for r in range(q)]
    aa = sum((abs(v) for v in left+right),F(0))
    return aa, sum(left+right,F(0))

def delta(k, count=300000):
    # Euler transformed alternating sum, with fast 1/t integral via Simpson.
    from math import exp
    L=k+1
    a=L/2
    # nonnegative integral representation, trapezoidal on t in (0,1)
    # for a>=1, smooth integrand; use fine midpoint quadrature.
    s=0.0
    for j in range(count):
        t=(j+0.5)/count
        s += 2*t**(a-1)/(1+t)
    return s/count

def lebesgue_mid(N, k):
    L=k+1
    h=N//2-L//2
    n=nodes(N,k,h)
    x=h+L/2
    aa=sum(1/abs(x-v) for v in n)
    dd=abs(sum((-1)**j/(x-v) for j,v in enumerate(n)))
    return aa/dd

def main():
    checks=0
    # Exact rational sample tests of the reordered barycentric denominator.
    for N in (24,48,96):
        for k in (1,2,3,5):
            h=N//2-k//2-1
            ns=nodes(N,k,h)
            for r in range(1,16):
                x=F(h,1)+F((k+1)*r,16)
                if x.denominator==1 and x.numerator in ns:continue
                A,D=rational_parts(ns,x)
                A2,D2=gap_parts(N,k,h,x)
                assert A==A2 and D==D2 and D>0
                checks+=3
            # Regular-cell alternating-sign formula and its >=8/3 bound.
            for cell in range(len(ns)-1):
                if ns[cell+1]-ns[cell]!=1:continue
                for u in (F(1,4),F(1,2),F(3,4)):
                    x=ns[cell]+u
                    A,D=rational_parts(ns,x)
                    B=F(1)/u-F(1)/(u+1)+F(1)/(1-u)-F(1)/(2-u)
                    assert D>=B>=F(8,3) and A/D>=1
                    checks+=3
    # Numerical finite-cutoff checks of the (nontrivial) gap response.
    for k in (1,2,3,5):
        dn=delta(k,10000)
        assert dn>0 and abs(dn-delta(k,20000))<1e-5
        y=[lebesgue_mid(N,k) for N in (200,2000,20000)]
        assert y[0]<y[1]<y[2]
        # The normalized coefficient converges slowly: finite tests only.
        assert abs(y[-1]/log(20000)-2/dn)<1.0
        checks+=4
    assert abs(delta(1,40000)-2*log(2))<1e-5
    checks+=1
    print('PASS:',checks,'exact-rational and numerical consistency assertions')
if __name__=='__main__':main()
