#!/usr/bin/env python3
"""Reproduce exact symbolic identities and sample Doppler-zero certificates."""
import sympy as sp
import mpmath as mp

x,w = sp.symbols('x w', real=True, nonzero=True)
expr = (sp.Rational(4,3)*(sp.cos(x)-sp.cos(2*x)) + (8*sp.sin(x)-4*sp.sin(2*x))/w)
fac = sp.Rational(8,3)*sp.sin(x/2)**2*(1+2*sp.cos(x)+6*sp.sin(x)/w)
assert sp.trigsimp(sp.expand_trig(expr-fac)) == 0
assert sp.simplify(sp.limit((fac/w**2).subs(x,w/3),w,0)-sp.Rational(10,27))==0
print('Exact trigonometric factorization and continuous value A(2/3,0)=10/27: PASS')

mp.mp.dps=65
third=mp.mpf(1)/3
h=third; L=2*third

def amp_num(omega):
    # On [0,1/3]: 4/9-t^2; on [1/3,2/3]: (1-t)^2-1/9.
    return 2*(mp.quad(lambda t:(mp.mpf(4)/9-t*t)*mp.cos(omega*t),[0,h]) +
              mp.quad(lambda t:((1-t)**2-mp.mpf(1)/9)*mp.cos(omega*t),[h,L]))

def Q(xx):return 1+2*mp.cos(xx)+2*mp.sin(xx)/xx if xx else mp.mpf(5)
def amp_formula(omega):
    if omega==0:return mp.mpf(10)/27
    return (mp.mpf(8)/(3*omega**2))*mp.sin(omega/6)**2*Q(omega/3)

omegas=[mp.mpf('0'),mp.mpf('0.3'),mp.mpf('1'),mp.mpf('3.75'),mp.mpf('6.5'),mp.mpf('9.25'),mp.mpf('17.1'),mp.mpf('27.5'),mp.mpf('50.0')]
errs=[]
for omega in omegas:
    a=amp_num(omega); b=amp_formula(omega)
    errs.append(abs(a-b))
assert max(errs)<mp.mpf('1e-55'),max(errs)
print('Independent piecewise oscillatory quadrature: 9 values, max error',mp.nstr(max(errs),9))

# Double zeros of exactly second order: factor gives Q(2*pi*n)=3.
for n in range(1,11):
    omega=6*mp.pi*n
    assert abs(amp_formula(omega))<mp.mpf('1e-120')
    assert abs(Q(omega/3)-3)<mp.mpf('1e-58')
print('Exact double-zero factor tests: 10 lattice sites PASS')

# Two simple Q roots per open period and no other positive Q roots
for k in range(12):
    base=2*mp.pi*k
    ra=mp.findroot(Q,(base+2*mp.pi/3+mp.mpf('.05'),base+mp.pi-mp.mpf('.05')))
    rb=mp.findroot(Q,(base+4*mp.pi/3+mp.mpf('.05'),base+2*mp.pi-mp.mpf('.05')))
    assert base<ra<base+mp.pi<rb<base+2*mp.pi
    assert abs(Q(ra))<mp.mpf('1e-55') and abs(Q(rb))<mp.mpf('1e-55')
    assert mp.diff(Q,ra)<0 and mp.diff(Q,rb)>0
    if k>=2:
        aa=base+2*mp.pi/3;bb=base+4*mp.pi/3
        assert abs((ra-aa)-1/aa) < mp.mpf(1)/k**2
        assert abs((rb-bb)-1/bb) < mp.mpf(1)/k**2
print('Simple root sequence/derivative sign: 24 roots in 12 periods PASS')

# At the resonant double zeros the complete two-variable Hessian is indefinite.
T, nu = sp.symbols('T nu', real=True)
ww=2*sp.pi*nu
H=T/2; J=1-T/2
G=(4*(1-T)*sp.cos(ww*H)-2*T*sp.cos(ww*J)+(8*sp.sin(ww*H)-4*sp.sin(ww*J))/ww)/ww**2
for n in range(1,5):
    pt={T:sp.Rational(2,3),nu:3*n}
    deriv=[]
    for vs in [(T,), (nu,), (T,T), (T,nu), (nu,nu)]:
        deriv.append(sp.simplify(sp.trigsimp(sp.diff(G,*vs).subs(pt))))
    assert deriv==[0,0,0,-sp.Rational(2,9*n),sp.Rational(4,81*n*n)], (n,deriv)
print('Exact two-variable Hessian and crossing tangents: 4 sites PASS')

print('Analytical uniqueness proof, not finite tests, establishes full census.')
