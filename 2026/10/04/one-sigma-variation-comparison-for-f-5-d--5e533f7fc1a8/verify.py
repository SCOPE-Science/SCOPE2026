from fractions import Fraction as F
from math import isqrt
import sympy as sp

# Exact rational interval arithmetic for the finite prefix 5<=d<=26.
DIG=70; SCALE=10**DIG
def sqrti(x):
    p,q=x.numerator,x.denominator; N=(p*SCALE*SCALE)//q; k=isqrt(N)
    return (F(k,SCALE),F(k+1,SCALE))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[1],a[1]-b[0])
def mul(a,b):
    z=[a[i]*b[j] for i in (0,1) for j in (0,1)]; return (min(z),max(z))
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def scale(a,c): return mul(a,(F(c),F(c)))
def powi(a,n):
    r=(F(1),F(1)); b=a
    while n:
        if n&1:r=mul(r,b)
        b=mul(b,b); n//=2
    return r
def sqrtI(a): return (sqrti(a[0])[0],sqrti(a[1])[1])
def AB(y):
    one=(F(1),F(1)); five=(F(5),F(5))
    sa=sqrti(F(2*(y+5),5*(y-2))); sb=sqrti(F(2*(y+3),5*(y-4)))
    A=div(five,add(five,div((F(y),F(y)),add(one,sa))))
    B=div(five,add(five,div((F(y-2),F(y-2)),add(one,sb))))
    return A,B
def M(y):
    one=(F(1),F(1)); A,B=AB(y); q=div(sub(one,B),sub(one,A)); h=F(y,2)
    r=powi(q,y//2) if y%2==0 else mul(powi(q,(y-1)//2),sqrtI(q))
    u=div(sub(one,A),A); v=sub(one,q)
    out=scale(sub(one,r),2)
    out=add(out,scale(mul(u,sub(one,mul(r,add(one,scale(v,h))))),F(3,1)/(h+1)))
    return sub(out,scale(A,2))
for y in range(5,27):
    assert M(y)[0]>0, y

# Exact algebraic tail certificates using resultants and Sturm root counts.
Y,a,b=sp.symbols('Y a b')
fa=5*(Y-2)*a**2-2*(Y+5); fb=5*(Y-4)*b**2-2*(Y+3)
A=5*(1+a)/(Y+5*(1+a)); B=5*(1+b)/(Y-2+5*(1+b))
h=Y/2; u=(1-A)/A; v=(B-A)/(1-A); z=h*v
L=sp.factor(2*z-z**2 + (3*u/(2*(h+1)))*(1-z)*z**2 - 2*A)
num=sp.fraction(sp.together(L))[0]
RL=sp.factor(sp.resultant(sp.resultant(num,fb,b),fa,a))
PL=sp.Poly(sp.factor(RL/(-200000000000000*(Y-2)**4)),Y,domain=sp.QQ)
assert PL.degree()==26 and sp.count_roots(PL,27,sp.oo)==0
aval=sp.sqrt(sp.Rational(64,125)); bval=sp.sqrt(sp.Rational(60,115))
assert sp.N(L.subs({Y:27,a:aval,b:bval}),50)>0

nz=sp.fraction(sp.together(z-1))[0]
Rz=sp.factor(sp.resultant(sp.resultant(nz,fb,b),fa,a))
Pz=sp.Poly(sp.factor(Rz/(-10000*(Y-2)**4)),Y,domain=sp.QQ)
assert Pz.as_expr()==9*Y**4-38*Y**3-162*Y**2+956*Y-2329
assert sp.count_roots(Pz,27,sp.oo)==0 and sp.N(z.subs({Y:27,a:aval,b:bval}),50)<1

C=5*(1-a)/(Y+5*(1-a)); D=5*(1-b)/(Y-2+5*(1-b)); delta=D-C
N=sp.factor(2*C-Y/(1-C)*(delta+sp.Rational(3,4)*delta**2/C+sp.Rational(1,8)*delta**3/C**2))
nN=sp.fraction(sp.together(N))[0]
RN=sp.factor(sp.resultant(sp.resultant(nN,fb,b),fa,a))
PN=sp.Poly(sp.factor(RN/(4000000000000*(Y-2)**4)),Y,domain=sp.QQ)
assert PN.degree()==22 and sp.count_roots(PN,14,sp.oo)==0
aval14=sp.sqrt(sp.Rational(38,60)); bval14=sp.sqrt(sp.Rational(34,50))
assert sp.N(N.subs({Y:14,a:aval14,b:bval14}),50)>0

T=3*Y**4-37*Y**3-108*Y**2+640*Y-800
for y in range(5,14): assert T.subs(Y,y)<0
r=sp.symbols('r', nonnegative=True)
assert sp.expand(T.subs(Y,14+r))==3*r**4+131*r**3+1866*r**2+8788*r+712
print('VERIFY_OK')
