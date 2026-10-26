"""Reproducible symbolic and numerical checks of a three-frequency sinc Gram design.
Run with: python check.py  (requires sympy, numpy, mpmath).
The infinite statements are proved analytically in RESULT.md, not by this checker.
"""
import sympy as sp
import numpy as np
import mpmath as mp

E, t = sp.symbols('E t', real=True)
sinc_polynomial = lambda z: sum((-1)**j*z**(2*j)/sp.factorial(2*j+1) for j in range(5))
u = sinc_polynomial(E*(1+t))
v = sinc_polynomial(E*(1-t))
w = sinc_polynomial(2*E)
G = sp.Matrix([[1,u,w],[u,1,v],[w,v,1]])
D6 = sp.factor(sp.expand(G.det()).coeff(E,6))
D8 = sp.factor(sp.expand(G.det()).coeff(E,8))
S2 = sp.factor(sp.expand(3-u**2-v**2-w**2).coeff(E,2))
c = sp.cancel(D6/S2)
assert sp.simplify(D6-4*(1-t*t)**2/sp.Integer(135)) == 0
assert sp.simplify(D8+16*(1-t*t)**2*(t*t+3)/sp.Integer(4725)) == 0
assert sp.simplify(S2-2*(t*t+3)/sp.Integer(3)) == 0
assert sp.simplify(c-2*(1-t*t)**2/(45*(t*t+3))) == 0
assert sp.simplify(c.subs(t,0)-sp.Rational(2,135)) == 0
assert sp.simplify(sp.diff(c,t,2).subs(t,0)+sp.Rational(28,405)) == 0

s=sp.sin(E)/E
cc=sp.sin(2*E)/(2*E)
lam=1+cc/2-sp.sqrt(cc**2/4+2*s**2)
assert sp.series(lam,E,0,8).removeO().expand() == sp.Rational(2,135)*E**4+sp.Rational(2,1701)*E**6

mp.mp.dps=65
checks=8
for a in [mp.mpf('0.12'),mp.mpf('0.2'),mp.mpf('0.35')]:
    exact=1+mp.sin(2*a)/(4*a)-mp.sqrt((mp.sin(2*a)/(2*a))**2/4+2*(mp.sin(a)/a)**2)
    approx=2*a**4/135+2*a**6/1701
    assert abs(exact-approx)<a**8
    checks+=1
for a in [0.10,0.20,0.35,0.50]:
    ts=np.linspace(-1,1,1001)
    for z in ts:
        xs=np.array([-a,a*z,a])
        d=xs[:,None]-xs[None,:]
        gamma=np.sinc(d/np.pi)
        ev=np.linalg.eigvalsh(gamma)
        assert ev[0] <= ev[1]+1e-12 and ev[1] <= ev[2]+1e-12
        assert ev[0] <= 2*a**4/135+2*a**6/1701+0.005*a**8+1e-10
        checks+=2

for z in [-1/3, 1/3]:
    a=1.5*np.pi
    xs=a*np.array([-1,z,1]);d=xs[:,None]-xs[None,:]
    assert np.max(np.abs(np.sinc(d/np.pi)-np.eye(3)))<2e-15
    checks+=1
assert abs(1-2*np.sqrt(2)/(3*np.pi)-0.6998945612809646)<1e-14
checks+=1
print(f'PASS: {checks} symbolic and finite numerical checks')
