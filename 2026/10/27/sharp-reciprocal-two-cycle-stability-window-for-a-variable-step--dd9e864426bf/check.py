#!/usr/bin/env python3
"""Independent reproducibility checks of the reciprocal BDFL2 periodic theorem."""
import sympy as s
import numpy as np
T=s.symbols('t',positive=True)

def A(w,v):
    d=4*v*(w+1)+2
    a0=v**2*(2*w*w-2*w-1)/d
    a1=(v**2*(-2*w*w+2*w+1)+2*v*(w+1)+1)/d
    return s.Matrix([[s.Rational(3,2),-a1,-a0],[1,0,0],[0,1,0]])

M=A(T,1/T)*A(1/T,T)
S=-(6*T**4+2*T**3-21*T**2+2*T+6)/(4*T*(2*T+3)*(3*T+2))
P=-(T**2+2*T-2)*(2*T**2-2*T-1)/(4*T*(2*T+3)*(3*T+2))
assert s.factor(s.trace(M)-1-S)==0
assert s.factor(M.det()-P)==0
assert ((M-s.eye(3))*s.ones(3,1)).applyfunc(s.factor)==s.zeros(3,1)
assert s.factor(1-P-(2*T**4+26*T**3+43*T**2+26*T+2)/(4*T*(2*T+3)*(3*T+2)))==0
assert s.factor(1-S+P-(T+1)**2*(T**2+4*T+1)/(T*(2*T+3)*(3*T+2)))==0
assert s.factor(1+S+P+(4*T**4-10*T**3-41*T**2-10*T+4)/(2*T*(2*T+3)*(3*T+2)))==0
Y=(5+s.sqrt(221))/4
Tc=float((Y-s.sqrt(Y*Y-4))/2)
assert 0.20<Tc<0.25
for t in (0.15,0.20,0.22,0.24,0.25,0.4,1.,2.,4.,4.25,5.):
    C1=np.array(A(s.Float(t),s.Float(1/t)),float)
    C2=np.array(A(s.Float(1/t),s.Float(t)),float)
    ev=np.linalg.eigvals(C1@C2)
    other=[complex(z) for z in ev if abs(z-1)>1e-5]
    assert len(other)==2
    target=(Tc<t<1/Tc)
    assert (max(abs(z) for z in other)<1-1e-6)==target
assert max(abs(z) for z in np.linalg.eigvals(np.array(A(s.Rational(1, 4),s.Integer(4)),float)))>=1-1e-12
assert max(abs(z) for z in np.linalg.eigvals(np.array(A(s.Rational(6, 25),s.Rational(25,6)),float)))>1
print('PASS: exact monodromy identities, sharp interval and frozen-unstable stable-periodic examples')
