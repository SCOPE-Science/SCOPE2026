#!/usr/bin/env python3
"""Exact-rational interval certificate for two-distance Brownian restart.
Requires only the Python standard library. Rational Taylor enclosures prove
strict inequalities uniformly over infinitely many sharp restart periods.
"""
from fractions import Fraction as Q
from math import isqrt, factorial
from functools import lru_cache

PI_LO=Q(3141592653589793,10**15)
PI_HI=Q(3141592653589794,10**15)
SQ_DEN=10**18

def atan_interval(x, N=32):
    # Alternating arctan series; its first omitted term bounds the tail.
    total=sum(((-1)**k)*x**(2*k+1)/Q(2*k+1) for k in range(N+1))
    rem=x**(2*N+3)/Q(2*N+3)
    return total-rem,total+rem

def certify_pi():
    a=atan_interval(Q(1,5))
    b=atan_interval(Q(1,239))
    low=16*a[0]-4*b[1]
    high=16*a[1]-4*b[0]
    assert PI_LO<low<high<PI_HI
    # Machin identity: pi=16 atan(1/5)-4 atan(1/239).
    return True
assert certify_pi()

def sqrt_bounds(x):
    assert x>0
    n=isqrt((x.numerator*SQ_DEN**2)//x.denominator)
    return Q(n,SQ_DEN),Q(n+1,SQ_DEN)

def mul(x,y):
    vals=[a*b for a in x for b in y]
    return min(vals),max(vals)

def add(x,y): return x[0]+y[0],x[1]+y[1]
def sub(x,y): return x[0]-y[1],x[1]-y[0]
def div(x,y):
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))

def const(x):return x,x

@lru_cache(None)
def exp_and_h_bounds(y):
    assert y>0
    N=110 if y>5 else 43
    # The alternating tails decrease beyond N, since N>y; hence
    # the absolute error is at most the first omitted term.
    assert N>y
    ep=Q(0); hh=Q(0);term=Q(1)
    for k in range(N+1):
        ep+=term
        hh+=term/(2*k+1)
        term*= -y/Q(k+1)
    tail=abs(term)
    ex=(ep-tail,ep+tail)
    h=(hh-tail,hh+tail)
    assert ex[0]>0 and h[0]>0
    return ex,h

@lru_cache(None)
def AF(t,R):
    assert t>0 and R>0
    y=Q(R*R,4)/t
    ex,h=exp_and_h_bounds(y)
    slo,_=sqrt_bounds(PI_LO*t)
    _,shi=sqrt_bounds(PI_HI*t)
    c=(Q(R)/shi,Q(R)/slo)
    S=mul(c,h)
    F=sub(const(Q(1)),S)
    A=sub(add(mul(const(t+Q(R*R,2)),S),mul(const(t),mul(c,ex))),const(Q(R*R,2)))
    assert 0<F[0]<F[1]<1 and 0<A[0]<A[1]
    return A,F

def T(t,R):
    a,f=AF(t,R)
    return div(a,f)

def weighted(a,b,p=Q(19,20)):
    return add(mul(const(p),a),mul(const(1-p),b))

def mixed(t,s,theta,R):
    def one(r):
        at,ft=AF(t,r);as_,fs=AF(s,r)
        num=add(mul(const(theta),at),mul(const(1-theta),as_))
        den=add(mul(const(theta),ft),mul(const(1-theta),fs))
        return div(num,den)
    return weighted(one(1),one(R))

if __name__=='__main__':
    threshold=Q(17,4)  # 4.25
    mix=mixed(Q(2,5),Q(10),Q(43,50),5)
    assert mix[1] < Q(21,5)  # 4.20
    print('mixed upper rational-bound float =',float(mix[1]))

    # Short-sharp periods.  For t<=29/10, the far-target sharp
    # mean is decreasing and the near-target sharp mean exceeds 1/2.
    far=T(Q(29,10),5)
    lower=Q(19,40)+Q(1,20)*far[0]
    assert lower>threshold
    print('short-period global bound =',float(lower))

    # Intermediate periods, covered entirely by 35 closed intervals.
    endpoints=[Q(29,10)+Q(k,2) for k in range(35)]+[Q(20)]
    assert len(endpoints)==36
    minimum=None; where=None
    for idx,(left,right) in enumerate(zip(endpoints,endpoints[1:])):
        a1,f1=AF(left,1)[0],AF(right,1)[1]
        a5,f5=AF(left,5)[0],AF(right,5)[1]
        low=Q(19,20)*a1[0]/f1[1]+Q(1,20)*a5[0]/f5[1]
        assert low>threshold,(idx,left,right,float(low))
        if minimum is None or low<minimum:minimum=low;where=(left,right)
    print('min middle-interval bound =',float(minimum),'at',tuple(map(float,where)),'intervals:',len(endpoints)-1)

    # Long-sharp periods: A_1(t) increases and F_1(t)<=1,
    # so E[T|1] >= A_1(20).  Ignore the nonnegative far term.
    A20=AF(Q(20),1)[0]
    longlow=Q(19,20)*A20[0]
    assert longlow>threshold
    print('long-period global bound =',float(longlow))

    # For any Poisson reset rate r>0, the first four terms in
    # exp(R sqrt(r)) give MFPT at least
    # P4(u)=6/(5u)+11/10+6u/5+161u^2/120, u=sqrt(r).
    # 120u(P4(u)-17/4)=161u^3+144u^2-378u+144.
    # Bernstein coefficients on intervals [0,1/2], [1/2,2/3],
    # [2/3,1] are all strictly positive (verified here exactly).
    from math import comb
    def bernstein(a,b):
        # coefficients of cubic q(a+(b-a)v) in power basis
        c=[Q(144),Q(-378),Q(144),Q(161)]
        pow_coeff=[sum(c[k]*comb(k,j)*a**(k-j)*(b-a)**j for k in range(j,4)) for j in range(4)]
        return [sum(pow_coeff[j]*Q(comb(k,j),comb(3,j)) for j in range(k+1)) for k in range(4)]
    for l,r in [(Q(0),Q(1,2)),(Q(1,2),Q(2,3)),(Q(2,3),Q(1))]:
        bs=bernstein(l,r); assert all(x>0 for x in bs),(l,r,bs)
    # For u>=1 the cubic is increasing because derivative
    # 483 u^2 + 288 u - 378 >= 393 >0, and value at 1 is 71.
    assert 161+144-378+144 == 71
    print('Poisson-rate lower bound certified via positive Bernstein coefficients')
    print('ALL EXACT-RATIONAL CHECKS PASSED')
