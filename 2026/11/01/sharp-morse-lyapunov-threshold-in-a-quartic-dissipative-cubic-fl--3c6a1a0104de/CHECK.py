#!/usr/bin/env python3
"""Exact polynomial certificate checks; analytic universal quantifiers are in RESULT.md."""
import sympy as s
x,y,k,e=s.symbols('x y k e',real=True)
F=s.Matrix([-x**3+k*y**3,-y**3-k*x**3])
R=s.Matrix([[0,-1],[1,0]])
z=s.Matrix([x,y])
w=(x**4+y**4)/4
rad=s.expand((z.T*F)[0])
assert s.simplify((s.Matrix([s.diff(w,x),s.diff(w,y)]).T*F)[0]+x**6+y**6)==0
assert s.expand(rad+(x**4+y**4)-k*x*y*(y*y-x*x))==0
Frot=F.subs({x:-y,y:x}, simultaneous=True)
assert all(s.simplify(t)==0 for t in (Frot-R*F))
identity=(x**4+y**4)**2-8*x*x*y*y*(y*y-x*x)**2-(x**4-4*x*x*y*y+y**4)**2
assert s.expand(identity)==0
assert s.simplify(rad.subs({x:1,y:2,k:3})-1)==0
assert s.simplify(rad.subs({x:2,y:1,k:-3})-1)==0
m=x*x+y*y+e*w
assert s.hessian(m,[x,y]).subs({x:0,y:0})==2*s.eye(2)
assert s.simplify((s.Matrix([s.diff(m,x),s.diff(m,y)]).T*F)[0]-2*rad+e*(x**6+y**6))==0
h11,h12,h22=s.symbols('h11 h12 h22',real=True)
H=s.Matrix([[h11,h12],[h12,h22]])
avg=sum([(R**j).T*H*(R**j) for j in range(4)],s.zeros(2))/4
assert avg==(h11+h22)/2*s.eye(2)
print('EXACT_QUARTIC_LIE_DERIVATIVE_PASS')
print('EXACT_RADIAL_AND_C4_EQUIVARIANCE_PASS')
print('SHARP_PERFECT_SQUARE_AND_POSITIVITY_WITNESS_PASS')
print('MORSE_HESSIAN_AND_EXPLICIT_DERIVATIVE_PASS')
print('AVERAGED_QUADRATIC_MATRIX_PASS')
print('GAS_CONVERSE_AND_UNIVERSAL_MORSE_NONEXISTENCE_PROVED_ANALYTICALLY')
