#!/usr/bin/env python3
"""Exact independent slice-count checks for low-dimensional lattice joins.
Run with Python 3.10 or later; no third-party dependencies.
"""
from fractions import Fraction as F
from math import gcd


def finite_polynomial(values):
    """Monomial coefficients from integer values at 0,1,...,degree."""
    degree=len(values)-1
    out=[F(0)]*(degree+1)
    for j,v in enumerate(values):
        basis=[F(1)]
        denom=1
        for i in range(degree+1):
            if i==j:continue
            nxt=[F(0)]*(len(basis)+1)
            for k,c in enumerate(basis):
                nxt[k]-=i*c
                nxt[k+1]+=c
            basis=nxt
            denom*=j-i
        for k,c in enumerate(basis):out[k]+=F(v,denom)*c
    return out


def interval_slice(t,a,b):
    return sum((a*(t-j)+1)*(b*j+1) for j in range(t+1))


def interval_coeff(a,b):
    return [F(1),F(6+3*a+3*b-a*b,6),F(a+b,2),F(a*b,6)]


def polygon_slice(t,lc,b):
    return sum(lc(t-j)*(b*j+1) for j in range(t+1))


def polygon_coeff(A,B,b):
    A=F(A);B=F(B)
    return [F(1),(2*A+(3-b)*B+6*b+12)/12,((6-b)*A+3*B+6*b)/12,(4*A+b*B)/12,A*b/12]


def rectangle_counts(u,v):
    return lambda t:(u*t+1)*(v*t+1)


def triangle_counts(m,h):
    # Directly enumerate points in dilates of the right lattice triangle
    def count(t):
        return sum(1 for x in range(m*t+1) for y in range(h*t+1) if h*x+m*y<=m*h*t)
    return count


def main():
    cases=0
    for a in range(1,23):
      for b in range(1,23):
        vals=[interval_slice(t,a,b) for t in range(4)]
        assert finite_polynomial(vals)==interval_coeff(a,b),(a,b)
        for t in (4,5,9):
          assert interval_slice(t,a,b)==sum(c*t**i for i,c in enumerate(interval_coeff(a,b)))
        cases+=1
    assert interval_coeff(7,7)[1]==F(-1,6)
    assert all(interval_coeff(a,b)[1]>=0 for a in range(1,50) for b in range(1,50) if a*b<49)
    assert (interval_coeff(6,8)[1],interval_coeff(7,7)[1])==(0,F(-1,6))

    for u in range(1,16):
      for v in range(1,9):
        B=2*(u+v);A=u*v
        f=rectangle_counts(u,v)
        for b in range(1,14):
          val=[polygon_slice(t,f,b) for t in range(5)]
          assert finite_polynomial(val)==polygon_coeff(A,B,b),(u,v,b)
          assert polygon_slice(7,f,b)==sum(c*7**i for i,c in enumerate(polygon_coeff(A,B,b)))
          cases+=1
    for m in range(1,17):
      for h in range(1,8):
        A=F(m*h,2);B=m+h+gcd(m,h)
        f=triangle_counts(m,h)
        base=[f(t) for t in range(5)]
        assert all(base[t]==A*t*t+F(B*t,2)+1 for t in range(5))
        for b in range(1,13):
          vals=[polygon_slice(t,f,b) for t in range(5)]
          assert finite_polynomial(vals)==polygon_coeff(A,B,b),(m,h,b)
          cases+=1

    assert polygon_coeff(F(39,2),41,5)[1]==F(-1,12)
    c=polygon_coeff(148,82,8)
    assert c[1:3]==[F(-9,2),F(-1,6)]
    assert all(polygon_coeff(148,82,b)[1]<0 and polygon_coeff(148,82,b)[2]<0 for b in range(8,100))
    assert all(polygon_coeff(148,82,b)[2]>=0 or polygon_coeff(148,82,b)[1]>=0 for b in range(1,8))
    assert polygon_slice(1,rectangle_counts(37,4),8)==199
    assert polygon_slice(2,rectangle_counts(37,4),8)==2402
    print('LATTICE_JOIN_SIGN_PHASE_OK cases=',cases)

if __name__=='__main__':main()
