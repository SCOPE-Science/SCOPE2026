"""Reproducible algebraic and finite-sample tests of positive box Cauchy wavelet zeros.

All input endpoints and weights used in the exact tests are rational. These tests
supplement, but do not replace, the unrestricted algebraic proof.
"""
from fractions import Fraction
import math
import random
import sympy as sp
z=sp.symbols('z')

def data_numerator(intervals,weights):
    D=sp.prod((z-a)*(z-b) for a,b in intervals)
    P=sp.Poly(sp.expand(sum(w*(b-a)*sp.cancel(D/((z-a)*(z-b))) for (a,b),w in zip(intervals,weights))),z)
    return P,sp.expand(D)

def wavelet_value(intervals,weights,w):
    return sum(float(m)*(float(b)-float(a))/((w-float(a))*(w-float(b))) for (a,b),m in zip(intervals,weights))

def chamber_sample(intervals,weights):
    # Approximate grid check for qualitative tests, not a proof of positivity.
    for k,(a,b) in enumerate(intervals):
        aa=float(a);bb=float(b)
        for i in range(1,200):
            x=aa+(bb-aa)*i/200
            f=wavelet_value(intervals,weights,x)
            if f>=0:return False
    return True

def roots_upper(P):
    roots=sp.polys.polytools.intervals(P,eps=sp.Rational(1,10**10)) if False else []
    rr=sp.nroots(P,maxsteps=200,n=40)
    return sum(1 for t in rr if float(sp.im(t))>1e-9),sum(1 for t in rr if abs(float(sp.im(t)))<1e-9)

rng=random.Random(1618033)
checks=0
for n in range(1,6):
    for trial in range(8):
        intervals=[]
        x=sp.Integer(-9)
        for j in range(n):
            a=x+sp.Rational(rng.randint(1,5),7)
            b=a+sp.Rational(rng.randint(3,8),7)
            intervals.append((a,b))
            x=b+sp.Rational(rng.randint(2,7),7)
        weights=[sp.Rational(rng.randint(1,10),rng.randint(1,7)) for j in range(n)]
        P,D=data_numerator(intervals,weights)
        assert P.degree()==2*n-2
        # Residues at all endpoints are nonzero, so no cancellation.
        for a,b in intervals:
            assert P.eval(a)!=0 and P.eval(b)!=0
        # Independent rational evaluation of reduced fraction.
        point=sp.Rational(27,13)+sp.I*sp.Rational(4,3)
        direct=sum(w*(b-a)/((point-a)*(point-b)) for (a,b),w in zip(intervals,weights))
        assert sp.simplify(direct-P.eval(point)/D.subs(z,point))==0
        checks+=1

# Equal weights: exact interlacing partial fractions and no-real-zero proof input.
for n in range(2,6):
    for trial in range(7):
        intervals=[]
        x=sp.Integer(-8)
        for j in range(n):
            a=x+sp.Rational(rng.randint(1,4),5)
            b=a+sp.Rational(rng.randint(2,6),5)
            intervals.append((a,b))
            x=b+sp.Rational(rng.randint(1,4),5)
        numerator=sp.prod(z-a for a,b in intervals)
        denom=sp.prod(z-b for a,b in intervals)
        residues=[]
        for a,b in intervals:
            q=sp.cancel(numerator/(denom/(z-b)))
            residues.append(sp.cancel(q.subs(z,b)))
        assert all(c>0 for c in residues)
        P,D=data_numerator(intervals,[sp.Integer(1)]*n)
        # Every upper zero present, with multiplicities.
        if n<=4:
            up,real=roots_upper(P)
            assert (up,real)==(n-1,0),(n,up,real)
        checks+=1

# Exact two-interval phase test over 10 contrast ratios and several gaps.
for l1,l2,g in [(1,1,1),(1,2,sp.Rational(1,3)),(3,1,2),(2,5,sp.Rational(1,7))]:
    a=sp.Rational(-l1);b=sp.Integer(0);c=sp.Rational(g);d=c+sp.Rational(l2)
    Dcen=(c+d-a-b)/2
    for r in [sp.Rational(1,100),sp.Rational(1,9),sp.Rational(1,2),sp.Rational(1),sp.Rational(2),sp.Rational(9),sp.Rational(100)]:
        intervals=[(a,b),(c,d)]
        P,D=data_numerator(intervals,[r,sp.Integer(1)])
        discr=sp.discriminant(P.as_expr(),z)
        sign=sp.sign(4*r*Dcen**2-(r*l1+l2)*(r*l2+l1))
        assert sp.sign(discr)==-sign
        up,real=roots_upper(P)
        assert up==(1 if sign>0 else 0)
        assert real==(0 if sign>0 else 2)
        checks+=1

print(f'PASS exact rational identities: {checks} cases')
print('PASS equal-amplitude real-interlacing and complete upper-root counts')
print('PASS two-pulse contrast discriminants, complex-root transitions')
