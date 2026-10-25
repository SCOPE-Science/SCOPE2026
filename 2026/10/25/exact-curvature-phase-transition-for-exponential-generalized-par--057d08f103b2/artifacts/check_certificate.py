"""Exact-rational certificate for the generalized-parabola exponential threshold.

Requires Python 3 and SymPy. No floating-point arithmetic is used for
inequalities, and numerical root-finding is not needed.
"""
from fractions import Fraction as F
import sympy as S

L,t=S.symbols('L t'); Y=t*(2*L-t); a=L/(4*(1-L))
E1=sum(t**j/S.factorial(j) for j in range(11))
E2=sum((2*t)**j/S.factorial(j) for j in range(13))+21*(2*t)**13/S.factorial(13)
B1=2-Y+Y**2/S.Integer(12)-Y**3/S.Integer(360)
B2=Y/S.Integer(4)-Y**2/S.Integer(12)+Y**3/S.Integer(90)
P=a*(B1*E1-2)-B2*E2
Q=S.cancel((1-L)*P/t**2)
assert S.simplify(Q*t*t-(1-L)*P)==0
poly=S.Poly(Q,t); assert poly.degree()==17
lo,hi=F(693,1000),F(694,1000)

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    v=[u*w for u in x for w in y]
    return min(v),max(v)

def intv(expr):
    cs=S.Poly(expr,L).all_coeffs()
    out=(F(0),F(0))
    for c in cs:
        out=add(mul(out,(lo,hi)),(F(c),F(c)))
    return out

coef=[intv(poly.nth(j)) for j in range(poly.degree()+1)]
assert coef[0][0]>F(468,10000)
assert all(coef[j][0]>0 for j in range(1,18) if j not in (14,16))
assert coef[14][0]<0 and coef[16][0]<0
max_t=F(1388,1000)
neg=sum(max(F(0),-x[0])*max_t**j for j,x in enumerate(coef) if j>0)
assert neg<F(23,100000)
assert coef[0][0]-neg>F(46,1000)
# Rational verification of 693/1000 < log 2 < 694/1000.
def exp_partial(x,n):return sum((x**j/F(S.factorial(j))) for j in range(n+1))
assert exp_partial(hi,10)>2
assert exp_partial(lo,13)+F(3)*lo**14/F(S.factorial(14))<2
# e<11/4, hence e^3<21 and the exponential Taylor remainder
# at t<=1.388 is at most 21 (2t)^13/13!.
assert exp_partial(F(1),8)+F(3)/F(9*S.factorial(8))<F(11,4)
assert F(11,4)**3<21
print('PASS: exact log bracket, polynomial identity, coefficient intervals')
print('Q0 lower =',float(coef[0][0]),'negative terms <=',float(neg))
print('Q lower >',float(coef[0][0]-neg))
