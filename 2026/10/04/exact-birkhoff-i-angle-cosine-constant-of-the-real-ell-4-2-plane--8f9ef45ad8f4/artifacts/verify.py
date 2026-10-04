#!/usr/bin/env python3
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 80
D=Decimal

def poly_mul(a,b):
    c=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def poly_sub(a,b):
    n=max(len(a),len(b)); c=[Fraction(0) for _ in range(n)]
    for i in range(n):
        c[i]=(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
    return c

h=[Fraction(1),Fraction(9),Fraction(6)]
B=[Fraction(1),Fraction(2),Fraction(9),Fraction(4)]
left=poly_sub(poly_mul(h,h),[9*x for x in B])
right=[Fraction(-8),Fraction(0),Fraction(12),Fraction(72),Fraction(36)]
assert left==right, (left,right)

def q(u): return D(9)*u**4+D(18)*u**3+D(3)*u**2-D(2)
lo,hi=D(0),D(1)
assert q(lo)<0 and q(hi)>0
for _ in range(300):
    m=(lo+hi)/2
    if q(m)<0: lo=m
    else: hi=m
u=(lo+hi)/2
assert hi-lo < D('1e-70')
C=(D(1)/D(6)-u*u/D(2)).sqrt()

z=u*u/(D(1)+D(3)*u*u)
t=(D(1)-(D(1)-D(4)*z).sqrt())/D(2)
a=t.sqrt().sqrt()
b=(D(1)-t).sqrt().sqrt()
c=(t**3+(D(1)-t)**3).sqrt().sqrt()
c=D(1)/c
# y=(c*b^3, -c*a^3)
y1=c*b**3; y2=-c*a**3

normx4=a**4+b**4
normy4=y1**4+y2**4
birk=a**3*y1+b**3*y2
P=((a+y1)**4+(b+y2)**4)
M=((a-y1)**4+(b-y2)**4)
obj=(P.sqrt()-M.sqrt())/D(4)
if obj<0: obj=-obj
assert abs(normx4-D(1)) < D('1e-60')
assert abs(normy4-D(1)) < D('1e-60')
assert abs(birk) < D('1e-60')
assert abs(obj-C) < D('1e-50')
assert D('0.41005') < u < D('0.41006')
assert D('0.28739') < C < D('0.28740')
print('u0=',u)
print('C_B=',C)
print('x=',a,b)
print('y=',y1,y2)
print('VERIFY_OK')
