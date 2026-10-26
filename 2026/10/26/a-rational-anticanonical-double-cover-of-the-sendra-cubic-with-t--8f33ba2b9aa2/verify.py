"""Exact symbolic checks for the double-cover (2,3) complete intersection."""
import sympy as sp

w,a,b,c,d,z,t,v,s=sp.symbols('w a b c d z t v s')
F=w*w*b+a*a*c+b**3+c**3+d**3
Q=z*z+b*c
B=1-t**6+v**3
D=1+B*s**2
A=t*(B*s**2-1)/D
C=-2*t*s/D
BB=-t**2*C
DD=v*C
ZZ=t*C
assert sp.cancel(F.subs({w:1,a:A,b:BB,c:C,d:DD}))==0
assert sp.cancel(Q.subs({b:BB,c:C,z:ZZ}))==0
assert sp.cancel(ZZ/C-t)==0
assert sp.cancel(DD/C-v)==0
assert sp.cancel(C/(A-t)-s)==0
assert sp.factor(F.subs({b:0,c:0}))==d**3
# Branch-plane cubic partials have no common nonzero projective zero:
# G(u,v,h)=u^2*v+v^3+h^3.
u, vv, h=sp.symbols('u vv h')
G=u**2*vv+vv**3+h**3
partials=[sp.diff(G,x) for x in (u,vv,h)]
assert sp.solve(partials,(u,vv,h))==[(0,0,0)]
# The special transverse binary quartic has four distinct linear factors.
T=sp.symbols('T')
q=T**4+T
assert sp.gcd(q,sp.diff(q,T))==1
# Binary-quartic invariants: I=0, J=-27, hence smooth equianharmonic elliptic curve.
coef=[sp.Integer(x) for x in [1,0,0,1,0]]
alpha,beta,gamma,delta,epsilon=coef
I=12*alpha*epsilon-3*beta*delta+gamma**2
J=72*alpha*gamma*epsilon+9*beta*gamma*delta-27*alpha*delta**2-27*beta**2*epsilon-2*gamma**3
assert (I,J,4*I**3-J**2)==(0,-27,-729)
print('VERIFY_OK rational_inverse double_cover_cubic smooth_branch_elliptic j_zero special_quartic')
