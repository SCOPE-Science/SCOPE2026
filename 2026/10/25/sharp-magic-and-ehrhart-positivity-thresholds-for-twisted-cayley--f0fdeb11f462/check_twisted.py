#!/usr/bin/env python3
"""Exact independent enumeration of lattice points in twisted rectangular Cayley polytopes."""
from fractions import Fraction as Q

def count(a, b, n):
    assert a >= 1 and b >= 1 and n >= 0
    return sum((1 + a*(n-k) + b*k)*(1 + b*(n-k) + a*k)
               for k in range(n+1))

def interpolate(a, b):
    y = [Q(count(a,b,n)) for n in range(4)]
    d1 = y[1]-y[0]
    d2 = y[2]-2*y[1]+y[0]
    d3 = y[3]-3*y[2]+3*y[1]-y[0]
    c3 = d3/6
    c2 = d2/2-3*c3
    c1 = d1-c2-c3
    c0 = y[0]
    B0=c0
    B1=c1-3*B0
    B2=c2-3*B0-2*B1
    B3=c3-B0-B1-B2
    return (c0,c1,c2,c3),(B0,B1,B2,B3)

def exact_formula(a,b):
    gap2=(a-b)**2
    ordinary=(Q(1),Q(a+b+1)-Q(gap2,6),Q(a*b+a+b),Q(a*a+4*a*b+b*b,6))
    magic=(Q(1),Q(a+b-2)-Q(gap2,6),Q((a-1)**2+(a-1)*(b-1)+(b-1)**2,3),Q(0))
    return ordinary, magic

def main():
    checked=0
    min_nonmagic=(10**20, None)
    min_nonordinary=(10**20, None)
    for a in range(1,61):
        for b in range(1,61):
            observed=interpolate(a,b)
            target=exact_formula(a,b)
            assert observed==target,(a,b,observed,target)
            o,mag=target
            assert all(sum(o[i]*n**i for i in range(4))==count(a,b,n) for n in (4,5,6,9))
            assert (all(v>=0 for v in mag) == ((a-b)**2 <= 6*(a+b-2)))
            assert (all(v>0 for v in o) == ((a-b)**2 < 6*(a+b+1)))
            volume = a*a+4*a*b+b*b
            if mag[1]<0 and volume<min_nonmagic[0]:min_nonmagic=(volume,(a,b))
            if o[1]<=0 and volume<min_nonordinary[0]:min_nonordinary=(volume,(a,b))
            checked+=1
    assert min_nonmagic==(97,(1,8)),min_nonmagic
    assert min_nonordinary==(141,(1,10)),min_nonordinary
    for m in range(1,61):
        o,magi=exact_formula(m,1)
        assert (all(v>=0 for v in magi))==(m<=7)
        assert (all(v>0 for v in o))==(m<=9)
    print('TWISTED_RECTANGULAR_CAYLEY_OK cases=',checked,
          ' min_magic_failure=',min_nonmagic,
          ' min_ehrhart_nonpositive=',min_nonordinary)

if __name__=='__main__': main()
