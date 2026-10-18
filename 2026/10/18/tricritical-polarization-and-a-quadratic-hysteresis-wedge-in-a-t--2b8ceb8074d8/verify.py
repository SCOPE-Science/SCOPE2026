"""Reproducibility checks for a logistic opinion-motif bifurcation.
Dependencies: Python 3, SymPy, mpmath. Analytical proof is in RESULT.md.
"""
import math
import sympy as sp
import mpmath as mp

x, g = sp.symbols('x g', real=True)
a = 2*g-1  # critical surface: mu=0
f = sp.sinh(2*g*x)/(sp.cosh(2*g*x)+a*sp.exp(-g*x*x))-x
ser = sp.series(f,x,0,8).removeO().expand()
c3 = sp.factor(ser.coeff(x,3))
c5 = sp.factor(ser.coeff(x,5))
assert sp.simplify(c3-(4*g*g-3)/6)==0
star = sp.sqrt(3)/2
assert sp.simplify(c3.subs(g,star))==0
assert sp.simplify(c5.subs(g,star)+sp.Rational(3,10))==0
assert sp.simplify(sp.diff(c3,g).subs(g,star)-2*sp.sqrt(3)/3)==0

mp.mp.dps=65
gs=mp.sqrt(3)/2
b=2*mp.sqrt(3)/3
ycoeff=10*mp.sqrt(3)/9
mucoeff=-mp.mpf(10)/9

def G(y,ga,mu):
    ax=2*ga/(1+mu)-1
    xx=mp.sqrt(y)
    return mp.sinh(2*ga*xx)/(xx*(mp.cosh(2*ga*xx)+ax*mp.exp(-ga*y)))-1

for nu in (mp.mpf('0.02'),mp.mpf('0.01'),mp.mpf('0.005')):
    ga=gs+nu
    Y,M=mp.findroot((lambda y,m:G(y,ga,m),lambda y,m:mp.diff(lambda t:G(t,ga,m),y)),(ycoeff*nu,mucoeff*nu*nu),tol=mp.mpf('1e-45'),maxsteps=45)
    assert Y>0 and M<0
    assert abs(G(Y,ga,M))<mp.mpf('1e-45')
    assert abs(mp.diff(lambda t:G(t,ga,M),Y))<mp.mpf('1e-40')
    assert abs(float(Y/nu-ycoeff))<.15
    assert abs(float(M/nu**2-mucoeff))<.12
    print(f'nu={mp.nstr(nu,6)}, y_fold/nu={mp.nstr(Y/nu,14)}, mu_fold/nu^2={mp.nstr(M/nu**2,14)}')

# At the degenerate point, full vector-field sign and fifth-order slope.
delta_star=1+mp.log(2*gs-1)/gs
for xx in (mp.mpf('.02'),mp.mpf('.05'),mp.mpf('.1')):
    fval=mp.sinh(2*gs*xx)/(mp.cosh(2*gs*xx)+(2*gs-1)*mp.exp(-gs*xx**2))-xx
    assert fval<0
    assert abs(float(fval/xx**5 + mp.mpf(3)/10))<.02
print('PASS: exact cubic/quintic identities, analytic fold limits, and field-direction checks')
