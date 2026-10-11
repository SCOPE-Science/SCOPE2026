"""Exact-algebra replay for the three-view Cauchy cubature theorem."""
import sympy as sp

epsilon, delta, t = sp.symbols("epsilon delta t", nonnegative=True, real=True)
L = sp.Rational(1, 3) - epsilon / 2
wmax = sp.Rational(1, 3) + epsilon
r = sp.factor(L / wmax)
assert sp.factor(r - (2-3*epsilon)/(2+6*epsilon)) == 0
assert sp.factor(1-r**2 - 9*epsilon*(4+3*epsilon)/(4*(1+3*epsilon)**2)) == 0
assert sp.simplify(4*(1+3*epsilon)**2-(4+3*epsilon)-(21*epsilon+36*epsilon**2)) == 0

weights = [sp.Rational(1,3)+delta,
           sp.Rational(1,3)-delta/2,
           sp.Rational(1,3)-delta/2]
assert sp.simplify(sum(weights)-1)==0
assert sp.factor(sum(x*x for x in weights) - (sp.Rational(1,3)+sp.Rational(3,2)*delta**2))==0
assert sp.simplify(1-2*weights[1]-(sp.Rational(1,3)+delta))==0

ct, st = sp.symbols("c s", positive=True, real=True)
B = sp.Matrix([[1,0,0],[st,ct,0],[0,0,1]])
Binv = B.inv()
assert Binv == sp.Matrix([[1,0,0],[-st/ct,1/ct,0],[0,0,1]])
assert sp.factor((Binv[:,0].dot(Binv[:,0])).subs(st**2,1-ct**2)-1/ct**2)==0
assert Binv[:,1].dot(Binv[:,1])==1/ct**2
assert Binv[:,2].dot(Binv[:,2])==1

u1=sp.Matrix([1,0,0]); u2=sp.Matrix([st,ct,0]); u3=sp.Matrix([0,0,1])
assert sp.simplify(u1.dot(u2)-st)==0
for s1 in (-1,1):
 for s2 in (-1,1):
  for s3 in (-1,1):
   v=s1*u1+s2*u2+s3*u3
   assert sp.factor(v.dot(v)-(2+ct**2+st**2+2*s1*s2*st))==0
print("VERIFY_OK")
print("near_optimal_weight_bounds=exact")
print("near_optimal_angle_expression=exact")
print("weight_perturbation_profile=exact")
print("tilt_matrix_and_signed_sum_profile=exact")
