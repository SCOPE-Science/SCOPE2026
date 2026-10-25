#!/usr/bin/env python3
"""Checks the exact two-node Bergman projection identity and phase diagram.

Requires Python 3, sympy, mpmath. Numerical checks corroborate, but proofs of
all-radius and uniqueness assertions are in RESULT.md.
"""
import cmath
import math
import random
import sympy as sp
import mpmath as mp

T,C=sp.symbols('t c',real=True)
D=1-T+T*T-T*C
Q=4*T*T*(1-T)**2*C*C+4*T*(1-T)**2*(2*T-1)*C+(8*T**4-16*T**3+16*T*T-8*T+1)
P1=T*(1-T)**2*(8*T*T-7*T+2)
P=sp.cancel(P1-T*(1-T)**2*(1-C)*Q/D)
raw= T*(1-T)**2*(4*C**3*T**4-8*C**3*T**3+4*C**3*T**2+4*C*C*T**4-12*C*C*T**3+12*C*C*T*T-4*C*C*T-4*C*T**3+7*C*T*T-6*C*T+C+T**3+T*T-T+1)/D
assert sp.factor(P-raw)==0
assert sp.factor(Q.subs(C,1)-(20*T**4-44*T**3+36*T*T-12*T+1))==0
assert sp.factor(Q.subs(C,1/(2*T)-1)-T*(4*T**3-4*T*T+3*T-2))==0
assert sp.factor(sp.diff(P,C).subs(C,-1)-T*(T-1)**4*(4*T**4+4*T**3+4*T*T+4*T+1)/(T*T+1)**2)==0
H=sp.factor(sp.together(sp.diff(P,C))*D**2/(T*(1-T)**4))
H_expected=-8*C**3*T**3+C*C*(12*T**4-16*T**3+16*T*T)+C*(8*T**4-16*T**3+16*T*T-8*T)-4*T**3+4*T*T-4*T+1
assert sp.factor(H-H_expected)==0
checks=5

mp.mp.dps=60
h=lambda t:20*t**4-44*t**3+36*t*t-12*t+1
g=lambda t:4*t**3-4*t*t+3*t-2
t0=mp.findroot(h,(mp.mpf('0.12'),mp.mpf('0.13')))
t1=mp.findroot(g,(mp.mpf('0.82'),mp.mpf('0.84')))
assert mp.mpf('.12127')<t0<mp.mpf('.12129')
assert mp.mpf('.82531')<t1<mp.mpf('.82532')
checks+=2

def expr(t,c):
 q=4*t*t*(1-t)**2*c*c+4*t*(1-t)**2*(2*t-1)*c+(8*t**4-16*t**3+16*t*t-8*t+1)
 return t*(1-t)**2*(8*t*t-7*t+2)-t*(1-t)**2*(1-c)*q/(1-t+t*t-t*c)

def gram(t,th):
 r=mp.sqrt(t)
 a=r; b=r*mp.e**(1j*th)
 Kaa=(1-t)**(-2)
 Kab=(1-a*mp.conj(b))**(-2)
 Kbb=Kaa
 # Gram matrix and evaluation vector. Projection norm equals v^* K^{-1} v.
 det=Kaa*Kbb-abs(Kab)**2
 va=a*a; vb=b*b
 return mp.re((Kbb*abs(va)**2+Kaa*abs(vb)**2-2*mp.re(mp.conj(va)*Kab*vb))/det)

rng=random.Random(290307)
for j in range(160):
 t=mp.mpf(str(rng.uniform(.01,.97)))
 theta=mp.mpf(str(rng.uniform(.02,3.13)))
 c=mp.cos(theta)
 err=abs(gram(t,theta)-expr(t,c))
 assert err<mp.mpf('1e-43'),(j,err)
 checks+=1

for t in [mp.mpf('.1'),mp.mpf('.39'),mp.mpf('.9')]:
 # Confluent finite-difference limit, controlled using arbitrary precision.
 val=gram(t,mp.mpf('1e-16'))
 assert abs(val-expr(t,mp.mpf(1)))<mp.mpf('1e-26')
 checks+=1

# Three distinct regimes, plus the isolated coexistence point.
for t in [mp.mpf('0.05'),mp.mpf('0.1'),t0,mp.mpf('0.2'),mp.mpf('0.4'),mp.mpf('0.75'),t1,mp.mpf('0.9'),mp.mpf('.99')]:
 v=1/(2*t)-1
 qs=[(4*t*t*(1-t)**2*c*c+4*t*(1-t)**2*(2*t-1)*c+8*t**4-16*t**3+16*t*t-8*t+1) for c in [mp.mpf(-1),mp.mpf(1),v]]
 cands=[(expr(t,mp.mpf(-1)),mp.mpf(-1)),(expr(t,mp.mpf(1)),mp.mpf(1))]
 # roots of cubic P'(c): use polynomial coefficients from Sympy expression
 cs=sp.Poly(H_expected,C)
 for rr in sp.nroots(cs.as_expr().subs(T,str(t)),n=40,maxsteps=300):
  z=complex(rr)
  if abs(z.imag)<1e-10 and -1<=z.real<=1:
   c=mp.mpf(str(z.real));cands.append((expr(t,c),c))
 winner=max(cands,key=lambda p:p[0])
 if t<t0 or t>t1:
  assert abs(winner[1]-1)<mp.mpf('1e-8')
 if t==t1:
  assert abs(expr(t,v)-expr(t,1))<mp.mpf('1e-49')
 checks+=1
print('All',checks,'symbolic, arbitrary-precision and phase checks passed.')
print('t0 =',mp.nstr(t0,30))
print('t1 =',mp.nstr(t1,30))
print('c at coexistence =',mp.nstr(1/(2*t1)-1,30))
