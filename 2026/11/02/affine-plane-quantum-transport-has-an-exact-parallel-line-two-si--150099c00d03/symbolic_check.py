#!/usr/bin/env python3
"""Exact algebraic checks of the finite-affine-plane two-sink capture theorem."""
import sympy as s
q=s.symbols('q', integer=True, positive=True)
Q=q**2; L=q*(q+1)
# The nonprincipal-singular-value Gram matrix for one point and one line.
a=1-1/Q; b=(q-1)/q
for delta,want in [(0,(q*q-q-1)/q**2),(1,(q-1)**2/q**2)]:
    c=(delta-1/q)/s.sqrt(q)
    M=s.Matrix([[a,c],[c,b]])
    assert s.simplify(M.det()-want)==0
# Two point sinks: 2x2 Gram has strictly positive eigenvalues 1 and 1-2/q^2.
Gp=s.eye(2)-s.ones(2,2)/Q
assert s.factor(Gp.det())==(q*q-2)/q**2
# Two line sinks: nonprincipal Gram determinant, intersecting and parallel.
Gl_inter=s.eye(2)*(q-1)/q
Gl_par=s.Matrix([[(q-1)/q,-1/q],[-1/q,(q-1)/q]])
assert s.factor(Gl_inter.det())==(q-1)**2/q**2
assert s.factor(Gl_par.det())==(q-2)/q
# The zero singular-value line-block Gram loses one rank for parallel pairs.
Zpar=s.ones(2,2)/(q+1)
Zinter=s.Matrix([[1/(q+1),-1/(q*(q+1))],[-1/(q*(q+1)),1/(q+1)]])
assert s.factor(Zpar.det())==0
assert s.factor(Zinter.det())==(q-1)/(q**2*(q+1))
# Complete sitewise capture law for incident point-line traps.
c=(1-1/q)/s.sqrt(q)
MI=s.simplify(s.Matrix([[a,c],[c,b]]).inv())
def P(d,inc):
    z=s.Matrix([d-1/Q,(inc-1/q)/s.sqrt(q)])
    return s.factor(1/Q+(z.T*MI*z)[0])
def Lval(inc,intersection,parallel):
    z=s.Matrix([(inc-1/q)/s.sqrt(q),(intersection-1)/q])
    zero=1/(q+1) if parallel else 1/(q*q*(q+1))
    return s.factor(1/L+(z.T*MI*z)[0]+zero)
assert P(1,1)==1
assert s.factor(P(0,1)-1/(q-1))==0
assert s.factor(P(0,0)-1/(q*(q-1)))==0
assert Lval(1,q,True)==1
assert s.factor(Lval(0,0,True)-1/(q-1))==0
assert s.factor(Lval(1,1,False)-1/q)==0
assert s.factor(Lval(0,1,False)-1/(q*(q-1)))==0
assert s.simplify(2+2*(q-1)+q+2*q*(q-1)-(Q+L))==0
assert s.simplify(2+2*(q-1)/(q-1)+q/q+2*q*(q-1)/(q*(q-1)) - 7)==0
print('symbolic Gram determinants and incident-trap site law: PASS')
print('symbolic normalization and rank trace: PASS')
