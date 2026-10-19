#!/usr/bin/env python3
"""Independent exact-rational and numerical spot checks for cyclic-generator claims.
This code is auxiliary to, not a replacement for, the mathematical proof.
"""
from fractions import Fraction as F
from math import exp, sin, cos, pi, log

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def mul(A, B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), F(0)) for j in range(n)] for i in range(n)]

def add(A,B,alpha=F(1)):
    return [[x+alpha*y for x,y in zip(row,sow)] for row,sow in zip(A,B)]

def inv(A):
    n=len(A); b=[list(a)+list(e) for a,e in zip(A,eye(n))]
    for j in range(n):
        row=next(i for i in range(j,n) if b[i][j]); b[j],b[row]=b[row],b[j]
        t=b[j][j]; b[j]=[x/t for x in b[j]]
        for i in range(n):
            if i!=j:
                t=b[i][j]; b[i]=[x-t*y for x,y in zip(b[i],b[j])]
    return [x[n:] for x in b]

def power(A,k):
    B=eye(len(A))
    while k:
        if k&1:B=mul(B,A)
        k//=2
        if k:A=mul(A,A)
    return B

def cycle(n):
    P=[[F(int(j==(i+1)%n)) for j in range(n)] for i in range(n)]
    return P,add(P,eye(n),-1)

def approx(n,h,s):
    _,Q=cycle(n);m=2**s;a=F(h,2*m)
    R=mul(add(eye(n),Q,a),inv(add(eye(n),Q,-a)))
    return power(R,m)

def bisect(f,lo,hi,steps=100):
    for _ in range(steps):
        mid=(lo+hi)/2
        if f(mid)*f(lo)<=0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def run():
    checks=0
    # Every rationally evaluated matrix keeps exact unit row sums.
    for n in (2,3,4,5,6):
        for h in (F(1,10),F(3,2),F(7),F(50)):
            for s in range(4):
                T=approx(n,h,s)
                assert all(sum(row)==1 for row in T)
                checks+=1
    # Cycle length two: unsquared Padé is stochastic for all these tests.
    for h in (F(1,100),F(1),F(50),F(500)):
        assert min(x for row in approx(2,h,0) for x in row)>0
        checks+=1
    # Three-cycle: one squaring is positive at every rational test step.
    for h in (F(1,100),F(1),F(10),F(50),F(1000)):
        assert min(x for row in approx(3,h,1) for x in row)>0
        checks+=1
    # Four-cycle, 50-unit step: exact prescribed signed witness.
    row=approx(4,F(50),1)[0]
    assert row==[F(273799579,309830404),F(-9599175,309830404),
                 F(13114375,309830404),F(32515625,309830404)]
    checks+=1
    for s in (1,2,3,4):
        h=F(2_000_000)
        assert approx(4,h,s)[0][1]<0
        checks+=1
    # Fourier critical scaling and positivity transition.
    qstar=bisect(lambda x: exp(x)-1-2*sin(x),0.1,1.5)
    assert abs(qstar-0.9777603734668504)<1e-13
    checks+=1
    for q in (0.1,0.5,0.9,0.99,1.1,2,3,6):
        t0=(1+exp(-q)+2*exp(-q)*cos(q))/4
        t1=(1-exp(-q)-2*exp(-q)*sin(q))/4
        t2=(1+exp(-q)-2*exp(-q)*cos(q))/4
        t3=(1-exp(-q)+2*exp(-q)*sin(q))/4
        assert abs(t0+t1+t2+t3-1)<1e-12
        assert min(t0,t2,t3)>0
        assert (t1>0)==(q>qstar)
        checks+=1
    # Compare the exact spectral finite dyadic matrix with its critical-scale limit.
    for m in (64,128,256):
        for q in (0.6,1.2,2.5):
            h=round(2*m*m/q)
            s=m.bit_length()-1
            T=approx(4,F(h),s)
            qq=2*m*m/h
            limiting=(1-exp(-qq)-2*exp(-qq)*sin(qq))/4
            assert abs(float(T[0][1])-limiting)<0.1
            checks+=1
    print('PASS',checks,'rational/numerical assertions')

if __name__=='__main__':run()
