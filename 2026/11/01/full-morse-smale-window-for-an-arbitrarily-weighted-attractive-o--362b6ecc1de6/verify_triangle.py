#!/usr/bin/env python3
"""Exact identities and finite diagnostic samples for a weighted attractive phase triangle."""
import math
import sympy as s
x,y,w,h=s.symbols('x y w h',real=True)
V=-s.cos(x)-s.cos(y)-w*s.cos(x-y)
M=s.Matrix([[2,1],[1,2]])
f=-M*s.Matrix([s.diff(V,x),s.diff(V,y)])
expected=s.Matrix([-2*s.sin(x)-s.sin(y)-w*s.sin(x-y), -s.sin(x)-2*s.sin(y)+w*s.sin(x-y)])
assert all(s.trigsimp(z)==0 for z in f-expected)
H=s.hessian(V,(x,y))
assert (H.subs({x:0,y:0})-s.Matrix([[1+w,-w],[-w,1+w]])).is_zero_matrix
assert set((M*H.subs({x:0,y:0})).eigenvals())=={s.Integer(3),1+2*w}
print('synchrony weighted Hessian eigenvalues', [s.factor(q) for q in (M*H.subs({x:0,y:0})).eigenvals()])
assert s.factor(H.subs({x:s.pi,y:0}).det())==-1
assert s.factor(H.subs({x:0,y:s.pi}).det())==-1
HH=H.subs({x:s.pi,y:s.pi})
assert s.simplify(HH*s.Matrix([1,1])+s.Matrix([1,1]))==s.zeros(2,1)
assert s.simplify(HH*s.Matrix([1,-1])-(2*w-1)*s.Matrix([1,-1]))==s.zeros(2,1)
c,C=s.symbols('c C',real=True)
HN=s.Matrix([[c+w*C,-w*C],[-w*C,c+w*C]])
assert s.factor((HN*s.Matrix([1,1]))[0]-c)==0
assert s.factor((HN*s.Matrix([1,-1]))[0]-(c+2*w*C))==0
assert s.simplify((c+2*w*C).subs({c:-1/(2*w),C:1/(2*w*w)-1})-(1-4*w*w)/(2*w))==0
# invariant-circle checks: sum-zero and diagonal
assert s.trigsimp((f[0]+f[1]).subs(y,-x))==0
assert s.trigsimp((f[0]-f[1]).subs(y,x))==0
# Routh spectral orientation check via symmetric Hessian metric
for a in (s.Rational(1,4), s.Rational(3,4),s.Integer(1),s.Integer(3)):
  pts=[(0,0),(s.pi,0),(0,s.pi),(s.pi,s.pi)]
  if a>s.Rational(1,2):
    t=math.acos(-1/(2*float(a)))
    pts += [(t,-t),(-t,t)]
  indices=[]
  for px,py in pts:
    mat=(M*H).subs({x:px,y:py,w:a})
    ev=[float(s.re(q)) for q in mat.eigenvals()] if len(mat.eigenvals())==2 and px in [0,s.pi] else [complex(v).real for v in mat.evalf().eigenvals()]
    assert all(abs(z)>1.e-6 for z in ev)
    indices.append(sum(z<0 for z in ev))
  assert indices==([0,1,1,2] if a<s.Rational(1,2) else [0,1,1,1,2,2]),(a,indices)
  L=max(3,1+2*float(a))
  for ht in (0.1/L,0.95/L,1.1/L,1.8/L):
    assert abs(1-3*ht)<1 and abs(1-(1+2*float(a))*ht)<1
print('fixed-point index transition, invariant circles, and full descent-step synchrony spectral checks: PASS')
