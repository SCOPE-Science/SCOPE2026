"""Finite supplementary checks for exact linearized sphere-slab area formula."""
import math
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import eval_legendre

s,h,t=sp.symbols('s h t', real=True)
for ell in range(13):
    P=sp.legendre(ell,t)
    J=sp.factor(sp.integrate(P-t*sp.diff(P,t),(t,s,s+h)))
    J_boundary=sp.factor(2*sp.integrate(P,(t,s,s+h))+s*P.subs(t,s)-(s+h)*P.subs(t,s+h))
    assert sp.simplify(J-J_boundary)==0
    if ell==0:
        assert sp.simplify(J-h)==0
    elif ell==1:
        assert J==0
    else:
        poly=sp.Poly(J,s)
        c=sp.factorial(2*ell)/(2**ell*sp.factorial(ell)**2)
        assert poly.degree()==ell
        assert sp.simplify(poly.LC()-h*(1-ell)*c)==0
    if ell%2==1:
        assert sp.simplify(J.subs(s,-h/2))==0

width=.73
offset=-.39
for ell in range(5):
    def actual_area(eps):
        r=lambda q: 1+eps*eval_legendre(ell,q)
        low=brentq(lambda q:r(q)*q-offset,-1,1)
        high=brentq(lambda q:r(q)*q-(offset+width),-1,1)
        def f(q):
            rr=r(q)
            if ell==0:
                dp=0.
            else:
                dp=ell*(q*eval_legendre(ell,q)-eval_legendre(ell-1,q))/(q*q-1)
            return 2*math.pi*rr*rr*math.sqrt(1+(1-q*q)*(eps*dp/rr)**2)
        return quad(f,low,high,epsabs=1e-12)[0]
    fd=(actual_area(1e-5)-actual_area(-1e-5))/(2e-5)
    P=sp.legendre(ell,t)
    J=sp.integrate(P-t*sp.diff(P,t),(t,s,s+h))
    expected=2*math.pi*float(J.subs({s:offset,h:width}))
    assert abs(fd-expected)<1e-7, (ell,fd,expected)
print('VERIFY_OK')
print('finite_degrees_exact=0..12')
print('independent_radial_area_checks=0..4')
print('all_levels_transversal=True')
