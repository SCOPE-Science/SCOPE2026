"""Exact rational certificates for the six-cell SSPRK3-DG entropy threshold.
Requires Python 3 standard library only. No floating point is used.
Run: python3 check_six_cell_entropy.py
"""
from fractions import Fraction as F
from math import comb

def add(a,b):
    n=max(len(a),len(b))
    return tuple((a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(n))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return tuple(c)
def scale(a,c):return tuple(c*x for x in a)
def shift(a):return (F(0),)+a
def const(x):return (F(x),)
def coeff(a,k):return a[k] if k<len(a) else F(0)
def bernstein_range(p):
    # p(s)=sum a_j s^j, 0<=s<=1/4: transform to t=4s in [0,1]
    n=len(p)-1
    bs=[sum((p[j]/(4**j))*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
    return min(bs),max(bs)
def scheme(N):
    one=const(1);zero=const(0)
    init=[(one if i>=N//2 else zero,zero) for i in range(N)]
    def rhs(z):
        flux=[]
        for i in range(N):
            a=add(z[i][0],z[i][1]);b=sub(z[(i+1)%N][0],z[(i+1)%N][1])
            flux.append(sub(scale(add(mul(a,a),mul(b,b)),F(1,4)),scale(sub(b,a),F(3,4))))
        return [(sub(flux[(i-1)%N],flux[i]),sub(add(scale(mul(z[i][0],z[i][0]),F(3)),mul(z[i][1],z[i][1])),scale(add(flux[i],flux[(i-1)%N]),F(3)))) for i in range(N)]
    def update(z0,z1,d,s_weight,base_weight):
        return [tuple(add(add(scale(z0[i][j],base_weight),scale(z1[i][j],1-base_weight)),shift(scale(d[i][j],s_weight))) for j in range(2)) for i in range(N)]
    d0=rhs(init)
    one_stage=update(init,init,d0,F(1),F(0))
    d1=rhs(one_stage)
    two_stage=update(init,one_stage,d1,F(1,4),F(3,4))
    d2=rhs(two_stage)
    last=update(init,two_stage,d2,F(2,3),F(1,3))
    return init,one_stage,two_stage,last

def assert_poly(a,b):
    assert all(coeff(a,i)==coeff(b,i) for i in range(max(len(a),len(b))))

# Denominators and coefficients written as exact expected new theorem formulas.
expected = {
6: (384, [0,0,528,-1560,-392,1545,1158,-195]),
8: (384, [0,0,480,-1320,-728,1999,578,63]),
10:(24, [0,0,30,-82,-46,125,36,4]),
12:(24, [0,0,30,-82,-46,125,36,4]),
}
for N in (2,4,6,8,10,12):
    stages=scheme(N)
    # All input states at all three DG evaluations fall within [-1/2,3/2].
    for z in stages[:3]:
        for m,b in z:
            for trace in (add(m,b),sub(m,b)):
                low,high=bernstein_range(trace)
                assert low>=F(-1,2),(N,low)
                assert high<=F(3,2),(N,high)
    final=stages[3]
    # Conservation of the sum of means, as expected from periodic DG.
    sm=const(0)
    for m,b in final:sm=add(sm,m)
    assert_poly(sm,const(N//2))
    if N in (2,4):
        # All means in [0,1] for *every* 0 <= s <= 1/4.
        for m,b in final:
            l,h=bernstein_range(m)
            assert l>=0 and h<=1,(N,l,h)
    else:
        m=final[N//2+1][0]
        numerator=tuple(F(v,expected[N][0]) for v in expected[N][1])
        assert_poly(sub(m,const(1)),numerator)
        # Every target overshoot > s^2 /4 on 0 < s <= 1/4.
        # An elementary lower bound for the parenthesis suffices.
        if N==6:
            assert F(528)-F(1560,4)-F(392,16)-F(195,1024)>F(384,4)
        elif N==8:
            assert F(480)-F(1320,4)-F(728,16)>F(384,4)
        else:
            assert F(30)-F(82,4)-F(46,16)>F(24,4)
        # An exact rational witness at s=1/4.
        val=sum(coeff(m,k)/4**k for k in range(len(m)))
        assert val>1+F(1,128)
    print('PASS N=',N,'exact symbolic SSPRK3, mass, traces and bounds')
print('CERTIFICATE_OK')
