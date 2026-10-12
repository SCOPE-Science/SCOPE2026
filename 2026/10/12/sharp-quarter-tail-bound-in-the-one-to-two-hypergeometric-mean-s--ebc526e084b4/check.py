#!/usr/bin/env python3
"""Exact certificate for a one-quarter hypergeometric two-hit inequality.

No third-party dependencies. The finite grid comparison is a polynomial
identity certificate because both sides have bidegree at most five.
"""
from fractions import Fraction as F
from math import comb, factorial

# rows indexed by x power; columns indexed by y power
M = [
    [12528000, 13424880, 5677500, 1180950, 120300, 4770],
    [13424880, 14203976, 5945750, 1228840, 125110, 5004],
    [5677500, 5945750, 2466200, 505755, 51160, 2035],
    [1180950, 1228840, 505755, 102645, 10215, 395],
    [120300, 125110, 51160, 10215, 980, 35],
    [4770, 5004, 2035, 395, 35, 1],
]

def falling(a,j):
    r=1
    for h in range(j):r*=a-h
    return r

def polynomial_certificate(x,y):
    i=5+x;k=5+y;n=i*k-1
    den=falling(n,5)
    q=-30*den
    for j in range(2,6):
        q += (120//factorial(j)) * (-1)**j*(j-1) * falling(i,j)*falling(k,j)*falling(n-j,5-j)
    return q

def matrix_polynomial(x,y):
    return sum(M[a][b]*x**a*y**b for a in range(6) for b in range(6))

def tail_ge2(n,i,k):
    return F(sum(comb(i,j)*comb(n-i,k-j) for j in range(2,min(k,i)+1)
                 if 0 <= k-j <= n-i),comb(n,k))

def five_bonferroni(n,i,k):
    return sum(((-1)**j)*(j-1)*F(comb(i,j)*comb(k,j),comb(n,j))
               for j in range(2,min(5,i,k)+1))

def main():
    assert len(M)==6 and all(len(r)==6 for r in M)
    assert all(v>0 for row in M for v in row)
    count=0
    for x in range(6):
        for y in range(6):
            assert polynomial_certificate(x,y)==matrix_polynomial(x,y)
            count+=1
    # Both polynomials have degree <=5 in each variable; a 6x6 interpolation
    # grid proves formal equality globally (not a finite-experiment argument).
    for k in [2,3,4]:
        for z in range(20):
            i=5+z;n=i*k-1
            p=tail_ge2(n,i,k)
            if k==2: expected=F(1,2*z+9)
            elif k==3: expected=F(z*z+17*z+54,3*(3*z+13)*(3*z+14))
            else: expected=F(3*(z+4)*(z*z+14*z+43),2*(2*z+9)*(4*z+17)*(4*z+19))
            assert 4*p-1 == expected and p>F(1,4)
            count+=1
    for k in range(2,31):
        for n in range(4*k,18*k+1):
            i0=n//k+1
            if i0*k>2*n:continue
            h=tail_ge2(n,i0,k)
            bound=tail_ge2(i0*k-1,i0,k)
            assert h>=bound and bound>F(1,4)
            assert h>=F(k,n)
            count+=4
    for k in range(5,31):
        for i in range(5,31):
            n=i*k-1
            p=tail_ge2(n,i,k)
            b=five_bonferroni(n,i,k)
            q=polynomial_certificate(i-5,k-5)
            assert p>=b>F(1,4)
            assert 120*falling(n,5)*(b-F(1,4)) == q
            count+=3
    for h in range(6,70):
        s=sum(((-1)**j)*(j-1)*comb(h,j) for j in range(2,6))
        assert s==1-F(4*h+1,5)*comb(h-2,4) and s<=1
        count+=1
    print('PASS:',count,'exact assertions; polynomial identity via 36 interpolation nodes; all 36 coefficients positive.')

if __name__=='__main__':main()
