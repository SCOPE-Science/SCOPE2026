#!/usr/bin/env python3
"""Symbolic and numerical consistency checks for the four-Gaussian rectangle theorem.
Run with Python 3, sympy, mpmath, numpy.
"""
import math
import sympy as sp
import mpmath as mp

# Symbolic four-state Gram determinant, where z is the unit symplectic phase.
h, k, z = sp.symbols('h k z', nonzero=True)
G = sp.Matrix([
    [1, h, k, h*k],
    [h, 1, h*k*z, k*z],
    [k, h*k/z, 1, h/z],
    [h*k, k/z, h*z, 1],
])
expected = ((1-h*h)*(1-k*k))**2 - (h*k*(z+1/z-2))**2
assert sp.factor(G.det()-expected)==0
print('PASS exact Gram determinant in four symbolic variables')

u=sp.symbols('u',real=True)
square=(1-sp.exp(-u))**4-16*sp.exp(-2*u)*sp.sin(u/2)**4
assert sp.simplify(sp.diff(square,u,6).subs(u,0))==240 # coefficient 1/3
assert sp.simplify(sp.diff(square,u,5).subs(u,0))==0
print('PASS balanced rectangle leading order u^6/3')

x=sp.symbols('x',positive=True)
f=((1-sp.exp(-x))/x)**2-sp.exp(-x)
g=sp.expand(sp.simplify(sp.diff(f,x)*x**3*sp.exp(2*x)))
H=(x**3+2*x+4)*sp.exp(x)-2*sp.exp(2*x)-2*x-2
assert sp.simplify(g-H)==0
for n in range(4,32):
    num=n*(n-1)*(n-2)+2*n+4-2**(n+1)
    assert (num>0 if n in (4,5,6) else num<0)
assert sp.factor(2*(x*(x-1)*(x-2)+2*x+4)-((x+1)*x*(x-1)+2*(x+1)+4)) == (x-2)*(x*x-4*x-1)
print('PASS one-sign-change coefficient structure and induction identity for unique maximizer')

mp.mp.dps=65
F=lambda t: ((1-mp.exp(-t))/t)**2-mp.exp(-t)
xstar=mp.findroot(lambda t:mp.diff(F,t),(mp.mpf('2.2'),mp.mpf('2.6')))
cstar=F(xstar)
assert mp.mpf('2.38') < xstar < mp.mpf('2.39')
assert mp.diff(F,xstar,2)<0
print('unique limiting maximizer x* =',mp.nstr(xstar,40))
print('sharp small-area coefficient =',mp.nstr(cstar,40))

sinc=lambda t: mp.sin(t)/t if t else mp.mpf(1)
A=lambda t: -mp.expm1(-t)/t if t else mp.mpf(1)

def det_scaled(uu,xx):
    yy=uu**2/xx
    return A(xx)**2*A(yy)**2-mp.exp(-xx-yy)*sinc(uu/2)**4

def matrix_det(a,b):
    p=[(mp.mpf(0),mp.mpf(0)),(a,mp.mpf(0)),(mp.mpf(0),b),(a,b)]
    M=mp.matrix(4)
    for i,(xi,wi) in enumerate(p):
        for j,(xj,wj) in enumerate(p):
            M[i,j]=mp.exp(-mp.pi*((xi-xj)**2+(wi-wj)**2)/2)*mp.exp(mp.pi*1j*(xi*wj-wi*xj))
    return mp.re(mp.det(M))

for uu in map(mp.mpf,['0.03','0.08','0.2','0.6','1.6']):
    for xx in [xstar,uu,mp.sqrt(uu)]:
        a=mp.sqrt(xx/mp.pi);b=uu/(mp.pi*a)
        numeric=matrix_det(a,b)
        closed=uu**4*det_scaled(uu,xx)
        assert mp.fabs(numeric-closed)<mp.mpf('1e-52')
print('PASS 15 direct complex 4x4 Gram determinants versus scaled formula')

for uu in map(mp.mpf,['0.12','0.06','0.03','0.015']):
    xc=mp.findroot(lambda xx:mp.diff(lambda v:det_scaled(uu,v),xx),(mp.mpf('2.2'),mp.mpf('2.5')))
    ratio=det_scaled(uu,xc)/cstar
    assert abs(ratio-1)<2*uu**2
    assert abs(xc-xstar)<uu**2*3
    balanced=uu**4*det_scaled(uu,uu)
    assert abs(balanced/(uu**6/3)-1)<3*uu
    print('u',mp.nstr(uu,6),'x_opt',mp.nstr(xc,20),'normalized_opt',mp.nstr(ratio,20),'square_to_u6third',mp.nstr(balanced/(uu**6/3),16))
print('PASS small-area optimal asymptotic, stationary branches, balanced comparison')
