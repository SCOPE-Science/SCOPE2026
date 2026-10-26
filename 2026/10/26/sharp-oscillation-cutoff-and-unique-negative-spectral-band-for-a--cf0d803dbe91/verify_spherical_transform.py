"""Numerical and algebraic checks of a hyperbolic spherical-transform formula.
Finite numerical checks are not substitutes for an analytic continuum proof.
"""
import mpmath as mp
import sympy as sp
mp.mp.dps=50
c=mp.pi/2
u=mp.findroot(lambda x:x*mp.tanh(x)-1,(mp.mpf('1.1'),mp.mpf('1.3')))
wstar=2*u/mp.pi
print('u_star', mp.nstr(u,40))
print('omega_star',mp.nstr(wstar,40))
for w in (mp.mpf('.3'),wstar,mp.mpf('.9'),mp.mpf('1.5')):
    for lam in (mp.mpf('.15'),mp.mpf('1.1'),mp.mpf('3.5')):
        integral = (4*mp.pi/lam)*mp.quad(lambda r:mp.sech(r)**2*mp.cos(w*r)*mp.sinh(r)*mp.sin(lam*r),[0,1,3,10,30,70])
        analytic=(mp.pi**2/lam)*((lam+w)*mp.sech(c*(lam+w))+(lam-w)*mp.sech(c*(lam-w)))
        print('w',mp.nstr(w,7),'lambda',mp.nstr(lam,5),'transform',mp.nstr(analytic,14),'error',mp.nstr(abs(integral-analytic),4))
# exact symbolic simplification of sum vs hyperbolic fraction
x,y=sp.symbols('x y',real=True)
A=sp.cosh(x)*sp.cosh(y)
B=sp.sinh(x)*sp.sinh(y)
expr=(x+y)/sp.cosh(x+y)+(x-y)/sp.cosh(x-y)
rational=2*(x*A-y*B)/(A**2-B**2)
print('Hyperbolic addition identity equals 0:',sp.simplify(sp.trigsimp(expr-rational)))
print('L2 radial unmodulated norm-squared:',mp.nstr(4*mp.pi*mp.quad(lambda r:mp.sech(r)**4*mp.sinh(r)**2,[0,1,10,50]),20))
