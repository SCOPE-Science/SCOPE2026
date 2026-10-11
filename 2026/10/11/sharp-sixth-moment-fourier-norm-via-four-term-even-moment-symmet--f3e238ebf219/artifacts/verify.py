#!/usr/bin/env python3
"""Exact algebra checks and independent finite consistency checks for a four-frequency Fourier inequality."""
from __future__ import annotations
import cmath
import itertools
import math
import random
from decimal import Decimal, getcontext
from fractions import Fraction


def conv(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def poly_add(a, b):
    z=[0]*max(len(a),len(b))
    for i,x in enumerate(a):z[i]+=x
    for i,x in enumerate(b):z[i]+=x
    return z


def poly_sub(a,b):
    return poly_add(a,[-x for x in b])


def poly_deriv(a):
    return [(i+1)*a[i+1] for i in range(len(a)-1)]


def trimmed(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def moment6(x):
    v=conv(conv(x,x),x)
    return sum(abs(z)**2 for z in v)


def norm2(x):
    return sum(abs(z)**2 for z in x)


def rvals(x):
    a,b,c,d=x
    return (a*a+b*b+c*c+d*d, a*b+b*c+c*d, a*c+b*d, a*d)


def rformula(r):
    r0,r1,r2,r3=r
    return r0**3+6*r0*(r1**2+r2**2+r3**2)+6*r1**2*r2+12*r1*r2*r3


def polynomial_exact_test():
    # Triple convolution of the coefficient-polynomial array [1,t,t,1]
    # indexed jointly by Fourier degree and power of t.
    tensor=[[0]*4 for _ in range(10)]
    for inds in itertools.product(range(4),repeat=3):
        n=sum(inds)
        tpower=sum(1 for j in inds if j==1 or j==2)
        tensor[n][tpower]+=1
    out=[0]*7
    for v in tensor:
        w=conv(v,v)
        for j,a in enumerate(w):out[j]+=a
    expected=[20,0,180,120,180,60,20]
    assert out==expected,(out,expected)
    P=[1,0,9,6,9,3,1]
    assert out==[20*k for k in P]
    # (1+t^2)P'-6tP = -3t(t^5+4t^4+t^3-6t-4).
    lhs=poly_sub(conv([1,0,1],poly_deriv(P)),conv([0,6],P))
    rhs=conv([0,-3],[-4,-6,0,1,4,1])
    assert trimmed(lhs)==trimmed(rhs),(lhs,rhs)


def rational_exact_test():
    rg=random.Random(1990)
    for i in range(300):
        x=[Fraction(rg.randint(0,40),rg.randint(1,20)) for j in range(4)]
        r=rvals(x)
        assert moment6(x)==rformula(r)
        a,b,c,d=x
        # The two Cauchy-Schwarz square inequalities are exact.
        assert (a*b+c*d)**2 <= (a*a+d*d)*(b*b+c*c)
        assert (a*c+b*d)**2 <= (a*a+d*d)*(b*b+c*c)
        assert 2*a*d<=a*a+d*d
        assert 2*b*c<=b*b+c*c


def decimal_root_and_optimizer():
    getcontext().prec=65
    D=Decimal
    def H(t):return t**5+4*t**4+t**3-6*t-4
    lo,hi=D('1.161'),D('1.162')
    assert H(lo)<0<H(hi)
    for i in range(220):
        md=(lo+hi)/2
        if H(md)>0: hi=md
        else:lo=md
    r=(lo+hi)/2
    F=D(5)*(r**6+3*r**5+9*r**4+6*r**3+9*r**2+1)/(D(2)*(1+r*r)**3)
    assert abs(r-D('1.16174797736568'))<D('0.00000000000002')
    assert abs(F-D('9.20352638278473'))<D('0.00000000000002')
    return float(r),float(F)


def complex_grid_tests(rho,C6):
    rg=random.Random(684)
    N=64  # exact quadrature for a trigonometric polynomial of degree <=9, up to rounding
    for k in range(150):
        x=[complex(rg.uniform(-1,1),rg.uniform(-1,1)) for j in range(4)]
        v=moment6(x)
        samples=[]
        for t in range(N):
            z=cmath.exp(2j*math.pi*t/N)
            poly=sum(x[j]*z**j for j in range(4))
            samples.append(abs(poly)**6)
        assert abs(v-sum(samples)/N)<2e-8*(1+v)
        base=norm2(x)
        assert v<=C6*base**3*(1+1e-12)
        a,b,c,d=[abs(y) for y in x]
        A=math.sqrt((a*a+d*d)/2)
        B=math.sqrt((b*b+c*c)/2)
        for s in (2,3,4,5,6):
            def m(x):
                w=list(x)
                for _ in range(s-1):w=conv(w,x)
                return sum(abs(y)**2 for y in w)
            assert m(x)<=m([A,B,B,A])*(1+5e-12)
    for beta in (0,0.13,0.77,2.12,math.pi):
        x=[1,rho*cmath.exp(1j*beta),rho*cmath.exp(2j*beta),cmath.exp(3j*beta)]
        val=moment6(x)/norm2(x)**3
        assert abs(val-C6)<1e-10


def main():
    polynomial_exact_test()
    rational_exact_test()
    rho,c=decimal_root_and_optimizer()
    complex_grid_tests(rho,c)
    print('VERIFY_OK exact_convolution=PASS exact_derivative=PASS rational_tests=300 complex_grids=150 all_even_symmetry=2..6')
    print('root=%.15f sharp_sixth_power=%.15f' % (rho,c))

if __name__=='__main__':main()
