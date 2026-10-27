#!/usr/bin/env python3
"""Self-contained independent-arithmetic checks of the stated finite identities.
This is not a substitute for the proof of the universal result.
"""
import cmath
import math
from fractions import Fraction as F


def symbol(r, q):
    return (
        ((r-1)*(r-2) + q*r*(r-1))/2,
        r*(2-r),
        (r*(r-1)+q*r*(r+1))/2,
        1-r*r,
    )


def matrix_norm_squared(b):
    a, v, c, d = b
    tr = abs(a)**2 + abs(v)**2 + abs(c)**2 + abs(d)**2
    dt = abs(a*d-v*c)**2
    return (tr + math.sqrt(max(0., tr*tr-4*dt)))/2


def formula(r):
    u=r*(1-r)
    return 1-2*u+2*u*u+2*u*math.sqrt(1+(1-u)**2)


def real_matrix(n,r):
    T=[[0.0 for _ in range(2*n)] for _ in range(2*n)]
    for k in range(n):
        for j,x in [(2*k,r),(2*k+1,1+r)]:
            vals=[(x-1)*(x-2)/2,x*(2-x),x*(x-1)/2]
            for d,z in enumerate(vals):T[j][(2*k+d)%(2*n)]+=z
    return T


def shifted_matrix(n,s):
    T=[[0.0 for _ in range(2*n)] for _ in range(2*n)]
    for j in range(2*n):
        x=j+s
        k=math.floor(x/2)
        t=x-2*k
        vals=[(t-1)*(t-2)/2,t*(2-t),t*(t-1)/2]
        for d,z in enumerate(vals):T[j][(2*k+d)%(2*n)]+=z
    return T

def real_norm(T,v):
    return math.sqrt(sum(sum(a*x for a,x in zip(row,v))**2 for row in T))


def verify():
    tests=0
    for numer in range(101):
        r=F(numer,100)
        u=r*(1-r)
        a,b,c,d=symbol(r,F(1))
        trace=a*a+b*b+c*c+d*d
        det=(a*d-b*c)**2
        assert trace == 2-4*u+4*u*u
        assert det == 1-4*u
        tests+=1
        for q in (complex(1.),complex(-1.),complex(0.,1.),cmath.exp(1j*math.pi/3)):
            z=(1-q.real)/2
            aa,bb,cc,dd=symbol(float(r),q)
            tr=abs(aa)**2+abs(bb)**2+abs(cc)**2+abs(dd)**2
            dt=abs(aa*dd-bb*cc)**2
            assert math.isclose(tr,2-4*float(u)+4*float(u)**2+2*float(u)*(1-float(u))*z,abs_tol=4e-14)
            assert math.isclose(dt,1-4*float(u)+float(u)*(2+float(u))*z,abs_tol=4e-14)
            assert matrix_norm_squared((aa,bb,cc,dd)) <= formula(float(r))+5e-13
            tests+=1
    # Complete discrete Fourier sweeps: all singular blocks, across several periods.
    for n in (2,3,4,5,7,11,16,25):
        for j in range(1,100):
            r=j/100
            qnorms=[matrix_norm_squared(symbol(r,cmath.exp(2j*math.pi*k/n))) for k in range(n)]
            assert abs(qnorms[0]-formula(r))<1e-12
            assert all(qnorms[0]>=a-2e-12 for a in qnorms)
            tests+=n
    # Sharp nonnegative-input witness and exact rational elementary update.
    r=F(1,2)
    a,b,c,d=symbol(r,F(1))
    assert (a,b,c,d)==(F(1,4),F(3,4),F(1,4),F(3,4))
    assert a+3*b == c+3*d == F(5,2)
    assert F(2)*F(5,2)**2 / (1+9)==F(5,4)
    for n in (2,3,4,5,11,17):
        T=real_matrix(n,0.5)
        v=[1.0 if j%2==0 else 3.0 for j in range(2*n)]
        assert math.isclose(real_norm(T,v)/math.sqrt(sum(x*x for x in v)),math.sqrt(5)/2,abs_tol=1e-13)
        tests+=1
    # Arbitrary signed Courant displacement and parity-preserving cycle reductions.
    for n in (2,3,5,8):
        for k in range(-16,17):
            s=k/4
            A=shifted_matrix(n,s)
            t=s-math.floor(s)
            predicted=formula(t)
            qs=[cmath.exp(2j*math.pi*m/n) for m in range(n)]
            bmax=max(matrix_norm_squared(symbol(t,q)) for q in qs)
            assert abs(bmax-predicted)<3e-12
            for j in range(2*n):
                column=[A[i][j] for i in range(2*n)]
                assert sum(z*z for z in column)<=predicted+1e-12
            tests+=1
    print(f'PASS: {tests} exact-rational or floating algebra/block/witness checks. Universal claims proved separately.')


if __name__=='__main__':verify()
