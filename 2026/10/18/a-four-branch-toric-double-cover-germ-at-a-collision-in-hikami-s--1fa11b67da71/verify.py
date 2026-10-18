#!/usr/bin/env python3
"""Exact symbolic identities for the determinantal-quintic local singularity."""
import sympy as s

a,b,c,d,e=s.symbols('a b c d e')
M=s.Matrix([
[2,2,2-a,-d,0],
[2,2,2,-b,-e],
[2-a,2,2,0,-c],
[-d,-b,0,2,0],
[0,-e,-c,0,2]])
f=s.expand(M.det())
A=2*(b*b+e*e-4)
B=-2*(4*b*b+b*c*d*e-4*b*d-4*c*e+4*e*e)
C=2*(b*c-c*d+d*e)**2
assert s.expand(f-(A*a*a+B*a+C))==0
F=4*(b-d)**2+(4-d*d)*e*e
G=b*b*(c*c-4)-4*(c-e)**2
assert s.expand(B*B-4*A*C+4*F*G)==0
assert A.subs({b:0,c:0,d:0,e:0})==-8
assert M.subs({a:0,b:0,c:0,d:0,e:0}).rank()==3
alpha=s.sqrt(4-d*d); beta=s.sqrt(c*c-4)
z1=2*(b-d)+s.I*e*alpha
z2=2*(b-d)-s.I*e*alpha
z3=b*beta-2*(c-e)
z4=b*beta+2*(c-e)
assert s.simplify(s.expand(z1*z2)-F)==0
assert s.simplify(s.expand(z3*z4)-G)==0
sub={b:0,c:0,d:0,e:0}
J=s.Matrix([[s.diff(z,x).subs(sub) for x in (b,c,d,e)] for z in (z1,z2,z3,z4)])
assert s.simplify(J.det())==-64
assert len({str((i,j)) for i in range(4) for j in range(i+1,4)})==6
print('VERIFY_OK')
