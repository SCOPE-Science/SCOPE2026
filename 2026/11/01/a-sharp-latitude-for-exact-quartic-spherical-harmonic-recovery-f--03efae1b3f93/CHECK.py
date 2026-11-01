#!/usr/bin/env python3
"""Exact rational certificate and independent floating Gram check for the degree-four latitude theorem.
Run with Python 3 standard library only: python CHECK.py
"""
from fractions import Fraction as F
from math import comb, factorial, sqrt, pi, cos, sin

# Polynomial coefficients are ordered from low to high degree.
def add(p, q):
    n=max(len(p),len(q))
    return [ (p[i] if i<len(p) else F(0))+(q[i] if i<len(q) else F(0)) for i in range(n)]
def scale(p,c):
    return [F(c)*v for v in p]
def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,u in enumerate(p):
        for j,v in enumerate(q):r[i+j]+=u*v
    return r
def power(p,n):
    r=[F(1)]
    for _ in range(n): r=mul(r,p)
    return r
def ev(p,x):
    r=F(0)
    for a in reversed(p):r=r*x+a
    return r
def subst_affine(p,left,right):
    h=right-left
    ans=[F(0)]
    for i,c in enumerate(p):
        ans=add(ans,scale(power([left,h],i),c))
    return ans

def bernstein_coeffs(p,left,right):
    q=subst_affine(p,left,right)
    n=len(q)-1
    return [sum((q[j]*F(comb(i,j),comb(n,j)) for j in range(i+1)),F(0)) for i in range(n+1)]

T=[F(0),F(1)]
ONE=[F(1)]
Q=add(add(scale(power(T,2),35),scale(T,-30)),[F(3)])
P=add(add(scale(power(T,3),147),scale(power(T,2),-147)),add(scale(T,33),[F(-1)]))
a=[scale(power(Q,2),F(1,64)),
   scale(mul(mul(T,add(ONE,scale(T,-1))),power(add(scale(T,7),[F(-3)]),2)),F(5,16)),
   scale(mul(power(add(ONE,scale(T,-1)),2),power(add(scale(T,7),[F(-1)]),2)),F(5,32)),
   scale(mul(T,power(add(ONE,scale(T,-1)),3)),F(35,16)),
   scale(power(add(ONE,scale(T,-1)),4),F(35,128))]
identity=add(a[0],scale(add(add(add(a[1],a[2]),a[3]),a[4]),2))
assert ev(identity,F(0))==1 and all(z==0 for z in add(identity,[F(-1)]))
print('Addition-theorem polynomial identity: PASS')

outer=[(F(0),F(3,100),4,3), (F(3,100),F(3,20),4,0),
       (F(3,20),F(1,4),3,2), (F(1,3),F(1,2),3,1),
       (F(1,2),F(1),2,4)]
for left,right,i,j in outer:
    cert=bernstein_coeffs(add(scale(a[i],4),scale(a[j],-13)),left,right)
    assert all(v>=0 for v in cert)
    print('Bernstein certificate [%s,%s]: 4*a%d-13*a%d >= 0; coefficients =' % (left,right,i,j),[str(x) for x in cert])

# The exact rational isolator has P(left)>0>P(right). Uniqueness on [1/4,1/3]
# follows because P'(t)<0 there: P''(t)=882t-294<=0 and P'(1/4)<0.
lo,hi=F(27605,100000),F(27606,100000)
assert ev(P,lo)>0>ev(P,hi)
assert 3*147*F(1,4)**2-2*147*F(1,4)+33<0
assert ev(P,F(1,4))>0>ev(P,F(1,3))
# The exact optimum C lies below 13/4 throughout the isolator.
def ratio1(t):return 7*(1-t)**2/(7*t-3)**2
assert ratio1(hi)<F(13,4)
assert ratio1(lo)>F(3) and ratio1(hi)<F(13,4)

# Rational interval arithmetic encloses values a_i(root) with no floating assumptions.
def isum(a,b):return (a[0]+b[0],a[1]+b[1])
def iprod(a,b):
    v=[u*w for u in a for w in b]
    return min(v),max(v)
def ipower(a,n):
    out=(F(1),F(1))
    for _ in range(n):out=iprod(out,a)
    return out
def iconst(c):return (F(c),F(c))
def iscale(a,c):return iprod(a,iconst(c))
T0=(lo,hi); OM=isum(iconst(1),iscale(T0,-1))
L1=isum(iscale(ipower(T0,2),35),isum(iscale(T0,-30),iconst(3)))
L2=isum(iscale(T0,7),iconst(-3))
L3=isum(iscale(T0,7),iconst(-1))
intervals=[iscale(ipower(L1,2),F(1,64)),
           iscale(iprod(iprod(T0,OM),ipower(L2,2)),F(5,16)),
           iscale(iprod(ipower(OM,2),ipower(L3,2)),F(5,32)),
           iscale(iprod(T0,ipower(OM,3)),F(35,16)),
           iscale(ipower(OM,4),F(35,128))]
assert intervals[3][0] > max(intervals[i][1] for i in [0,1,2,4])
for i in (0,4):
    assert intervals[i][0] > max(intervals[1][1],intervals[2][1])
print('Unique root isolator, exact ordering at optimum: PASS', 'r in', (str(lo),str(hi)))
print('Squared condition number in', float(ratio1(lo)),float(ratio1(hi)))

# Independently check the spherical harmonics by their normalized associated-Legendre forms.
# The real or complex normalization is with respect to probability area measure on S^2.
def legendre_derivative(m,z):
    return [(35*z**4-30*z*z+3)/8,
            F(5,2)*z*(7*z*z-3),
            F(15,2)*(7*z*z-1),
            105*z,
            105][m]
checks=0
for n in (9,10,13):
    for t in (.025, .15, .27605089944806715, .3, .65):
        z=sqrt(t)
        amps={m:sqrt(9*factorial(4-m)/factorial(4+m))*(1-t)**(m/2)*float(legendre_derivative(m,z)) for m in range(5)}
        matrix=[]
        for j in range(n):
            phi=2*pi*j/n
            matrix.append([amps[abs(m)] * complex(cos(m*phi),sin(m*phi)) for m in range(-4,5)])
        Gram=[[sum(matrix[j][c].conjugate()*matrix[j][d] for j in range(n)) for d in range(9)] for c in range(9)]
        for c in range(9):
            for d in range(9):
                target=9*n*float(ev(a[abs(c-4)],F(str(t)))) if c==d else 0
                assert abs(Gram[c][d]-target)<3e-9, (n,t,c,d,Gram[c][d],target)
                checks+=1
print('Independent normalized spherical-harmonic Gram entries: PASS',checks)
print('Overall exact algebraic certificate and numerical checks: PASS')
