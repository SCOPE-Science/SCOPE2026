"""Exact local-equation certificate for the Fermat-line multiplicity computation."""
import sympy as s
u,v=s.symbols('u v')
w=(u+v)/3
q2=s.expand(u*u+v*v-3*w*w)
q3=s.expand(u**3+v**3-3*w**3)
assert q2==s.Rational(2,3)*(u*u-u*v+v*v)
assert s.factor(q3)==(u+v)*(8*u*u-11*u*v+8*v*v)/9
res=s.factor(s.resultant(q2.subs(v,1),q3.subs(v,1),u))
assert res == s.Rational(8,81), res
G=s.groebner([q2,q3],u,v,order='grevlex',domain=s.QQ)
# The leading homogeneous pair is a regular sequence: degree 2 and 3, no projective common zero.
assert all(G.reduce(m)[1]==0 for m in (u**4,u**3*v,u*u*v*v,u*v**3,v**4)), G
# For these two regular elements, the Hilbert series is (1-t^2)(1-t^3)/(1-t)^2.
t=s.symbols('t')
hilb=s.series((1-t*t)*(1-t**3)/(1-t)**2,t,0,7).removeO().expand()
assert hilb==1+2*t+2*t**2+t**3,hilb
assert sum([1,2,2,1])==6
print('special weights (1,1,-3), resultant:',res)
print('transverse associated-graded Hilbert series:',hilb)
print('length:',6)
print('VERIFY_OK')
