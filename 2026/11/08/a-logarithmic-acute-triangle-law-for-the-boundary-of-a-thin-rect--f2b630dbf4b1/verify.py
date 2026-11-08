"""Reproducible checks for perimeter-uniform acute triangles in long rectangles.

Requires Python 3, sympy, mpmath. These are supplementary checks; the
all-aspect theorem is established by the geometric integration and bounds.
"""
import math
import sympy as sp
import mpmath as mp

L = sp.symbols('L', positive=True)
r = sp.symbols('r', positive=True)
s = sp.sqrt(L**2-4)
A = L**2 / 2 - L*s/2 + 2*sp.log((L+s)/2)
B = (L**3-(L**2-4)**sp.Rational(3,2))/3
assert sp.simplify(sp.diff(A,L) - (L-s))==0
assert sp.simplify(sp.diff(B,L) - L*(L-s))==0
assert sp.simplify(A.subs(L,sp.Integer(2))-2)==0
assert sp.simplify(B.subs(L,sp.Integer(2))-sp.Rational(8,3))==0

x=sp.symbols('x',positive=True)
series_A=sp.series(A.subs(L,1/x)+2*sp.log(x)-1,x,0,3).removeO().expand()
series_B=sp.series(B.subs(L,1/x)-2/x,x,0,2).removeO().expand()
assert sp.simplify(series_A+x**2)==0
assert sp.simplify(series_B+2*x)==0

mp.mp.dps=55
def w(t):
    return t if t<=2 else t-mp.sqrt(t*t-4)
def J_quad(ell):
    if ell<=2: return mp.quad(lambda t:(ell-t)*t,[0,ell])
    return mp.quad(lambda t:(ell-t)*t,[0,2]) + mp.quad(lambda t:(ell-t)*w(t),[2,ell])
def J_closed(ell):
    if ell<=2: return ell**3 / 6
    sq=mp.sqrt(ell*ell-4)
    av=ell*ell/2 -ell*sq/2+2*mp.log((ell+sq)/2)
    bv=(ell**3-(ell*ell-4)**mp.mpf('1.5'))/3
    return ell*av-bv
for ell in [2,3,4,10,20,100]:
    assert abs(J_quad(mp.mpf(ell))-J_closed(mp.mpf(ell)))<mp.mpf('1e-40')

def p_dom(ell):
    return 3*J_closed(ell)/(2*(ell+1)**3)
def p_approx(ell):
    return (3*mp.log(ell)-mp.mpf('1.5'))/ell**2

for ell in [100,500,1000,2000]:
    normalized=(p_dom(mp.mpf(ell))-p_approx(mp.mpf(ell)))*ell**3/mp.log(ell)
    assert abs(normalized)<15

# Representative finite-aspect estimates for the exact dominant event.
for ell in (2,10,100,1000):
    bound=(12*(2+4*math.log(ell))+8+48/ell)/(2*(ell+1))**3
    val=float(p_dom(mp.mpf(ell)))
    print('L=%4d: dominant %.12g; rigorous total in [%.12g, %.12g]' %
          (ell,val,val,val+bound))
print('VERIFY_OK primitive_derivatives=2 endpoint_values=2 symbolic_series=2 quadratures=6 asymptotic_checks=4')
