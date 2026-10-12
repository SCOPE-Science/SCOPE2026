"""Exact coefficient certificate and numerical checks for the fixed-horizon binary occupancy design theorem."""
from fractions import Fraction
from math import factorial
import sympy as S
import mpmath as M

x,y=S.symbols('x y')
P=x*x
polys=[P]
for k in range(4):
    P=S.expand((y-1)*(S.diff(P,x)+2*y*S.diff(P,y))-2*(k+1)*y*P)
    polys.append(P)
P2=polys[2]; P4=polys[4]
assert S.simplify(P2-(y*y*(4*x*x-8*x+2)+y*(4*x*x+8*x-4)+2))==0
assert S.simplify(P4-(y**4*(16*x*x-64*x+48)+y**3*(176*x*x-192*x-48)+y**2*(176*x*x+192*x-48)+y*(16*x*x+64*x+48)))==0

def expcoeff(P,n):
    ans=S.Integer(0)
    for (i,j),coef in S.Poly(P,x,y).terms():
        if n>=i:
            ans+=coef*(2*j)**(n-i)*factorial(n)//factorial(n-i) if False else coef*S.Integer(2*j)**(n-i)*factorial(n)/factorial(n-i)
    return S.Rational(ans)

for n in range(0,8):
    assert expcoeff(P2,n)==0 if n<3 else expcoeff(P2,n)<0, (n,expcoeff(P2,n))
for n in range(8,100):
    assert expcoeff(P2,n)>0
for n in range(0,6):
    assert expcoeff(P4,n)==0,(n,expcoeff(P4,n))
for n in range(6,26):
    assert expcoeff(P4,n)<0,(n,expcoeff(P4,n))
for n in range(26,70):
    assert expcoeff(P4,n)>0,(n,expcoeff(P4,n))
# Positive x >= 26 follows because each exponential summand's coefficient is positive separately.
for n in range(26,100):
    terms=[(16*n*(n-1)*8**(n-2)-64*n*8**(n-1)+48*8**n),
           (176*n*(n-1)*6**(n-2)-192*n*6**(n-1)-48*6**n),
           (176*n*(n-1)*4**(n-2)+192*n*4**(n-1)-48*4**n),
           (16*n*(n-1)*2**(n-2)+64*n*2**(n-1)+48*2**n)]
    assert min(terms)>0

M.mp.dps=55
f=lambda z:z*z/M.expm1(2*z) if z else M.mpf(0)
f1=lambda z:M.diff(f,z)
f2=lambda z:M.diff(f,z,2)
f3=lambda z:M.diff(f,z,3)
f4=lambda z:M.diff(f,z,4)
a=M.findroot(f2,(M.mpf('1.5'),M.mpf('1.6')))
b=M.findroot(f4,(M.mpf('2.7'),M.mpf('3.5')))
c=M.findroot(f1,(M.mpf('.7'),M.mpf('.9')))
assert M.mpf('1.54')<a<M.mpf('1.55')<b
assert M.mpf('.79')<c<M.mpf('.80')
assert f2(M.mpf('0.6'))<0 and f2(2)>0 and f4(2)<0 and f4(4)>0
for T in [M.mpf('1'),M.mpf('2'),M.mpf('3'),2*a,M.mpf('3.1'),M.mpf('4'),M.mpf('8')]:
    F=lambda q:f(q)+f(T-q)
    xs=[T*j/500 for j in range(1,500)]
    yvals=[F(q) for q in xs]
    gridmax=xs[yvals.index(max(yvals))]
    if T<=2*a:
        assert abs(gridmax-T/2)<T/100
    else:
        assert abs(gridmax-T/2)>M.mpf('.01')
# At a long horizon the best interval is close to the unconstrained single-interval maximum.
T=M.mpf(8)
opt=M.findroot(lambda q:f1(q)-f1(T-q),(.7,.9))
assert abs(opt-c)<M.mpf('.0002')
print('VERIFY_OK P2_signs=3..7_negative_8plus_positive P4_signs=6..25_negative_26plus_positive')
print('inflection_a=',M.nstr(a,35),'threshold_2a=',M.nstr(2*a,35),'fourth_deriv_turn_b=',M.nstr(b,30))
print('single_gap_optimum=',M.nstr(c,30),'T8_short_optimum=',M.nstr(opt,30))
