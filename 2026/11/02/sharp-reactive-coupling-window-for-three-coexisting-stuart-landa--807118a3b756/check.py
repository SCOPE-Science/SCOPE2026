#!/usr/bin/env python3
"""Standalone symbolic and numerical checks for the three-oscillator bistability theorem."""
import sympy as sp
import numpy as np

a,p,q,beta,lam=sp.symbols('a p q beta lam',real=True)
C=sp.Matrix([[p,-q],[q,p]])
E=sp.eye(6)

def blocks(chirality):
    J=sp.zeros(6)
    for j in range(3):
        th=chirality*2*sp.pi*j/3
        vec=sp.Matrix([sp.cos(th),sp.sin(th)])
        for h in range(3):
            J[2*j:2*j+2,2*h:2*h+2]=C
        J[2*j:2*j+2,2*j:2*j+2] -= 2*a*vec*vec.T
    return J

pred=lam*(lam+2*a)*((lam**2+(2*a-3*p)*lam-3*a*p)**2+9*q**2*(lam+a)**2)
for chirality in (-1,1):
    J=blocks(chirality)
    assert sp.expand((lam*E-J).det()-pred)==0
    assert sp.expand(J*sp.Matrix([0,1,-chirality*sp.sqrt(3)/2,-sp.Rational(1,2),chirality*sp.sqrt(3)/2,-sp.Rational(1,2)]))==sp.zeros(6,1)

Js=sp.zeros(6)
for j in range(3):
    for h in range(3):
        Js[2*j:2*j+2,2*h:2*h+2]=C
    Js[2*j:2*j+2,2*j:2*j+2]-=3*C+2*beta*sp.diag(1,0)
pred_sync=lam*(lam+2*beta)*((lam+3*p)*(lam+2*beta+3*p)+9*q*q)**2
assert sp.expand((lam*E-Js).det()-pred_sync)==0

# Verify the sharp imaginary-axis crossing in the two conjugate quadratic blocks.
qstar2 = p*(2*a-3*p)**2/(3*(a-3*p))
Om=3*a*q/(2*a-3*p)
Q=(lam**2+(2*a-3*p-3*sp.I*q)*lam-3*a*(p+sp.I*q))
assert sp.simplify(sp.expand(Q.subs(lam,sp.I*Om)).subs(q*q,qstar2))==0
s,t=sp.symbols('s t',real=True)
F=(2*t-9)**2/(3*(t-6))
assert sp.factor(F-(8+4*(t-sp.Rational(15,2))**2/(3*(t-6))))==0
roots=[sp.Rational(3,8)*(12+s+sign*sp.sqrt(s*(s-8))) for sign in (-1,1)]
for rt in roots:
    assert sp.simplify(4*rt**2-(36+3*s)*rt+81+18*s)==0
assert sp.simplify(F.subs(t,sp.Rational(15,2))-8)==0

def significant_eigenvalues(a_val,p_val,q_val):
    J=np.asarray(blocks(1).subs({a:a_val,p:p_val,q:q_val}),float)
    ev=np.linalg.eigvals(J)
    z=np.argmin(abs(ev))
    assert abs(ev[z])<1.e-8
    return np.delete(ev,z)

for bb,pp,qq,stable in [(8,1,3,True),(8,1,-3,True), (8,1,2,False),
                          (10,1,4,True),(10,1,3,False),(6,1,100,False),
                          (7,1,3,True),(7,1,0,False)]:
    ev=significant_eigenvalues(bb-3*pp,pp,qq)
    if stable:
        assert max(ev.real)<-1.e-7,(bb,pp,qq,ev)
    else:
        assert max(ev.real)>1.e-7,(bb,pp,qq,ev)

print('PASS: two chirality characteristic polynomials, neutral directions, synchrony polynomial,')
print('      imaginary crossing, exact double-tangency, quadratic growth-window boundaries,')
print('      eight representative full six-dimensional spectral checks.')
